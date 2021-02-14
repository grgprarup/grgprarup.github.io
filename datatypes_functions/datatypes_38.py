"""
    38. Write a Python program to remove a key from a dictionary.
"""
input_dict = {'first_name':'David','last_name':'Chhetri','address':'Kathmandu','mobile_no':'9846323445'}
print(f'Dictionary before removing key: {input_dict}')
input_dict.pop('first_name')
print(f'Dictionary after removing key: {input_dict}')
