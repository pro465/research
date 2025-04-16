def f(arr):
    last=arr.pop()
    if last==0: return arr
    badpart=arr[::]
    for i in range(len(arr)-1, -1, -1):
        if arr[i] <= last:
            badpart=arr[i+1:]
            break
    if len(badpart)==0: return arr
    for i in range(1, last+1):
        arr += [x*2**i for x in badpart]
    return arr

arr=[6,5,4,3]
n=1
while len(arr:=f(arr)):
    print(arr, n)
    n+=1
