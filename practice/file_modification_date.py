# Python program to to get a file creation and modification date


# # method 1
# import os.path, time, pathlib

# file = pathlib.Path("factorial.py")

# print("Last modification time: %s" % time.ctime(os.path.getmtime(file)))
# print("Creation time: %s" % time.ctime(os.path.getctime(file)))


# method 2
from datetime import datetime
import pathlib

file_name = pathlib.Path("jijo.jpeg")

print("Last modification time: %s" % datetime.fromtimestamp(file_name.stat().st_mtime))
print("Creation time: %s" % datetime.fromtimestamp(file_name.stat().st_ctime))
