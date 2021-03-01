#!/usr/bin/env python
# coding: utf-8

import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import (
    QApplication,
    QGridLayout,
    QLayout,
    QLCDNumber,
    QPushButton,
    QSizePolicy,
    QWidget,
)


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        #self.setWhatsThis("Help on widget")
        self.initUI()
        self.setWindowTitle('Calculator')
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        # This can be used for Windows
        # self.setWindowFlags(Qt.Dialog | Qt.MSWindowsFixedSizeDialogHint)
        self.show()

    def initUI(self):
        grid = QGridLayout()
        grid.setHorizontalSpacing(2)
        grid.setVerticalSpacing(2)
        # Reference
        # https://stackoverflow.com/questions/16673074/how-can-i-fully-disable-resizing-a-window-including-the-resize-icon-when-the-mou
        grid.setSizeConstraint(QLayout.SetFixedSize)
        self.setLayout(grid)

        lcd = QLCDNumber(self)
        lcd.setDigitCount(12)
        #lcd.display(0.)
        lcd.display(0.123456789)
        lcd.setStyleSheet("QLCDNumber {color:darkgreen;}")
        lcd.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(lcd, 0, 0, 1, 4)
        grid.setRowMinimumHeight(0, 48)

        list_key = (
            ('Ｃ', 1, 0, 'func'),
            ('％', 1, 1, 'func'),
            ('√', 1, 2, 'func'),
            ('÷', 1, 3, 'ope'),
            ('７', 2, 0, 'num'),
            ('８', 2, 1, 'num'),
            ('９', 2, 2, 'num'),
            ('×', 2, 3, 'ope'),
            ('４', 3, 0, 'num'),
            ('５', 3, 1, 'num'),
            ('６', 3, 2, 'num'),
            ('－', 3, 3, 'ope'),
            ('１', 4, 0, 'num'),
            ('２', 4, 1, 'num'),
            ('３', 4, 2, 'num'),
            ('＋', 4, 3, 'func'),
            ('０', 5, 0, 'num'),
            ('・', 5, 1, 'num'),
            ('±', 5, 2, 'func'),
            ('＝', 5, 3, 'ope'),
        )
        for key in list_key:
            self.gen_key_pad(grid, key)

    def gen_key_pad(self, grid, info):
        label = info[0]
        y = info[1]
        x = info[2]
        button = QPushButton(label)
        button.setStyleSheet("QPushButton {font-size:12pt; padding:5px 20px; color:#888}")
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(button, y, x)


def main():
    app = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
