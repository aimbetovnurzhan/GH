#!/usr/bin/python3

import random as rd

min_val = 1
default_attempts_cnt = 5
max_attempts_cnt = 10
max_guessing_number_val = 100
guessing_number = rd.randint(1, max_guessing_number_val)
answers = {-2: "Too Low", -1: "Little low", 0: "You guessed it, great job", 1: "Little high", 2: "Too high", }

def check_user_input(is_attempt): # returns number in range 0 to 100/10 or 0 (user_exit/defaultval) for True/False.  
    max_val = max_attempts_cnt
    break_msg = "to continue with %d attempts: " %default_attempts_cnt
    if is_attempt:
        max_val = max_guessing_number_val
        break_msg = "if you're giving up: "
    while True:
        user_input = input("Enter a number or press 'Enter' %s" %break_msg)
        if user_input.isdigit():
            user_input = int(user_input)
            if min_val <= user_input <= max_val:
                return user_input
            else:
                print("Number should be between 1 and %d" %max_val)
        else:
            if user_input == "":
                if is_attempt:
                    return 0
                else:
                    return default_attempts_cnt
            else:
                print("You should enter a number")

def check_attempt(guessing_number, attempt): # Function returns code of result
    if attempt < guessing_number:
        if attempt - guessing_number < -5:
            return -2
        else:
            return -1
    elif attempt == guessing_number:
        return 0
    else:
        if attempt - guessing_number <= 5:
            return 1
        else:
            return 2

def main():
    print("Welcome to guessing number game")
    attempts_cnt = check_user_input(False)

    for i in range(1, attempts_cnt + 1):
        print("Attempt #%d" %i)
        attempt = check_user_input(True)
        if attempt == 0:
            print("L_user gave up, see ya xD")
            return
        attempt_res = check_attempt(guessing_number, attempt)
        print(answers[attempt_res])
        if attempt_res == 0:
            break
    else:
        print("L_user, probably you'll win next time xD")

if __name__ == '__main__':
  main()



"""
def main():
  print('donuts')
  # Each line calls donuts, compares its result to the expected for that call.
  test(donuts(4), 'Number of donuts: 4')
  test(donuts(9), 'Number of donuts: 9')
  test(donuts(10), 'Number of donuts: many')
  test(donuts(99), 'Number of donuts: many')

  print()
  print('both_ends')
  test(both_ends('spring'), 'spng')
  test(both_ends('Hello'), 'Helo')
  test(both_ends('a'), '')
  test(both_ends('xyz'), 'xyyz')


  print()
  print('fix_start')
  test(fix_start('babble'), 'ba**le')
  test(fix_start('aardvark'), 'a*rdv*rk')
  test(fix_start('google'), 'goo*le')
  test(fix_start('donut'), 'donut')

  print()
  print('mix_up')
  test(mix_up('mix', 'pod'), 'pox mid')
  test(mix_up('dog', 'dinner'), 'dig donner')
  test(mix_up('gnash', 'sport'), 'spash gnort')
  test(mix_up('pezzy', 'firm'), 'fizzy perm')
"""