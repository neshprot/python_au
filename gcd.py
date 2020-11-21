def gcd(first_num, sec_num):
    if sec_num == 0:
        return first_num
    return gcd(sec_num, first_num % sec_num)


print(gcd(1404, 15912))
