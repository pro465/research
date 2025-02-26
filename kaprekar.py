# https://www.youtube.com/watch?v=d8TRcZklX_Q

def step(n, b):
    x=sorted(n)
    y=x[::-1]
    carry=0
    res=[]
    for i,j in zip(x, y):
        res.append((b+i-j-carry)%b)
        carry=i-j-carry<0
    return res


def k(n, b):
    while True:
        t=step(n, b)
        if t==n: return n
        print(t)
        n=t

for n in range(3, 100, 2):
    print(k([0]*n+[1], 10))
