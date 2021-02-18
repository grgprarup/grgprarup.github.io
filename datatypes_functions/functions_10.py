"""
    10. Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
"""
def get_even(item):
    return item%2 == 0

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_list = list(filter(get_even, input_list))
print(even_list)
