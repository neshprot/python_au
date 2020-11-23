import math


def prime(value):
    if value % 2 == 0 or value % 10 == 0 or value % 3 == 0:
        return False
    for i in range(3, math.ceil(math.sqrt(value)) - 1, 2):
        if value % i == 0:
            return False
    return True


if prime(int(input())):
    print("Число простое")
else:
    print("Число составное")
