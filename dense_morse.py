def cost(cost_map: [(int, int)], n: int) -> float:
    costs=[0]*(n+1)
    for i in range(1, n+1):
        costs[i]=min(map(lambda c: costs[i-c[0]]+c[1], filter(lambda c: c[0] <= i, cost_map)), default=10000000)

    return costs

def inc(c, n):
    for i in range(len(c)-1,-1,-1):
        if c[i] < n:
            c[i]+=1
            return True
        c[i]=1
    return False

def find(c, n):
    min_setting=[1]*len(c)
    min_cost=sum(cost(list(zip(min_setting, c)), n))
    curr=min_setting.copy()
    while inc(curr, n):
        c_cost=sum(cost(list(zip(curr, c)), n))
        if c_cost < min_cost:
            min_cost=c_cost
            min_setting=curr.copy()

    return min_setting

c=[2, 3, 4, 5, 6]
n=2
sol=find(c, n)

print(sol)
print(cost(list(zip(sol, c)), n))
