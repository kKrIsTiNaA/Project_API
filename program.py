from json_poisk import json_poisk_roma
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore


class Map_Find(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('interface.ui', self)
        self.spn = 0.005
        self.coord = [0, 0]
        self.metka = False
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Show Map')
        self.type = ['map', 'sat', 'sat,skl']
        json_poisk_roma(self.spn, self.coord, 'map')
        self.pixmap = QPixmap('map.png')
        self.label.setPixmap(self.pixmap)
        self.label.setFocus()
        self.zapros = 'Москва, ул. Ак. Королева, 12'

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_PageUp:
            self.spn += 0.01
        if event.key() == QtCore.Qt.Key_PageDown:
            self.spn -= 0.01
        if event.key() == QtCore.Qt.Key_Up:
            self.coord[1] += 0.002
        if event.key() == QtCore.Qt.Key_Down:
            self.coord[1] -= 0.002
        if event.key() == QtCore.Qt.Key_Right:
            self.coord[0] += 0.002
        if event.key() == QtCore.Qt.Key_Left:
            self.coord[0] -= 0.002
        if self.spn >= 1:
            self.spn = 1
        if self.spn <= 0.005:
            self.spn = 0.005
        if self.coord[0] > 0.02:
            self.coord[0] = 0.02
        if self.coord[0] < -0.02:
            self.coord[0] = -0.02
        if self.coord[1] > 0.02:
            self.coord[1] = 0.02
        if self.coord[1] < -0.02:
            self.coord[1] = -0.02
        json_poisk_roma(self.spn, self.coord, 'map', self.zapros, self.metka)
        self.pixmap = QPixmap('map.png')
        self.label.setPixmap(self.pixmap)
        self.update()


app = QApplication(sys.argv)
ex = Map_Find()
ex.show()
sys.exit(app.exec_())
