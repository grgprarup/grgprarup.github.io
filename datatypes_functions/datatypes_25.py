"""
    25. Write a Python program to check whether all dictionaries in a list are empty or
not.
Sample list : [{},{},{}]
Return value : True
Sample list : [{1,2},{},{}]
Return value : False
"""
input_list = [{},{},{}]
count = 0
for item in input_list:
    if not item:
        count = 1
    else:
        count = 0
        break
if count is 1:
    print('All dictionaries are empty')
else:
    print('All dictionaries are not empty')
