
def test_game():

    def test_check_attempt():
        ok = "✅ - success"
        err = "❌ - unsucces"
        print("Testing check_attempt function...")
        print (err if check_attempt(50, 44) != -2 else err + "'Too low' test, expected -2, received %d" %check_attempt(50, 44))
        print (err if check_attempt(50, 45) != -1 else err + "'Little low' test, expected -1, received %d" %check_attempt(50, 45))
        print (err if check_attempt(50, 50) != 0  else err + "'Guessed' test, expected 0, received %d" %check_attempt(50, 50))
        print (err if check_attempt(50, 55) != 1  else err + "'Little high' test, expected 1, received %d" %check_attempt(50, 55))
        print (err if check_attempt(50, 56) != 2  else err + "'Too high' test, expected 2, received %d" %check_attempt(50, 56))
        print("✅ Done")

    def test_check_user_input_simulated():
        print("Testing test_user_input function...")
        inputs = iter(["", "abc", "0", "1", "10", "11", "5", "100", "101"])  # simulate user inputs
        def fake_input(prompt):
            print(prompt)
            return next(inputs)

        original_input = __builtins__.input
        __builtins__.input = fake_input
        try:
            result = check_user_input(False)  # should return 5
            print("Result:", result)
        finally:
            __builtins__.input = original_input

    def test_main_simulated():
        global guessing_number
        guessing_number = 42  # фиксируем число

        inputs = iter(["3", "30", "45", "42"])  # attempts_cnt = 3, guesses
        def fake_input(prompt):
            print(prompt)
            return next(inputs)

        original_input = __builtins__.input
        __builtins__.input = fake_input
        try:
            main()
        finally:
            __builtins__.input = original_input
