# Python program to safely create nested directory

# # method 1:

# from pathlib import Path

# Path("/root/dirA/dirB").mkdir(parents=True, exist_ok=True)


# # method 2:

# import os

# os.makedirs("/root/dirA/dirB")


# # method 3:

# import distutils.dir_util

# distutils.dir_util.mkpath("/root/dirA/dirB")


# method 4:

import os

try:
    os.makedirs("/dirA/dirB")
except FileExistsError:
    print("File already exists")
