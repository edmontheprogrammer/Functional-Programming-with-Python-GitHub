# Lambdas in Python
# Lambdas is a one-line, unnamed functions that can be defined inside
# larger expressions
# We use lambdas inside larger expressions because functions that we
# create using the 'def' keyword can't be placed inside of larger expressions
# lambdas's basic form: 'lambda x, y: x + y'
# Note 1; no need for return keyword
# Note 2; the function body of a lambda is only one statment long.
# the point of making lambda functions one line of code is to keep it
# simple.

numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def add(x, y): return x + y


print(add(2, 3))

# Note 3; We almost always wrap the 'map()' and 'filter()'
# function with the 'list()' map because both 'map()' and 'fliter()'
# return iterable object, meaning they do not return values or data.
# In order for us to get the values or data in 'string' 'integer' or
# other human readable types, we have to use a 'loop' or the 'list()'
# function as shown below so that we can get the actual values.
double_numbers = list(map(lambda x: x * 2, numbers_list))
print(double_numbers)


def create_multiplier(a):
    return lambda x: x * a


double = create_multiplier(2)
print(double(5))
