# Grafana / Loki access (oc1.octo.oraclecloud.com)

`Last-verified: 2026-08-31` (bundle; old-Mac paths). Source: `raw/codex-memories/grafana-cookie-access.md`.
Cookie `picauth_0` from Chrome **Profile 2** Cookies DB, decrypted with Keychain `Chrome Safe Storage`/`Chrome`
(PBKDF2 as in [[slack-access]]); Chrome `meta.version >= 24` prepends 32 bytes SHA256(host_key) — strip before decode.
Verify: `GET /grafana/api/health` → 200 → Loki proxy `/grafana/api/datasources/proxy/uid/<uid>/loki/api/v1/query_range`.
CLI (old paths): `bin/grafana-loki-query --mode health`, `scripts/grafana_loki_query.py --query '<LOGQL>' --last 30m`.
Never store decrypted cookie in files. Related: [[access]].
