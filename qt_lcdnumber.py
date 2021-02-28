#!/usr/bin/env python
# coding: utf-8
# reference : https://github.com/andriyantohalim/PySide2_Tutorial

import sys
from PySide2.QtWidgets import QLCDNumber, QSlider, QVBoxLayout, QWidget, QApplication, QMainWindow
from PySide2 import QtCore


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('LCDNumber')
        self.show()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(QtCore.Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
