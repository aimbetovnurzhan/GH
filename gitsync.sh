#!/bin/bash
set -euo pipefail
LOG_FILE="/c/Users/NRG/Gitlog.txt"

# ---------- Ротация логов по размеру ----------
MAX_SIZE=500000   # 500 KB

if [ -f "$LOG_FILE" ]; then
    FILE_SIZE=$(stat -c%s "$LOG_FILE")
    if [ "$FILE_SIZE" -gt "$MAX_SIZE" ]; then
        mv "$LOG_FILE" "${LOG_FILE}.1"
        touch "$LOG_FILE"
    fi
fi

# ---------- Цветные функции ----------
red()    { echo -e "\e[31m$1\e[0m"; }
green()  { echo -e "\e[32m$1\e[0m"; }

# ---------- Логирование ----------
log() {
    echo "$1" | tee -a "$LOG_FILE"
}

log "$(date '+%Y-%m-%d_%H:%M:%S') - started"
cd /c/Users/NRG/GH

if git pull origin main >> "$LOG_FILE" 2>&1; then
    green "Pull OK"
else
    red "Pull FAILED"
    exit 1
fi

if [ -n "$(git status --porcelain)" ]; then
    if git add . >> "$LOG_FILE" 2>&1; then
        green "Files added"
    else
        red "Git add error"
        exit 1
    fi
    if git commit -m "$(date '+%Y-%m-%d_%H:%M:%S')" >> "$LOG_FILE" 2>&1; then
        green "Commit created"
    else
        red "Commit creation error"
        exit 1
    fi
    if git push origin main >> "$LOG_FILE" 2>&1; then
        green "Changes Pushed to GitHub"
    else
        red "Pushing ended with error"
    fi
else
    log "$(date '+%Y-%m-%d_%H:%M:%S'): No changes"
fi

{
  echo "Uniq days with commits:"
  git log --since="1 year ago" --format="%ad" --date=short | sort -u | wc -l

  echo "Today's commits count:"
  git log --since=midnight --oneline | wc -l
  echo "------------------------------------"
} | tee -a "$LOG_FILE"

sleep 5