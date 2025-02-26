def nz(arr): return [x for x in arr if x>0]

def p(arr):
    lim=arr[0]
    arr[0]-=1
    rep_idx=0
    for i,x in enumerate(arr):
        if x>=lim:
            rep_idx=i-(x>lim)
            break
    res=[lim-1]
    rep=arr[:rep_idx+1]
    for i in arr[rep_idx:]:
        res+=[i] if i != lim else rep

    return res

def f(arr):
    arr=nz(arr)
    n=0
    while len(arr):
        print(arr[:10], len(arr))
        n+=1
        arr=nz(p(arr))
    return n

print(f([3, 3, 3, 3, 3, 3]))
