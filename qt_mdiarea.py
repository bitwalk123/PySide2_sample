#!/usr/bin/env python
# coding: utf-8

import sys
from PySide2 import QtCore
from PySide2.QtGui import QFont
from PySide2.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QMdiArea,
    QMdiSubWindow,
    QVBoxLayout,
    QWidget,
)


class Hello(QMainWindow):
    def __init__(self):
        super(Hello, self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        widget = self.initSubWindow()

        sub_window = QMdiSubWindow()
        sub_window.setWidget(widget)
        sub_window.setWindowTitle("MdiSubWindow")

        self.mdiArea = QMdiArea()
        self.setCentralWidget(self.mdiArea)
        self.mdiArea.addSubWindow(sub_window)
        self.setWindowTitle("MdiArea")

    def initSubWindow(self):
        label: QLabel = QLabel('こんにちは、世界！')
        font: QFont = QFont()
        font.setPointSize(24)
        label.setFont(font)
        label.setAlignment(QtCore.Qt.AlignCenter)
        layout: QVBoxLayout = QVBoxLayout()
        layout.addWidget(label)
        widget = QWidget()
        widget.setLayout(layout)
        return widget


def main():
    app: QApplication = QApplication(sys.argv)
    ex: Hello = Hello()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
