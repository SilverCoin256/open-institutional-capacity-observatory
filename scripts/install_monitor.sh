#!/bin/sh
set -eu

LABEL="com.oico.validation-monitor"
ROOT="$HOME/Library/Application Support/OICO/monitor"
PLIST="$HOME/Library/LaunchAgents/$LABEL.plist"
PROJECT="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
PYTHON3="${OICO_PYTHON:-$(command -v python3)}"

if [ -z "$PYTHON3" ]; then
  echo "python3 not found" >&2
  exit 1
fi

mkdir -p "$ROOT" "$HOME/Library/LaunchAgents"
cat > "$PLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>$LABEL</string>
  <key>ProgramArguments</key><array><string>$PYTHON3</string><string>$PROJECT/scripts/monitor_public_activity.py</string></array>
  <key>EnvironmentVariables</key><dict><key>OICO_MONITOR_DIR</key><string>$ROOT</string></dict>
  <key>StartInterval</key><integer>21600</integer>
  <key>RunAtLoad</key><true/>
  <key>LowPriorityIO</key><true/>
  <key>ProcessType</key><string>Background</string>
  <key>StandardOutPath</key><string>$ROOT/launchd.out.log</string>
  <key>StandardErrorPath</key><string>$ROOT/launchd.err.log</string>
</dict></plist>
EOF

launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$PLIST"
echo "installed $LABEL"
