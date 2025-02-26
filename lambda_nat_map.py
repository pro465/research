def shift(expr, offset, cutoff=0):
    if isinstance(expr, int):
        return expr + (offset if expr >= cutoff else 0)
    elif isinstance(expr, tuple):
        return (shift(expr[0], offset, cutoff), shift(expr[1], offset, cutoff))
    else:
        return [shift(expr[0], offset, cutoff + 1)]

def substitute(expr, value, depth=0):
    if isinstance(expr, int):
        if expr == depth:
            return shift(value, depth)
        elif expr > depth:
            return expr - 1
        else:
            return expr
    elif isinstance(expr, tuple):
        return (substitute(expr[0], value, depth), substitute(expr[1], value, depth))
    else:
        return [substitute(expr[0], value, depth + 1)]
        
def beta_reduce(expr):
    if isinstance(expr, tuple) and isinstance(expr[0], list):
        return substitute(expr[0][0], expr[1])
    elif isinstance(expr, tuple):
        a=beta_reduce(expr[0])
        return (a, beta_reduce(expr[1]) if a == expr[0] else expr[1])
    elif isinstance(expr, list):
        return [beta_reduce(expr[0])]
    else:
        return expr

def t(n, b=2):
    d=n%b
    r=n//b
    if d==b-2:
        tr,r=t(r, b+1)
        return ([tr], r)
    if d==b-1:
        param,r=t(r, b)
        fn,r=t(r, b)
        return ((fn, param), r)
    return (d, r)

def n_to_l(n):
    res,n=t(n, 3)
    res = [res]
    while n>0:
        r1,n=t(n)
        res=(r1, res)
    return res

def tb(term, b):
    if isinstance(term, list):
        res, n = tb(term[0], b+1)
        return (b-2+b*res, n*b)
    if isinstance(term, tuple):
        res1, n1 = tb(term[0], b)
        res2, n2 = tb(term[1], b)
        return (b-1+b*(res2+res1*n1), n1*n2*b)
    return (int(term), b)

def l_to_n(term):
    if isinstance(term, tuple):
        fn, n1 = tb(term[0], 2)
        arg, n2 = l_to_n(term[1])
        return (arg + n2*fn, n1*n2)
    a,b=tb(term[0], 3)
    return a,b

def r(a, b, k=100):
    a,b = n_to_l(a), n_to_l(b)
    for i in range(k):
        if a == b: return True
        a=beta_reduce(a)
    return a == b

def all_reduces(i, k=100):
    res=[i]
    i=n_to_l(i)
    for j in range(k):
        n=beta_reduce(i)
        if n!=i: break
        n=i
        res.append(l_to_n(i)[0])
    return res

for i in range(500):
    print(i, all_reduces(i))
    # for j in range(500):
    #     print(" #"[r(i, j)], end="")
    # print(i)
