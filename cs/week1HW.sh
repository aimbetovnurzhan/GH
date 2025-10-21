#!/bin/bash

start="AI-Powered Learning"
end="2025 Usefy"
outfile="/c/Users/NRG/GH/CS/week1HwRes.txt"

curl https://www.usefy.com/ \
| sed 's/<[^>]*>//g' \
| sed -n "/$start/,/$end/p" \
> "$outfile"