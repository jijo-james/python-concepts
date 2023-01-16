import os
from datetime import datetime



# get current directory
print(os.getcwd())

# change directory
os.chdir('/mnt/sda7/projects/python3')

print(os.getcwd())

#list directory
print(os.listdir())

# rename
os.rename('bronx_copy.jpeg', 'jijo_copy.jpeg')

#list directory tree
os.chdir('/mnt/sda7/projects/ds/da-course/machinelearningplus')
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print("Path : ", dirpath)
    print("Directories : ",dirnames)
    print('Files : ', filenames)




#info about a file
mod_time = os.stat('enumerator.py').st_mtime
print(datetime.fromtimestamp(mod_time))



lib = os.path.dirname(__file__)
k = os.path.dirname(lib)
print(lib)
