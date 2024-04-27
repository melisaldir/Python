ad=input("Kaydedilecek kişi adı:")
no=input("Kaydedilecek kişi numarası:")
ogrenci={
    "Adi" : ad,
    "Numarasi" : no
}

dosya=open("dosyalar/rehber.xx","a")
dosya.write(f'{str({"adi":ad,"num":no})}')
dosya.close()

okunan=open("dosyalar/rehber.xx")
bb=okunan.readline()
aa=bb
for a in aa:
    print(a)
okunan.close()
