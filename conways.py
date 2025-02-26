#        survives                  guaranteed to be alive (regardless of current state)
#f1(x) = x*8C2*x^2*(1-x)^6 +       8C3*x^3*(1-x)^5
#        survives                  births
#f2(x) = x                 + (1-x)*8C3*x^3*(1-x)^5

import random

def f1(x): return 4*7*x**3*(1-x)**6 + 8*7*x**3*(1-x)**5
def f2(x): return x                 + 8*7*x**3*(1-x)**6
x=0.5
for i in range(1000000):
    x = f2(f1(x))

for i in range(10):
    x = f2(f1(x))
    print(x)
