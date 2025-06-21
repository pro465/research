"""
1RB0RA
0LC0LD
1RA1LB
---1LE
1LE1LF
1LC0LC
"""

A=ord("A")
def parse(c):
    res=[]
    for i in c.split("_"):
        s=[]
        for j in range(0,len(i),3):
            if i[j]=="-": 
                s.append([-1]*3)
                continue
            a=int(i[j])
            b=[-1,1][i[j+1]=="R"]
            c=ord(i[j+2])-A
            s.append([a,b,c])
        res.append(s)
    return res

tm=parse("1RB0RA_0LC0LD_1RA1LB_---1LE_1LE1LF_1LC0LC")

print(tm)
state=0
mem=[0]
ptr=0
c=100
while c>0:
    print("".join(str(i) for i in mem))
    print(" "*ptr+"^")
    print(" "*ptr+chr(A+state))
    c-=1
    if c==0:c=int(input())

    (mem[ptr],d,state)=tm[state][mem[ptr]]
    if state==-1: break
    ptr+=d
    if ptr < 0:
        mem=[0]*(-ptr)+mem
        ptr=0
    if ptr >= len(mem): mem+=[0]*(ptr-len(mem)+1)

