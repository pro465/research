def from_reg(p):
    res = []
    poss = list(range(len(p)))
    for i in p:
        idx = poss.index(i)
        res.append(idx)
        poss = poss[:idx] + poss[idx+1:]
    return res
def construct_larger(smaller):
    poss = list(range(len(smaller) + 1))
    res = []
    for i,x in enumerate(smaller):
        idx = x if all(map(lambda j: i != j, poss[:x + 1])) else x + 1
        res.append(poss[idx])
        poss = poss[:idx] + poss[idx+1:]
    res += poss
    return res

print(construct_larger(from_reg([2, 1, 0])))
