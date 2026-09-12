# Confluence MCP Recovery Memory

Last validated: 2026-04-09

## Working Confluence MCP configuration
File: ~/.codex/config.toml

Required block:
[mcp_servers.confluence]
enabled = true
url = "https://emcp.oracle.com/atlassian/centralconfluence/v2"

Important:
- Do NOT keep a static auth override block for confluence:
  [mcp_servers.confluence.http_headers]
  Authorization = "Bearer ..."
- That override can break OAuth flow for this server in Codex desktop.

## Known-good verification target
- Space: OFSCdev
- Page title: Teams
- Page ID: 232259465
- URL: https://confluence.oraclecorp.com/confluence/pages/viewpage.action?pageId=232259465

## Key observations from 2026-04-09
- OAuth browser callback can succeed while MCP calls still fail.
- `codex mcp login confluence` success message alone is not enough.
- MCP handshake success (for example, resources/list works) must be followed by real Confluence tool call validation.
- Multiple Codex runtimes can create token drift/race:
  - Codex desktop app-server
  - VS Code Codex extension app-server
- Confluence server can fail independently of OAuth. Observed server-side tool error:
  - `name 'JSONResponse' is not defined`
  - affected `search`, `get_page`, `fetch`

## Symptoms and what they mean
- `invalid_grant: refresh token does not exist` during initialize:
  stale/rotated refresh token in client state; reset OAuth.
- HTTP 401 `invalid_token` from resource URL:
  token not accepted by server; re-auth and verify runtime state.
- MCP tools error `name 'JSONResponse' is not defined`:
  Confluence MCP server bug. OAuth is not the blocker.

## Step-by-step cookbook
1. Validate static config:
   - `codex mcp get confluence`
   - confirm URL and no `http_headers` override in `~/.codex/config.toml`
2. Ensure single runtime:
   - close Codex desktop + VS Code Codex extension sessions
   - start only one Codex runtime
3. Reset OAuth credentials:
   - `codex mcp logout confluence`
   - `codex mcp login confluence`
   - complete browser callback page (`Authentication complete`)
4. Verify in two phases:
   - Handshake phase: `resources/list` on `confluence` should return without auth error
   - Tool phase: run Confluence tool call (`search` or `get_page`)
5. Branch on result:
   - If auth error persists (`invalid_grant`, `invalid_token`): repeat steps 2-4
   - If handshake works but tool call fails with server exception (`JSONResponse`): treat as server-side MCP defect and use REST/web fallback

## Acceptance criteria
- Handshake passes without auth errors.
- `search` returns Teams page id `232259465`.
- `get_page` succeeds for page id `232259465`.

## Operator note
When user asks to "check access", run both checks:
1) MCP handshake check
2) real Confluence tool call check
Do not conclude from login callback alone.
