# Python program to safely create nested directory

# # method 1:

# from pathlib import Path

# Path("/root/dirA/dirB").mkdir(parents=True, exist_ok=True)


# method 2:

import os

os.makedirs("/root/dirA/dirB")
