#!/usr/bin/env python
# coding: utf-8
# reference
# https://stackoverflow.com/questions/53252404/how-to-set-qlabel-using-base64-string-or-byte-array

import sys
from bz2 import decompress
from PySide2.QtCore import QByteArray
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import (
    QApplication,
    QLabel,
    QVBoxLayout,
    QWidget,
)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle('Label')
        self.show()

    def initUI(self):
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        lab = QLabel()
        lab.setPixmap(self.get_pixmap())
        vbox.addWidget(lab)

    def get_pixmap(self):
        base64data = b'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'
        byte_array = decompress(QByteArray.fromBase64(base64data))
        pixmap = QPixmap()
        pixmap.loadFromData(byte_array)

        return pixmap


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
