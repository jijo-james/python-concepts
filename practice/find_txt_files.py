# Python program to find all files with a .txt extension present inside a directory


# method 1
import os, glob

os.chdir("files")

for file in glob.glob("*.txt"):
    print(file)