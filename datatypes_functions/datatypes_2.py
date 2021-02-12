"""
    2. Write a Python program to get a string made of the first 2 and the last 2 chars
from a given a string. If the string length is less than 2, return instead of the
empty string.
Sample String : 'Python'
Expected Result : 'Pyon'
Sample String : 'Py'
Expected Result : 'PyPy'
Sample String : ' w'
Expected Result : Empty String
"""
string = input('Enter a string: ')
length = len(string)
if length < 2:
    print('Empty String')
else:
    first_two = string[:2]
    last_two = string[-2:]
new_string = first_two + last_two
print(f'Resulting String= {new_string}')
