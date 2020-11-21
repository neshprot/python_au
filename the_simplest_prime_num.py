import math


def prime(value):
    if value % 2 == 0 | (value > 10 & value % 10 == 0):
        return "False"
    for i in range(3, math.ceil(math.sqrt(value)) - 1, 2):
        if value % i == 0:
            return "False"
    return "True"


print(prime(8731))
