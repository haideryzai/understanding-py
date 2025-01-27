# Write a lambda function that doubles a number.
# Use map() to apply this function to a list of numbers.


double_number = lambda x: x * 2

numbers = [3, 5, 6, 9]
print("Double of numbers : ", list(map(double_number, numbers)))

