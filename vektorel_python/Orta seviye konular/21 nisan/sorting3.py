import random
dizi = []
kullanilanlar = []
max = 10000
for a in range(max):
    deger = random.randint(1,max*10)

    if not deger in kullanilanlar:
        kullanilanlar.append(deger)
        dizi.append(deger)
    else:
        print("Var")

#for a in range(max):
#    print(a,dizi[a])

print(dizi)

dizi.sort()
print(dizi)