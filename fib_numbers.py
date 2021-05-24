import itertools

first_2_fibs = [1, 1]


class Fib:
    """По объектам этого класса можно итерироваться и получать 6 чисел Фибоначчи"""

    class _FibNum_iter:
        """Внутренний класс — итератор"""

        def __init__(self):
            self.i = 0
            self.fibs = first_2_fibs  # они у нас выше были

        def __next__(self):
            j = self.i
            self.i += 1
            x = self.fibs[j] + self.fibs[j + 1]
            self.fibs.append(x)
            return self.fibs[j]

    def __iter__(self):
        """Создать и вернуть итератор"""
        return Fib._FibNum_iter()


Fibonacci = Fib()
N = 20
print(list(itertools.islice(Fibonacci, N)))
for i, f in zip(itertools.count(1), itertools.islice(Fibonacci, N)):
    print(f"{i}){f}")
