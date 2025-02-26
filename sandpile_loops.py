# 0 0 0 0 0
# 0 0 1 .5 0
# 0 1 0 0 0
# 0 .5 0 0 0
# 0 0 0 0 0

# 0  0  0
# 0  0 .5
# 0 .5  0
from random import shuffle
def f(m, n, arr):
    curr=[[0]*n for _ in range(m)]
    r=[[0]*n for _ in range(m)]

    for (i, j) in arr:
        curr[i][j] -= 4
        curr[((i-1)+m)%m][j] += 1
        curr[((i+1)+m)%m][j] += 1
        curr[i][((j-1)+n)%n] += 1
        curr[i][((j+1)+n)%n] += 1
        r[i][j]=min(r[i][j], curr[i][j])
    return -sum(map(sum, r))
m=2
n=2
t=3
a=[(i, j) for i in range(m) for j in range(n)]*t
print(a)
print(f(m, n, a))
shuffle(a)
print(f(m, n, a))


# import numpy as np
#
# def to_mat(arr, tw, th):
#     h=len(arr)
#     w=len(arr[0])
#     els=tw*th
#     res=[[0]*els for _ in range(els)]
#     
#     for r in range(els):
#         i,j=r%tw,r//tw
#         for c in range(w*h):
#             a,b=c%w,c//w
#             offa,offb=a-w//2,b-h//2
#             x,y=i+offa,j+offb
#             x%=tw
#             y%=th
#             c=y*tw+x
#             res[r][c]+=arr[a][b]
#     print(res)
#
#     return np.array(res, order='F')
#
# arr=[[0, 1, 0], [1, -4, 1], [0, 1, 0]]
#
# mat=to_mat(arr, 4, 3)
#
# print(mat)
#
# matinv=np.linalg.det(mat)
#
# print(matinv)
#
# print(np.dot(mat, matinv))
#
# flattened=[arr[i//5][i%5] for i in range(25)]
# print(list(map(sum, matinv*np.array(flattened))))

# from scipy import signal
#
# p=[1, 0, 1]
# id=[0, 1, 0]
#
# print(signal.deconvolve(id, p))
#
# res=[p[0]]
#
# for i in range(1, 100):
#     s=0
#     for j in range(1, i+1):
#         if j>=len(p): break
#         s+=res[i-j]*p[j]
#     res.append(s*-p[0])
# print(res)
