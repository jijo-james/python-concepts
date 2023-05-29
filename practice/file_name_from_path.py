# Python program to get the file name from the file path


# # method 1
# import os

# file_name = os.path.basename('/root/file.ext')

# print(os.path.splitext(file_name)[0])


# method 2
from pathlib import Path

print(Path('/root/file.ext').stem)