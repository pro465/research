# multiplicative persistence

from copy import deepcopy

sdp=[2, 3, 5, 7]

def factorize(n):
    f=[0]*4

    for i,base in enumerate(sdp):
        while n%base==0:
            n//=base
            f[i]+=1

    if n == 1: return f

def new(f):
    a = []
    for i in range(4): a += [[0]*i+[1]+[0]*(3-i)+[sdp[i]]]*f[i]
    return a

def next(a, f):
    if len(a)==0: return

    x=a[-1]
    a=a[:-1]

    fc=f.copy()

    for i in a:
        for j in range(4): f[j]-=i[j]

    for i in range(x[4]+1, 10):
        f2=factorize(i)
        for j in range(4):
            if f2[j] > f[j]: break
        else: break
        continue
    else:
        return next(a, fc)

    a.append(f2+[i])
    for i in range(4): f[i]-=f2[i]
    return a+new(f)

c=1

for i in range(1,211):
    if factorize(i) is not None: c+=1

print(c)

def most(n):
    f=factorize(n)
    if f is None: return 0
    print(n)

    step=0
    curr=new(f)

    while curr is not None:
        num=0
        for i in curr:
            num=num*10+i[4]
        curr=next(curr, f.copy())
        if num == n: continue
        step=max(step, most(num))

    return step+1

print(most(int(input())))
