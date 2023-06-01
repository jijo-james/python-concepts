# Python program to get the full path of the current working directory


# # method 1
# import pathlib

# print(pathlib.Path("jijo.jpeg").parent.absolute())
# print(pathlib.Path().absolute())


# method 2
from os import path, getcwd

print(path.dirname(path.abspath("jijo.jpeg")))
print(path.abspath(getcwd()))
