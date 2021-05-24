import math
import cmath
import numpy as np
import matplotlib.pyplot as plt

ITERATIONS = 20


def my_ln(x):
    x_pow = x - 1
    multiplier = 1
    partial_sum = x - 1
    for n in range(1, ITERATIONS):
        x_pow *= x - 1
        multiplier *= -1
        partial_sum += multiplier * x_pow / (n + 1)
    return partial_sum


print('Библиотечный натуральный логарифм', help(math.log), math.log(1.4))
print('Наш натуральный логарифм', (help(my_ln), my_ln(1.4)))

complex_ln = cmath.exp(0.8)
print(complex_ln)
print("Достигает ли 0.8 наш натуральный логарифм?", my_ln(complex_ln))
print("А библиотечный?", cmath.log(complex_ln))

vs = np.vectorize(my_ln)
print(my_ln, vs)
arguments = np.r_[1:2:0.01]
plt.plot(arguments, np.log(arguments))
plt.plot(arguments, vs(arguments))
plt.show()
