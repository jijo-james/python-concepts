import math


class ThetaOutOfRangeError(Exception):
    pass


def straight_length(r, theta):
    if theta < 0:
        raise ThetaOutOfRangeError("Theta value is less than 0.")
    elif theta > 2 * math.pi:
        raise ThetaOutOfRangeError("Theta value is greater than 2*pi.")

    return math.sqrt(2 * r**2 - 2 * r * math.cos(theta))


try:
    r = 5
    theta = 3 * math.pi

    result = straight_length(r, theta)
    print(f"straight_length = {result}")
except ThetaOutOfRangeError as e:
    print(f"Custom Exception: {e}")
