"""
13. Write a function to write a comma-separated value (CSV) file. It
should accept a filename and a list of tuples as parameters. The
tuples should have a name, address, and age. The file should create
a header row followed by a row for each tuple. If the following list of
tuples was passed in:
[('George', '4312 Abbey Road', 22), ('John', '54 Love Ave',
21)] it should write the following in the file:
name,address,age
George,4312 Abbey Road,22
John,54 Love Ave,21
"""
import csv

records = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
field_names = ['name', 'address', 'age']
with open('records.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(field_names)
    writer.writerows(records)