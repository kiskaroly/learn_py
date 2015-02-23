__author__ = 'Adel'


def is_prime (x):
    flag = False
    if x > 2 and x % 2 != 0:
        for n in range(2, x):
            if x % n == 0 and x != n:
                flag = False
                break
            else:
                flag = True
    elif x == 2:
        flag = True
    else:
        flag = False
    return flag


int_i = 1
for x in (range(2, 30)):
    if is_prime(x):
        print str(int_i) + ". ", str(x), "is prime"
        int_i += 1
