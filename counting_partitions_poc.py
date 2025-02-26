def p(n):
    res=0
    curr=[0]*(n-1)
    while curr[n-2] == 0:
        res+=1
        s=sum(map(lambda i: curr[i]*(i+2), range(n-1)))
        num_ones=n-s
        part_sum=num_ones
        for i in range(n-1):
            if i+2 <= part_sum:
                curr[i]+=1
                curr[:i]=[0]*i
                break
            part_sum+=curr[i]*(i+2)
    return res+1
prev=1
for i in range(2, 40):
    c=p(i)
    print(i, c/prev)
    prev=c
