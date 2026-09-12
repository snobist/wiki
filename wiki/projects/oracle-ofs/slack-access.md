# Slack access (browser-derived, macOS)

`Last-verified: 2026-08-31` (bundle; paths are old-Mac). Source: `raw/codex-memories/slack-browser-access.md`.
Method: Keychain browser Safe-Storage passphrase → PBKDF2-HMAC-SHA1 (`saltysalt`, 1003 iters, 16 bytes) → decrypt
`.slack.com` cookies `d`,`x` from browser Cookies DB → `xoxc-…` tokens from Local Storage leveldb → validate via `auth.test`.
Script: `slack_browser_auth.py` (`workspaces` / `export --team-id` / `call --use-env --method …`) in skill `slack-browser-access`.
Known team id `T0168MWKBK7`. Rules: never print tokens; creds live in env only; ask before any write.
**Port needed**: skill path `/Users/oleksandrgrytsenko/.codex/skills/…` → new Mac. Cowork VM cannot read Keychain.
Related: [[access]].
