from math import factorial
from random import randrange

def is_won(prev):
    n=len(prev)
    nums=[0]*n

    for i in range(n):
        for j in range(i):
            if prev[i][j] is True:
                nums[i]+=1
                nums[j]+=1

    return n-1 in nums and nums.index(n-1)

def is_winning(prev, rem, last):
    winnable=[True, True]

    for i in range(len(last)):
        for j in range(len(prev)):
            for k in range(j):
                if last[i] not in [j, k] or (j, k) == last: continue
                if prev[j][k] is False:
                    winnable[i]=False
                    break
                prev[j][k]=True
            if not winnable[i]: break
        if is_won(prev) is not False:
            winnable[i]=False
        for x, y in rem:
            prev[x][y]=None

    return winnable[0] or winnable[1]

def winning_move(prev, edge):
    rem=[]
    for i in range(len(prev)):
        for j in range(i):
            if (i, j) != edge and prev[i][j] is None: rem.append((i, j))

    (x, y) = edge
    if rem==[]:
        prev[x][y]=True
        return True
    wins=[0, 0]
    for i in range(2):
        move=i==1
        prev[x][y] = move
        if len(rem) > 0 and is_won(prev) is not False: continue
        res=True
        for last_edge in rem:
            w = is_winning(prev, rem, last_edge)
            # print(last_edge, ":", w)
            res &= w
            wins[i] += w

        # if res: return (move, wins)

    move=wins[1]==max(wins)
    if wins[0]==wins[1]:
        move=randrange(0, 2)==0
    prev[x][y]=move
    return (move, wins)

def perm(n, l):
    res=[]

    for base in range(len(l), 0, -1):
        idx=n%base
        res.append(l[idx])
        l.pop(idx)
        n//=base
    
    return res

def test(n):
    edges=[(i, j) for i in range(n) for j in range(i)]
    tot=factorial(len(edges))
    won=0
    for p in range(tot):
        choice=perm(p, edges[::])
        game=[[None]*i for i in range(n)]
        lost_curr=False
        for e in choice[:-1]:
            winning_move(game, e)
            if is_won(game): 
                lost_curr=True
                break
        if lost_curr:
            continue
        winning_move(game, choice[-1])
        if is_won(game): won+=1
        # else: print(choice)
    return (tot, won)

print(test(int(input())))
# n=5
# res=[[None]*i for i in range(n)]
# g=[(4, 3), (1, 0), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2)]
# for c in g:
#     print(winning_move(res, c))
#     print(is_won(res))
#     print(res)
# res=[[None]*i for i in range(int(input()))]
#
# while True:
#     print(winning_move(res, tuple(sorted(tuple(map(int, input().split())), reverse=True))))
