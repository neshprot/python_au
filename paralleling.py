import random
import multiprocessing
import time

number = 30000


def count_pi(x):
    amount_circle = 0
    for i in range(number):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x * x + y * y <= 1:
            amount_circle += 1
    return amount_circle


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    t0 = time.time()
    list_circle = pool.map(count_pi, range(2))
    S = 0
    for i in range(2):
      S += list_circle[i]
    print(4*S/2/number)
    print("Time spent:", time.time() - t0)
