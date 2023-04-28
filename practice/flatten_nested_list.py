# Python program for flatten a nested list

# # method 1:

# my_list = [[1], [2, 3], [4, 5, 6, 7]]

# flat_list = [num for sublist in my_list for num in sublist]
# print(flat_list)


# # method 2:

# my_list = [[1], [2, 3], [4, 5, 6, 7]]

# flat_list = []
# for sublist in my_list:
#     for num in sublist:
#         flat_list.append(num)

# print(flat_list)


# # method 3:

# import itertools

# my_list = [[1], [2, 3], [4, 5, 6, 7]]

# flat_list = list(itertools.chain(*my_list))
# print(flat_list)


# # method 4:

# my_list = [[1], [2, 3], [4, 5, 6, 7]]

# flat_list = sum(my_list, [])
# print(flat_list)


# method 5:

from functools import reduce

my_list = [[1], [2, 3], [4, 5, 6, 7]]
print(reduce(lambda x, y: x + y, my_list))
