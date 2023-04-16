# Python program to find H.C.F of two numbers


def hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i

    return hcf


first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

print(
    "HCF of {} and {} is {}".format(
        first_number, second_number, hcf(first_number, second_number)
    )
)
