def parse_ident(prog):
    res,i="",0
    while i<len(prog) and prog[i].isalnum():
        res+=prog[i]
        i+=1
    return res,i

def parse(prog):
    i=0
    while prog[i] not in "\\`" and not prog[i].isalpha(): i+=1
    if prog[i]=="`":
        res1,i_=parse(prog[i+1:])
        res2,j_=parse(prog[i+i_+1:])
        return ((res1,res2),i+i_+j_+1)
    elif prog[i]=='\\':
        res1,i_=parse_ident(prog[i+1:])
        res2,j_=parse(prog[i+i_+1:])
        return ([res1,res2],i+i_+j_+1)
    res,i_=parse_ident(prog[i:])
    return res,i+i_

def trans(prog,v=[]):
    l="abcdefghijklmnopqrstuvwxyz0123456789"
    if type(prog) is list:
        return [trans(prog[1], v+[prog[0]])]
    if type(prog) is tuple:
        return (trans(prog[0],v),trans(prog[1],v))
    for i in range(len(v)):
        if v[len(v)-1-i]==prog:
            return (i+1)*"1"+"0"

i=0
def print_prog(p):
    global i
    if type(p) is list:
        i=(i+1)%80
        return "00"+print_prog(p[0])
    elif type(p) == tuple:
        i=(i+1)%80
        return "01"+print_prog(p[0])+print_prog(p[1])
    else:
        i=(i+1)%80
        return p

a=input("input file: ")
b=input("output file: ")

with open(a, "r") as f:
    with open(b, "wb") as f2:
        f2.write(bytes(print_prog(trans(parse(f.read())[0])), encoding="utf8"))
