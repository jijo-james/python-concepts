# Python program to convert two lists into a dictionary


# # method 1
# index = [1, 2, 3]
# languages = ['python', 'c', 'c++']

# dictionary = dict(zip(index, languages))
# print(dictionary)


# method 2
index = [1, 2, 3]
languages = ['python', 'c', 'c++']

dictionary = {k: v for k, v in zip(index, languages)}
print(dictionary)