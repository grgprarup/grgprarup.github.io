"""
    20. Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given list of
strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
"""
string_list = ['abc','xyz','aba','1221','2de2','abcde','abcda','defed']
count = 0
for item in string_list:
    if len(item) >= 2 and item.endswith(item[0]):
        count += 1
print(count)
