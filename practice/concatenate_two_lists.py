# Python program to concatenate two lists

# # method 1
# list_1 = [1, 'a']
# list_2 = [3, 4, 5]

# list_joined = list_1 + list_2
# print(list_joined)

# # method 2
# list_1 = [1, 'a']
# list_2 = range(2, 4)

# list_joined = [*list_1, *list_2]
# print(list_joined)

# # method 3
# list_1 = [1, 'a']
# list_2 = [1, 2, 3]

# list_joined = list(set(list_1 + list_2))
# print(list_joined)

# method 4
list_1 = [1, 'a']
list_2 = [1, 2, 3]

list_2.extend(list_1)
print(list_2)