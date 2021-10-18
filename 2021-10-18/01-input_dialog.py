from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("2021-10-18/01-input_dialog.ui", self)
        self.ingresar.clicked.connect(self.on_ingresar)

    def on_ingresar(self):
        # Texto
        #texto, ok = QInputDialog.getText(self, 'Ingresar', 'Ingrese un texto', text='Texto por defecto')
        #if ok and texto:
            #self.entrada.setText(texto)

        #Enteros
        #entero, ok = QInputDialog.getInt(self, 'Ingresar', 'Ingrese un numero entero', value=5, min=0, max=100, step=2)
        #if ok:
            #self.entrada.setText(str(entero))
        
        #Decimales
        #decimal, ok = QInputDialog.getDouble(self, 'Ingresar', 'Ingrese un decimal', 1.5, 0, 100, 3)
        #if ok:
        #    self.entrada.setText(str(entero))

        #Lista
        items = ['Rojo', 'Verde', 'Azul']
        item, ok = QInputDialog.getItem(self, 'Ingresar', 'Elija un item', items, 1, False)
        if ok:
            self.entrada.setText(item)

app = QApplication([])

win = MiVentana()
win.show()

app.exec_()
