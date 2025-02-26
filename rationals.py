import math
import itertools

def radd(a, b):
    gcd=math.gcd(a[1],b[1])
    return ((a[0]*b[1]+b[0]*a[1])//gcd, a[1]//gcd*b[1])
def recip(x): return (x[1],x[0])

def find(r):
    if r==(0,1): return 0
    if r==(1,1): return 1
    i=2
    answers = [{((0, 1),2)}, {((1, 1), 2)}]
    while i<5:
        s=set()
        for j in range(1, i//2+1):
            k=i-j
            for l in answers[j]:
                for m in answers[k]:
                    a=radd(l[0], m[0])
                    b=recip(a)
                    s.add((a, 0))
                    s.add((b, 1))
                    if r==a:
                        return i
                    if r==b:
                        return i
        print(i, s)
        answers.append(s)
        i+=1

def time(n):
    if n<2: return 1
    res = [0]*(n+1)
    res[1]=1
    for i in range(2, n+1):
        for j in range(1, i//2+1):
            print(i, j)
            if j==i-j:
                res[i] += math.comb(res[j]+1, 2)
            else:
                res[i] += res[j]*res[i-j]
    return res
a,b = 5, 6
l=[[2, 2, 0, 2, 2, 2, 0, 0, 1]]

def frac(a, b):
    return f"\\frac{{{a}}}{{{b}}}"

def latex(l):
    res=[[l[0], 1]]
    for i in range(1, len(l)):
        if l[i-1] == l[i]: res[-1][1]+=1
        else: res.append([l[i],1])
    stack=[]
    for i in res:
        if i[0]==2: stack += ["1"]*i[1]
        if i[0]==0:
            for j in range(i[1]):
                a=stack.pop()
                stack[-1] += "+"+a
        if i[0]==1:
            e=frac(1, stack.pop())
            for j in range(i[1]):
                e = frac(1, stack.pop()) + "+" + e
            e = frac(1, e)
            stack.append(e)

    res=stack[-1].replace(frac(1, 1), "1")
    for i in range(10, 1, -1):
        res = res.replace("+".join("1"*i), str(i))
    return res

def estimate(r):
    if r[0]<r[1]: r=r[1],r[0]
    a=1
    b=1
    i=1
    while (a<=r[0] or b<=r[1]):
        a,b = a+b,a
        i+=1
    return i-1

def radd_nonred(a, b):
    ((a, b),(c, d)) = (a,b)
    return (a*d+b*c,b*d)

def list_upto(n):
    i=2
    answers = [{}, {(1, 1)}]
    while i<n:
        s=set()
        for j in range(1, i//2+1):
            k=i-j
            for l in answers[j]:
                for m in answers[k]:
                    a=radd_nonred(l, m)
                    b=recip(a)
                    s.add(a)
                    s.add(b)
        print(i, min(map(lambda x: x[1], filter(lambda x: x[0]<=x[1], s))))
        answers.append(s)
        i+=1

# list_upto(19)

print("$$", frac(a,b), "$$")
for i in l:
    print("$$ =", latex(i), "$$")
