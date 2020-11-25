#!/usr/bin/env python
# coding: utf-8

import sys
from PySide2.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):

    def initUI(self):
        self.statusBar().showMessage('準備完了')
        self.setGeometry(300, 300, 200, 150)
        self.setWindowTitle("Status Bar")
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