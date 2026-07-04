#!/bin/bash
input=$(cat)
command=$(printf '%s' "$input" | sed -n 's/.*"command"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p')
echo "$(date '+%Y-%m-%d %H:%M:%S') | $(printf '%s' "$command" | head -c 120)" >> session-log.md
