from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("2021-10-22/01-combo_box.ui", self)
        self.combo.currentIndexChanged.connect(self.on_cambio)

    def on_cambio(self, index):
        indice = self.combo.currentIndex()
        self.etiqueta.setText(str(indice) + ' - ' + self.combo.currentText())

        # Agregar un item
        # self.combo.addItem('item')

        # Editar un item
        # self.combo.setItemText(indice, 'nuevo nombre')

        # Quitar un item
        # self.combo.removeItem(indice)

        # Quitar todo los items
        # self.combo.clear()

app = QApplication([])

win = MiVentana()
win.show()

app.exec_()

