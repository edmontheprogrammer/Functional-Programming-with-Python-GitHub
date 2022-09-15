# Closure

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


def create_counter():
    count = 0

    def get_count():
        return count

    def increment():
        nonlocal count
        count += 1

    return (get_count, increment)


get_count, increment = create_counter()
print(get_count())
increment()
increment()
increment()
print(get_count())
