"""
date: 29/09/24
New math problem!

you're in charge of something *like* the patent office. you have to assign a number to every [thing to be classified] that enters the building. You don't know how many kinds of things there are, but you do know one thing: they appear in a zipfian distribution. this means, if you're lucky or skilled enough, you could assign N numbers a,b,c... to the classes with frequencies A, B, C... to the items such that `1*A = 2*B = 3*C = 4*D ...` and a<b<c...

1. if your strategy is to give the number 1 to the first kind of thing you see, then 2 to the second, and so on... what is the average *deviation* between the number you assign and the ideal number?
2. what is the optimal strategy?

Example scenario:
there are 3 kinds of things: red, green, blue. P(red) = 6/11, P(green) = 3/11, P(blue) = 2/11.

you see the following:
green, red, red, blue, red, green, red, green, red
you label green=1, red=2, and blue=3. ideally, red=1, green=2, and blue=3. the average difference is (abs(1-2) + abs(2-1) + abs(3-3))/3 = 2/3.

1 restated: what is that average, given N, the number of "kinds" (colors, in this example)
2 restated: what strategy minimizes this average?

<@358359026083430410> <@1101094851090591804> <@459616693518467073> <@696824456697479240> <@521726876755165184> <@275982450432147456> <@609410502539608064>

clarification 1:
you can try this problem using Natural numbers as your labels or using Rationals as your labels, or Integers, or Reals. These are all fine, and if there's a different answer depending on which you use, all the better for this exploration.
"""

from itertools import combinations
import math

def solve_simpler(n, m, num_things, lookup, b):
    others=[b/(i+1) for i in range(num_things) if i+1 != n]
    return sum(lookup[c] for c in combinations(others, m-1))*b/n

def average(n, num_things, lookup, b):
    return sum(abs(n-m)*solve_simpler(n, m, num_things, lookup, b) for m in range(1, num_things+1))

def score(num_things):
    b=1/sum(1/(i+1) for i in range(num_things))
    l=[b/(i+1) for i in range(num_things)]
    lookup={():1.}
    for i in range(1, num_things):
        for c in combinations(l, i):
            p=sum(c)
            s=0
            for j,p2 in enumerate(c):
                others=c[:j]+c[j+1:]
                s+=lookup[others]*p2/(1-p)
            lookup[c]=s

    return sum(average(n, num_things, lookup, b) for n in range(1, num_things+1))/num_things


def product(i):
    r=1
    for i in i:
        r*=i
    return r

def score2(num_things):
    b=1/sum(1/(i+1) for i in range(num_things))
    l=[b/(i+1) for i in range(num_things)]
    lookup={():1.}
    for i in range(1, num_things):
        for c in combinations(l, i):
            p=sum(c)
            lookup[c]=product(map(lambda x: math.e**x - 1, c))

    return sum(average(n, num_things, lookup, b) for n in range(1, num_things+1))/num_things


import random

def score_sim(r):
    prev=[]
    res=0
    for i in r:
        if i not in prev:
            prev.append(i)
            res+=abs(len(prev)-i)
    return res

def simulate(n, k, lim):
    sc=0
    num=list(range(1, n+1))
    b=1/sum(1/i for i in num)
    dist=[b/i for i in num]
    for _ in range(k):
        sc+=score_sim(random.choices(num, weights=dist, k=lim))
    return sc/k/n

# for i in range(1, 21):
#     print(i, simulate(i, 50000, 200))
#
prev=0
for i in range(1, 21):
    c=score2(i)
    print(i, c)
    prev=c
