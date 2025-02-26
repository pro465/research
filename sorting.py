from random import random

def apply(fs):
    x=0
    for f in fs:
        x=f[0]*x+f[1]
    return x

def all_(arr, score):
    print(arr, score)
    for i in range(1, len(arr)):
        for j in range(i):
            ac = arr.copy()
            ac[i],ac[j]=ac[j],ac[i]
            print(ac, apply(ac))
            if score < apply(ac): return False
    return True

def r(m): return random()*m - m/2

arr=[(-1.2669932999508509, -0.2334139209220929), (-0.7770975410833514, 0.9455888699997534), (0.9631674833222443, 1.0487582165000209)]
all_(arr, apply(arr))
arr=arr[-1:]+arr[:-1]
print(arr, apply(arr))
# m = 3
# n = 3
# while True:
#     arr=[(r(m), r(m)) for _ in range(n)]
#     arrc = arr[1:]+arr[:1]
#     score = apply(arrc)
#     if score < apply(arr) and all_(arrc, score):
#         print(arrc)
#         break
