from math import gcd, isqrt

def init_base(u):
    r=[2]
    for i in range(3, u):
        for j in r:
            if j*j>i: 
                r.append(i)
                break
            if i%j==0: break
    return [-1]+r

def factor(n, base):
    r=[0]
    if n<0: 
        r=[1]
        n=-n
    for p in base[1:]:
        c=0
        while n%p==0:
            n//=p
            c+=1
        r.append(c)
    return (r, n)

def tobits(a):
    res=0
    for (i, x) in enumerate(a): res|=(x&1)<<i
    return res

def find_square(smooths, m):
    a=[1<<i for i in range(len(smooths))]
    fs=[tobits(f) for (_,f) in smooths]

    for i in range(m):
        last_one=-1
        for (j, f) in enumerate(fs):
            if (f>>i)&1==1:
                if last_one>=0:
                    fs[last_one]^=f
                    a[last_one]^=a[j]
                last_one=j
        if last_one>=0:
            a.pop(last_one)
            fs.pop(last_one)

    return [[x for (i, x) in enumerate(smooths) if (res>>i)&1==1] for res in a]

def sqrtmod(p):
    res = [[] for _ in range(p)]
    for i in range(p):
        res[(i*i)%p].append(i)
    return res

def sieve(smooths, curr, k, n, base, sqrtmodps):
    global blocksize
    s=[[(curr+i)**2-n*k, [0]] for i in range(blocksize)]
    for i in range(blocksize):
        if s[i][0]>=0: break
        s[i]=[-s[i][0], [1]]

    for (i, (p, sqrts)) in enumerate(zip(base[1:], sqrtmodps)):
        i+=1
        for sqrt in sqrts[(n*k)%p]:
            start = (sqrt-curr)%p
            for j in range(start, blocksize, p):
                c=0
                assert s[j][0]%p==0, f"{(n*k)%p} {sqrt} {p} {s[j][0]%p}"
                while s[j][0]%p==0:
                    s[j][0]//=p
                    c+=1
                for _ in range(len(s[j][1]), i): s[j][1].append(0)
                s[j][1].append(c)

    #print(k)
    for (i, [r, f]) in enumerate(s):
        if r==1:
            smooths.append((curr+i, f))
            print(len(smooths))

def f(n):
    global blocksize
    base=init_base(1000)
    sqrtmodps=[sqrtmod(p) for p in base[1:]]
    m=len(base)
    print(n, base, m)
    klim=1
    curr=isqrt(n)-100
    while True:
        smooths=[]
        while len(smooths)<m+1:
            for k in range(-klim, klim+1):
                if len(smooths)>m: break
                sieve(smooths, curr, k, n, base, sqrtmodps)
           # print(s)
            curr+=blocksize
           # print(curr)
           # return

        u=find_square(smooths, m)
        for u in u:
            a,b=1,[0]*m
            for (r, es) in u:
                a*=r
                for (i, e) in enumerate(es):
                    b[i]+=e
            c=1
            for (p, e) in zip(base, b): c*=p**(e//2)
            assert (a*a-c*c)%n==0
            print("done")
            j,k = gcd(a-c,n),gcd(a+c, n)
            if 1<j<n: return j,n//j
            if 1<k<n: return k,n//k



blocksize=100000
p=210239178542499293758264810223
q=14756920832661448242304775251734300884245057976431
print(f(257*257))
