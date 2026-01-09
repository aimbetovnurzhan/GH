#!/bin/bash
set -euo pipefail
LOG_FILE="/c/Users/NRG/Gitlog.txt"
echo "------------------------------------" >> "$LOG_FILE"
echo "$(date '+%Y-%m-%d_%H:%M:%S') - started" >> "$LOG_FILE"
cd /c/Users/NRG/GH

if git pull origin main >> "$LOG_FILE" 2>&1; then
    echo "Pull OK"
else
    echo "Pull FAILED"
    exit 1
fi

if [ -n "$(git status --porcelain)" ]; then
    if git add . >> "$LOG_FILE" 2>&1; then
        echo "Files added"
    else
        echo "Git add error" >> "$LOG_FILE"
        exit 1
    fi
    if git commit -m "$(date '+%Y-%m-%d_%H:%M:%S')" >> "$LOG_FILE" 2>&1; then
        echo "Commit created"
    else
        echo "Commit creation error" >> "$LOG_FILE"
        exit 1
    fi
    if git push origin main >> "$LOG_FILE" 2>&1; then
        echo "$(date '+%Y-%m-%d_%H:%M:%S'): Changes Pushed to GitHub" >> "$LOG_FILE"
    else
        echo "$(date '+%Y-%m-%d_%H:%M:%S'): Pushing error" >> "$LOG_FILE"
    fi
else
	echo "No changes"
    echo "$(date '+%Y-%m-%d_%H:%M:%S'): No changes" >> "$LOG_FILE"
fi

{
  echo "Uniq days with commits:"
  git log --since="1 year ago" --format="%ad" --date=short | sort -u | wc -l

  echo "Today's commits count:"
  git log --since=midnight --oneline | wc -l
} | tee -a "$LOG_FILE"

sleep 5