# Returning Functions

# Example of defining a function that returns a function and prints
# something to the console.
# These are also known as  function creator

# Creating a function named 'create_printer()' this function body
# has another function named 'printer()' that prints the string
# 'Hello functional', then 'create_printer()' returns the 'printer()'
# function at the end
def create_printer():
    def printer():
        print('Hello functional')
    # Note 1; Note that here the 'return statment ' returns the function
    # itself using the syntax 'printer' without adding the double parenthesis '()'
    # Note 2; When working in functional programming use the function name such as
    # 'printer' to refer to the functional itself and use the function name with parenthesis
    # when you want to make a call to the function or call the function 'printer()'
    return printer


# Creating a variable named 'my_printer' and assigning it to the function
# call 'create_printer()'. 'my_printer' name equals to whatever value that's being
# returned  by the 'create_printer()' function.
# Note 3: We created a function variable here using 'my_printer' and assign it to
# 'create_printer()'
my_printer = create_printer()

# This line is calling the 'my_printer()' function
# Note 4; this is like magic since we never defined and declare the
# 'my_printer()' as a function with body and return value.
# Python automaitcally knows you're calling the 'my_printer()'
# function even though you only create a variable named 'my_printer'
# and assigned it to 'create_printer()' function so far.
my_printer()


def double(x):
    return x * 2


def triple(x):
    return x * 3


def quadruple(x):
    return x * 4


def create_multiplier(a):
    def multiplier(x):
        return x * a

    return multiplier


double = create_multiplier(2)
triple = create_multiplier(3)
quadruple = create_multiplier(4)

print(double(5))
print(triple(6))
print(quadruple(7))
