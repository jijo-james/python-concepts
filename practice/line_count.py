# Python program to print line count of a file


# # method 1
# def file_legth(filename):
#     with open(filename) as f:
#         for i, l in enumerate(f):
#             pass
#     return i + 1


# print(file_legth("file.txt"))


# method 2
number_of_line = sum(1 for line in open("text.txt"))

print(number_of_line)
