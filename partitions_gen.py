def f(n):
    arr=[0]*(n+1)
    arr[0]=1
    for i in range(1, n+1):
        arr[i:] = [arr[j] - arr[j-i] for j in range(i, n+1)]
    return arr[n]

for i in range(100):
    print(f(i))
