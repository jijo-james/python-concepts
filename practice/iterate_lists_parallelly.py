# Python program to iterate through two lists in parallel


# # method 1
# list_1 = [1, 2, 3, 4]
# list_2 = ['a', 'b', 'c']

# for i, j in zip(list_1, list_2):
#     print(i, j)


# method 2
from itertools import zip_longest

list_1 = [1, 2, 3, 4]
list_2 = ["a", "b", "c"]

for i, j in zip_longest(list_1, list_2):
    print(i, j)
