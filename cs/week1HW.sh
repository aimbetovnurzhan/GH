#!/bin/bash

#curl https://www.usefy.com/ -o /c/Users/NRG/GH/CS/week1HwRes.txt
#curl https://www.usefy.com/ | sed 's/<[^>]*>//g' > /c/Users/NRG/GH/CS/week1HwRes.txt

curl https://www.usefy.com/ | \
  sed 's/<[^>]*>//g' | \
  sed 's/&[a-z]*;/ /g' | \
  sed 's/^[[:space:]]*//g' | \
  sed '/^$/d' | \
  grep -i -E "(usefy|course|learning|organization|AI|platform|video)" \
  > /c/Users/NRG/GH/CS/week1HwRes.txt