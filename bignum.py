def max_reg(p):
    if type(p) is int: return p
    if len(p)==4 and type(p[3]) is bool: return 0
    return max(map(max_reg, p))

def score(s):
    return sum(s[i][2]/2**i for i in range(min(len(s), 60)))

def run(p,l):
    stack=[[p, 0, 0, False]]
    regs=[0]*(l+1)
    while len(stack)>0:
        el=stack.pop()
        [p, i, j] = el[:2]+[regs[el[2]]] if el[3] else el[:3]

        if j>0:
            stack+=[[p, i, j-1, False]]*regs[i]
            continue
        temp=[]
        for i in p:
            if type(i) is int: regs[i]+=1
            else: temp.append(i)
        stack+=temp[::-1]
    return regs

def parse_int(s,i):
    init=i
    while i < len(s) and s[i] in "0123456789":i+=1
    return int(s[init:i]),i

def parse(p):
    res=[]
    i=0
    while i<len(p):
        if p[i]=="+":
            r,i=parse_int(p, i+1)
            res.append(r)
        elif p[i]=="(":
            m,i=parse_int(p, i+1)
            assert p[i]=='|'
            i+=1
            n,i=parse_int(p, i)
            assert p[i]=='|'
            i+=1
            c=1
            for j,ch in enumerate(p[i:]):
                if ch in "()": c+=2*int(ch=='(') - 1
                if c==0: break
            r=parse(p[i:i+j])
            i+=j+1
            res.append([r, m, n, True])
        else: 
            i+=1
    return res

p="""
+0+0+0+0
+1+1+1+1
(1|1|+0(0|0|+0+0))
"""
p=parse(p)
print(run(p, max_reg(p)))
