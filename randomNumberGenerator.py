import random


def erika_function(n):
    for ii in range(1, n):
        randomNo1 = random.uniform(-1, 1)
        randomNo2 = random.uniform(-1, 1)
        r = randomNo1**2+randomNo2**2
        if randomNo1**2+randomNo2**2 <= 1:
            break
    return r
