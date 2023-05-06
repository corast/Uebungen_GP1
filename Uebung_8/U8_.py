import typing
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Uebungen_GP1\\Uebung_8\\U8_gui.ui",self)

        figure = plt.figure(figsize=(16,9))
        self.canvas = FigureCanvas(figure)
        self.horizontalLayout.removeWidget(self.widget)
        self.horizontalLayout.insertWidget(0,self.canvas)

        self.button.clicked.connect(self.plot)          

        self.show()

    def plot(self):
        try:
            plt.clf()
            f1 = self.Funktion.text()
            f2 = eval(f1)
            f = np.poly1d(f2)
            mini = self.Min.value()
            min = int(mini)
            maxi = self.Max.value()
            max = int(maxi)
            anza = self.Anzahl.value()
            anz = int(anza)
            x = np.linspace(min,max,anz)
            y = f(x)

        except:
            QMessageBox.critical(self, "Fehler", "Bitte korrekt eingeben")
            return
        
        try:
            farbe = self.comboBox.currentText()
            if farbe == "Rot":
                plt.plot(x, y, "ro-")
            elif farbe == "Schwarz":
                plt.plot(x, y, "ko-")
            elif farbe == "Cyan":
                plt.plot(x, y, "co-")
            elif farbe == "Grün":
                plt.plot(x, y, "go-")
            elif farbe == "Blau":
                plt.plot(x, y, "bo-")
            plt.axis("equal")
            self.canvas.draw()
        except:
            QMessageBox.critical(self, "Fehler", "Bitte Eingabe überprüfen ")
        

app = QApplication([])
window = Window()
app.exec()