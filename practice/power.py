# Python program to calculate the power of a number


# # method 1
# base = 3
# exponent = 4

# result = 1

# while exponent != 0:
#     result *= base
#     exponent -= 1

# print(int(result))


# method 2
base = 3
exponent = 4

result = 1

for exponent in range(exponent, 0, -1):
    result *= base

print(int(result))