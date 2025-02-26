
"""
partial credit goes to Denise Roßberg for providing the links to learn about Euler's generating function for partitions, which is what this builds upon.

check out their solution: 

https://code.sololearn.com/cNBcNkTisKOE/?ref=app

mathematical basis:
let p'(n, k) be the no. of partitions of n with each summand being <= k.
e.g. p'(2, 1)=1 since only 2=1+1 has each summand <= 1, and 2+0 does not, since 2>1.

then (allergen warning: LaTeX below)

 p'(n, k)=\sum_{i=0}^{\lfloor {n \over k} \rfloor} p'(n - i k,k-1)
 
obviously, p(n), the actual partition function, is equal to p'(n, n).

this eq. also implies, via induction, p'(n, n+k)=p'(n, n).

just sprinkle dynamic programming on top, and you get this:
"""

def p(n):
    curr,prev=[0]*(n+1),[0]*(n+1)
    curr[0]=1 # p'(0, 0)=1
    
    for i in range(1, n+1):
        prev,curr=curr,prev
        curr[i-1]=prev[i-1]
        for j in range(i, n+1):
            curr[j] = sum(map(lambda m: prev[j-m*i], range(j//i+1)))
    
    return curr
print(p(10))
def viz(n, k, l):
    if k > n: return viz(n, n, l)
    if k > 0:
        for i in range(n//k+1):
            viz(n-i*k, k-1, l)
    l[k][n] = (n, k)

for i in range(10):
    l=[{} for _ in range(i+1)]
    viz(i, i, l)
    for j in l: 
        for k in reversed(j):
            print(j[k], end=" ")
        print()
    print("===")

# for i in range(500):
#     p(i)
