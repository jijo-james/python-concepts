import math

length = lambda l_function, r, theta: f"{l_function.__name__} = {l_function(r, theta)}"

r = 5
theta = 0.5

straight_length = lambda r, theta: math.sqrt(2 * r**2 - 2 * r * math.cos(theta))
straight_length.__name__ = "straight_length"
arc_length = lambda r, theta: r * theta
arc_length.__name__ = "arc_length"

result1 = length(straight_length, r, theta)
result2 = length(arc_length, r, theta)

print(result1)
print(result2)
