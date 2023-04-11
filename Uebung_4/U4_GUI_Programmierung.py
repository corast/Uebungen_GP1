import sys
from PyQt5.QtWidgets import *

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
        self.button = QPushButton("Save")

        # GUI-Elemente dem Layout hinzufügen
        layout.addRow("Vorname:", self.vorname)
        layout.addRow("Name:", self.name)
        layout.addRow("Geburtstag:", self.geburtstag)
        layout.addRow("Adresse:", self.adresse)
        layout.addRow("Postleitzahl:", self.plz)
        layout.addRow("Ort:", self.ort)
        layout.addRow("Land:", self.land)
        layout.addRow(self.button)

        # Klick auf Button "Save"
        self.button.clicked.connect(self.speichern)

        # Menubar
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        
        save = QAction("Save", self)
        save.triggered.connect(self.speichern)
        
        quit = QAction("Quit", self)
        quit.setMenuRole(QAction.QuitRole)
        quit.triggered.connect(self.close)

        filemenu.addAction(save)
        filemenu.addAction(quit)
     
        # Zentrales Widget erstellen und Layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenster anzeigen
        self.show()


    def speichern(self):
        file = open("output.txt", "w", encoding="utf-8")
        v = self.vorname.text()
        n = self.name.text()
        g = self.geburtstag.text()
        a = self.adresse.text()
        p = self.plz.text()
        o = self.ort.text()
        l = self.land.currentText()
        txt = f"{v}, {n}, {g}, {a}, {p}, {o}, {l}"
        file.write(txt + "\n")
        file.close
    
def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()