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

        vorname = QLineEdit()
        name = QLineEdit()
        geburtstag = QDateEdit()
        adresse = QLineEdit()
        plz = QLineEdit()
        ort = QLineEdit()
        land = QComboBox()
        land.addItems(["Schweiz", "Deutschland", "Österreich"])
        button = QPushButton("Save")

        # GUI-Elemente dem Layout hinzufügen
        layout.addRow("Vorname", vorname)
        layout.addRow("Name", name)
        layout.addRow("Geburtstag", geburtstag)
        layout.addRow("Adresse", adresse)
        layout.addRow("PLZ", plz)
        layout.addRow("Ort", ort)
        layout.addRow("Land", land)
        layout.addRow(button)

        # Klick auf Button "Save"
        button.clicked.connect(self.speichern)

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

        text = f"({vorname}, {name}, {geburtstag}, {adresse}, {plz}, {ort}, {land})"


    def speichern(self):
        file = open("output.txt", "a")
        #text = f"({vorname}, {name}, {geburtstag}, {adresse}, {plz}, {ort}, {land})"
        file.write("Test")
        file.close
    
def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()