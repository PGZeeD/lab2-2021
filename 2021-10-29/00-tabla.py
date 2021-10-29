from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("2021-10-29/00-tabla.ui", self)

        # Crear las columnas
        self.tabla.setColumnCount(3)

        # Nombrar las columnas
        self.tabla.setHorizontalHeaderLabels(('Nombre', 'Apellido', 'e-mail'))


        # Agregar fila en blanco
        self.tabla.insertRow(0)

        # Agregar items de la fila
        self.tabla.setItem(0, 0, QTableWidgetItem("Pepe"))
        self.tabla.setItem(0, 1, QTableWidgetItem("Sanchez"))
        self.tabla.setItem(0, 2, QTableWidgetItem("ps@mail.com"))


app = QApplication([])

win = MiVentana()
win.show()

app.exec_()

