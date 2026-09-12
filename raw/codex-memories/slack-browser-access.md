# Slack Browser Access Memory (macOS)

## Goal
Use local browser session auth to access Slack Web API when MCP Slack connector is unavailable.

## How it works

1. Read browser safe-storage passphrase from macOS Keychain (`security find-generic-password`).
2. Derive AES key with `PBKDF2-HMAC-SHA1` (`salt=saltysalt`, `iterations=1003`, `key_len=16`).
3. Decrypt `.slack.com` cookies (`d`, `x`) from browser `Cookies` DB.
4. Extract `xoxc-...` tokens from `Local Storage/leveldb`.
5. Validate token/workspace via Slack `auth.test`.

## Default local tool

- Script:
  - `/Users/oleksandrgrytsenko/.codex/skills/slack-browser-access/scripts/slack_browser_auth.py`

## Typical usage

1. List available workspaces:

```bash
python3 /Users/oleksandrgrytsenko/.codex/skills/slack-browser-access/scripts/slack_browser_auth.py workspaces
```

2. Export auth for selected team:

```bash
eval "$(python3 /Users/oleksandrgrytsenko/.codex/skills/slack-browser-access/scripts/slack_browser_auth.py export --team-id T0168MWKBK7)"
```

3. Call Slack API:

```bash
python3 /Users/oleksandrgrytsenko/.codex/skills/slack-browser-access/scripts/slack_browser_auth.py call \
  --use-env \
  --method conversations.history \
  --param channel=C08A5KQBESX \
  --param limit=10
```

## Safety rules

- Never print full token/cookies in summaries.
- Keep credentials in memory or shell env only.
- Ask before any external write action.
