# Python program to display the Fibonacci sequence

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


number = int(input("Enter a number: "))

if number <= 0:
    print("Enter a positive integer: ")
else:
    print("Fibonacci series: ")
    for i in range(number):
        print(fibonacci(i))