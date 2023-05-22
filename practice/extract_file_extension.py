# Python program to extract file extension


# method 1
import os
file_details = os.path.splitext('/jijo.jpeg')
print(file_details)
print(file_details[1])