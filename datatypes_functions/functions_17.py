"""
    17. Write a Python program to find if a given string starts with a given character
using Lambda
"""
input_string = 'hello nepal'
starts_with = lambda input_string: input_string.startswith('l')
if starts_with(input_string):
    print('True')
else:
    print('False')
