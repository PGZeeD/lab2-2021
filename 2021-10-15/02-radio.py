from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("2021-10-15/02-radio.ui", self)
        self.aceptar.clicked.connect(self.on_aceptar)
    
    def on_aceptar(self):
        mensaje = ""

        if self.opcion1.isChecked():
            mensaje = "opcion 1\n"
        if self.opcion2.isChecked():
            mensaje = "opcion 2\n"
        if self.opcion3.isChecked():
            mensaje = "opcion 3\n"

        if self.opciona.isChecked():
            mensaje = mensaje + "opcion A"
        if self.opcionb.isChecked():
            mensaje = mensaje + "opcion B"
        if self.opcionc.isChecked():
            mensaje = mensaje + "opcion C"
        
        self.mensaje.setText(mensaje)



app = QApplication([])

win = MiVentana()
win.show()

app.exec_()
