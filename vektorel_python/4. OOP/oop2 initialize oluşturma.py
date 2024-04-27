class Ogrenci:
    ad = "yok"
    no = "bos"
    def __init__ (self,xx,yy):
        self.ad = xx
        self.no = yy

print("Sınıftaki ad değeri:",Ogrenci.ad)

ogrenci1 = Ogrenci("Ahmet Bal",10)
print("ogrenci1 ad değeri:",ogrenci1.ad)

ogrenci2 = Ogrenci("Ertan Öner",20)
print("Sınıftaki ad değeri:",Ogrenci.ad)
print("Sınıftaki ad değeri:",ogrenci1.ad)
print("Sınıftaki ad değeri:",ogrenci2.ad)