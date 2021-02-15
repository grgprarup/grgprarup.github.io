"""
    7. Write a Python function that accepts a string and calculate the number of
upper case letters and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
"""
def count(string):
    lower, upper = 0, 0
    for letter in string:
        if letter >= 'a' and letter <= 'z':
            lower += 1
        elif letter >= 'A' and letter <= 'Z':
            upper += 1
    return lower,upper

input_string = 'The quick Brow Fox'
lower, upper = count(input_string)
print(f'There are {lower} lower case letters and {upper} upper case letters.')
