"""
    22. Write a Python program to remove duplicates from a list.
"""
input_list = [1,2,3,4,2,1,4,'apple','banana','cat','apple']
duplicate_removed = list(dict.fromkeys(input_list))
print(duplicate_removed)
