from copy import deepcopy
def r1(x, y):
    x_=deepcopy(x)
    for i in range(3):
        for j in range(3):
            idx=i*3+j
            x[idx]=x_[j*3+2-i]
            if i in [0, 2] and j in [0, 2]:
                x[idx]=[x[idx][0]]+x[idx][:0:-1]

    for i in range(3):
        i*=3
        if i == 3:
            y[i]=x[i+2][::-1]
        else:
            y[i]=x[i+2][1::-1]+[x[i+2][2]]

def r2(x, y):
    y_=deepcopy(y)
    for i in range(3):
        for j in range(3):
            idy=i*3+j
            y[idy]=y_[(2-j)*3+i]
            if i in [0, 2] and j in [0, 2]:
                y[idy]=[y[idy][0]]+y[idy][:0:-1]

    for i in range(3):
        i*=3
        if i == 3:
            x[i+2]=y[i][::-1]
        else:
            x[i+2]=y[i][1::-1]+[y[i][2]]




init=[[[0, 3, 2], [0, 2], [0, 1, 2], 
       [0, 3], 0, [0, 1], 
       [0, 3, 4], [0, 4], [0, 1, 4]],
      [[1, 0, 2], [1, 2], [1, 5, 2],
       [1, 0], 1, [1, 5],
       [1, 0, 4], [1, 4], [1, 5, 4]]]

curr=deepcopy(init)
r1(curr[0], curr[1])
r2(curr[0], curr[1])

print(curr)
count=1

while curr!= init:
    r1(curr[0], curr[1])
    r2(curr[0], curr[1])
    count+=1
print(count)
