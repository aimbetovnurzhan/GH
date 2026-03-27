#!/bin/bash
set -euo pipefail
LOG_FILE="/c/Users/NRG/Gitlog.txt"
MAX_SIZE=500000   # 500 KB

# ---------- Ротация логов ----------
if [ -f "$LOG_FILE" ]; then
    FILE_SIZE=$(stat -c%s "$LOG_FILE")
    if [ "$FILE_SIZE" -gt "$MAX_SIZE" ]; then
        mv "$LOG_FILE" "${LOG_FILE}.1"
        touch "$LOG_FILE"
    fi
fi

red()    { echo -e "\e[31m$1\e[0m"; }
green()  { echo -e "\e[32m$1\e[0m"; }
log()    { echo "$1" | tee -a "$LOG_FILE"; }

log "$(date '+%Y-%m-%d_%H:%M:%S') - started"

# ---------- Репозиторий GH ----------
cd /c/Users/NRG/GH
if git pull origin main >> "$LOG_FILE" 2>&1; then
    green "GH: Pull OK"
else
    red "GH: Pull FAILED"
fi
if [ -n "$(git status --porcelain)" ]; then
    git add .
    git commit -m "Auto commit $(date '+%Y-%m-%d_%H:%M:%S')"
    git push origin main
    green "GH: Changes pushed"
else
    log "GH: No changes"
fi

# ---------- Репозиторий LMS ----------
cd /c/Users/NRG/LMS
if git pull origin main >> "$LOG_FILE" 2>&1; then
    green "LMS: Pull OK"
else
    red "LMS: Pull FAILED"
fi
if [ -n "$(git status --porcelain)" ]; then
    git add .
    git commit -m "Auto commit $(date '+%Y-%m-%d_%H:%M:%S')"
    git push origin main
    green "LMS: Changes pushed"
else
    log "LMS: No changes"
fi

log "--------------------------------------------"