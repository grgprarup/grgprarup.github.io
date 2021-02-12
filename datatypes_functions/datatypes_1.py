"""
    1. Write a Python program to count the number of characters (character
frequency) in a string. Sample String : google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
"""

string = 'google.com'
length = len(string)
counter_dict = {string[i]: string.count(string[i]) for i in range(length)}      # dictionary comprehension
print(counter_dict)
