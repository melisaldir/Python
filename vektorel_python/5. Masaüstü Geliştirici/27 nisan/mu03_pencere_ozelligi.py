import sys
from PyQt5.QtWidgets import *
app = QApplication(sys.argv)
pencere = QWidget()
pencere.setWindowTitle("deneme")
pencere.resize(300,50)
#pencere.setFixedSize(100,100)

pencere.show()


app.exec()