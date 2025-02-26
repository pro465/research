from math import comb

def rec(n, k):
    if n>=0 and k==0: return 1
    if n>0 and k>0: return comb(n+k-1, k) 
    return 0

def c(n, k):
    res=0
    for i in range(n+1):
        res += (-1)**(n-i) * comb(n, i) * comb(comb(i, 2), k)
    return res

def f(n):
    if n<=2: return 1
    res=f(n-1)
    return res*(res + 3)//2

for i in range(1, 30):
#     # for j in range(1, 10):
        print(f"c({i}) = ", f(i))
