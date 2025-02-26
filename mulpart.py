from copy import deepcopy

def inc(base, curr):
    for (i, b) in reversed(list(enumerate(base))):
        if curr[i] < b:
            curr[i]+=1
            return True
        curr[i]=0
    return False

def sub(a, b):
    for (i, v) in enumerate(b):
        if a[i] < v: return False
        a[i]-=v
    return True

def idx(base, vec):
    res=0
    for (b, v) in zip(base, vec):
        res = res*(b+1) + v
    return res

def mulpart(base):
    num_factors = 1
    for i in base:
        num_factors*=i+1

    x=[0]*len(base)
    curr,prev=[0]*num_factors,[0]*num_factors
    curr[0]=1 # since [0, 0, ..] = [0, 0, ..]*1

    while inc(base, x):
        prev,curr=curr,prev
        n=[0]*len(base)
        while True:
            n_idx=idx(base, n)
            curr[n_idx]=prev[n_idx]
            o=deepcopy(n)
            while sub(o, x):
                curr[n_idx] += prev[idx(base, o)]
            if not inc(base, n): break


    return curr[num_factors-1]

print(mulpart([2, 3]))
