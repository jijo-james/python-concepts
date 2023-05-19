# Python program to check if a string is a number


# # method 1
# def isfloat(num):
#     try:
#         float(num)
#         return True
#     except ValueError:
#         return False

# print(isfloat('s12'))
# print(isfloat('1.123'))


# method 2
def isint(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

print(isint('s12'))
print(isint('1123'))