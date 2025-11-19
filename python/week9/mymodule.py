import random as rd

def rolling_simmulator():
    a = rd.randint(1,6)
    b = rd.randint(1,6)
    return (a, b, a + b)
