#!/usr/bin/env python
# coding: utf-8
# reference : https://github.com/andriyantohalim/PySide2_Tutorial

import sys
from PySide2.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QLCDNumber,
    QPushButton,
    QSizePolicy,
    QWidget,
)


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle('Calculator')
        self.show()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        grid.setRowMinimumHeight(0, 48)

        r = 0
        lcd = QLCDNumber(self)
        lcd.setDigitCount(12)
        lcd.display(0.123456789)
        lcd.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(lcd, r, 0, 1, 4)
        r += 1

        btn_clear = QPushButton('Ｃ')
        btn_clear.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(btn_clear, r, 0)

        btn_percent = QPushButton('％')
        btn_percent.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(btn_percent, r, 1)

        btn_root = QPushButton('√')
        btn_root.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(btn_root, r, 2)

        btn_div = QPushButton('÷')
        btn_div.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(btn_div, r, 3)
        r += 1

        btn_7 = QPushButton('７')
        btn_7.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(btn_7, r, 0)

        btn_8 = QPushButton('８')
        btn_8.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(btn_8, r, 1)

        btn_9 = QPushButton('９')
        btn_9.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(btn_9, r, 2)

        btn_mul = QPushButton('×')
        btn_mul.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(btn_mul, r, 3)

        r += 1

        btn_4 = QPushButton('４')
        btn_4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(btn_4, r, 0)

        btn_5 = QPushButton('５')
        btn_5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(btn_5, r, 1)

        btn_6 = QPushButton('６')
        btn_6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(btn_6, r, 2)

        btn_minus = QPushButton('ー')
        btn_minus.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(btn_minus, r, 3)

        r += 1

        btn_1 = QPushButton('１')
        btn_1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(btn_1, r, 0)

        btn_2 = QPushButton('２')
        btn_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(btn_2, r, 1)

        btn_3 = QPushButton('３')
        btn_3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(btn_3, r, 2)

        btn_plus = QPushButton('＋')
        btn_plus.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(btn_plus, r, 3)

        r += 1

        btn_0 = QPushButton('０')
        btn_0.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(btn_0, r, 0)

        btn_point = QPushButton('・')
        btn_point.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(btn_point, r, 1)

        btn_sign = QPushButton('±')
        btn_sign.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(btn_sign, r, 2)

        btn_equal = QPushButton('＝')
        btn_equal.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(btn_equal, r, 3)

        r += 1


def main():
    app = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
