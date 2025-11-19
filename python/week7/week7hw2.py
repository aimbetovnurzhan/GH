#!/usr/bin/python3

import sys

def print_words(filename):
  word_count = parse_file(filename)
  for word in sorted(word_count.keys()):
    print(word, word_count[word])

def print_top(filename):
  word_count = parse_file(filename)
  sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
  for word, count in sorted_words[:20]:
    print(word, count)

def parse_file(filename):
  word_count = {}
  with open(filename, 'r') as f:
    words =  f.read()\
              .lower()\
              .replace('\n', ' ')\
              .translate(str.maketrans('', '', '.,!?;:'))\
              .split()
  for word in words:
    word_count[word] = word_count.get(word, 0) + 1
  return word_count

def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()