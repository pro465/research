import time

def expand(a):
    if len(a) == 0: return None
    l=a.pop()
    idx=-1
    for i in range(len(l)-1, -1, -1):
        if l[i]>0:
            idx=i
            break
    if idx==-1: return a
    l[idx]-=1
    a.append(l)
    a.append(l.copy())
    if idx==0: return a
    for i in range(len(a)):
        a[i][idx-1]+=1
    return a

def p(a):
    for i in a: 
        print(f"({', '.join(map(str, i))})", end="")
    print()

def solve(a):
    if len(a)==0: return 0
    c=0
    r=[0]*len(a[0])
    for col in a[::-1]:
        for i in range(len(col)):
            col[i]+=r[i]
        c2,r2=solve_column(col)
        c+=c2
        for i in range(len(r)):
            r[i]+=r2[i]
    return c

def solve_column(l):
    idx=-1
    for i in range(len(l)-1, -1, -1):
        if l[i]>0:
            idx=i
            break
    r=[0]*len(l)
    if idx==-1: return (0, r)
    l[idx]-=1
    if idx>0: l[idx-1]+=1
    c1,r1=solve_column(l)
    for i in range(len(l)):l[i]+=r1[i]
    c2,r2=solve_column(l)
    for i in range(len(l)):r2[i]+=r1[i]
    if idx>0: r2[idx-1]+=1
    return (c1+c2+1, r2)

a=[[3]*2 for _ in range(2)]
i=0

print(solve(a))
while a is not None:
    #time.sleep(1)
    if (i:=i+1)%100==0:
        print("step", i)
        p(a)
    a=expand(a)

print(i)
