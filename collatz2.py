# x=[1]
# y=[0]
#
# num=int(input())
# idx=0
# assert num%2==1
#
# def next(x, y, idx):
#     y[idx]+=2
#     n=(x[idx] << y[idx])//3
#     if n%3==0 or n in x: return n
#     x.append(n)
#     y.append(1-n%3)
#     return n
#
# while True:
#     c=next(x, y, idx)
#     print(c)
#     if c==num: break
#     l=len(x)
#     idx=(l+idx-1)%l

for i in range(1, 18, 2):
    p=3-i%3
    if p==3: continue
    print(i, (i<<p)//3)
