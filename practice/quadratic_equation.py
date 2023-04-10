# The standard form of a quadratic equation is:

# ax2 + bx + c = 0, where
# a, b and c are real numbers and
# a ≠ 0
# The solutions of this quadratic equation is given by:

# (-b ± (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

# sol 1
# for real solution

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))

# d = (b**2) - (4*a*c)

# solution_1 = (-b + d**.5)/(2*a)
# solution_2 = (-b - d**.5)/(2*a)

# print("Solutions for quadratic equation are {} and {}". format(solution_1, solution_2))



# sol 2
# for imaginary solution

from cmath import sqrt

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

d = (b**2) - (4*a*c)

solution_1 = (-b + sqrt(d))/(2*a)
solution_2 = (-b - sqrt(d))/(2*a)

print("Solutions for quadratic equation are {} and {}". format(solution_1, solution_2))