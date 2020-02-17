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
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Show Map')
        json_poisk_roma(delta=self.spn)
        self.pixmap = QPixmap('map.png')
        self.label.setPixmap(self.pixmap)

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
        if self.spn >= 0.5:
            self.spn = 0.5
        if self.spn <= 0.005:
            self.spn = 0.005
        json_poisk_roma(self.spn, self.coord)
        self.pixmap = QPixmap('map.png')
        self.label.setPixmap(self.pixmap)
        self.update()


app = QApplication(sys.argv)
ex = Map_Find()
ex.show()
sys.exit(app.exec_())