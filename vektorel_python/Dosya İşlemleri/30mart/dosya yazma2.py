a = 5
b=4
c=a+b
dosya=open("deneme2.xx","w")
dosya.write(str(c))
dosya.close()

okunan=open("deneme2.xx")
aa=okunan.read()
print(aa)
print(aa*2)
print(int(aa)*2)
okunan.close()