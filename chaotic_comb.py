def decide(log,num_args):
   # return True
    for i in range(len(log)):
        m=len(log[i])-num_args-1
        for j in log[i+1:]:
            d=len(j)-len(log[i])
            if d>=0 and log[i][m:]==j[m+d:]:
                return False
            m=min(len(j)-num_args-1,m)
    return True

def decode(n,num_args):
    a=[]
    b=[]
    while n:
        a.append(n%num_args)
        n//=num_args
        b.append(n%num_args)
        n//=num_args
    while a and a.pop()==0:pass
    while b and b.pop()==0:pass
    return a,b

def run(p,num_args):
    log=[]
    if all(len(x)<=num_args for x in p): return
    curr=[0,1]*(num_args+1//2)+[0]
    i=0
    while len(curr)>num_args and i<100:
        log.append("".join(str(x) for x in curr))
        instr=curr.pop()
        args=[curr.pop() for _ in range(num_args)]
        curr+=[args[x] for x in p[instr]]
        i+=1
    if i >= 100 and decide(log,num_args):
        print(*(l for l in log),sep="\n")
        print(p)
        input()

num_args=3
for i in range(2**25):
    run(decode(i,num_args),num_args)

