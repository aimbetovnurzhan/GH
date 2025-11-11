import random as rd

a = rd.randint(1, 100)
attempts = 5
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