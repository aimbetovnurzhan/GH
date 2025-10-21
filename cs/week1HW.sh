#!/bin/bash

start="colorScheme"
end="Quick LinksLegalConnect"
outfile="/c/Users/NRG/GH/CS/week1HwRes.txt"

curl https://www.usefy.com/ \
| sed 's/<[^>]*>//g' \
| perl -0777 -ne "print \$1 if /$start(.*?)$end/s" \
> "$outfile"

