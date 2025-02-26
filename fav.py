# https://dolphywind.github.io/posts/the_silly_solution/
def count_parts(favs, n):
    curr = [1] + [0]*n

    for fav in favs:
        for i in range(fav, n+1):
            curr[i]+=curr[i-fav]

    return curr[-1]
    
for i in range(1, 100):
    print(i, count_parts([4, 5], i))
