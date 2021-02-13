"""
    26. Write a Python program to insert a given string at the beginning of all items in
a list.
Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
"""
input_list = [1,2,3,4]
string = 'emp'
new_list = []
for item in input_list:
    new_list.append(string+str(item))
print(new_list)
