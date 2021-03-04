"""
7. Create a list of tuples of first name, last name, and age for your friends
and colleagues. If you don't know the age, put in None. Calculate the
average age, skipping over any None values. Print out each name,
followed by old or young if they are above or below the average age.
"""

peoples = [('Prarup', 'Gurung', 2), ('Aakash', 'Shakya', 28), ('Sanjay', 'Maharjan', None), ('Jivan', 'Thapa', None)]
total = 0
for people in peoples:
    if people[2] is not None:
        total = total + people[2]
average = total / len(peoples)
for people in peoples:
    if people[2] is not None:
        if people[2] > average:
            print(f'{people[0]} {people[1]} Old')
        else:
            print(f'{people[0]} {people[1]} Young')
