import random
import multiprocessing
import time

num = 10


def count_pi(x):
    amount_circle = 0
    for i in range(100000):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x * x + y * y <= 1:
            amount_circle += 1
    return amount_circle


def test_all(pool):
    l = pool.map(count_pi, [0]*num)
    return l


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    t0 = time.time()
    print(4*sum(test_all(pool))/100000/num)
    print("Time spent:", time.time() - t0)
