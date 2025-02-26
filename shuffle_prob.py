from math import factorial

def derng(n):
    res=[0]*(n+1)
    res[0]=1
    for k in range(2, n+1):
        res[k]=(k-1)*(res[k-1]+res[k-2])
    return res

def derng2(n):
    res=[0]*(n+1)
    for i in range(n+1):
        for j in range(i+1):
            res[i]+=(-1)**(j&1) * factorial(i)//factorial(j)
    return res

def prob(n):
    res=[0]*(n+1)
    ders=derng(n)
    for k in range(n+1):
        res[n]+=k*ders[n-k]/(factorial(k)*factorial(n-k))
    #for i in range(n-1, -1, -1):
    #    res[i]+=res[i+1]
    return res

n=1000
x=list(range(n+1))
y=derng(n)
z=derng2(n)

print(y==z)
