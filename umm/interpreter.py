import sys

if len(sys.argv) < 2:
    print("please provide a path as an argument")
    exit(-1)

with open(sys.argv[1], 'r') as f:
    instrs = []
    for i,l in enumerate(l for l in f.readlines() if not l.startswith('#') and len(l.strip())!=0):
        curr=list(map(int, l.split()))[:2]
        if len(curr)==2:
            curr[1]+=i
        instrs.append(curr)
    print(instrs)

    ip=0
    regs=[]
    print("enter initial values of registers:")
    while (i := input()).strip() != '': regs.append(int(i))

    while ip < len(instrs):
        curr=instrs[ip]
        idx=curr[0]
        regs += [0]*(idx+1-len(regs))
        
        if len(curr)==1: regs[idx]+=1
        
        elif regs[idx] < 1: ip=curr[1]-1

        else: regs[idx] -= 1
        ip+=1
        print(regs)

    f.close()
