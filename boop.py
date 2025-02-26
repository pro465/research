from random import choice, randrange
from itertools import product
from copy import deepcopy
import sys

sys.setrecursionlimit(10000)

def is_line(game, i, j, dx, dy):
    l=len(game)
    prev=game[i][j]
    for m in range(1,3):
        if i+dx*m >= l: return False
        if j+dy*m >= l: return False
        curr=game[i+dx*m][j+dy*m]
        if curr!=prev: return False
        prev=curr
    return True

def sc(game):
    dirs = [(0, 1), (1, 0), (1, 1)]

    for i in range(len(game)):
        for j in range(len(game)):
            if game[i][j]==0: continue
            for dx,dy in dirs:
                if is_line(game, i, j, dx, dy):
                    return (game[i][j], i, j, dx, dy)

def boop(game, i, j):
    l=len(game)
    res=[]
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if (dx,dy)==(0,0): continue
            cx,cy=i+dx,j+dy
            nx,ny=i+2*dx,j+2*dy
            if cx>=l or cy>=l: continue
            if game[cx][cy]==0: continue
            v,game[cx][cy]=game[cx][cy],0
            if not(0<nx<l and 0<ny<l):
                res.append(v)
                continue
            if game[nx][ny]==0: game[nx][ny]=v
            else: game[cx][cy]=v
    return res

def randsc(game, kittens, turn, rec=0):
    if rec==100: return 0
    l=len(game)
    idx=(turn+1)//2
    if kittens[idx]==0:
        kittens[idx]=1
        kit=[(i,j) for i,j in product(range(l), repeat=2) if game[i][j]==turn]
        i,j=choice(kit)
        game[i][j]=0
    unoc=[(i,j) for i,j in product(range(l), repeat=2) if game[i][j]==0]
    i,j=choice(unoc)
    game[i][j]=turn
    fellkits=boop(game, i, j)
    for k in fellkits: kittens[(k+1)//2]+=1
    s=sc(game)
    if s is None: return randsc(game, kittens, -turn, rec+1)
    s,i,j,dx,dy=s
    for m in range(3): game[i+m*dx][j+m*dy]=0
    return randsc(game, kittens, -turn, rec+1)*0.95+s

def avgsc(game, kittens, turn, times):
    res=0
    for i in range(times):
        if i%100==0:print(res)
        res+=randsc(deepcopy(game), kittens.copy(), turn)
    return res/times

def bestmove(game, kittens, turn, times):
    l=len(game)
    best=float("-inf"),-1,-1
    for i,j in product(range(l), repeat=2):
        if game[i][j]!=0: continue
        game[i][j]=turn
        sc=avgsc(game, kittens, -turn, times)
        if sc>best[0]:
            best=sc,i,j
        game[i][j]=0
    return best

game=[
    [0, 0, 0, -1, 0, 0],
    [1, 0, 0, 0, 0, -1],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [-1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
]
turn=1
kittens=[5, 2]
times=1000
print(bestmove(game, kittens, turn, times))
