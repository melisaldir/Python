class Ogrenci: #veri kalıpları
    AdSoyad = "Tanımsız"
    NotOrtalamasi = ""
    DisiplinCezasi = 0

    def __init__(self,ad,no):
        self.AdSoyad =ad
        self.Numara = no

class ikiKati:
    def __init__(self,a):
        self.sayi = a

        
ogrenci1 = Ogrenci("Büşra", 10)
numara = int("42")
print("Numara:",numara*2)
print("ogrenci1.AdSoyad",ogrenci1.AdSoyad)
ogrenci2 = Ogrenci("Onat", 20)
print("ogrenci2.AdSoyad",ogrenci2.AdSoyad)
print("ogrenci1.AdSoyad",ogrenci1.AdSoyad)
print("ogrenci1.Numara",ogrenci1.Numara)



"""
ogrenci1 = Ogrenci
ogrenci1.AdSoyad = "Büşra"
print(ogrenci1.AdSoyad)
ogrenci2 = Ogrenci
ogrenci2.AdSoyad = "Onat"
print(ogrenci2.AdSoyad)
print(ogrenci1.AdSoyad)
"""