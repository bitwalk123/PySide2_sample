#!/usr/bin/env python
# coding: utf-8
import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton
from PySide2.QtCore import QCoreApplication


class Example(QWidget):

    def initUI(self):
        btn = QPushButton("プッシュボタン", self)
        btn.clicked.connect(self.buttonClicked)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setWindowTitle("PushButton")
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        print('「' + sender.text() + '」がクリックされました。')

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
