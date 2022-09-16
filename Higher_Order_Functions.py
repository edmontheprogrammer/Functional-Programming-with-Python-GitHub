# Higher Order Functions
# Functions that takes other functions as arguments and
# return or return functions are called high-order functions
# and using them in our code can provide flexibility and reusability.


def divide(x, y):
    return x / y

# creating a function that takes another function as input parameter
# note 1; we use the placehoder or variable name 'func' to repersent the
# input for data types that gets passed in as function
# 'func' is not a reserved keyword in Python. 'func' is just another
# common word that's used to repersent function variable that gets
# passed in as input parameter.


def second_argument_isnt_zero(func):
    def safe_version(*args):
        if args[1] == 0:
            print('Warning: second argument is zero')
            return
        return func(*args)

    return safe_version


divide_safe = second_argument_isnt_zero(divide)

divide_safe(10, 0)
