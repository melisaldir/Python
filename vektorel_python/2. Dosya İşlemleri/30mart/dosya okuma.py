okunan = open("deneme1.xx","r")
print(okunan.read(5)) #read(5) ile 5 karakter okunur
print(okunan.readline()) #readline ile satır okunur
try:
    okunan = open("deneme1.xx","r")
    print(okunan.read())
    okunan.close
except:
    print("Bir hata oluştu.")