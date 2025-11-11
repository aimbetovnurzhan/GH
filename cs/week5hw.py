import random as rd

answers = {-2: "Too Low", -1: "Little low", 0: "You guessed it, great job", 1: "Little high", 2: "Too high", }

def check_attempt(guessing_number, attempt): # Function returns code of result
    if attempt == guessing_number:
        return 0
    elif attempt < guessing_number:
        if attempt - guessing_number < -5:
            return -2
        else:
            return -1
    else:
        if attempt - guessing_number <= 5:
            return 1
        else:
            return 2


    if attempt > guessing_number:
        if attempt - guessing_number > 5:
            return 
            print("Too high")
        else:
            print("Little high")
    elif attempt < guessing_number:
        if guessing_number - attempt > 5:
            print("Too low")
        else:
            print("Little low")
    else:
        print("Nice job, correct, you won! ))")

a = rd.randint(1, 100)
attempts_cnt = 5
print("Gues the number, you have %d attempts to guess it" %(attempts)) #, a)

for attempt in range(attempts):
    attempt = int(input("Your %d attempt is: " %(attempt+1)))
    if attempt > a:
        if attempt - a > 5:
            print("Too high")
        else:
            print("Little high")
    elif attempt < a:
        if a - attempt > 5:
            print("Too low")
        else:
            print("Little low")
    else:
        print("Nice job, correct, you won! ))")
        break
else:
    print("Sorry, you lost )))")