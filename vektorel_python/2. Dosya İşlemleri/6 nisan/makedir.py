import os
aktifDizin = os.getcwd()
print("Çalışan dizin: ",aktifDizin)

os.chdir("D:\\")
os.mkdir("Rehber")

f = open("D:\\Rehber\deneme2.xx", "w")
f.write("vektörel")
f.close