class Ilan:
    ilanNo ="tanımsız"
    aciklama = "tanımsız"

    def __init__ (self,no):
        self.ilanNo = no

class Araba(Ilan):
    def __init__ (self,no):
        self.ilanNo = no

print(Ilan.ilanNo)
ilan1
print(ilan1.ilanNo)
print(ilan2.ilanNo)
