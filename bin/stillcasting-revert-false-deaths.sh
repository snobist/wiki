#!/usr/bin/env bash
# stillcasting — revert the 5 false deaths confirmed by the 2026-09-14 audit, create the 2 real
# persons that were never in the DB, drop the two wrong Wikipedia portraits, refresh death caches.
# Read-only verification is in wiki/analyses/stillcasting-bug-audit-2026-09-14.md (section A).
# Run on the Mac:  bash ~/Documents/wiki/bin/stillcasting-revert-false-deaths.sh
set -u
KEY="$HOME/.ssh/oci-mas.key"
HOST=ubuntu@130.61.219.74
ssh -i "$KEY" -o ServerAliveInterval=15 -o ConnectTimeout=20 "$HOST" 'bash -s' <<'REMOTE'
cat > /tmp/cleanup_false_deaths.py <<'PY'
from datetime import date
from celery import Celery
from stillcasting_api.config import get_settings
from stillcasting_api.database import create_engine_from_url, create_db_session
from stillcasting_api.models import Person, PersonStatus, StatusProvenance, Credit
from stillcasting_api.services.seo_service import recompute_person_indexable, recompute_title_indexable
from stillcasting_api.connectors.factory import get_connector
from stillcasting_api.services.import_service import _make_person_slug

s = get_settings(); eng = create_engine_from_url(s.database_url); cel = Celery(broker=s.redis_url)
DEATH_FIELDS = ('date_of_death','death_year','cause_of_death','cause_of_death_category','place_of_death',
                'burial_place','death_story','death_story_fetched_at','wiki_profile_path_local')
# shell id -> (who the Wikipedia entry really was, real tmdb id, death date from the Wikipedia page)
SHELLS = {
    321670: ('Jeremy Thomas, British film producer', '3056',    date(2026, 9, 11)),
    368825: ('Virginio Gazzolo, Italian actor',       '103104',  date(2026, 8, 19)),
    401991: ('Dave Kendall, British actor',           '101826',  date(2026, 7, 14)),
    28721:  ('Jeff Olson, American actor',            '1426772', date(2026, 6, 21)),
    31948:  ('Terence Donovan, Australian actor',     '75394',   date(2026, 7, 18)),
}
conn = get_connector()
with create_db_session(eng) as db:
    for pid, (real, real_tmdb, dod) in SHELLS.items():
        p = db.query(Person).filter_by(id=pid).first()
        if p is None or p.status != PersonStatus.DECEASED:
            print(f'skip {pid}: not found or already reverted'); continue
        before = (p.status.value, str(p.date_of_death), p.wiki_profile_path_local)
        p.status = PersonStatus.UNVERIFIED
        for f in DEATH_FIELDS:
            setattr(p, f, None)
        db.add(StatusProvenance(
            person_id=pid, status=PersonStatus.UNVERIFIED, source_type='manual',
            notes=f'False death reverted 2026-09-14 (audit): the Wikipedia deaths entry was {real} (tmdb {real_tmdb}); '
                  f'this record had matched by name only.',
            recorded_by='alex',
        ))
        db.flush()
        recompute_person_indexable(db, pid)
        tids = [t for (t,) in db.query(Credit.title_id).filter_by(person_id=pid).distinct()]
        for tid in tids:
            recompute_title_indexable(db, tid)
        print(f'reverted {pid} {p.slug}: {before} -> unverified, indexable={p.indexable}, titles recomputed={len(tids)}')

        real_person = db.query(Person).filter_by(tmdb_id=real_tmdb).first()
        if real_person is None:
            d = conn.get_person_detail(real_tmdb)
            real_person = Person(
                name=d.name, tmdb_id=real_tmdb, status=PersonStatus.DECEASED, date_of_death=dod,
                slug=_make_person_slug(db, d.name, d.birthday.year if d.birthday else None),
                date_of_birth=d.birthday, imdb_id=d.imdb_id, wikidata_id=d.wikidata_id,
                profile_path=d.profile_path,
            )
            db.add(real_person); db.flush()
            db.add(StatusProvenance(
                person_id=real_person.id, status=PersonStatus.DECEASED, source_type='wikipedia_deaths_page',
                source_url='https://en.wikipedia.org/wiki/Deaths_in_2026',
                notes=f'Death date {dod} from Wikipedia Deaths_in_2026; record created 2026-09-14 during audit cleanup (tmdb {real_tmdb})',
                recorded_by='alex',
            ))
            recompute_person_indexable(db, real_person.id)
            print(f'created real person {real_person.id} {real_person.slug} tmdb={real_tmdb} dob={d.birthday} tmdb_deathday={d.deathday}')
            for task, q in (('scan_person_task','scans'), ('wiki_scan_person_task','wiki-scans'),
                            ('download_profile_task','images'), ('import_person_filmography_task','imports')):
                cel.send_task(f'stillcasting_worker.tasks.{task}', args=[real_person.id], queue=q)
        else:
            print(f'real person present: {real_person.id} {real_person.slug} status={real_person.status.value} dod={real_person.date_of_death}')
    db.commit()
print('committed')
PY
docker cp /tmp/cleanup_false_deaths.py stillcasting-backend-1:/tmp/cleanup_false_deaths.py
docker exec stillcasting-backend-1 python /tmp/cleanup_false_deaths.py
echo "--- remove the two wrong Wikipedia portraits (fetched by name for another person)"
docker exec stillcasting-backend-1 sh -c 'rm -fv /app/media/profiles/2391998/wiki_w185.jpg /app/media/profiles/3081448/wiki_w185.jpg'
echo "--- refresh death caches"
docker exec stillcasting-worker-1 python -c "
import os, redis
from stillcasting_worker.tasks import _flush_death_caches
_flush_death_caches(redis.from_url(os.environ['REDIS_URL'], decode_responses=True), 2026)
print('flushed')"
echo "--- verify"
for s in jeremy-thomas jeremy-thomas-2 terence-donovan jeff-olson dave-kendall virginio-gazzolo; do
  curl -s -A Mozilla/5.0 "https://stillcasting.app/api/persons/$s" | python3 -c "import json,sys; d=json.load(sys.stdin); print('$s', d.get('status'), d.get('date_of_death'), d.get('wiki_profile_path_local'))" 2>/dev/null || echo "$s: (not found)"
done
REMOTE
