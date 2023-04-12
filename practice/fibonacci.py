# Program to display the Fibonacci sequence up to n-th term

nth_term = int(input("How many terms? "))

n1, n2 = 0, 1

count = 0

if nth_term <= 0:
    print("Please enter a positive integer!!!")

elif nth_term == 1:
    print("Fibonacci series upto ,", nth_term, " : \n", n1)

else:
    while count < nth_term:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
        