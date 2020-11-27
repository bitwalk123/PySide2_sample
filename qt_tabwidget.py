#!/usr/bin/env python
# coding: utf-8
# reference : http://mukaimame.blog111.fc2.com/blog-entry-842.html

import sys
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QTabWidget,
    QLabel,
)


class Tab1Widget(QWidget):
    def __init__(self, parent=None):
        super(Tab1Widget, self).__init__()
        closeBtn = QPushButton('Close')
        closeBtn.clicked.connect(parent.close)
        hbox = QHBoxLayout()
        hbox.addWidget(closeBtn)
        self.setLayout(hbox)


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        qtab = QTabWidget()
        qtab.addTab(Tab1Widget(parent=self), 'Tab1')
        qtab.addTab(QLabel('Label 2'), 'Tab2')

        hbox = QHBoxLayout()
        hbox.addWidget(qtab)

        self.setLayout(hbox)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Tab Layout')
        self.show()


def main():
    app = QApplication(sys.argv)
    ui = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
