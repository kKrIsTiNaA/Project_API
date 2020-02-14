from json_poisk import json_poisk_roma
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap


class Map_Find(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('interface.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Show Map')
        json_poisk_roma()
        self.pixmap = QPixmap('map.png')
        self.label.setPixmap(self.pixmap)


app = QApplication(sys.argv)
ex = Map_Find()
ex.show()
sys.exit(app.exec_())
