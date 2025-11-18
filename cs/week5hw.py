#!/usr/bin/python3

import random as rd
import sys

min_val = 1
default_attempts_cnt = 5
max_attempts_cnt = 10
max_guessing_number_val = 100
guessing_number = rd.randint(1, max_guessing_number_val)
answers = {-2: "❌ - too Low", -1: "❌ - little low", 0: "✅ - you guessed it, great job", 1: "❌ - little high", 2: "❌ - too high", }

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

def test_game():

    def test_check_attempt():
        ok = "✅ - success"
        err = "❌ - unsucces"
        print("\nTesting check_attempt function...\n")
        print ("'Too low' test, expected -2, received %d.." %check_attempt(50, 44) + ok if check_attempt(50, 44) == -2 else err)
        print ("'Little low' test, expected -1, received %d.." %check_attempt(50, 45) + ok if check_attempt(50, 45) == -1 else err)
        print ("'Guessed' test, expected 0, received %d.." %check_attempt(50, 50) + ok if check_attempt(50, 50) == 0  else err)
        print ("'Little high' test, expected 1, received %d.." %check_attempt(50, 55) + ok if check_attempt(50, 55) == 1  else err)
        print ("'Too high' test, expected 2, received %d.." %check_attempt(50, 56) + ok if check_attempt(50, 56) == 2  else err)
        print("✅ Done")

    def test_check_user_input_simulated():
        import itertools
        print("\nTesting test_user_input function...")
        inputs = [
            [""], 
            [0, 2],
            [1],
            [10],
            [100, 3],
            [101, 4],
            ["abc", 1]
        ]
        is_attempt_vals = [True, False]
        for is_attempt in is_attempt_vals:
            print(f"\n🔁 Test with {is_attempt} input value")
            for i, j in enumerate(inputs, start = 1):
                preview_iter, fake_user_input = itertools.tee(iter(j))
                preview = next(preview_iter)
                print(f"Test #{i} - input: {preview}")

                def fake_input(prompt):
                    print(prompt)
                    a = next(fake_user_input)
                    print(a)
                    return str(a)

                original_input = __builtins__.input
                __builtins__.input = fake_input
                try:
                    result = check_user_input(is_attempt)  # should return 5
                    print("Result:", result)
                finally:
                    __builtins__.input = original_input

    def test_main_simulated():
        print("\nTesting main function...\n")
        global guessing_number
        guessing_number = 42  # фиксируем число

        inputs = iter(["3", "30", "45", "42"])  # attempts_cnt = 3, guesses
        def fake_input(prompt):
            print(prompt)
            a = next(inputs)
            print(a)
            return a


        original_input = __builtins__.input
        __builtins__.input = fake_input
        try:
            main()
        finally:
            __builtins__.input = original_input
    
    test_check_attempt()
    test_check_user_input_simulated()
    test_main_simulated()

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        print(" ------ Test starting ------")
        test_game()
    else:
        main()