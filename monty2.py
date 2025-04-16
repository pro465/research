from random import randint
won_switch=0
won_noswitch=0
for i in range(100):
    choice=randint(0, 2)
    assert choice < 3
    others=[j for j in range(3) if choice!=j]
    if others[1]==2: 
        won_noswitch+=choice==0
    else:
        won_switch+=1
print(won_switch, won_noswitch)
