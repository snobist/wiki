# Grafana Cookie Access Memory (Chrome/macOS)

## Goal
Access `https://oc1.octo.oraclecloud.com/grafana` logs from CLI without manually copying browser cookies.

## How to find the key for access
1. The Chrome cookie encryption key is in macOS Keychain item:
   - Service: `Chrome Safe Storage`
   - Account: `Chrome`
2. Read it with:
   - `security find-generic-password -w -s "Chrome Safe Storage" -a "Chrome"`
3. Derive AES key from that value:
   - PBKDF2-HMAC-SHA1
   - salt: `saltysalt`
   - iterations: `1003`
   - key length: `16`

## How to find the right auth cookie
1. Check Chrome profile cookie DB (for this user, valid one was `Profile 2`):
   - `~/Library/Application Support/Google/Chrome/Profile 2/Cookies`
2. Query candidate cookies for target host:
   - host: `oc1.octo.oraclecloud.com`
3. In this environment, working cookie name was:
   - `picauth_0`
4. `grafana_session` was not present in Chrome DB for this host.

## Decryption caveat
- Chrome cookie DB `meta.version >= 24` prepends 32 bytes (`SHA256(host_key)`) to decrypted cookie bytes.
- Strip this prefix before UTF-8 decode.

## Verification flow
1. Decrypt cookie.
2. Call Grafana health endpoint with cookie:
   - `GET /grafana/api/health`
3. If status `200`, call Loki proxy query endpoint:
   - `/grafana/api/datasources/proxy/uid/<uid>/loki/api/v1/query_range`

## Reusable CLI in this workspace
- Health check:
  - `bash /Users/oleksandrgrytsenko/Documents/Codex_Work_Dir/bin/grafana-loki-query --mode health`
- Query logs:
  - `python3 /Users/oleksandrgrytsenko/Documents/Codex_Work_Dir/scripts/grafana_loki_query.py --query '<LOGQL>' --last 30m --limit 200`

## Safety
- Never print full cookie value in logs/output.
- Never store decrypted cookie in files.
