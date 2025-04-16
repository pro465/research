def step(arr, n):
    for i,a in list(enumerate(arr))[::-1]:
        if a < arr[-1]:
            return arr[:i]+arr[i:-1]*n

    return arr[:-1]

a=[0,1,1]
n=2

while a:
    print(a:=step(a, n), n)
    n+=1

