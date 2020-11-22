#!/usr/bin/env python
# coding: utf-8

import sys
from PySide2 import QtCore
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class Hello(QWidget):

    def initUI(self):
        label = QLabel('こんにちは、世界！')
        font = QFont()
        font.setPointSize(24)
        label.setFont(font)
        label.setAlignment(QtCore.Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
        self.setWindowTitle('Hello World!')
        self.show()

    def __init__(self):
        super(Hello, self).__init__()
        self.initUI()


def main():
    app = QApplication(sys.argv)
    ex = Hello()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
