#!/usr/bin/env bash
# Sync the wiki with its private git remote. Safe to run from macOS Terminal or from a Cowork session shell.
# Usage: bin/sync.sh ["commit message"]
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
export GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=safe.directory GIT_CONFIG_VALUE_0='*'
G="git -c user.name=Alex -c user.email=snobist@gmail.com"

# Token auth over HTTPS, read from .secrets/git-token (never committed).
if [ -f .secrets/git-token ]; then
  ASKPASS="$(mktemp)"; trap 'rm -f "$ASKPASS"' EXIT
  printf '#!/bin/sh\ncase "$1" in *sername*) echo "x-access-token";; *) cat "%s/.secrets/git-token";; esac\n' "$ROOT" > "$ASKPASS"
  chmod 700 "$ASKPASS"; export GIT_ASKPASS="$ASKPASS" GIT_TERMINAL_PROMPT=0
fi

[ -d .git ] || { $G init -q -b main; echo "initialised repo"; }
if [ ! "$($G remote 2>/dev/null)" ] && [ -f .secrets/git-remote ]; then
  $G remote add origin "$(tr -d '[:space:]' < .secrets/git-remote)"
fi

# Refuse to commit anything that looks like a secret.
PAT='(xox[abcp]-[0-9A-Za-z-]{10,}|ghp_[0-9A-Za-z]{20,}|github_pat_[0-9A-Za-z_]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY)'
HITS="$(git ls-files -o -c --exclude-standard | grep -v '^bin/sync.sh$' | tr '\n' '\0' | xargs -0 grep -lEI "$PAT" 2>/dev/null || true)"
if [ -n "$HITS" ]; then
  echo "ABORT: secret-looking content found — remove it or move to .secrets/:" >&2; echo "$HITS" >&2; exit 2
fi

$G add -A
if ! $G diff --cached --quiet; then
  $G commit -q -m "${1:-sync $(date +%Y-%m-%d\ %H:%M)}"
  echo "committed"
else
  echo "nothing to commit"
fi

if $G remote | grep -q origin; then
  $G pull -q --rebase origin main 2>/dev/null || $G pull --rebase origin main || true
  $G push -q -u origin main && echo "pushed" || echo "push failed (remote/token not set up? see wiki/access.md)"
else
  echo "no remote configured — put the HTTPS URL in .secrets/git-remote and a PAT in .secrets/git-token"
fi
