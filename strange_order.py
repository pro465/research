k=100
one=2**(k-1)
two=2**k

def turn_into_int(arr):
    global k,one
    sum=one
    for i in arr:
        sum-=one//((i+1)*(i+2)) if (i+1)*(i+2) < one else 0
    return sum

def next_valid(n, already_chosen):
    n+=1
    #print(n)
    while n in already_chosen: n+=1
    return n

def prev_valid(n, already_chosen):
    n-=1
    #print(n)
    while n in already_chosen: n-=1
    return n


def f(already_removed):
    global one,two
    n=turn_into_int(already_removed)
    chosen=one*one//n
    #print(chosen/one)
    closest_lt,closest_gt=chosen//one,chosen//one+1
    while True:
        flag=False
        #print(closest, next_)
        if closest_lt in already_removed:
            flag=True
            closest_lt=prev_valid(closest_lt, already_chosen)
        if closest_gt in already_removed:
            flag=True
            closest_gt=next_valid(closest_gt, already_chosen)
        if not flag: break

    if abs(closest_gt*one-chosen)<abs(closest_lt*one-chosen) or closest_lt<0:
        return closest_gt
    return closest_lt

times=59000
already_chosen=[]
for t in range(times):
    chosen=f(already_chosen)
    print(t+1, chosen)
    already_chosen.append(chosen)
