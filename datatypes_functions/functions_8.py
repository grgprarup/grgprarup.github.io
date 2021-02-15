"""
    8. Write a Python function that takes a list and returns a new list with unique
elements of the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
"""
def get_unique(input_list):
    return list(set(input_list))

input_list = [1,2,3,3,3,3,4,5]
print(f'Unique list : {get_unique(input_list)}')
