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

# ---------- Репозиторий GH ----------
cd /c/Users/NRG/GH

if git pull origin main >> "$LOG_FILE" 2>&1; then
    green "GH: Pull OK"
else
    red "GH: Pull FAILED"
    exit 1
fi

if [ -n "$(git status --porcelain)" ]; then
    if git add . >> "$LOG_FILE" 2>&1; then
        green "GH: Files added"
    else
        red "GH: Git add error"
        exit 1
    fi
    if git commit -m "$(date '+%Y-%m-%d_%H:%M:%S')" >> "$LOG_FILE" 2>&1; then
        green "GH: Commit created"
    else
        red "GH: Commit creation error"
        exit 1
    fi
    if git push origin main >> "$LOG_FILE" 2>&1; then
        green "GH: Changes Pushed to GitHub"
    else
        red "GH: Pushing ended with error"
    fi
else
    log "$(date '+%Y-%m-%d_%H:%M:%S'): GH: No changes"
fi

# ---------- Репозиторий LMS ----------
cd /c/Users/NRG/LMS

if git pull origin main >> "$LOG_FILE" 2>&1; then
    green "LMS: Pull OK"
else
    red "LMS: Pull FAILED"
    exit 1
fi

if [ -n "$(git status --porcelain)" ]; then
    if git add . >> "$LOG_FILE" 2>&1; then
        green "LMS: Files added"
    else
        red "LMS: Git add error"
        exit 1
    fi
    if git commit -m "$(date '+%Y-%m-%d_%H:%M:%S')" >> "$LOG_FILE" 2>&1; then
        green "LMS: Commit created"
    else
        red "LMS: Commit creation error"
        exit 1
    fi
    if git push origin main >> "$LOG_FILE" 2>&1; then
        green "LMS: Changes Pushed to GitHub"
    else
        red "LMS: Pushing ended with error"
    fi
else
    log "$(date '+%Y-%m-%d_%H:%M:%S'): LMS: No changes"
fi


# ---------- Статистика GH ----------
cd /c/Users/NRG/GH
{
  echo "GH: Uniq days with commits:"
  git log --since="1 year ago" --format="%ad" --date=short | sort -u | wc -l

  echo "GH: Today's commits count:"
  git log --since=midnight --oneline | wc -l
  echo "--------------------------------------------"
} | tee -a "$LOG_FILE"

# ---------- Статистика LMS ----------
cd /c/Users/NRG/LMS
{
  echo "LMS: Uniq days with commits:"
  git log --since="1 year ago" --format="%ad" --date=short | sort -u | wc -l

  echo "LMS: Today's commits count:"
  git log --since=midnight --oneline | wc -l
  echo "--------------------------------------------"
} | tee -a "$LOG_FILE"

sleep 5