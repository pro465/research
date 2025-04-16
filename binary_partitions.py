cch=dict()

def p(n, d):
    global cch
    if n==0: return 1
    if d==0: return 1
    if (n,d) in cch: return cch[(n, d)]
    s=0
    for i in range((n>>d)+1):
        s+=p(n-(i<<d), d-1)

    cch[(n,d)]=s
    return s

m=dict()
# p(7**7)=84218234192700589465606210455821859812806
def p2(n):
    global m
    if n<=1: return 1
    a=m[n//2] if n//2 in m else p2(n//2)
    b=m[n-2] if n-2 in m else p2(n-2)
    m[n]=a+b
    return a+b

#d = 16
for i in range(20):
    print(2**i, p2(2**i))
