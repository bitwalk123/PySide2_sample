#!/usr/bin/env python
# coding: utf-8
# Reference
# https://codeloop.org/pyqt5-qdial-example-with-valuechanged-signal/

import sys
from PySide2.QtWidgets import (
    QApplication,
    QDial,
    QLabel,
    QStyleFactory,
    QVBoxLayout,
    QWidget,
)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QDialog')
        self.initUI()

    def initUI(self):
        self.dial = QDial()
        self.dial.setMaximum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(0)
        self.dial.valueChanged.connect(self.dialer_changed)
        self.label = QLabel()
        vbox = QVBoxLayout()
        vbox.addWidget(self.dial)
        vbox.addWidget(self.label)
        self.setLayout(vbox)
        self.show()

    def dialer_changed(self):
        self.label.setText('値 : ' + str(self.dial.value()))


def main():
    app = QApplication(sys.argv)
    #print(QStyleFactory.keys())
    app.setStyle('Fusion')
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
