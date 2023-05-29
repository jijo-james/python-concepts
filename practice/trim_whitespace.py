# Python program to trim whitespace from a string


# # method 1
# my_string = " Python "

# print(my_string.strip())


# method 2
import re

my_string  = " Hello Python "
output = re.sub(r'^\s+|\s+$', '', my_string)

print(output)