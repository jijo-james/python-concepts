# Python program to display all the prime numbers within an interval
from math import sqrt
lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

# for num in range(lower, upper + 1):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, int(sqrt(num)+1)):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)


for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, int((num**.5)+1)):
           if (num % i) == 0:
               break
       else:
           print(num)