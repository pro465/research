def only_bin(x): return x in '01'

rule=list(map(int, filter(only_bin, input())))[3::-1]
init=list(map(int, filter(only_bin, input() or '010')))

def next(prev, curr): return rule[(prev<<1)|curr]

def step(state):
    prev=state[0]
    for (i, curr) in enumerate(state):
        state[i]=next(prev, curr)
        prev=curr
    state.append(next(prev, prev))

for i in range(int(input() or 100)):
    print(*map(lambda x: ' X'[x], init), sep="")
    step(init)
