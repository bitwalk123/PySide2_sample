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
    oldValue = 0
    minValue = 0
    maxValue = 100
    delta = 10

    def __init__(self):
        super().__init__()
        self.setWindowTitle('QDial')
        self.initUI()

    def initUI(self):
        dial = QDial()
        dial.setMaximum(self.minValue)
        dial.setMaximum(self.maxValue)
        dial.setValue(self.oldValue)
        dial.valueChanged.connect(lambda: self.dialer_changed(dial, label))
        label = QLabel()
        self.disp_value(label, self.oldValue)

        vbox = QVBoxLayout()
        vbox.addWidget(dial)
        vbox.addWidget(label)
        self.setLayout(vbox)
        self.show()

    def dialer_changed(self, d: QDial, l: QLabel):
        newValue = d.value()

        if (abs(newValue - self.oldValue) > self.delta):
            d.setValue(self.oldValue)
            newValue = self.oldValue
        else:
            self.oldValue = newValue

        self.disp_value(l, newValue)

    def disp_value(self, l, newValue):
        l.setText('value : ' + str(newValue))


def main():
    app = QApplication(sys.argv)
    # print(QStyleFactory.keys())
    app.setStyle('Fusion')
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
