#!/bin/bash

start="AI-Powered Learning"
end="reserved"
outfile="/c/Users/NRG/GH/CS/week1HwRes.txt"

curl https://www.usefy.com/ \
| sed 's/<[^>]*>//g' \
| perl -0777 -ne "print \$& if /$start(.*?)$end/s" \
> "$outfile"

