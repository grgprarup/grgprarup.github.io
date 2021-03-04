"""
5. Create a tuple with your first name, last name, and age. Create a list,
people, and append your tuple to it. Make more tuples with the
corresponding information from your friends and append them to the
list. Sort the list. When you learn about sort method, you can use the
key parameter to sort by any field in the tuple, first name, last name,
or age.
"""
people = []
my_tuple = ('Prarup', 'Gurung', 28)
people.append(my_tuple)
friend_tuple_1 = ('Aakash', 'Shakya', 28)
friend_tuple_2 = ('Sanjay', 'Maharjan', 27)
people.append(friend_tuple_1)
people.append(friend_tuple_2)
# sort by first name
people.sort()
print(people)
# sort by last name
people.sort(key=lambda p: p[1])
print(people)
# sort by age
people.sort(key=lambda p: p[2])
print(people)