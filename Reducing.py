# Reducing in Python
# Reducing allow us to take a list or any other iterable and reduce it down
# to a single value. For example, we can take a list of numbers
# and reduce it down to single value that gives us the sum or total,
# or average of the list of numbers.
# reduce function syntax, reduce(some_function, my_list),
# def some_function(acc, element)
# 'reduce()' function takes two arguments instead of one argument
# like 'fliter()' and 'map()' functions
# def get_sum(acc, element):
#     return acc + element

# Note 1; in addition to the functon and the two arguments that we
# pass, we can also provide it wth another argument, the starting value
# of our accumulator variable. This is the value 'reduce' will start with.


from functools import reduce

numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Find the sume of an array of numbers


def get_sum(acc, x):
    print(f'acc is {acc}, x is {x}')
    return acc + x


sum = reduce(get_sum, numbers_list)
print(sum)
