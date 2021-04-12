<<<<<<< HEAD
import egcdm2
from package.egcdm2 import e_gcd
def m1f1(NUM1, NUM2):
    if NUM1 < NUM2:
        NUM1, NUM2 = NUM2, NUM1
    if NUM1 == NUM2 & NUM1 != 0 or NUM2 == 1:
        S = str(NUM1) + ' * ' + str(1) + ' + ' + str(NUM2) + ' * ' + str(0) + ' = ' + str(0)
    else:
        if NUM2 == 0:
            if NUM1 == 0:
                S = str(NUM1) + ' * ' + str(0) + ' + ' + str(NUM2) + ' * ' + str(0) + ' = ' + str(0)
            else:
                S= str(NUM1) + ' * ' + str(1) + ' + ' + str(NUM2) + ' * ' + str(0) + ' = ' + str(0)
        else:
            S = str(NUM1) + ' * ' + str(package.egcdm2.e_gcd(NUM1, NUM2)[0]) + ' + ' + str(NUM2) + ' * ' + str(package.egcdm2.e_gcd(NUM1, NUM2)[1]) + ' = ' + str(package.egcdm2.e_gcd(NUM1, NUM2)[2][2])
    return(S)
=======
import package.egcdm2
from package.egcdm2 import e_gcd
def m1f1(NUM1, NUM2):
    if NUM1 < NUM2:
        NUM1, NUM2 = NUM2, NUM1
    if NUM1 == NUM2 & NUM1 != 0 or NUM2 == 1:
        S = str(NUM1) + ' * ' + str(1) + ' + ' + str(NUM2) + ' * ' + str(0) + ' = ' + str(0)
    else:
        if NUM2 == 0:
            if NUM1 == 0:
                S = str(NUM1) + ' * ' + str(0) + ' + ' + str(NUM2) + ' * ' + str(0) + ' = ' + str(0)
            else:
                S= str(NUM1) + ' * ' + str(1) + ' + ' + str(NUM2) + ' * ' + str(0) + ' = ' + str(0)
        else:
            S = str(NUM1) + ' * ' + str(package.egcdm2.e_gcd(NUM1, NUM2)[0]) + ' + ' + str(NUM2) + ' * ' + str(package.egcdm2.e_gcd(NUM1, NUM2)[1]) + ' = ' + str(package.egcdm2.e_gcd(NUM1, NUM2)[2][2])
    return(S)
>>>>>>> 543d229... Module
