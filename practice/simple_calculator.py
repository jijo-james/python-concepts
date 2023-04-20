# Simple Calculator by Using Functions


def addition(x, y):
    return x + y


def substraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


print(
    """Select operation to be performed :\n
      1. Addition\n
      2. Substraction\n
      3. Multiplication\n
      4. Division"""
)

while True:
    choice = int(input("Enter your choice: "))

    if choice in (1, 2, 3, 4):
        try:
            first_number = int(input("Enter first number: "))
            second_number = int(input("Enter second number: "))
        except Exception as e:
            print("Enter valid numbers...")
            print(e)

        if choice == 1:
            addition(first_number, second_number)
        elif choice == 2:
            substraction(first_number, second_number)
        elif choice == 3:
            multiplication(first_number, second_number)
        elif choice == 4:
            division(first_number, second_number)
        else:
            print("Invalid choice...!!!")
        next_calculation = input("Do you want to perform another operation(Y/n): ")
        if next_calculation == "N" or next_calculation == "n":
            break
    else:
        print("Invalid choice!!!")
