import math


def prime(value):
    if value % 2 == 0 | value % 10 == 0:
        return "FALSE"
    for i in range(3, math.ceil(math.sqrt(value)) - 1, 2):
        if value % i == 0:
            return "FALSE"
    return "TRUE"


print(prime(8731))
