# Buton ekleyelim
from PyQt5.QtWidgets import *
aa = QApplication([]) #app
ww = QWidget() #pencere

icerik = QVBoxLayout() #aradaki V vertical için kullanılınır.
# V yerine H yazılarak horizontal yanı yatay konumlandırılır.


icerik.addWidget(QPushButton('Tıkla'))
icerik.addWidget(QPushButton('Dene'))
icerik.addWidget(QLabel('Bilgi'))

ww.setLayout(icerik)

ww.show()
aa.exec()