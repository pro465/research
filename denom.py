def f(n):
    res=[[0, 1]]
    if n<=1: return [res[0][:n+1]]
    for i in range(2, n+1):
        res2=[]
        res3=[]
        for s in res:
            for j in s:
                k=i-j
                if j>k: break
                if k in s: res2.append(s)
                else: res3.append(s+[k])
        res=(res2, res3)[len(res2)==0]
    return res

for n in range(100):
    print(n, f(n)[0])
