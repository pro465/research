def count(n, nums):
    if n==0: return 1
    if len(nums)==0: return 0
    return sum(map(
                 lambda x: count(n-x, nums[1:]), 
                 range(min(n, nums[0])+1)
            ))

print(count(1, [5]*3))
