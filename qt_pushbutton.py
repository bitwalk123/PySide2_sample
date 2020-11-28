#!/usr/bin/env python
# coding: utf-8
# reference : https://github.com/andriyantohalim/PySide2_Tutorial

import sys
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QWidget, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn: QPushButton = QPushButton('プッシュボタン', self)
        btn.clicked.connect(self.buttonClicked)
        btn.resize(btn.sizeHint())
        btn.move(50, 20)

        self.setWindowTitle('PushButton')
        self.show()

    @Slot()
    def buttonClicked(self):
        obj: QPushButton = self.sender()
        print('「' + obj.text() + '」がクリックされました。')


def main():
    app: QApplication = QApplication(sys.argv)
    ex: Example = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
