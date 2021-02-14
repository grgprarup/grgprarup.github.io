"""
43. Write a Python program to remove an item from a tuple.
"""
input_tuple = (1, 2, 3, 4, 'apple', 'cat', 'black')
tuple_to_list = list(input_tuple)
tuple_to_list.remove(3)
output_tuple = tuple(tuple_to_list)
print(output_tuple)
