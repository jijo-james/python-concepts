# Python program to check the filesize


# # method 1
# from os import stat

# file_size = stat("jijo.jpeg").st_size
# print(file_size)


# method 2
from pathlib import Path

file = Path("jijo.jpeg")
print(file.stat().st_size)