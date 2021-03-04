"""
6. Create a list with the names of friends and colleagues. Search for the
name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.
"""
names = ['Sujan', 'Jivan', 'Aakash', 'Samip', 'Sita', 'Sonika']
status = False
for name in names:
    if name.lower() != 'John'.lower():
        status = False
    else:
        status = True
        break

if status is False:
    print('Not Found')
