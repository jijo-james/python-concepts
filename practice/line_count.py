# Python program to print line count of a file


# method 1
def file_legth(filename):
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


print(file_legth("file.txt"))
