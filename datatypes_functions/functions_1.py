"""
    1. Write a Python function to find the Max of three numbers.
"""
def maximum(a,b,c):
    if a > b and  a > c:
        return a
    elif  b > c:
        return b
    return c

num1, num2, num3 = 3555, 554, 9866
max = maximum(num1, num2, num3)
print(f'The maximum values is: {max}')
