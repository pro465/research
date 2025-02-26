l="IfyVcAyOOCP]7A8eB]Z42KA6TyNjTOhpIFrDjLRQv]]jthYorrF4W5vPoUYsW9WFRGSCfhEFA04KZGnb]moddD93IEpuXFLAJH02Xn4CgpNrwuYnjEXo)Mj6jG3gI)PmJc0x8W55]5H9OSqxcEDPx1o5!"
l2="eL01ydXXWAXZagjYglxeAmH)5Rv8zM9Q8kJVFYysG7n1LHY2sKvKf7kZFrRERVVNhLbDjGx3uJpDQCpmiLq3J]fS6BCEUDjMZ)3DRF4xzjOCZx)JiET8y94KI8Zz8)0SMyHVG7LC3bXnz8na2zNIJbWjDTDW]pr2adVtHA7aOQ!"
l3="".join([chr(ord(x)-5) for x in l2])
print(l3)
freq={}

def add(k):
    freq.setdefault(k, 0)
    freq[k]+=1

for i in range(0, len(l)-1):
    add(l[i])
print(sorted(freq.items(), key=lambda x: x[1]))
for i in range(0, len(l)-1):
    add(l2[i])

print(sorted(freq.items(), key=lambda x: x[1]))
