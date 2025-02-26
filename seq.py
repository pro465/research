# 2, 3, 5, 7
# 277777788888899

def try_n(x, r=0):
    new = 0
    x2 = x
    for p in [2, 3, 5, 7]:
        while x2 % p == 0:
            new = new*10 + p
            x2 //= p
    if x2 > 1:
        return (x, r)
    return try_n(new, r+1)

def try2(n, r=0):
    if n < 10: return r
    new = 1
    while n > 0:
        new *= n%10
        n //= 10

    return try2(new, r+1)

for i in range(int(input())):
    t = try2(i)
    if t > 11:
        print(i)
