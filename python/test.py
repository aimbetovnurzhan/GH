{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d0f7027b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "unknown option: -f\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\NRG\\anaconda3\\lib\\site-packages\\IPython\\core\\interactiveshell.py:3465: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "#!/usr/bin/python3\n",
    "import sys\n",
    "\n",
    "def file_parser(filename):\n",
    "    with open(file_name, 'r') as fn:\n",
    "        text = fn.read().replace(\"\\n\", \" \").replace(\".\", \"\").replace(\",\", \"\").split(\" \")\n",
    "        word_cnt = {}\n",
    "        for word in text:\n",
    "            word_cnt[text] =  word_cnt[text, \"0\"] + 1\n",
    "    return word_cnt\n",
    "\n",
    "def print_words(file_name):\n",
    "    print(file_parser(file_name))\n",
    "    \n",
    "def print_top(file_name):\n",
    "    print(file_name)\n",
    "        \n",
    "def main():\n",
    "  if len(sys.argv) != 3:\n",
    "    print('usage: ./wordcount.py {--count | --topcount} file')\n",
    "    sys.exit(1)\n",
    "\n",
    "  option = sys.argv[1]\n",
    "  filename = sys.argv[2]\n",
    "  if option == '--count':\n",
    "    print_words(filename)\n",
    "  elif option == '--topcount':\n",
    "    print_top(filename)\n",
    "  else:\n",
    "    print('unknown option: ' + option)\n",
    "    sys.exit(1)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "  main()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
