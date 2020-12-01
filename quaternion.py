from numbers import Number
import itertools


class QuaternionDomainError(ValueError):
    pass


class Quaternion:

    def __init__(self, arg=0):
        """
        coefficients -- коэффициенты
        """
        if isinstance(arg, Number):
            self.coefficients = [arg]
        elif isinstance(arg, list):
            self.coefficients = arg.copy()
        elif isinstance(arg, Quaternion):
            self.coefficients = arg.coefficients.copy()
        else:
            raise QuaternionDomainError("You are trying to create quaternion from " + repr(arg))

    def __str__(self):
        return (" + ".join([
            str(c) + ("" if i == 0 else "*i" if i == 1 else "*j" if i == 2 else "*k")
            for c, i in list(zip(self.coefficients, itertools.count()))
        ])) if len(self.coefficients) else '0'

    def __eq__(self, other):
        if isinstance(other, Number):
            other = Quaternion(other)

        if isinstance(other, Quaternion):
            return self.coefficients == other.coefficients
        else:
            raise QuaternionDomainError("Can't say if Quaternion is equal to " + str(type(other)))

    def __add__(self, other):
        if isinstance(other, Number):
            other = Quaternion(other)

        sc = self.coefficients.copy()
        oc = other.coefficients.copy()

        # make lengths equal
        sc += [0] * (len(oc) - len(sc))
        oc += [0] * (len(sc) - len(oc))

        return Quaternion([
            sce + oce for sce, oce in zip(sc, oc)
        ])

    def __neg__(self):
        return Quaternion([-c for c in self.coefficients])

    def __sub__(self, other):
        if isinstance(other, Number):
            other = Quaternion(other)

        return self.__add__(other.__neg__())

    def __rsub__(self, other):
        return self.__neg__().__add__(other)

    def __mul__(self, other):
        if isinstance(other, Number):
           return Quaternion([other * i for i in self.coefficients])

        c = [0] * 4
        minus = [1, 1, 1, 1, -1, 1, -1, 1, -1, 1, 1, -1, -1, -1, 1, 1]
        otc = [0, 1, 2, 3, 1, 0, 3, 2, 2, 3, 0, 1, 3, 2, 1, 0]
        for i in range(0, 4):
            for j in range(4):
                c[j] += self.coefficients[i] * other.coefficients[otc[j + otc[0]]] * minus[j + otc[0]]
            otc[0] += 4

        return Quaternion(c)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Number):
            other = Quaternion([other, 0, 0, 0])
        cof = 0
        for i in range(4):
            cof += other.coefficients[i] * other.coefficients[i]
            if i != 0:
                other.coefficients[i] *= -1
        other = self.__mul__(other)
        for i in range(4):
            other.coefficients[i] = float(other.coefficients[i])
        return Quaternion([i/cof for i in other.coefficients])

    def __float__(self):
        self.coefficients[0] = float(self.coefficients[0])
        return self.coefficients[0]


p1 = Quaternion([4, 3, 5, 8])
p2 = Quaternion([7, 2, 1, 17])
p3 = Quaternion(3)
print(p1 == p2)
print(p3 == 3)
print(p1, p2, p3)
print(p1+p2)
print(p1-p2)
print(p1*p2)
print(p1*4)
print(p1/4)
print(p1*(p2-p1)*p2)
print(p1/p2)
print(float(p3))

