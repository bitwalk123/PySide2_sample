#!/usr/bin/env python
# coding: utf-8
# Reference:
# https://codeloop.org/how-to-create-progressbar-in-pyside2/

import sys
from PySide2.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QProgressBar,
    QStatusBar,
)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.setWindowTitle("ProgressBar")
        self.setGeometry(100, 100, 500, 400)
        self.show()

    def initUI(self):
        statusLabel = QLabel("Showing Progress")

        self.progressbar = QProgressBar()
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(100)
        self.progressbar.setValue(10)

        statusBar = QStatusBar()
        statusBar.addWidget(statusLabel, 1)
        statusBar.addWidget(self.progressbar, 2)

        self.setStatusBar(statusBar)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
