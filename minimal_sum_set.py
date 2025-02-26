# problem: given N, return a subset S of whole numbers s.t. for all x in [N] = {0, 1, ..., N}, there exists a,b in S s.t. a+b=x.
import itertools
import math

def works(n, sol):
    for i in range(n+1):
        b=False
        for idx, j in enumerate(sol):
            for k in sol[idx:]:
                if j+k==i:
                    b=True
                    break
            if b: break
        if not b: return False
    return True

def minsumset_b(last, n):
    l=list(range(n+1))
    for i in range(last, n+1):
        for j in itertools.combinations(l, i):
            if works(n, j): return list(j)
    return l

def first_nonhit(l):
    for i,x in enumerate(l):
        if not x:
            return i
    return len(l)

def mss1(n):
    res=[]
    covered=[False]*(n+1)
    while not all(covered):
        best_score=0
        best_idx=0
        best_c=covered
        for next in range(n+1):
            c=covered[::]
            s=0
            for a in res+[next]:
                if next+a<len(c):
                    if not c[next+a]:
                        s+=1
                    c[next+a]=True
            if s>best_score:
                best_score=s
                best_idx=next
                best_c=c
        covered=best_c
        res.append(best_idx)

    return sorted(res)

def int2list(num, base):
    res=[]
    while num>0:
        res.append(num%base)
        num//=base
    return res[::-1]

def mss2(n):
    b=4*n*n
    num=0
    for i in range(n+1):
        num=num*b+1
    num=1+math.isqrt(num-1)
    print(int2list(num, 2*n))
    l=int2list(num, 2*n)
    if len(l)&1 != 1: l.append(0)
    num=[1]
    for i in range(1, len(l), 2):
        num+=[l[i]*2*n + l[i+1]]
    print(num)

def nonhit(n, sol):
    for i in range(n+1):
        b=False
        for idx,j in enumerate(sol):
            for k in sol[idx:]:
                if i==j+k:
                    b=True
                    break
            if b: break
        if not b: return False
    return True

for i in range(1, 10):
    sol=mss2(i)
    print(i, sol)
    # assert nonhit(i, sol)
# last=0
# for i in range(50):
#     s=minsumset_b(last, i)
#     last=len(s)
#     print(i, s)
