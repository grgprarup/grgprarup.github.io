"""
9. Write a binary search function. It should take a sorted sequence and
the item it is looking for. It should return the index of the item if found.
It should return -1 if the item is not found.
"""


def binary_search(num_list, item):
    length = len(num_list)
    start = 0
    end = length
    for i in range(length + 1):
        mid = int((start + end) / 2)
        if num_list[mid] == item:
            return mid
        elif num_list[mid] > item:
            end = mid - 1
        else:
            start = mid + 1
    return -1


num_list = [23, 45, 5, 67, 2, 3, 56, 4, 35, 34, 65, 76, 12]
num_list.sort()
print(num_list)
item = int(input('Item to search? '))
index = binary_search(num_list, item)
if index != -1:
    print(f'Item at {index}')
else:
    print('Item not found')
