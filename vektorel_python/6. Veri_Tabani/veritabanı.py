from PyQt5.QtWidgets import *

def sifreOlustur():
    dosya = open("rehberpwd.xx","w")
    dosya.write("adm 123")
    dosya.close()
     
class anaEkran(QMainWindow):
    def __init__(self,xx="Başlıksız"):
        super().__init__()
        self.setWindowTitle(xx)

        icerik = QVBoxLayout()
        self.dugme1 = QPushButton('Ekle')
        icerik.addWidget(self.dugme1)
        self.dugme2 = QPushButton('Listele')
        icerik.addWidget(self.dugme2)
        self.dugme3 = QPushButton('Sil')
        icerik.addWidget(self.dugme3)

        self.dugme1.clicked.connect(self.ekle)
    
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)
    
    def ekle(self):
        print("Ekleme tıklandı")
        import sqlite3

        xxx1 = sqlite3.connect("rehber.db")
        xxx2 = sqlite3.connect("rehber1.db")
        cvt = xxx1.cursor()
        cvt.execute("INSERT INTO  deneme1  (id,adi,soyadi,telefonu)")
        xxx1.commit()
        xxx1.close()


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
        self.edit2.setEchoMode(QLineEdit.EchoMode.Password)
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

        if t1=="q" and t2 == "q":
            print("giriş ok")
            self.close()
        else:
            print("İzin yok")
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Bilgilendirme!")
            dlg.setText("İzin yok")
            dlg.exec()

sifreOlustur( )
uygulama = QApplication([])
pencere = loginPenceresi("Giriş")
anapencere = anaEkran("MENU")
pencere.show()
anapencere.show()
uygulama.exec()