#!/usr/bin/env bash
# One-time install on the Mac: a LaunchAgent that runs bin/sync.sh every 15 minutes and at login.
# Run from Terminal:  bash ~/Documents/wiki/bin/install-sync-agent.sh
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LABEL=com.alex.wiki-sync
PLIST="$HOME/Library/LaunchAgents/$LABEL.plist"
mkdir -p "$HOME/Library/LaunchAgents" "$ROOT/.secrets"
command -v git >/dev/null || { echo "git not found — install Xcode Command Line Tools: xcode-select --install"; exit 1; }
cat > "$PLIST" <<PL
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>$LABEL</string>
  <key>ProgramArguments</key><array><string>/bin/bash</string><string>$ROOT/bin/sync.sh</string></array>
  <key>StartInterval</key><integer>900</integer>
  <key>RunAtLoad</key><true/>
  <key>StandardOutPath</key><string>$ROOT/.secrets/sync.log</string>
  <key>StandardErrorPath</key><string>$ROOT/.secrets/sync.log</string>
  <key>EnvironmentVariables</key><dict><key>PATH</key><string>/usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin</string></dict>
</dict></plist>
PL
launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$PLIST"
launchctl kickstart -k "gui/$(id -u)/$LABEL"
sleep 3; echo "--- last sync output:"; tail -n 5 "$ROOT/.secrets/sync.log" || true
echo "Installed $LABEL (every 15 min + at login). Uninstall: launchctl bootout gui/$(id -u)/$LABEL && rm '$PLIST'"
