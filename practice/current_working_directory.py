# Python program to get the full path of the current working directory


# method 1
import pathlib

print(pathlib.Path('jijo.jpeg').parent.absolute())
print(pathlib.Path().absolute())