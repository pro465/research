from math import comb
def step(p):
    return 28*p**3*(1-p)**5*(3-p)

p=.5
for _ in range(100000):
    print(p)
    p=step(p)
