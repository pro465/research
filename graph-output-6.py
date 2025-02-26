import copy

a = [[[3, 4], [5], [5], [0], [0], [1, 2]], [[2, 5], [4], [0], [4], [1, 3], [0]]]

def encode(p, g):
    res = 1

    for i in range(len(g)):
        exp = 1
        for j in g[i]:
            exp *= p[j]

        res *= p[i] ** exp 
    return res

orig = [2, 3, 5, 7, 11, 13]

def perm(a, res, p, b):
    global orig
    if len(p) == 0:
        return encode(res, a) == encode(orig, b)
    return any(map(lambda x: perm(a, res + [x[1]], p[:x[0]]+p[x[0]+1:], b), enumerate(p)))

def is_isomorph(a, b):
    global orig
    return perm(a, [], orig, b)

def isomorph(a):
    for i in range(len(a)):
        for j in range(i):
            if is_isomorph(a[i], a[j]):
                return (a[i], a[j])

def primes(n):
    res = []
    i = 2
    while len(res)<n:
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
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
    
    #if p[j] == 7: print("n1", n1, "n2", n2)
    
    if n1 > n2:
        # swap_if_less
        #print(g, n1, n2)
        return

    swap_primes(p, i, j)

def swap_primes(p, i, j):
    (p[i], p[j]) = (p[j], p[i])

def rearrange(g, p):
    for i in range(len(g)):
        for j in range(i):
            if p[j] > p[i]:
                swap_primes(p, i, j)
                swap_graph(g, i, j)
                (g[i], g[j]) = (g[j][:], g[i][:])


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

for i in a:
    c = copy.deepcopy(i)
    m = minimal(c)
    if m != i:
        print(i, m)

    print(encode([2, 3, 5, 7, 11, 13], i))

print(isomorph(a))
