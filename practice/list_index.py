# Python program to find index of list

# # method 1:

# my_list = [21, 44, 35, 11]

# for index, val in enumerate(my_list):
#     print(index, val)


# # method 2:
# my_list = [21, 44, 35, 11]

# for index, val in enumerate(my_list, start=1):
#     print(index, val)


# method 3:
my_list = [21, 44, 35, 11]

for index in range(len(my_list)):
    value = my_list[index]
    print(index, value)