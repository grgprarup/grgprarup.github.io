"""
8. Write a Python program to remove the nth index character from a nonempty string.
"""
input_string = input('Enter a string: ')
index_char = int(input('Enter an index of character to remove: '))
input_string_tolist = list(input_string)
input_string_tolist.remove(input_string_tolist[index_char])
output_string = ''.join(input_string_tolist)
print(output_string)
