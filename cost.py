def m(n):
    a=[0]*(n+1)
    for i in range(2, n+1):
        a[i]=a[i-1]+1
        for f in range(2, i):
            if i%f==0:
                a[i]=min(a[i], a[i//f]+a[f])

    return a

def m2(n):
    return n-1

print(*enumerate(m(100)), sep='\n')
