#!/bin/bash
input=$(cat)
f=$(printf '%s' "$input" | sed -n 's/.*"file_path"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p')
if [[ "$f" == charts/*.png ]]; then
  n=$(ls charts/*.png 2>/dev/null | wc -l)
  echo "Chart saved: $(basename "$f") — $n/5 charts complete"
fi
