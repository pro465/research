def count_bst(n):
    c=[0]*(n+1)
    p=[0]*(n+1)
    p[0]=1
    c[0]=1
    d=[p[-1]]
    for depth in range(n):
        comb=[0]*n
        comb[0]=1

        for i in range(1, n+1):
            c[i]=0

            for j in range(i):
                c[i]+=comb[j]*p[j]*p[i-j-1]

            for j in range(n-1, 0, -1):
                comb[j]+=comb[j-1]

        d.append(c[-1])
        c,p=p,c

    for i in range(n, 0, -1):
        d[i]-=d[i-1]

    return d

for i in range(10):
    print(count_bst(i))
