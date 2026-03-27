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

# ---------- Универсальная функция ----------
process_repo() {
    local path=$1
    local name=$2
    local branch=$3

    cd "$path"

    if git pull origin "$branch" >> "$LOG_FILE" 2>&1; then
        green "$name: Pull OK"
    else
        red "$name: Pull FAILED"
        exit 1
    fi

    if [ -n "$(git status --porcelain)" ]; then
        if git add . >> "$LOG_FILE" 2>&1; then
            green "$name: Files added"
        else
            red "$name: Git add error"
            exit 1
        fi
        if git commit -m "$(date '+%Y-%m-%d_%H:%M:%S')" >> "$LOG_FILE" 2>&1; then
            green "$name: Commit created"
        else
            red "$name: Commit creation error"
            exit 1
        fi
        if git push origin "$branch" >> "$LOG_FILE" 2>&1; then
            green "$name: Changes Pushed to GitHub"
        else
            red "$name: Pushing ended with error"
        fi
    else
        log "$(date '+%Y-%m-%d_%H:%M:%S'): $name: No changes"
    fi
}

# ---------- Репозитории ----------
process_repo "/c/Users/NRG/GH" "GH" "main"
process_repo "/c/Users/NRG/LMS" "LMS" "main"
process_repo "/c/Users/NRG/LC" "LC" "main"

# ---------- Статистика ----------
stats_repo() {
    local path=$1
    local name=$2

    cd "$path"
    {
      echo "$name: Uniq days with commits:"
      git log --since="1 year ago" --format="%ad" --date=short | sort -u | wc -l

      echo "$name: Today's commits count:"
      git log --since=midnight --oneline | wc -l
      echo "--------------------------------------------"
    } | tee -a "$LOG_FILE"
}

stats_repo "/c/Users/NRG/GH" "GH"
stats_repo "/c/Users/NRG/LMS" "LMS"
stats_repo "/c/Users/NRG/LC" "LC"

sleep 5
