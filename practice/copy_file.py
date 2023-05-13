# Python program to copy a file

from shutil import copyfile

copyfile("/root/a.txt", "/root/b.txt")


""" 
There are other methods 
copy(), 
copy2(), 
copyfile(), 
copyfileobj() 
which serve the same purpose with some metadata changes.
"""
