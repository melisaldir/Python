ogrenciler=["Melisa","Ece","Defne","Duru","Ceylin"]
dosya=open("deneme2.xx","w")
dosya.write(str(ogrenciler))
dosya.close()

okunan=open("deneme2.xx")
aa=okunan.read()
print(aa)
print(aa*2)
okunan.close()