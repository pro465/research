def div(a, b):
    while len(a)>0:
        q=a[0]/b[0]
        yield q
        left=[]
        for i in range(1, len(b)):
            if i>=len(a):
                left.append(-b[i]*q)
                continue
            left.append(a[i]-b[i]*q)
        if len(b)<len(a):
            left+=a[len(a)-len(b):]

        a=left
    return

a=[1]
b=[-1, 1]

for i in div(a, b):
    print(i)
