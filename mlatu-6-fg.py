def f(n, a):
    if a[0]==[]:
        return a[1:]
    return [f(n, a[0])]*n+a[1:]

c=2
a=[[[[]]]]
while a!=[]:
    a=f(c, a)
    c+=1
    if c%1000==0:print(c)

print(c)
