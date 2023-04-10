# If a, b and c are three sides of a triangle. Then,

# s = (a+b+c)/2
# area = √(s(s-a)*(s-b)*(s-c))

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

s= (a+b+c)/2

area = (s*(s-a)*(s-b)*(s-c))**.5
print("Area of triamgle with side {}, {} and {} is {}".format(a,b,c,area))