#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import numpy
import matplotlib.pyplot as mpp

#импорт библиотек

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__':
    arguments = numpy.r_[0:200:0.1] #Значения по оси 0X с шагом 0.1
    mpp.plot( #подсчёт графика
        arguments,
        [math.sin(a) * math.sin(a/20.0) for a in arguments] #заданная функция
    )
    mpp.show() #вывод графика
