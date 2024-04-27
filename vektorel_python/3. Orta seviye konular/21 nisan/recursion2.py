sonuc = 0
def selamla(xx):
    global sonuc 
    
    sonuc *= xx
    print("Sayi",xx)

    xx -= 1
    
    if xx > 1 : selamla(xx)

selamla(6)
print("Sonuç:",sonuc)