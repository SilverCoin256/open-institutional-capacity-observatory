#!/bin/sh
set -eu

LABEL="com.oico.validation-monitor"
ROOT="${OICO_MONITOR_DIR:-$HOME/Library/Application Support/OICO/monitor}"
launchctl print "gui/$(id -u)/$LABEL" 2>/dev/null || true
printf '\nState directory: %s\n' "$ROOT"
if [ -f "$ROOT/state.json" ]; then
  sed -n '1,80p' "$ROOT/state.json"
else
  printf '%s\n' 'No checks have completed.'
fi
