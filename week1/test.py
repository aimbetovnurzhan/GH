# comment symbol
def my_function():
    print("hello again")

#print("Hello, World")
#my_function()

def greating_function(name, extra_word):
    print("hello, " + name + ". Welcome and " + extra_word)

def greating_function(name, extra_word):
    print("hello, %s. Welcome and %s"%(name,extra_word))

def sum_two_numbers(x, y):
    return x + y

def multiply_two_numbers(x, y):
    return x*y


#greating_function("Nurzhan","bye bye")
#greating_function("Aizhan", "make your self comfortable")
z=sum_two_numbers(9,7.5)
#print(z)
#we have to count 21*21 + 46*47

print(sum_two_numbers(multiply_two_numbers(21,21),multiply_two_numbers(46,47)))

help(print)