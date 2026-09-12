# Confluence access (Oracle)

`Last-verified: 2026-04-09` (cookbook). Source: `raw/codex-memories/confluence-mcp-recovery.md`.
- Codex MCP `confluence` → `https://emcp.oracle.com/atlassian/centralconfluence/v2`, OAuth. **Do not** add a static
  `http_headers` Authorization override — it breaks OAuth.
- Known-good verification target: space `OFSCdev`, page "Teams", id `232259465`.
- Recovery: single Codex runtime → `codex mcp logout confluence` → `codex mcp login confluence` → verify handshake
  (`resources/list`) **and** a real tool call (`search`/`get_page`). Login callback alone proves nothing.
- Error signatures: `invalid_grant` / `invalid_token` = client token state (re-auth); `name 'JSONResponse' is not defined`
  = server-side MCP bug → use REST/browser fallback.
- Browser fallback: skill `confluence-browser-access` (Chrome remote-debugging session). Preferred when MCP is flaky.
Related: [[access]], [[oracle-ofs-index]].
