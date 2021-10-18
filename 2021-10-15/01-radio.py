from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("2021-10-15/01-radio.ui", self)
        #self.aceptar.clicked.connect(self.on_aceptar)
        self.opcion1.toggled.connect(self.on_aceptar)
        self.opcion2.toggled.connect(self.on_aceptar)
        self.opcion3.toggled.connect(self.on_aceptar)

    def on_aceptar(self):
        print("Cambio de opcion")
        if self.opcion1.isChecked():
            self.mensaje.setText("Se elige la opcion 1")
        elif self.opcion2.isChecked():
            self.mensaje.setText("Se elige la opcion 2")
        elif self.opcion3.isChecked():
            self.mensaje.setText("Se elige la opcion 3")
        else:
            self.mensaje.setText("No se eligio opcion")

app = QApplication([])

win = MiVentana()
win.show()

app.exec_()
