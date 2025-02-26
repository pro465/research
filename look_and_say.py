def f(n):
    r=[1]
    if n==1: return 1
    for i in range(n):
        r2=[]
        j=0
        while j<len(r):
            c=1
            if j+1<len(r) and r[j]==r[j+1]:
                c+=1
                if j+2<len(r) and r[j]==r[j+2]:
                    c+=1
            r2+=[c, r[j]]
            j+=c
        r=r2
        print(i)
    return len(r)

print(f(70))
