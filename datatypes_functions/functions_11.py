"""
    11. Write a Python program to create a lambda function that adds 15 to a given
number passed in as an argument, also create a lambda function that multiplies
argument x with argument y and print the result.
"""
number = int(input('Enter a number: '))
add = lambda num: num+15
print(add(number))

x = 20
y = 3
mul = lambda x,y: x*y
print(mul(x,y))
