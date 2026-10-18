#!/usr/bin/env python3
"""False-death audit for stillcasting.app (read-only).

Looks at every person marked deceased in the last N days and cross-checks the sources:
  TMDB_RETRACTED   TMDb no longer has a death date and no other source recorded one  → vandalism (Gal Gadot 2026-10-17)
  WIKIDATA_MISMATCH Wikidata has a different death date                               → wrong date
  TMDB_MISMATCH    TMDb has a different death date                                    → wrong date
  NAME_TWIN        another record with the same name died within 3 days               → likely the same death on two records
  UNCONFIRMED      only TMDb says so, Wikidata has an item but no death               → watch (obscure deaths lag; famous ones are suspect)
  OK               confirmed by Wikidata or by a non-TMDb source
Usage: python3 stillcasting-false-death-check.py [--days 14] [--json OUT]
Needs: ~/.ssh/oci-mas.key (prod DB + TMDb key stay on the box; nothing is printed except verdicts).
"""
import argparse, json, subprocess, sys, time, urllib.parse, urllib.request

HOST = "ubuntu@130.61.219.74"
KEY = "~/.ssh/oci-mas.key"
UA = {"User-Agent": "StillCastingAudit/1.0 (snobist@gmail.com)", "Accept": "application/sparql-results+json"}

REMOTE = r'''
cd /home/ubuntu/stillcasting; k=$(grep -E '^TMDB_API_KEY=' .env | cut -d= -f2- | tr -d '"'"'"' ')
docker exec stillcasting-postgres-1 psql -U postgres -d stillcasting -Atc "
select p.id, p.slug, p.name, coalesce(p.tmdb_id,''), coalesce(p.wikidata_id,''), p.date_of_death, coalesce(p.tmdb_popularity,0),
       (select string_agg(distinct s.source_type, ',') from status_provenance s where s.person_id=p.id and s.status='deceased'),
       (select string_agg(o.slug||'@'||o.date_of_death, ' ') from persons o where o.id<>p.id and lower(o.name)=lower(p.name)
          and o.status='deceased' and abs(o.date_of_death - p.date_of_death) <= 3)
from persons p where p.status='deceased' and p.date_of_death >= current_date - %d order by p.tmdb_popularity desc nulls last" </dev/null \
| while IFS='|' read id slug name tmdb wd dod pop src twin; do
  td=""; if [ -n "$tmdb" ]; then td=$(curl -s -m 15 "https://api.themoviedb.org/3/person/$tmdb?api_key=$k" | python3 -c "import json,sys; print(json.load(sys.stdin).get('deathday') or '')" 2>/dev/null); sleep 0.25; fi
  printf '%%s\t%%s\t%%s\t%%s\t%%s\t%%s\t%%s\t%%s\t%%s\t%%s\n' "$id" "$slug" "$name" "$tmdb" "$wd" "$dod" "$pop" "$src" "$twin" "$td"
done
'''

def wikidata_dod(tmdb_id: str, wikidata_id: str):
    """(has_item, dod) via Wikidata: by TMDb id first, else by Q-id."""
    if tmdb_id:
        q = f'SELECT ?item ?dod WHERE {{ ?item wdt:P4985 "{tmdb_id}" . OPTIONAL {{ ?item wdt:P570 ?dod }} }} LIMIT 3'
    elif wikidata_id:
        q = f'SELECT ?item ?dod WHERE {{ BIND(wd:{wikidata_id} AS ?item) OPTIONAL {{ ?item wdt:P570 ?dod }} }} LIMIT 3'
    else:
        return (False, None)
    try:
        url = "https://query.wikidata.org/sparql?" + urllib.parse.urlencode({"query": q, "format": "json"})
        b = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30))["results"]["bindings"]
    except Exception:
        return (None, None)
    if not b:
        return (False, None)
    dods = [x["dod"]["value"][:10] for x in b if "dod" in x]
    return (True, dods[0] if dods else None)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--days", type=int, default=14); ap.add_argument("--json")
    a = ap.parse_args()
    out = subprocess.run(["ssh", "-i", KEY, "-o", "ConnectTimeout=25", "-o", "ConnectionAttempts=3", HOST, "bash -s"],
                         input=REMOTE % a.days, capture_output=True, text=True, timeout=1800)
    rows = [l.split("\t") for l in out.stdout.splitlines() if l.count("\t") == 9]
    results = []
    for pid, slug, name, tmdb, wd, dod, pop, src, twin, tmdb_dod in rows:
        has_item, wd_dod = wikidata_dod(tmdb, wd); time.sleep(0.6)
        srcs = set(filter(None, (src or "").split(",")))
        tmdb_only = srcs <= {"tmdb_scan"}
        if tmdb_only and tmdb and not tmdb_dod and not wd_dod:
            verdict = "TMDB_RETRACTED"
        elif wd_dod and wd_dod != dod:
            verdict = "WIKIDATA_MISMATCH"
        elif tmdb_dod and tmdb_dod != dod:
            verdict = "TMDB_MISMATCH"
        elif twin:
            verdict = "NAME_TWIN"
        elif wd_dod or not tmdb_only:
            verdict = "OK"
        elif has_item:
            verdict = "UNCONFIRMED"
        else:
            verdict = "OK"  # no Wikidata item at all: obscure, TMDb is the only source there is
        results.append({"id": int(pid), "slug": slug, "name": name, "tmdb_id": tmdb, "ours": dod, "tmdb": tmdb_dod or None,
                        "wikidata": wd_dod, "popularity": float(pop or 0), "sources": sorted(srcs), "twin": twin or None, "verdict": verdict})
    order = {"TMDB_RETRACTED": 0, "WIKIDATA_MISMATCH": 1, "TMDB_MISMATCH": 2, "NAME_TWIN": 3, "UNCONFIRMED": 4, "OK": 5}
    results.sort(key=lambda r: (order[r["verdict"]], -r["popularity"]))
    counts = {}
    for r in results: counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
    print(f"checked {len(results)} deaths from the last {a.days} days:", counts)
    for r in results:
        if r["verdict"] != "OK":
            print(f"  {r['verdict']:18s} {r['slug']:32s} id={r['id']:<8d} ours={r['ours']} tmdb={r['tmdb']} wikidata={r['wikidata']} pop={r['popularity']:.1f} src={','.join(r['sources'])}{' twin=' + r['twin'] if r['twin'] else ''}")
    if a.json:
        json.dump(results, open(a.json, "w"), indent=1)
    return 0

if __name__ == "__main__":
    sys.exit(main())
