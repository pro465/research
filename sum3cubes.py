from itertools import product
# solves a^3 + b^3 + c^3 = n (mod m) given n and m

def solve(n, m):
    n%=m
    cubes=[[] for _ in range(m)]
    for i in range(m):
        cubes[i**3%m].append(i)
    sols = set()
    for i in range(n+1):
        for j in range(i//2+2):
            k=(n-(i+j))%m
            # if k==0: continue
            sols.update(map(lambda x: tuple(sorted(x)), product(cubes[i], cubes[j], cubes[k])))

    return sols

def double(sols, n, m):
    nm=2*m
    n%=nm
    res=set()
    for i,j,k in sols:
        for i_,j_,k_ in product(range(2), repeat=3):
            i_=i_*m+i
            j_=j_*m+j
            k_=k_*m+k
            if (i_**3+j_**3+k_**3)%nm == n:
                res.add(tuple(sorted((i_, j_, k_))))
    return res
m=100
n=3
sols=solve(n, m)
for i in range(5):
    print(m*2)
    sols=double(sols, n, m)
    m*=2
    print(len(sols))
        
# for i in range(4, 100):
#     for j in range(2, i):
#         if i%j == 0: break
#     else: print(i, solve(3, i))
