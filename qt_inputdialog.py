#!/usr/bin/env python
# coding: utf-8
# reference : https://github.com/andriyantohalim/PySide2_Tutorial

import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QInputDialog


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setGeometry(300, 300, 280, 60)
        self.setWindowTitle('Input dialog')
        self.show()

    def initUI(self):
        self.btn = QPushButton('ダイアログ', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(110, 20)

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', '氏名の入力：')
        if ok:
            self.le.setText(str(text))


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
