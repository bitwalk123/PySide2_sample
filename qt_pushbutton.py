#!/usr/bin/env python
# coding: utf-8
# reference : https://github.com/andriyantohalim/PySide2_Tutorial

import sys
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QWidget, QPushButton


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton("プッシュボタン", self)
        btn.clicked.connect(self.buttonClicked)
        btn.resize(btn.sizeHint())
        btn.move(50, 20)

        self.setWindowTitle("PushButton")
        self.show()

    @Slot()
    def buttonClicked(self):
        sender = self.sender()
        print('「' + sender.text() + '」がクリックされました。')


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
