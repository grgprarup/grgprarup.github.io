"""
    10. Write a Python program to remove the characters which have odd index
values of a given string
"""
input_string = input('Enter a string:')
output_string = ''
for i in range(len(input_string)):
    if i % 2 == 0:
        output_string += input_string[i]
print(output_string)
