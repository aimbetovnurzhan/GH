import random as rd

def check_attempt(guessing_number, attempt):
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