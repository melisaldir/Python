class Ogrenci:
    AdSoyad ="Tanımsız"
    NotOrtalamasi = ""
    DisiplinCezasi = 0

    def __init__ (self,ad,no):
        self.AdSoyad = ad
        self.Numara =no
        print(f"Nesne {ad},{no} değerleriyle başarıyla oluşturuldu.")

    def Bilgi(self):
        print("Bilgi: Metod ile Adı Soyadı:",self.AdSoyad,",Numarası:")


print("Sınıftaki adSoyad değeri:",Ogrenci.AdSoyad)

ogrenci1 = Ogrenci("Ahmet BAL",20)
