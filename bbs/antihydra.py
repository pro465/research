"""
1RB1RA
0LC1LE
1LD1LC
1LA0LB
1LF1RE
---0RA
"""
"""
# see antihydra.txt
tm=[[(1,1,1),(1,1,0)],
    [(0,-1,2),(1,-1,4)],
    [(1,-1,3),(1,-1,2)],
    [(1,-1,0),(0,-1,1)],
    [(1,-1,5),(1,1,4)],
    [(0,-1,2),(0,1,0)],
      ]
state=0
mem=[0]
ptr=0

for _ in range(1000):
    (mem[ptr],d,state)=tm[state][mem[ptr]]
    ptr+=d
    if ptr < 0:
        mem=[0]*(-ptr)+mem
        ptr=0
    if ptr >= len(mem): mem+=[0]*(ptr-len(mem)+1)
    if state==1:
        print("".join(str(i) for i in mem))
        print(" "*ptr+"^")
"""

n=6
c=0
while ~c and c<100:
    c+=(n&1)*-3+2
    n+=n>>1
    print(n)
