def modfib(mod):
    a,b=1%mod,1%mod
    p=1
    while True:
        if a==0 and b==1%mod: break
        p+=1
        a,b=b,(a+b)%mod
    return p

def fib(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a

def product(iter):
    res=1
    for i in iter:
        res*=i
    return res

def choice(n, k):
    return product(range(n-k+1, n+1))//product(range(1, k+1))

def fib2(n):
    return sum(map(lambda i: choice(n-i, i), range(n//2+1)))
import math

print("   ", *map(lambda x: str(x).rjust(3), range(1, 100)), "", sep = "|")

for i in range(1, 100):
    # print(fib2(i), fib(i+1))
    # assert fib2(i) == fib(i+1)

    # print(i, end=": ")
    # prev=1
    # for p in range(1, 7):
    #     c=modfib(i**p)
    #     print(c, c/prev)
    #     prev=c
    # print()

    # for j in range(2, i):
    #     if i%j==0: break
    # else:
    s=modfib(i)
    print(str(i).rjust(3), end="|")
    for j in range(1, 100):
         js=modfib(j)
         assert modfib(i*j) % math.lcm(s, js) == 0
         print(str(modfib(i*j) // math.lcm(s, js)).rjust(3), end="|")
    print()
