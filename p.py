def f(n, p):
    r=0
    for _ in range(n):
        r = p + r*(1.-p)
    return r

def exp(p, a, b):
    return p*a+(1.-p)*b

p=1/365
a=7000000
b=-30

for n in range(262):
    print(f(n, p))
