"""
    3. Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336
"""
def mul_all(input_list):
    mul = 1
    for num in input_list:
        mul = mul * num
    return mul

input_list = [8, 2, 3, -1, 7]
print(mul_all(input_list))
