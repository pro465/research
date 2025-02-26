def calc(rules):
    for i in range(len(rules)):
        rules[i].append([])
        for j in range(i):
            if any(map(lambda x: x[0]>0 and x[1]>0, zip(rules[i][0], rules[j][1]))):
                rules[i][2].append(j)
        rules[i][2] += [*range(i, len(rules))]
    return rules

def isprime(n):
    for i in range(2, n):
        if n%i==0: return False
    return True

def factorize(n):
    res=[]

    for i in filter(isprime, range(2, n+1)):
        c=0
        while n%i==0:
            c+=1
            n//=i
        res.append(c)
        if n==1: break

    return res

# 13/(3*7), (5*7*11)/13, 1/7, 3/11, 7/2, 1/3
prog=[[13, 21], [385, 13], [1, 7], [3, 11], [7, 2], [1, 3]]

for i,fraction in enumerate(prog):
    prog[i]=list(map(factorize, fraction))

num_regs=max(map(lambda x: max(len(x[0]), len(x[1])),prog))

for i in range(len(prog)):
    for j in range(2):
        prog[i][j]+=[0]*(num_regs-len(prog[i][j]))

print(num_regs)

calc(prog)

print(prog)

curr=[1000, 1000]
curr += [0]*(num_regs-len(curr))
ip=0

def next():
    global ip, curr, prog
    next_ip=prog[ip][2]
    for ip in next_ip:
        denom = prog[ip][1]
        if all(map(lambda x: x[0] >= x[1], zip(curr, denom))):
            return True
    return False

while next():
    [num, denom, _] = prog[ip]
    for i in range(num_regs):
        curr[i]+=num[i]-denom[i]

print(curr)
