# in a game of N coin flips where every HH scores a point for A, 
# and every HT scores a point for B, how often do either of them win? 
# HHH counts as two points for A, HHT scores one point for each.

# let h(n, s) be the number of n-coin-flips games where <points of A> - <points of B> = s.
# and each game ends with an H. 
# Let t(n, s) be the same but with each game ending with a T.

# then, 
#      h(n, s) = h(n-1, s-1) + t(n-1, s).
#                ..HH          ..TH
# and, similarly,
#      t(n, s) = h(n-1, s+1) + t(n-1, s)
#                ..HT          ..TT
# which means,
#      t(n, s) = \sum_{i=1}^{n-1} h(i, s+1).
#      h(n, s) = \sum_{i=1}^{n-1} t(n-i, s-i+1).

# c(n, a, b) = c(n-1, a, b) + \sum_{i=2}^{n} c(n-i, a-i+2, b-1)

# c(n, a, b) = {b+t-1 \choose b}{a+b \choose a} + {b+t \choose b}{a+b-1 \choose a}, where t=n-a-2b

from math import comb

def count_scores(n, s):
    r=0
    for a in range(max(0, s), (n+2*s)//3+1):
        b=a-s
        t=n-a-2*b
        r+=comb(b+t-1, b)*comb(a+b, a) if t >= 1 else 0
        r+=comb(b+t, b)*comb(a+b-1, a) if b >= 1 else 0
    return r

def f(n, s):
    return comb(s, n) + comb(s, n-1) - comb(s-1, n-1)

def count_wins_1(n):
    r=[0, 0]
    for a in range(n+1):
        for b in range((n-a)//2+1):
            if a==b: continue
            i=a<b
            t=n-a-2*b
            r[i]+=comb(b+t-1, b)*comb(a+b, a) if t >= 1 else 0
            r[i]+=comb(b+t, b)*comb(a+b-1, a) if b >= 1 else 0

    return r

for i in range(1, 9):
    print(i, count_scores(3, i), f(3, abs(i)))

def count_wins_bf(n):
    c=r_a=r_b=0
    l=2**n
    while c<l:
        p=c&1
        s=0
        for i in range(1, n):
            d=(c&(1 << i)) >> i
            s+=p*(d*2-1)
            p=d

        r_a += s>0
        r_b += s<0
        c += 1

    return r_a,r_b

for i in range(101):
    print(i, count_wins_1(i))
