"""
new problem: given a symmetric n by n matrix M, find a permutation p such that the sum of M[p(i)][p(j)]*|i-j| for all 0<=i<=j<n is minimized 
symmetric means M[i][j]=M[j][i] for all i,j
"""

import random

def cost(m, a):
    return sum(m[x][y]*(i-j)
               for (i,x) in enumerate(a)
               for (j,y) in enumerate(a[:i]))

def try_solve(m, n, it):
    a=list(range(n))
    min_cost=cost(m, a)
    random.shuffle(a)
    done=False
    while not done:
        done=True
        for i in range(len(a)):
            for j in range(i):
                (a[i], a[j])=(a[j], a[i])
                current_cost=cost(m, a)
                if current_cost<min_cost:
                    min_cost=current_cost
                    done=False
                else: (a[i], a[j])=(a[j], a[i])
    print("done", min_cost, a)
    return (min_cost, a)

n=6
m=[[random.randrange(100) for i in range(j+1)] for j in range(n)]
for i in range(1, n):
    for j in range(i):
        m[j].append(m[i][j])
for r in m: print(r)
sols=[try_solve(m, n, i) for i in range(100)]
print(sols)
(mincost, minsol)=min(sols, key=lambda a: a[0])
print(mincost, minsol)
"""
def convert(p, n):
    m=[[abs(i-j) for i in range(n)] for j in range(n)]
    left=list(range(n))
    perm=[]
    for i in range(n, 0, -1):
        perm.append(left.pop(p%i))
        p//=i
    if p: return None
    print(perm)
    res=[]
    for i in perm:
        res.append(m[i])
    for i in range(n):
        temp=res[i].copy()
        for (j, k) in enumerate(perm):
            res[i][j]=temp[k]
    return tuple(map(tuple, res))

n=4
p=0
l=[]
s=set()
while (c:=convert(p, n)) is not None:
    s.add(c)
    l.append(c)
    #print(c)
    p+=1
print(len(l), len(s))
"""
