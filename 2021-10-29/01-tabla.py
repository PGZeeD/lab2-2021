from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("2021-10-29/01-tabla.ui", self)

        # Crear las columnas
        self.tabla.setColumnCount(3)

        # Nombrar las columnas
        self.tabla.setHorizontalHeaderLabels(('Nombre', 'Apellido', 'e-mail'))

        self.filas = 0
        self.agregar.clicked.connect(self.on_agregar)

    def on_agregar(self):
        # Agregar fila en blanco
        fila = self.filas
        self.tabla.insertRow(fila)

        # Agregar items de la fila
        nombre = self.nombre.text()
        self.tabla.setItem(fila, 0, QTableWidgetItem(nombre))

        apellido = self.apellido.text()
        self.tabla.setItem(fila, 1, QTableWidgetItem(apellido))

        email = self.email.text()
        self.tabla.setItem(fila, 2, QTableWidgetItem(email))

        self.filas = self.filas + 1


app = QApplication([])

win = MiVentana()
win.show()

app.exec_()

