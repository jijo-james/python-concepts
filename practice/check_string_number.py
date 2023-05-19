# Python program to check if a string is a number


# method 1
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

print(isfloat('s12'))
print(isfloat('1.123'))