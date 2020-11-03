import math
import numpy as np
from matplotlib import pyplot as pp
MODEL_G = 9.81
MODEL_DT = 0.001


class Body:
    def __init__(self, x, y, vx, vy):
        """
        Создать тело.

        Пареметры:
        ----------
        x: float
            горизонтальная координата
        y: float
            вертикальная координата
        vx: float
            горизонтальная скорость
        vy: float
            вертикальная скорость
        """

        self.cor_x = x
        self.cor_y = y
        self.vec_x = vx
        self.vec_y = vy

        self.trajectory_x = []
        self.trajectory_y = []

    def advance(self):
        """
        Выполнить шаг мат. модели применительно к телу, предварительно записав его координаты
        """
        self.trajectory_x.append(self.cor_x)
        self.trajectory_y.append(self.cor_y)

        self.cor_x += self.vec_x * MODEL_DT
        self.cor_y += self.vec_y * MODEL_DT
        self.vec_y -= MODEL_G * MODEL_DT


class Rocket(Body):
    def __init__(self, x, y):
        """
        Создать ракету.

        Пареметры:
        ----------
        x: float
            горизонтальная координата
        y: float
            вертикальная координата
        """
        super().__init__(x, y, 10, 10)
        self.rel_speed = 0.01  # относитльная скорость газа
        self.fuel_speed = 1  # скорость расхода топлива
        self.fuel_mass = 0.6  # масса топлива
        self.last_mass = self.fuel_mass  # масса оставшегося топлива
        self.vyr = 0  # добавочная скорость по оси OY
        self.vxr = 0  # добавочная скорость по оси OX

    def advance(self):
        super().advance()  # вызовем метод предка — тела, т.к. и он для ракеты актуален.
        self.last_mass -= self.fuel_speed * MODEL_DT
        if self.last_mass > 0:  # далее используем формулу Циолковского
            self.vyr = self.rel_speed * math.log(self.fuel_mass/self.last_mass, math.e)
            self.vec_y += self.vyr
            self.vxr = self.rel_speed * math.log(self.fuel_mass/self.last_mass, math.e)
            self.vec_x += self.vxr


b = Body(0, 0, 10, 10)
r = Rocket(0, 0)

bodies = [b, r]
# Дальше мы уже не будем думать, кто тут ёжик, кто ракета, а кто котлета —
# благодаря возможностям ООП будем просто работать со списком тел

for t in np.r_[0:2:MODEL_DT]:  # для всех временных отрезков
    for b in bodies:  # для всех тел
        b.advance()  # выполним шаг


for b in bodies:  # для всех тел
    pp.plot(b.trajectory_x, b.trajectory_y)  # нарисуем их траектории
pp.show()
