# Python program to read a file line by line into a list


# # method 1
# with open("data_file.txt") as f:
#     content_list = f.readlines()

# print(content_list)

# # remove new line characters
# content_list = [x.strip() for x in content_list]
# print(content_list)


# method 2
with open('data_file.txt') as f:
    content_list = [line for line in f]

print(content_list)

# removing the characters
with open('data_file.txt') as f:
    content_list = [line.rstrip() for line in f]

print(content_list)