# Python program to find all files with a .txt extension present inside a directory


# # method 1
# import glob
# from os import chdir

# chdir("files")

# for file in glob.glob("*.txt"):
#     print(file)


# # method 2
# from os import listdir

# for file in listdir("files"):
#     if file.endswith(".txt"):
#         print(file)


# method 3
from os import walk

for root, dirs, files in walk("files"):
    for file in files:
        if file.endswith(".txt"):
            print(file)
