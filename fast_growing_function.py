def condense(rlel):
  i = 1
  while i < len(rlel):
    x,y = rlel[i-1], rlel[i]
    if x[0] == y[0]:
      rlel[i-1:i+1] = [(x[0], x[1]+y[1])]
    else:
      i += 1

def f(a, n):
  while len(a):
    (x,y) = a[0]
    while x==1 and y>0: 
        a+=[(x-1,i) for (x,i) in a if x>1 and i>0] * n
        n+=1
        y-=1
        a[0]=(x,y)
    while len(a) and a[0][1]==0: a=a[1:]
    if len(a)==0: break
    (x,y) = a[0]
    if x <= 1:
      if y <= 1:
        a[:1] = []
      else:
        a[0] = (x,y-1)
    else:
      if y <= 1:
        a[0] = (x-1, 1)
      else:
        a[:1] = [(x-1,1), (x, y-1)]
    condense(a)
    n+=1
  return n

r = []
for i in range(5):
    r.append(f([(5,1)], i))
print(r)

