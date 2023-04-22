# Factorial of a number using recursion

def factorial(n):
    if n == 1:
        return n
    else:
        return (n * factorial(n-1))


number = int(input("Enter a number: "))

if number < 0:
    print("Negative numbers don't have factorial")
elif number == 1:
    print("Factorial of 1 is 1 :)")
else:
    print(factorial(number))