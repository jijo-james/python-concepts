# Function to print binary number using recursion


def conversion(n):
    if n > 1:
        conversion(n // 2)
    print(n % 2, end="")


number = int(input("Enter the decimal number: "))

conversion(number)
print()