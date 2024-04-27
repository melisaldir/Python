import random
dizi = []
max = 10000
for a in range(max):
    dizi.append(random.randint(1,max))

#for a in range(max):
#    print(a,dizi[a])

print(dizi)

dizi.sort()
print(dizi)