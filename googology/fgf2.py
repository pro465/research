def f(arr, n):
    last,rest=arr[-1],arr[:-1]
    add = lambda x: [last-1]+x
    if last==0: return rest
    badpart=add(rest)
    for i in range(len(rest)-1, -1, -1):
        if rest[i] == last:
            badpart=add(rest[i+1:])
            break
    if len(badpart)==1: return add(rest)
    res=[]
    for i in arr:
        res += badpart*n if i==last else [i]
    return res

arr=[1,2,1,2]
n=1
while len(arr:=f(arr, n)):
    print(len(arr) if len(arr)>100 else arr, n)
    n+=1
