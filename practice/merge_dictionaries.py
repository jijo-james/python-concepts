# Python program to merge two dictonaries

# # method 1: using | operator

# dict_1 = {1: "a", 2: "b"}
# dict_2 = {2: "c", 4: "d"}

# print(dict_1 | dict_2)


# method 2: using * operator

dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

print({**dict_1, **dict_2})