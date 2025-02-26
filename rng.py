def collatz(n):
    i=0
    while n>1:
        n=(n>>1,n*3+1>>1)[n&1]
        i+=1
    return i

with open("random.bin", "w") as f:
    for i in range(1, 501):
        f.write("01"[collatz(i)&1])
