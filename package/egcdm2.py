import math


def e_gcd(first_num, sec_num):
    if sec_num == 0:
        return first_num
    kof2 = 1
    kof1 = 0
    gcd = e_gcd(sec_num, first_num % sec_num)
    buf = kof2
    kof2 = kof1 - (math.ceil(first_num / sec_num) - 1) * kof2
    kof1 = buf

import math

def e_gcd(first_num, sec_num):
    if sec_num == 0:
        return first_num
    kof2 = 1
    kof1 = 0
    gcd = e_gcd(sec_num, first_num % sec_num)
    buf = kof2
    kof2 = kof1 - (math.ceil(first_num / sec_num) - 1) * kof2
    kof1 = buf
    return kof1, kof2, gcd

