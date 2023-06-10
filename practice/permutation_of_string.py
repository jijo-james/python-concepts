# Python program to create all the permutations of a string


# # method 1
# def get_permutations(string, i=0):
#     if i == len(string):
#         print("".join(string))

#     for j in range(i, len(string)):
#         words = [c for c in string]
#         words[i], words[j] = words[j], words[i]

#         get_permutations(words, i + 1)


# get_permutations("jio")


# method 2
from itertools import permutations

words = ["".join(p) for p in permutations("jijo")]
print(words)
