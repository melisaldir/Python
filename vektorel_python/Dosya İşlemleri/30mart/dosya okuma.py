#not1 = 5
#with open("deneme.txt","a") as xx:
#   xx.write(f"Puan:{not1})

try:
    okunan = open("deneme1.xx","r")
    print(okunan.read())
    okunan.close
except:
    print("Bir hata oluştu.")