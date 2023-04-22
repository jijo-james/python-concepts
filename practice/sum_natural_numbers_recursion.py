# Python program to find the sum of natural using recursive function

def sum(n):
    if n <= 1:
        return n
    else:
        return (n + sum(n-1))

number = int(input("Enter a number: "))

if number < 1 :
    print("Enter a positive integer: ")
else:
    print(sum(number))