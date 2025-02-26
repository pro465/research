def part(n, x):
    res=[[[]]] + [[] for _ in range(n)]
    for i in range(x, n+1):
        for j in range(i, n+1):
            res[j] += [p + [i] for p in res[j-i]]
    return res
print(part(6, 2))
