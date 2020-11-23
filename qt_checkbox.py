#!/usr/bin/env python
# coding: utf-8

import sys
from PySide2.QtCore import Qt, Slot
from PySide2.QtWidgets import QApplication, QWidget, QCheckBox


class Example(QWidget):

    def initUI(self):
        cbox = QCheckBox('チェックボックス', self)
        cbox.move(20, 20)
        cbox.toggle()
        cbox.stateChanged.connect(self.checkboxChanged)

        self.setGeometry(300, 300, 200, 100)
        self.setWindowTitle("CheckBox")
        self.show()

    @Slot()
    def checkboxChanged(self, state):
        sender = self.sender()
        if state == Qt.Checked:
            print('「' + sender.text() + '」にチェックを入れました。')
        else:
            print('「' + sender.text() + '」のチェックを外しました。')

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
