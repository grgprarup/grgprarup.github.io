"""
    18. Write a Python program to check whether a given string is number or not
using Lambda.
"""
input_string = '12339'
is_digit = lambda input_string: input_string.isdigit()
if is_digit(input_string):
    print('True')
else:
    print('False')
