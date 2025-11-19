#!/bin/bash
set -euo pipefail
LOG_FILE="/c/Users/NRG/Gitlog.txt"
echo "$(date '+%Y-%m-%d_%H:%M:%S'): запуск" >> "$LOG_FILE"
cd /c/Users/NRG/GH

#echo "Количество уникальных дней с коммитами:"
#git log --since="1 year ago" --format="%ad" --date=short | sort -u | wc -l

#echo "Количество коммитов за сегодня:"
#git log --since=midnight --oneline | wc -l

if [ -n "$(git status --porcelain)" ]; then
    if git add . >> "$LOG_FILE" 2>&1; then
        echo "Файлы добавлены"
    else
        echo "ОШИБКА при git add" >> "$LOG_FILE"
        exit 1
    fi
    if git commit -m "$(date '+%Y-%m-%d_%H:%M:%S')" >> "$LOG_FILE" 2>&1; then
        echo "Коммит создан"
    else
        echo "ОШИБКА при создании коммита" >> "$LOG_FILE"
        exit 1
    fi
    if git push origin main >> "$LOG_FILE" 2>&1; then
        echo "$(date '+%Y-%m-%d_%H:%M:%S'): Изменения отправлены в GitHub" >> "$LOG_FILE"
    else
        echo "$(date '+%Y-%m-%d_%H:%M:%S'): ОШИБКА при отправке" >> "$LOG_FILE"
    fi
else
    echo "$(date '+%Y-%m-%d_%H:%M:%S'): Изменений нет" >> "$LOG_FILE"
fi

{
  echo "Количество уникальных дней с коммитами:"
  git log --since="1 year ago" --format="%ad" --date=short | sort -u | wc -l

  echo "Количество коммитов за сегодня:"
  git log --since=midnight --oneline | wc -l
} | tee -a "$LOG_FILE"

echo "---" >> "$LOG_FILE"
sleep 5
