import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Fenster-Titel definieren:
        self.setWindowTitle("GUI-Programmierung")

        # Layout erstellen:
        layout = QFormLayout()
        
        # GUI-Elemnente erstellen 

        self.vorname = QLineEdit()
        self.name = QLineEdit()
        self.geburtstag = QDateEdit()
        self.adresse = QLineEdit()
        self.plz = QLineEdit()
        self.ort = QLineEdit()
        self.land = QComboBox()
        self.land.addItems(["Schweiz", "Deutschland", "Österreich"])
        self.button1 = QPushButton("Speichern")
        self.button2 = QPushButton("Laden")
        self.button3 = QPushButton("Auf Karte anzeigen")

        # GUI-Elemente dem Layout hinzufügen
        layout.addRow("Vorname:", self.vorname)
        layout.addRow("Name:", self.name)
        layout.addRow("Geburtstag:", self.geburtstag)
        layout.addRow("Adresse:", self.adresse)
        layout.addRow("Postleitzahl:", self.plz)
        layout.addRow("Ort:", self.ort)
        layout.addRow("Land:", self.land)
        layout.addRow(self.button3)
        layout.addRow(self.button2)
        layout.addRow(self.button1)
        
        # Klick auf Buttons
        self.button1.clicked.connect(self.speichern)
        self.button2.clicked.connect(self.laden)
        self.button3.clicked.connect(self.karte)

        # Menubar
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        viewmenu = menubar.addMenu("View")
        
        save = QAction("Save", self)
        save.triggered.connect(self.speichern)
        
        quit = QAction("Quit", self)
        quit.setMenuRole(QAction.QuitRole)
        quit.triggered.connect(self.close)

        load = QAction("Laden", self)
        load.triggered.connect(self.laden)

        view = QAction("Karte", self)
        view.triggered.connect(self.karte)

        filemenu.addAction(save)
        filemenu.addAction(quit)
        filemenu.addAction(load)
        viewmenu.addAction(view)
     
        # Zentrales Widget erstellen und Layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenster anzeigen
        self.show()


    def speichern(self):
        filename, filter = QFileDialog.getSaveFileName(self, "Datei speichern ...","", "Text Datei (*.txt)" ) 
        v = self.vorname.text()
        n = self.name.text()
        g = self.geburtstag.text()
        a = self.adresse.text()
        p = self.plz.text()
        o = self.ort.text()
        l = self.land.currentText()
        txt = f"{v}, {n}, {g}, {a}, {p}, {o}, {l}"

        if filename != "":
            file = open(filename, "w", encoding="utf-8")
            file.write(txt + "\n")
            file.close
        else: 
            QMessageBox.information(self, "Kein Dateiname", "Bitte gib einen Dateinamen an!")

    def laden(self):
        filename, filter = QFileDialog.getOpenFileName(self, "Datei öffnen", "", "Test Files (*.txt)")

    def karte(self):
        adress = self.adresse.text()
        a = adress.replace(" ","+")
        plz = self.plz.text()
        o = self.ort.text()
        l = self.land.currentText()
        link= f"https://www.google.ch/maps/place/{a}+{plz}+{o}+{l}"
        QDesktopServices.openUrl(QUrl(link))         
    
def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()