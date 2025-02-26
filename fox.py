from random import randrange

def gen():
    res=[]
    rem=[5,5,6]
    n=3
    for i in range(4):
        arr=[]
        for j in range(4):
            c=randrange(n)
            while rem[c]==0: c+=1
            arr.append(c)
            rem[c]-=1
            if rem[c]==0:
                n-=1
        res.append(arr)
    return res

def test_dir(a, i, j, di, dj):
    l=[]
    while i<len(a) and j < len(a) and len(l) < 3:
        l.append(a[i][j])
        i+=di
        j+=dj
    return l in ([0, 1, 2], [2, 1, 0])

def test(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if test_dir(a, i, j, 0, 1) or test_dir(a, i, j, 1, 0) or test_dir(a, i, j, 1, 1):
                return False
    return True

def nums():
    a=gen()
    n=1
    while not test(a):
        a=gen()
        n+=1
    return n


a=[nums() for i in range(1000)]

print(a, sum(a)/1000)
