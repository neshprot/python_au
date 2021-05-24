def repeat(number):  # Вот это и надо реализовать
    def recurse_function(genuine_function):
        def fake_function(*args):  # Создаёт внутри фальшивую функцию
            result = args[0]
            for i in range(number):
                result = genuine_function(result)
            return result
        return fake_function
    return recurse_function


@repeat(2)
def plus_1(x_1):
    return x_1 + 1


@repeat(0)
def mul_2(x_2):
    return x_2 * 2


print(plus_1(3))  # должно выдать 5
print(mul_2(4))  # должно выдать 4
