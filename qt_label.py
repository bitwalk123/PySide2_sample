#!/usr/bin/env python
# coding: utf-8
# reference : https://github.com/andriyantohalim/PySide2_Tutorial

import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle("Label")
        self.show()

    def initUI(self):
        lb = QLabel('<font color=#888 size=40>ラベル</font>', self)
        lb.resize(lb.sizeHint())
        lb.move(50, 20)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
