"""
    4. Write a Python program to get a single string from two given strings, separated
by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
"""
first_string = input('Enter first string:')
second_string = input('Enter second string:')
output_string = first_string.replace(first_string[:2],second_string[:2]) + ' ' + second_string.replace(second_string[:2],first_string[:2])
print(output_string)
