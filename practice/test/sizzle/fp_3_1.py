import math


def straight_length(r, theta):
    return math.sqrt((2 * r**2) - (2 * r * math.cos(theta)))


def arc_length(r, theta):
    return r * theta


def length(l_function, r, theta):
    if l_function == straight_length:
        result = l_function(r, theta)
        return f"straight length = {result}"
    elif l_function == arc_length:
        result = l_function(r, theta)
        return f"arc length = {result}"
    else:
        return "Invalid function choice"


r = 5
theta = 0.5
x = straight_length
y = arc_length

result1 = length(x, r, theta)
result2 = length(y, r, theta)

print(result1)
print(result2)
