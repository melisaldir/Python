from PyQt5.QtWidgets import *

def sifreOlustur():
    dosya = open("rehberpwd.xx","w")
    dosya.write("adm 123")
    dosya.close()
     
class loginPenceresi(QMainWindow):
    def __init__(self,xx="Başlıksız"):
        super().__init__()
        self.setWindowTitle(xx)

        icerik = QVBoxLayout()
        icerik.addWidget(QLabel('Kullanıcı adı:'))
        self.edit1= QLineEdit()
        #self.edit1.width(50)
        icerik.addWidget(self.edit1)
        icerik.addWidget(QLabel('Şifre:'))
        self.edit2= QLineEdit()
        icerik.addWidget(self.edit2)
        self.dugme1 = QPushButton('Giriş yap')
        icerik.addWidget(self.dugme1)

        self.dugme1.clicked.connect(self.kontrolEt)
    
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)
    
    def kontrolEt(self):
        print("Düğmeye tıklandı")
        t1=self.edit1.text()
        t2=self.edit2.text()
        print("Edit 1 içeriği:", t1)
        print("Edit 2 içeriği:", t2)
        dosya = open("rehbergrlnpwd.xx","w")
        dosya.write(f"{t1} {t2}")
        dosya.close()

        if t1=="adm" and t2 == "11":
            print("giriş ok")

        else:
            print("İzin yok")
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Bilgilendirme!")
            dlg.setText("İzin yok")
            dlg.exec()

sifreOlustur( )
uygulama = QApplication([])
pencere = loginPenceresi("Giriş")
pencere.show()
uygulama.exec()