import math


class ThetaOutOfRangeError(Exception):
    pass


def straight_length(r, theta):
    if theta < 0:
        raise ThetaOutOfRangeError("Theta value is less than 0.")
    elif theta > 2 * math.pi:
        raise ThetaOutOfRangeError("Theta value is greater than 2*pi.")

    return math.sqrt(2 * r**2 - 2 * r * math.cos(theta))


def arc_length(r, theta):
    return r * theta


def length(l_function, r, theta):
    while True:
        try:
            result = l_function(r, theta)
            return f"{l_function.__name__} = {result}"
        except ThetaOutOfRangeError as e:
            if "greater than 2*pi" in str(e):
                theta -= 2 * math.pi
            elif "less than 0" in str(e):
                theta += 2 * math.pi
            else:
                raise


r = 5
theta = -3 * math.pi  # Adjust theta to be out of range for testing

result = length(straight_length, r, theta)
print(result)
