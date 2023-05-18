# Python program to randomly select an element from the list


# # method 1
# import random

# my_list = [1, 'a', 32, 'c', 'd', 31]
# print(random.choice(my_list))


# method 2
import secrets

my_list = [1, 'a', 32, 'c', 'd', 31]
print(secrets.choice(my_list))