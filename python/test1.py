#!/usr/bin/python3
import sys
testArgv = ['test1.py', '--count', 'c:/Users/NRG/GH/python/small.txt']

def file_parser(file_name):
    with open(file_name, 'r') as fn:
        text = fn.read().replace("\n", " ").replace(".", "").replace(",", "").split(" ")
        word_cnt = {}
        for word in text:
            word_cnt[word] =  word_cnt.get(word, 0) + 1
    return word_cnt

def print_words(file_name):
    print(file_parser(file_name))
    
def print_top(file_name):
    print(file_name)
        
def main():
#   if len(sys.argv) != 3:
  if len(testArgv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

#   option = sys.argv[1]
#   filename = sys.argv[2]
  option = testArgv[1]
  filename = testArgv[2]


  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
  