"""
2. Write an if statement to determine whether a variable holding a year is
a leap year.
"""
year = int(input('Enter year: '))
if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
    print('Leap Year')
else:
    print('Not a Leap year')
