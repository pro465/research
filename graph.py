import copy

def graph(g, e):
    res = []
    i = 0
    j = 0
    for _ in range(0, e):
        if j == 0: res.append([])

        if j >= i:
            j = 0
            i += 1
            res.append([])

        if g&1 == 1: res[i].append(j)

        j += 1

        g >>= 1
    return link(res)

def link(g):
    for i in range(len(g)):
        for j in g[i]:
            g[j].append(i)
    return g

def primes(n):
    res = []
    i = 2
    while len(res)<n:
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        if prime: res.append(i)
        i += 1
    return res

def minimal(g):
    p = primes(len(g))

    prev = encode(p, g)
    
    while True:
        for i in range(len(g)):
            for j in range(i):
                swap_if_less(g, p, j, i)

        curr = encode(p, g)
        if prev == curr: break
        prev = curr

    rearrange(g, p)

    for i in range(len(g)):
        g[i].sort()

    return g

def swap_if_less(g, p, i, j):
    n1 = encode(p, g)
    swap_primes(p, i, j)
    n2 = encode(p, g)
    print(p, n1, n2, sep='\n')
    
    #if p[j] == 7: print("n1", n1, "n2", n2)
    if n1 > n2:
        # swap_if_less
        # print(g,p, i, j)
        return
    swap_primes(p, i, j)

def rearrange(g, p):
    for i in range(len(g)):
        for j in range(i):
            if p[j] > p[i]:
                swap_primes(p, i, j)
                swap_graph(g, i, j)
                (g[i], g[j]) = (g[j][:], g[i][:])

def swap_primes(p, i, j):
    (p[i], p[j]) = (p[j], p[i])

def swap_graph(g, i, j):
    for w in set(g[i] + g[j]):
        for x in range(len(g[w])):
            if g[w][x] == i:
                g[w][x] = j
            elif g[w][x] == j:
                g[w][x] = i

def encode(p, g):
    res = 1

    for i in range(len(g)):
        exp = 1
        for j in g[i]:
            exp *= p[j]

        res *= p[i] ** exp 
    return res

def num_edges(n): return n*(n-1)//2

#print(encode([2, 3, 5, 7], [0, 1], 2)*encode([2, 3, 5, 7], [3], 7))

# v = int(input())
# edges = num_edges(v)
# a = []
#
# for i in range(0, 2**edges):
#     g = graph(i, edges)
#     orig = copy.deepcopy(g)
#     #print("===========\n",g)
#     m = minimal(g)
#     if orig == m:
#         a.append(m)
#         #print(graph(i, edges))
#         #print("=",m, encode([2, 3, 5, 7, 11], m))
#
# print(a)
p = [2, 3, 5, 7, 11, 13]

# print(encode(p, [[4, 5], [2, 3], [1], [1], [0], [0]]))
print(minimal([[2, 5], [4], [0], [4], [1, 3], [0]]))
print(encode(p, [[3, 4], [5], [5], [0], [0], [1, 2]]))
