"""
8. Write a function, is_prime, that takes an integer and returns True if the
number is prime and False if the number is not prime.
"""


def is_prime(number):
    status = True
    for i in range(2, number):
        if number % i == 0:
            status = False
            break
        else:
            status = True
    return status


number = int(input('Enter number: '))
if is_prime(number):
    print('Prime')
else:
    print('Not Prime')
