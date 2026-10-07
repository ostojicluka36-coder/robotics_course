import math

def atan2(x, y):
    """
    returns an angle [-pi, pi]
    """

    if y == 0 and x > 0:
        return math.pi/2
    elif y == 0 and x < 0:
        return -math.pi/2

    if x == 0 and y > 0:
        return 0
    if x == 0 and y < 0:
        return -math.pi


    if x > 0:
        if y > 0:
            return math.atan(x/y)
        elif y < 0:
            return math.atan(x/y) + math.pi
    elif x < 0:
        if y > 0:
            return math.atan(x/y)
        elif y < 0:
            return math.atan(x/y) - math.pi
