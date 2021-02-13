"""
    11. Write a Python program to count the occurrences of each word in a given
sentence.
"""
input_string = input('Enter a string: ')
splitted_string = input_string.split(sep=' ')
length = len(splitted_string)
dict_count_words = {splitted_string[i] : splitted_string.count(splitted_string[i]) for i in range(length)}
print(dict_count_words)
