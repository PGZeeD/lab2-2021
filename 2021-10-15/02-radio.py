from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("2021-10-15/02-radio.ui", self)

app = QApplication([])

win = MiVentana()
win.show()

app.exec_()
