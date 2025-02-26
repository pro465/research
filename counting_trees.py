from math import comb

def num_trees(cp, n):
    if n < 0: return 0
    return cp[n]

def tree(n):
    cache_p = [0]*(n+1)

    yield 1

    for i in range(min(2, n)):
        cache_p[i]=1
        yield 1

    for k in range(2, n+1):
        m=cache_p[k-2]-1

        for j in range(n, k, -1):
            for i in range(1, j//k+1):
                cache_p[j] += comb(m+i, i)*cache_p[j-i*k]
            idx=j-i*k
            cache_p[j] += comb(m+i, i) * (  num_trees(cache_p,idx-2) 
                                          - num_trees(cache_p,idx-1))

        cache_p[k]+=cache_p[k-1]

        yield cache_p[11]

    return 

with open("counting_trees.out.txt", "w") as file:
    for i, x in enumerate(tree(12)):
        print(f"{i-1} -> {x}")
        file.write(f"{i} -> {x}\n")
    file.close()
