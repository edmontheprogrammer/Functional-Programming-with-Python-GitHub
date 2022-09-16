# Closure means that when we define a function that returns another function
# that function we return still has access to the internal scope of the function
# that returned it. To See what I mean, let's code out an example
# that demonstrate closure.

# defining a function named 'create_printer()'
def create_printer():
    # creating a variable named 'my_favorite_number'
    my_favorite_number = 42

    # defining another function inside 'create_printer()' function named
    # 'printer()', so it's a function inside another function.
    #  the job of the 'printer()' function is to print some string
    # with the variable 'my_favorite_number' using format string
    def printer():
        print(f'My favorite number is {my_favorite_number}')

    # the 'create_printer()' function is returning the 'printer' function
    # itself.
    # Note 1; Note that we are refering to the function itself using 'printer'
    # or the function named itself without the parenthesis like we normally do
    # when calling functions, 'printer()'.
    return printer


# Creating a function variable named 'myPrinter' and assigning it to the
# function call 'create_printer()'
my_printer = create_printer()
# calling the 'myPrinter()' function.
my_printer()

# creating a function named 'create_counter()'


def create_counter():
    # creating a variable named count and assign it a value of 0
    count = 0

    # creating an inner function named 'get_count()' and make it
    # return 'count' variable
    def get_count():
        return count

    # creating another inner function named 'increment()' that
    # increaments 'count' variable by 1
    def increment():
        # this line 'nonlocal count' tells Python that the 'count' variable we are using
        # here is the one defined in the outter scope.
        # If we do not add this line 'nonlocal count', Python will assume
        # we are trying to create a new variable with the same name inside the
        # 'increment()' function.
        nonlocal count
        count += 1

    # a return statment that returns a tuple that returns the
    # 'get_count' and 'increment'
    # Note 1; we are returning the 'get_count' itself and 'incremenet'
    # itself without the parenthesis
    return (get_count, increment)


get_count, increment = create_counter()
print(get_count())
increment()
increment()
increment()
print(get_count())
