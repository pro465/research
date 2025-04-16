def cost(c, n):
    return sum(i*x*(1-x)**(n-1) for i,x in c)

def find(c, n, p, r=1., so_far=[]):
    if len(c)<=1: return (cost(so_far+[(c[0], r)], n), so_far+[(c[0], r)])
    (best_cost,best_sol)=(-1., [])
    for a in range(p):
        x=a/p*r
        (cst, sol)=find(c[1:], n, p, r-x, so_far+[(c[0], x)])
        if cst>best_cost:
            (best_cost, best_sol)=(cst, sol)
        print(a)
    return (best_cost, best_sol)

print(find([1,3,5], 3, 100))
