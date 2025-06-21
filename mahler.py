lim=25
m=15
a=list(range(2,2**m))
for i in range(m,lim):
    cm=0
    it=0
    while it<len(a):
        n=a[it]
        c=2
        while n&3:
            n+=n>>1
            c+=1
        cm=max(c,cm)
        if c>i:
            it+=1
            continue
        n=a.pop(it)
        a=[j for j in a if j<n or j-n&((1<<c)-1)]
        #print(n,c,a)
    print(cm,len(a)//2,"/",2**i-2)
    a+=[j+2**(i+1) for j in a]
    
