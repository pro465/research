def six(n):
    return n%6+(six(n//6)*10 if n>=6 else 0)

def collatz(n):
    n=4*n+3
    x,count=n,0
    while x>=n:
        print(x, end=" -> ")
        if x%2==0: x//=2
        else: x=3*x+1
        count+=1
    print(x)
    return (n, count)

def f(n):
    if n&1==1:
        n+=1
        while n&1==0:
            n//=2
            n*=3
        return (n-1)
    while n&1==0:
        n//=2
    return (n)

def c2(n):
    if n==1: return []
    r=[]
    while n > 2:
        a=0
        while n&1==0:
            n//=2
            a+=1
        r.append(a)
        a=0
        n+=1
        while n&1==0:
            n//=2
            n*=3
            a+=1
        n-=1
        r.append(a)
    if n==1: r+=[0, 1]
    if n==2: r+=[1]
    return r

def g(n):
    i=0
    while n&1==0:
        n//=2
        i+=1
    return i

def inv(m, n):
    (s, t) = (1, 0)
    while n > 0:
        q=m//n
        (m, n) = (n, m-q*n)
        (s, t) = (t, s-q*t)
    assert m==1
    return s

def nums_taking_path(a):
    (r,s)=(1,1)
    for i in range(len(a)-1,-1,-1):
        m=a[i]
        if i&1==0:
            r<<=m
            s<<=m
        else:
            s=((s+1)*inv(3**m, r))%r
            r<<=m
            s=(s<<m)-1
    return (r, s)

def step_thru_path(r, s, p):
    for i, n in enumerate(p):
        if i&1==0:
            r>>=n
            s>>=n
        else:
            s=((s+1)>>n)*3**n-1
            r=(r>>n)*3**n
    return r,s

def solve(a, b, c, d):
    m=d-b
    n=a-c
    if m%n==0: return m//n

def earliest_decrease(c,n):
    twos,threes=1,1
    for i in range(n-1,-1,-1):
        twos<<=1
        dig = (c>>i)&1
        if dig==1: threes*=3
        if twos > threes: return i
    return -1

def convert(p, l):
    res=[]
    last=0
    count=0
    for i in range(l-1,-1,-1):
        dig = (p>>i)&1
        if dig == last: count+=1
        else:
            last=dig
            res.append(count)
            count=1
    if count>0: res.append(count)
    return res


def nonloops(n):
    curr=0
    arr=[0]*2**n
    while curr<2**n:
        a=earliest_decrease(curr, n)
        if a==-1:
            curr+=1
            continue
        p=convert(curr>>a, n-a)
        r,s=nums_taking_path(p)
        t,u=step_thru_path(r,s,p)
        assert r>t
        assert r<=2**n
        m=int(s<=u)
        # print(f"{r}k+{s}, k>={m}")
        for i in range(m*r, 2**n-s, r):
            arr[i+s]=1

        curr=((curr>>a)+1)<<a
    print(sum(arr), sum(arr)/2**n)


# for i in range(50):
#     for j in range(1, 200):
#         iv=inv(3**i,2**j)
#         if iv<0:iv+=2**j
#         print(" @"[iv>=2**(j-1)], end="")
#
#     print()
for i in range(1, 30):
    nonloops(i)

# for i in range(100):
#     for j in range(1, 21):
#         print(g((2*i+1)*3**j-1), end=', ')
#     print()
#
# for i in range(100):
#     print(''.join(' #'[j=='1'] for j in bin(3**i)[2:]))
#
# # print(collatz(int(input())))
# print(*map(f, range(1, int(input())+1)), sep=', ')
