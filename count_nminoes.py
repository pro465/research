def inc(c, n):
    for i in range(len(c)):
        c[i]+=1
        if c[i]<n: return True
        c[i]=0
    return False

def is_match(p, x):
    for i in range(len(p)):
        if p[i:] + p[:i] == x: return True
    return False

def f(n, l):
    curr=[0]*l
    arr=[curr.copy()]
    while inc(curr, n):
        if all(map(lambda x: not is_match(x, curr), arr)): arr.append(curr.copy())
    return arr

def d(n, l):
    res = n**l

    for i in range(1, l):
        if l%i==0: res -= d(n, i)

    return res

print(d(2, 4))

def f_fast(n, l):
    res = 0

    for i in range(1, l+1):
        if l%i == 0:
            t = d(n, i) // i
            res += t
            print(i, "is", t)

    return res

n=2
k=12
print(f_fast(n, k))
a=f(n,k)
print(a)
print(len(a))
