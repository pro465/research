# a+bz where b^2 = 0
import math

def recip(x): return (x[1], x[0])

# solves ax+by=c, returning (m,n,o,p) where x=m+nt,y=o-pt is a solution for any integer t
def solve(a,b,c):
    (m, n) = (a, b)
    (s0, s1, t0, t1) = (1, 0, 0, 1)
    while b > 0:
        q=a//b
        (a, b) = (b, a-q*b)
        (s0, s1) = (s1, s0-q*s1)
        (t0, t1) = (t1, t0-q*t1)
    if c%a==0:
        q=c//a
        return (q*s0, n//a, q*t0, m//a)


def find_divisors(x):
    div=[]
    (m,n)=x
    for i in range(1, math.isqrt(m)+1):
        if m%i!=0: continue
        j=m//i
        res=solve(i,j,n)
        if res is None: continue
        (a,b,c,d)=res
        for t in range((b-a-1)//b,c//d+1):
            x=a+b*t
            y=c-d*t
            item=((i, y), (j, x))
            if (i==j and x<y) or [0, 1] in map(sorted,item): continue
            div.append(item)
    return set(div)

def m(a, b):
    return b if a is None else min(a, b)

def id(x): return x

def score(r, curr=0, best=None):
    if best is not None and curr>=best: return (curr, [])
    r_=tuple(sorted(r))
    if r_[0]<=1: 
        p=[2]*r_[1]
        if r_[0]==1: p += [int(r[1]==1)]*(r_[1]-1)
        return (curr+r_[r_[0]], p)
    best_p=[]

    for i, r in enumerate((r, recip(r))):
        for (a,b) in find_divisors(r):
            f=[id,recip][i]
            a,b=f(a),f(b)
            (sca, p1)=score(a, curr, best)
            (sc, p2)=score(b, sca, best)
            p=p1+p2+[i]
            o=best
            best=m(best, sc)
            if o != best or best is None: best_p=p

    return (best, best_p)

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

a,b=1229,321

s,l=score((b, a))

print(f"$$ {frac(a,b)} = {latex(l)} $$")

for a in range(1, 100):
    for b in range(1, 30):
        s,l=score((b, a))
        g=math.gcd(a,b)
        s2,l2=score((b//g, a//g))
        if s < s2:
            print(f"$$ {frac(a,b)} = {latex(l)} = {latex(l2)} $$")

# for i in range(10):
#     for j in range(10):
#         print(i, j, find_divisors((i, j)))
#
