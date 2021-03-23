#!/usr/bin/env python
# coding: utf-8
# Reference:
# https://codeloop.org/how-to-create-progressbar-in-pyside2/

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QProgressBar, QStatusBar, QLabel
from PySide2.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.setWindowTitle("ProgressBar")
        self.setGeometry(300, 200, 500, 400)
        self.show()

    def initUI(self):
        self.statusLabel = QLabel("Showing Progress")

        self.progressbar = QProgressBar()
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(100)
        self.progressbar.setValue(10)

        self.statusBar = QStatusBar()
        self.statusBar.addWidget(self.statusLabel, 1)
        self.statusBar.addWidget(self.progressbar, 2)

        self.setStatusBar(self.statusBar)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
