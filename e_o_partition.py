def f(n):
    e, o = [0]*(n+1),[0]*(n+1)
    e[0] = 1

    for i in range(1, n+1):
        for j in range(n, i-1, -1):
            e[j]+=o[j-i]
            o[j]+=e[j-i]
    
    return list(zip(e, o))

print(f(10))
