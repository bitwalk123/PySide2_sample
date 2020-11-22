#!/usr/bin/env python
# coding: utf-8

import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QInputDialog


class Example(QWidget):

    def initUI(self):
        self.btn = QPushButton('ダイアログ', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(110, 20)

        self.setGeometry(300, 300, 280, 60)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', '氏名の入力：')
        if ok:
            self.le.setText(str(text))

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
