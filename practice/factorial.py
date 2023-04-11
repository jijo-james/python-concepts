# Python program to find the factorial of a number provided by the user
# using recursion


def factorial(x):

    if x == 1:
        return 1
    else:
        # recursive call to the function
        return x * factorial(x - 1)


num = int(input("Enter a number: "))

result = factorial(num)
print("The factorial of", num, "is", result)
