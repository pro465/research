def to_list(num, base, l):
    res=[]
    for _ in range(l):
        res.append(num%base)
        num//=base
    return res[::-1]

def max_prefix(a, b):
    for i in range(len(a), -1, -1):
        if a[:i]==b[-i:]: return i
    return 0

def e3(a, b, base, l, n):
    lookup=[[[None]*base for _ in range(l+1)] for _ in range(2)]

    a=to_list(a, base, l)
    b=to_list(b, base, l)

    for i in range(2):
        for j in range(l+1):
            res=(a, b)[i][:j]+[0]
            for k in range(base):
                res[-1]=k
                a_match=max_prefix(a, res)
                b_match=max_prefix(b, res)
                lookup[i][j][k] = (1, b_match) if b_match > a_match else (0, a_match)

    prev=[[[0]*(2*n+1) for _ in range(l+1)] for _ in range(2)]
    curr=[[[0]*(2*n+1) for _ in range(l+1)] for _ in range(2)]
    for i in range(2):
        for j in range(l+1):
            curr[i][j][n]=1

    for _ in range(1, n+1):
        curr, prev = prev, curr

        for i in range(2):
            for j in range(l+1):
                curr[i][j] = [0]*(2*n+1)
                for b in range(base):
                    i_, j_ = lookup[i][j][b]
                    o=0
                    if j_ == l: o=[-1, 1][i_]

                    for s in range(max(-n, -n-o), min(n, n-o)+1):
                        curr[i][j][s+n]+=prev[i_][j_][s+n+o]

    return sum(curr[0][0][:n]),curr[0][0][n],sum(curr[0][0][n+1:])


# def e2(a, b, base, l, n):
#     num=base**(l-1)
#     prev=[[0]*(2*n+1) for _ in range(num)]
#     curr[[0]*(2*n+1) for _ in range(num)]
#
#     for i in range(num):
#         prev[i][n]=base
#         if i==a//base:
#             prev[i][n+1]=1
#             prev[i][n]-=1
#         if i==b//base:
#             prev[i][n-1]=1
#             prev[i][n]-=1
#
#     for i in range(l+1, n+1):
#         for j in range(num*base):
#             if j in (a, b): continue
#             for k in range(-n, n+1):
#                 curr[j//base][k+n]+=prev[j%num][k+n]
#
#         for k in range(-n, n):
#             curr[a//base][k+n+1]+=prev[a%num][k+n]
#             curr[b//base][k+n]+=prev[b%num][k+n+1]
#         prev,curr=curr,[[0]*(2*n+1) for _ in range(num)]
#         
#     return (sum(map(lambda x: sum(x[:n]), prev)), 
#             sum(map(lambda x: x[n], prev)), 
#             sum(map(lambda x: sum(x[n+1:]), prev)))

p=6
n=2**p

adv={}
b,b_score=[], None

for i in range(n):
    avg=min((-adv[(k, i)] if (k, i) in adv else adv[(n-i-1, n-k-1)] for k in range(i)), default=None)
    for j in range(i+1, n):
        if (n-j-1, n-i-1) in adv:
            s=-adv[(n-j-1, n-i-1)]
            print(i, j, s)
            avg=s if avg is None else min(avg, s)
            continue

        s=e3(i, j, 2, p, 100)
        # assert s == e2(i, j, 2, p, 100)
        # assert (s[2], s[1], s[0]) == e3(j, i, 2, p, 100)
        s=s[2]-s[0]
        print(i, j, s)
        avg=s if avg is None else min(avg, s)
        adv[(i, j)] = s
    print("max advantage for B:", -avg)
    if b_score is None or avg>b_score:
        b,b_score=[i],avg
    elif avg==b_score:
        b.append(i)

def ht(x):
    res=""
    for _ in range(p):
        res+="HT"[x%2]
        x//=2
    return res[::-1]

print("best:", b, "score:", b_score)
