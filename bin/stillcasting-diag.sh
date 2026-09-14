#!/usr/bin/env bash
# stillcasting — phase 1: install OCI key locally + collect diagnostics for the three fixes
# (duplicate Jeremy Thomas entity, /sitemap.xml 404, dev.stillcasting.app lock-down).
# Run on the Mac:  bash ~/Documents/wiki/bin/stillcasting-diag.sh
# Output lands in ~/Documents/wiki/raw/docs/stillcasting-diag-<date>.txt (readable by Cowork sessions).
set -u
SRC="$HOME/Library/CloudStorage/OneDrive-OracleCorporation/private_folder/stillcasting/ssh-key-2026-03-18.key"
KEY="$HOME/.ssh/oci-mas.key"
HOST=ubuntu@130.61.219.74
OUT="$HOME/Documents/wiki/raw/docs/stillcasting-diag-$(date +%F).txt"
mkdir -p "$HOME/.ssh" "$(dirname "$OUT")"

if [ ! -s "$KEY" ]; then
  echo "== copying key from OneDrive (forces download if cloud-only)"
  cat "$SRC" > "$KEY" || { echo "cannot read $SRC — open the OneDrive folder in Finder and choose 'Always keep on this device', then rerun"; exit 1; }
  chmod 600 "$KEY"
fi
S="ssh -i $KEY -o ServerAliveInterval=15 -o ConnectTimeout=20 -o StrictHostKeyChecking=accept-new $HOST"

{
echo "### stillcasting diagnostics $(date -u +%FT%TZ)"
$S 'bash -s' <<'REMOTE'
set +e
sec(){ echo; echo "=== $1"; }
sec "disk"; df -h / /data 2>/dev/null; du -sh /var/lib/docker 2>/dev/null
sec "containers"; docker ps -a --format 'table {{.Names}}\t{{.Status}}\t{{.Image}}'
sec "stillcasting tree"; ls -la /home/ubuntu/stillcasting; ls /home/ubuntu/stillcasting-staging 2>/dev/null | head
sec "compose"; sed -n '1,200p' /home/ubuntu/stillcasting/docker-compose.yml 2>/dev/null || ls /home/ubuntu/stillcasting/*.y*ml
sec "Caddyfile"; cat /home/ubuntu/stillcasting/Caddyfile 2>/dev/null
sec "git"; cd /home/ubuntu/stillcasting 2>/dev/null && git remote -v && git log --oneline -5 && git status --short | head
sec "sitemap routes in frontend"; grep -rIl --exclude-dir=node_modules --exclude-dir=.next -E 'sitemap' /home/ubuntu/stillcasting 2>/dev/null | head -20
grep -rIn --exclude-dir=node_modules --exclude-dir=.next -E 'sitemap' /home/ubuntu/stillcasting/*/app/*sitemap* /home/ubuntu/stillcasting/*/src/app/*sitemap* 2>/dev/null | head -40
sec "died-this-week source"; grep -rIln --exclude-dir=node_modules --exclude-dir=.next -E 'died.this.week|died_this_week|remembered' /home/ubuntu/stillcasting 2>/dev/null | head -20
sec "workers/cron"; crontab -l 2>/dev/null; systemctl list-timers --no-pager 2>/dev/null | head -20
sec "postgres container + schema"
PG=$(docker ps --format '{{.Names}}' | grep -i -E 'postgres|db' | head -1); echo "PG=$PG"
if [ -n "$PG" ]; then
  Q(){ docker exec "$PG" psql -U "${PGUSER:-postgres}" -d "${PGDB:-postgres}" -Atc "$1" 2>&1 || docker exec "$PG" sh -c 'psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -Atc "'"$1"'"' 2>&1; }
  echo "-- tables"; Q "\dt"
  echo "-- person table columns"; Q "select table_name, string_agg(column_name||':'||data_type, ', ' order by ordinal_position) from information_schema.columns where table_name in ('persons','people','person') group by 1"
  echo "-- jeremy thomas rows"; for t in persons people person; do Q "select * from $t where slug in ('jeremy-thomas','jeremy-thomas-2')" ; done
  echo "-- death-related tables"; Q "select table_name from information_schema.tables where table_name ilike '%death%' or table_name ilike '%status%'"
fi
sec "dev subdomain"; curl -s -o /dev/null -w 'dev: %{http_code} size=%{size_download}\n' -H 'Host: dev.stillcasting.app' http://127.0.0.1/ ; curl -sI https://dev.stillcasting.app/ | head -15
sec "sitemap.xml locally"; curl -s -o /dev/null -w 'sitemap.xml: %{http_code}\n' https://stillcasting.app/sitemap.xml; curl -s -o /dev/null -w 'sitemap/0.xml: %{http_code}\n' https://stillcasting.app/sitemap/0.xml
REMOTE
} | tee "$OUT"
echo; echo "written: $OUT"
