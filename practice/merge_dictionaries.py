# Python program to merge two dictonaries

# # method 1: using | operator

# dict_1 = {1: "a", 2: "b"}
# dict_2 = {2: "c", 4: "d"}

# print(dict_1 | dict_2)


# # method 2: using ** operator

# dict_1 = {1: 'a', 2: 'b'}
# dict_2 = {2: 'c', 4: 'd'}

# print({**dict_1, **dict_2})


# method 3: using copy() and update()

dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

dict_3 = dict_2.copy()
dict_3.update(dict_1)

print(dict_3)