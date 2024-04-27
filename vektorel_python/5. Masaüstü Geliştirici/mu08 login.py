from PyQt5.QtWidgets import *

class loginPenceresi(QMainWindow):
    def __init__(self,xx="Başlıksız"):
        super().__init__()
        self.setWindowTitle(xx)

        icerik = QVBoxLayout()
        icerik.addWidget(QLabel('Kullanıcı adı:'))
        edit1= QLineEdit('Kullanıcı adınız...')
        icerik.addWidget(edit1)
        icerik.addWidget(QLabel('Şifre:'))
        edit2= QLineEdit()
        icerik.addWidget(edit2)
        dugme1 = QPushButton('Giriş yap')
        icerik.addWidget(dugme1)

        dugme1.clicked.connect(self.kontrolEt)
    

        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)
    
    def kontrolEt(self):
        print("Düğmeye tıklandı..")

        
uygulama = QApplication([])
pencere = loginPenceresi("Giriş")
pencere.show()
uygulama.exec()