from copy import deepcopy

def map_children(t, f):
    return t[:1]+[f(c) for c in t[1:]]

def reset_label(a, x):
    return [x]+[reset_label(c, x) for c in a[1:]]

def replace_leaves(a, x):
    f=lambda c: replace_leaves(c, x)
    if len(a) == 1: return deepcopy(x)
    else: return map_children(a, f)

def reset_tree(t1, t2):
    f=lambda c: reset_tree(c, t2)
    return replace_leaves(t2, map_children(t1, f))

def pn(a, n):
    if a == 0: return None
    return n if a == -1 else a-1

def p(t, n):
    pred=pn(t[0], n)
    if pred is None: return False
    i=-1
    for j in range(1, len(t)):
        if p(t[j], n):
            i=j
            break
    if i>=0:
        for j in range(1, i):
            t[j]=reset_label(t[j], pred)
    else:
        d=reset_label(t, pred)
        t[:]=reset_tree(d, d)
    return True

n=2
i=0
a=[n, [n], [n]]
while p(a, n):
    i+=1
    print(i, a)
