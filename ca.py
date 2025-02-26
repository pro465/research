# 9/12/2024
import random
def next(rule, so_far, k):
    idx=so_far[-1]
    for i in range(1, k):
        idx|=so_far[len(so_far)//(i+1)]<<i
    return (rule>>idx)&1

k=5
it=0
num_it=100000
# [(23, 48813), (29, 50060), (45, 47112), (53, 49993), (71, 49976), (77, 48901), (83, 49979), (85, 50000), (89, 50007), (101, 50207), (105, 50544), (113, 47406), (147, 47435), (149, 50047), (165, 48517), (197, 48566), (209, 50597)]
rules=[random.randint(0, 2**(2**k)-1)]
so_far=[[random.randint(0, 1) for j in range(k)] for i in rules]
nums=[0]*len(rules)
tol=0.05
with open("random.bin", "w") as f:
    for it in range(num_it):
        i=0
        while i<len(rules):
            rule=rules[i]
            curr=next(rule, so_far[i], k)
            f.write(str(curr))
            so_far[i].append(curr)
            nums[i]+=curr
            # if it > 10000 and not (-tol<nums[i]/it-0.5<tol):
            #     rules=rules[:i]+rules[i+1:]
            #     so_far=so_far[:i]+so_far[i+1:]
            #     nums=nums[:i]+nums[i+1:]
            #     continue
            i+=1

print([(rules[i], x) for i,x in enumerate(nums)])

