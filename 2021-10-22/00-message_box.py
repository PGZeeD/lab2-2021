from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("2021-10-22/00-message_box.ui", self)
        self.mensaje.clicked.connect(self.on_mensaje)

    def on_mensaje(self):
        msg = QMessageBox()

        # Titulo y mensaje
        msg.setWindowTitle('Titulo del mensaje')
        msg.setText('Mensaje a mostrar')

        # Iconos
        #msg.setIcon(QMessageBox.Information)
        #msg.setIcon(QMessageBox.Question)
        #msg.setIcon(QMessageBox.Warning)
        msg.setIcon(QMessageBox.Critical)

        # Botones
        #msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel | QMessageBox.Ok | QMessageBox.Open | QMessageBox.Close | QMessageBox.Save | QMessageBox.SaveAll | QMessageBox.Abort | QMessageBox.Retry | QMessageBox.Ignore)
        msg.setStandardButtons(QMessageBox.No | QMessageBox.Yes | QMessageBox.Cancel) 

        # Ejecuto
        resultado = msg.exec_()
        if resultado == QMessageBox.Yes:
            print('el usuario eligio Si')
        if resultado == QMessageBox.No:
            print('el usuario eligio No')
        if resultado == QMessageBox.Cancel:
            print('el usuario eligio Cancelar')

app = QApplication([])

win = MiVentana()
win.show()

app.exec_()
