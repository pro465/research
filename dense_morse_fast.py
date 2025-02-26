def cost(cost_map: [(int, int)], n: int) -> float:
    costs=[0]*(n+1)
    for i in range(1, n+1):
        costs[i]=min(map(lambda c: costs[i-c[0]]+c[1], filter(lambda c: c[0] <= i, cost_map)), default=10000000)

    return sum(costs)/n

def find(c, n):
    c.sort()
    sol=[1]
    for i in c[1:]: 
        sol+=[min(range(1, n+1), key=lambda j: cost(list(zip(sol, c))+[(j, i)], n))]

    return sol

c=[2, 3, 4, 5, 6]
n=40
sol=find(c, n)

print("n=", n)
print(c)
print(sol)
print(cost(list(zip(sol, c)), n))
