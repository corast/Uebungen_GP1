from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *
from PyQt5.QtGui import *

class UIFenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Uebungen_GP1/Uebung_6/showmap.ui", self)
        self.show()

        self.pushButton.clicked.connect(self.karte)

    def karte(self):
        l = self.lineEdit.text()
        b = self.lineEdit_2.text()
        print(l, b)
        link= f"https://www.google.ch/maps/place/{b},{l}"
        QDesktopServices.openUrl(QUrl(link))

app = QApplication([])
win = UIFenster()
app.exec()