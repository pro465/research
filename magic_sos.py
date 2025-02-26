def sqs(mod):
    squares=[(2*s*s)%mod for s in range(mod)]
    res=[]
    for s in range(mod):
        sq=(2*s*s)%mod
        res.append([])
        for i in range(mod):
            for j in range(i):
                if (i*i + j*j)%mod == sq:
                    res[-1].append((i, j))
    return res

print(sqs(100))

