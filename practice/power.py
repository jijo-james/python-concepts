# Python program to calculate the power of a number


# method 1
base = 3
exponent = 4

result = 1

while exponent != 0:
    result *= base
    exponent -=1

print(int(result))