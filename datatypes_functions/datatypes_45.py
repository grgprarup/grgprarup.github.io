"""
    45. Write a Python program to find the index of an item of a tuple.
"""
input_tuple = (1,2,3,4,'apple','cat','black')
for item in input_tuple:
    print(f'{item} : {input_tuple.index(item)}')
