# Python program to split a list into evenly sized chunks

# # method 1
# def split(list_a, chunk_size):

#   for i in range(0, len(list_a), chunk_size):
#     yield list_a[i:i + chunk_size]

# chunk_size = 2
# my_list = [1,2,3,4,5,6,7,8,9]
# print(list(split(my_list, chunk_size)))

# method 2
chunk_size = 2
my_list = [1,2,3,4,5,6,7,8,9]
list_chunked = [my_list[i:i + chunk_size] for i in range(0, len(my_list), chunk_size)]
print(list_chunked)