# Python Program to find the L.C.M. of two input number


# def lcm(x, y):
#     if x > y:
#         greater = x
#     else:
#         greater = y

#     while True:
#         if (greater % x == 0) and (greater % y == 0):
#             lcm = greater
#             break
#         greater += 1
#     return lcm


# first_number = input("Enter a number: ")
# second_number = input("Enter second number: ")

# print(
#     "LCM of {} and {} is {}".format(
#         first_number, second_number, lcm(first_number, second_number)
#     )
# )


# using hcf(gcd)

def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

num1 = 54
num2 = 24 

print("The L.C.M. is", compute_lcm(num1, num2))
