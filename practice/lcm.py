# Python Program to find the L.C.M. of two input number


def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1
    return lcm


first_number = input("Enter a number: ")
second_number = input("Enter second number: ")

print(
    "LCM of {} and {} is {}".format(
        first_number, second_number, lcm(first_number, second_number)
    )
)
