#!/usr/bin/env python
# coding: utf-8

import sys
from PySide2.QtCore import Qt
from PySide2.QtGui import (
    QImage,
    QPixmap,
)
from PySide2.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QLabel,
    QLayout,
    QWidget,
)


class Example(QWidget):
    length_max = 300.0
    file_name = 'sample_picture.jpg'

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle('QPixmap')
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.show()

    def initUI(self):
        image = QImage(self.file_name)
        if image.width() > image.height():
            pixmap = QPixmap(image.scaledToWidth(self.length_max))
        else:
            pixmap = QPixmap(image.scaledToHeight(self.length_max))

        label = QLabel(self)
        label.setPixmap(pixmap)

        vbox = QVBoxLayout(self)
        vbox.addWidget(label)
        vbox.setSizeConstraint(QLayout.SetFixedSize)
        self.setLayout(vbox)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
