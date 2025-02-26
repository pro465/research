import sys

if len(sys.argv) < 2:
    print("please provide a path as an argument")
    exit(-1)

def encode(n, m):
    bits=[]
    n<<=1

    while m > 0:
        bits.append(m&1)
        m >>= 1

    for i in bits[::-1]:
        n=(n<<2) | (i<<1) | 1

    return n


with open(sys.argv[1], 'r') as f:
    instrs = []
    for i,l in enumerate(l for l in f.readlines() if not l.startswith('#') and len(l.strip())!=0):
        curr=list(map(int, l.split()))[:2]
        if len(curr)==2:
            curr[1]+=i
        instrs.append(curr)
    print(instrs)

    addrs = [0]
    prev = 0

    for i in range():
        pass

    f.close()
