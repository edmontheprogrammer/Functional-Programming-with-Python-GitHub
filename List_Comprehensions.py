# List Comprehensions
# List Comprehensions are a readable way of transforming elements in a
# in a list - either by mapping or filtering.
# You can think of list comphrensions as a combinations of
# map, filter and lambdas.

numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# This line says multiply every element in the list, 'numbers_list',
#  by 2 and store the results in a
# list variable named 'doubled'
# We can change this part 'x * 2' to return anything we want.
# This is how list Comprehensions work.
doubled = [x * 2 for x in numbers_list]
print(doubled)

# Flitering elements
# Note 1: we added additional logic to the list comprehensions to
# force elements filtering, here we are creating an if statment
# that makes the list comprehesions return results based on the if condition
# 'if x % 2 == 0'
evens = [x * 2 for x in numbers_list if x % 2 == 0]
print(evens)
