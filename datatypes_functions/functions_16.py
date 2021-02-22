"""
    16. Write a Python program to square and cube every number in a given list of
integers using Lambda
"""
input_list = [1,2,3,4,5,6,7,8,9,10]
mapped_square = list(map(lambda x: x*x, input_list))
mapped_cube = list(map(lambda x: x*x*x, input_list))
print(f'Square: {mapped_square}')
print(f'Cube: {mapped_cube}')