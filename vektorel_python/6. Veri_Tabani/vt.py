from PyQt5.QtWidgets import *

def sifreOlustur():
  kullaniciAdi = "adm"
  sifre = "123"
  dosya = open("rhbpwd.txt","w")
  dosya.write(f"{kullaniciAdi} {sifre}")
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
    self.dugme2.clicked.connect(self.listele)

    araclar = QWidget()
    araclar.setLayout(icerik)
    self.setCentralWidget(araclar)

  def ekle(self):
    self.close()
    self.listeleme = VeriListeEkranı('Kayıt Ekleme')
    self.listeleme.show()


  def listele(self):
    self.close()
    self.ekleme = EkleEkrani('Kayıt Ekleme')
    self.ekleme.show()



class loginPenceresi(QMainWindow):
  def __init__(self,xx="Başlıksız"):
    super().__init__()
    self.setWindowTitle(xx)

    icerik = QVBoxLayout()
    icerik.addWidget(QLabel('Kullanıcı adı:'))
    self.edit1 = QLineEdit('Kullanıcı adınız...')
    # self.edit1.width(50)
    icerik.addWidget(self.edit1)
    icerik.addWidget(QLabel('Şifre:'))
    self.edit2 = QLineEdit()
    self.edit2.setEchoMode(QLineEdit.EchoMode.Password)
    icerik.addWidget(self.edit2)
    self.dugme1 = QPushButton('Giriş yap')
    icerik.addWidget(self.dugme1)

    self.dugme1.clicked.connect(self.kontrolEt)

    araclar = QWidget()
    araclar.setLayout(icerik)
    self.setCentralWidget(araclar)

  def kontrolEt(self):
    print("Düğmeye tıklandı..")
    t1 = self.edit1.text()
    t2 = self.edit2.text()
    print("Edit 1 içeriği:", t1)
    print("Edit 2 içeriği:", t2)
    dosya = open("rhbgirilenpwd.txt","w")
    dosya.write(f"{t1} {t2}")
    dosya.close()

    if t1=="q" and t2 == "q" :
      print("Giriş ok")
      self.close()
      self.ap = anaEkran()
      self.ap.show()
    else:
      print("İzin yok")
      dlg = QMessageBox(self)
      dlg.setWindowTitle("Bilgilendirme!")
      dlg.setText("İzin yok")
      dlg.exec()

class EkleEkrani(QMainWindow):
  def __init__(self,xx="Başlıksız"):
    super().__init__()
    self.setWindowTitle(xx)

    icerik = QVBoxLayout()
    icerik.addWidget(QLabel('Ad soyad:'))
    self.edit1 = QLineEdit('')
    # self.edit1.width(50)
    icerik.addWidget(self.edit1)
    icerik.addWidget(QLabel('Numara'))
    self.edit2 = QLineEdit()
    self.edit2.setEchoMode(QLineEdit.EchoMode.Password)
    icerik.addWidget(self.edit2)
    self.dugme1 = QPushButton('Kaydet')
    icerik.addWidget(self.dugme1)

    self.dugme1.clicked.connect(self.kaydet)

    araclar = QWidget()
    araclar.setLayout(icerik)
    self.setCentralWidget(araclar)

  def kaydet(self):
    t1 = self.edit1.text()
    t2 = self.edit2.text()
    print("Edit 1 içeriği:", t1)
    print("Edit 2 içeriği:", t2)
    import sqlite3
    vt = sqlite3.connect('rehber.db')
    svt = vt.cursor()
    svt.execute("CREATE TABLE IF NOT EXISTS isimler(id INTEGER PRIMARY KEY AUTOINCREMENT,ad,nu)")
    svt.execute(f"INSERT INTO isimler(ad,nu) VALUES ('{t1}','{t2}')")
    vt.commit()
    vt.close()

    self.close() # mevcut pencereyi kapa
    self.ae = anaEkran() # anaekran isimli pencere tanımla
    self.ae.show() # anaekran ı göster.

class VeriListeEkranı(QMainWindow):
  def __init__(self,xx="Başlıksız"):
    super().__init__()
    self.setWindowTitle(xx)

    icerik = QVBoxLayout()
    icerik.addWidget(QLabel('Ad soyad:'))
    icerik.addWidget(QLabel('Numara'))

    self.d1= QPushButton("Ana ekrana döön")
    icerik.addWidget(self.d1)
    self.d1.clicked.connect(self.anaEkranaDön)

    araclar = QWidget() 
    araclar.setLayout(icerik)
    self.setCentralWidget(araclar)

    t1 = self.edit1.text()
    t2 = self.edit2.text()
    print("Edit 1 içeriği:", t1)
    print("Edit 2 içeriği:", t2)

    import sqlite3
    vt = sqlite3.connect('rehber.db')
    svt = vt.cursor()
    liste=svt.execute(f"SELECT * FROM isimler")
    vt.commit()
    vt.close()

    self.close() # mevcut pencereyi kapa
    self.ae = anaEkran() # anaekran isimli pencere tanımla
    self.ae.show() # anaekran ı göster.


sifreOlustur()
uygulama = QApplication([])
# pencere = loginPenceresi("Giriş1")
pencere = anaEkran("Giriş1")
pencere.show()
# anaPencere = anaEkran("MENU")
# anaPencere.show()
uygulama.exec() 
# self.edit2.setEchoMode(QLineEdit.EchoMode.Password)
