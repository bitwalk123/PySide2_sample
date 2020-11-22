#!/usr/bin/env python
# coding: utf-8
import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel


class Example(QWidget):

    def initUI(self):
        lb = QLabel("ラベル", self)
        lb.resize(lb.sizeHint())
        lb.move(50, 20)

        self.setWindowTitle("Label")
        self.show()

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
