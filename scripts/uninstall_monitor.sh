#!/bin/sh
set -eu

LABEL="com.oico.validation-monitor"
PLIST="$HOME/Library/LaunchAgents/$LABEL.plist"
launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null || true
rm -f "$PLIST"
echo "uninstalled $LABEL; bounded logs remain under $HOME/Library/Application Support/OICO/monitor"
