#!/usr/bin/python3

import random as rd

guessing_number = rd.randint(1, 100)
answers = {-2: "Too Low", -1: "Little low", 0: "You guessed it, great job", 1: "Little high", 2: "Too high", }
attempts_cnt = 5

def check_user_attempts_count(attempts_cnt, user_input):
    resp_msg = False    # Means that user selected value by default
    if user_input.isdigit():
        if 0 < user_input <= 10:
            resp_msg = True # User entered own attempts count
            attempts_cnt = user_input
        else:
            resp_msg = "Number should be more than 0, less or equal to 10"
    elif user_input != "":
        resp_msg = "You should enter a number"
    return attempts_cnt, resp_msg


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
    print("Welcome to guessing number game, do you want to enter attempts count?")

    while True: #checking user input
        user_input = input("Enter attempts count (maximum is 10) or press enter to continue with %d attempts" %attempts_cnt)
        checking_result = check_user_attempts_count(attempts_cnt, user_input)
        if checking_result[1] == True:
            attempts_cnt = checking_result[0]
            break
        elif checking_result[1] != False:
            print(checking_result[1])

    for i in range(1, attempts_cnt + 1):
        attempt = int(input("Your %d attempt is: " %i)) # Have to add additional check for input (isdigit)
        attempt_res = check_attempt(guessing_number, attempt)
        print(answers[attempt_res])
        if attempt_res == 0:
            break
    else:
        print("Probably you'll win next time, loser xD")


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


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()