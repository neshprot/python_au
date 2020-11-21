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


NUM1 = 1404
NUM2 = 15912
if NUM1 < NUM2:
    NUM1, NUM2 = NUM2, NUM1
if NUM1 == NUM2 & NUM1 != 0:
    print(print(NUM1, "*", 1, "+", NUM2, "*", 0, "=", 0))
else:
    if NUM2 == 0:
        if NUM1 == 0:
            print(NUM1, "*", 0, "+", NUM2, "*", 0, "=", 0)
        else:
            print(NUM1, "*", 1, "+", NUM2, "*", 0, "=", 0)
    else:
        print(NUM1, "*", e_gcd(NUM1, NUM2)[0], "+", NUM2, "*", e_gcd(NUM1, NUM2)[1], "=", e_gcd(NUM1, NUM2)[2][2])
