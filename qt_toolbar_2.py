#!/usr/bin/env python
# coding: utf-8
# reference : https://pythonbasics.org/pyqt-toolbar/

import sys
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QToolBar,
    QToolButton,
    QGridLayout,
    QPlainTextEdit,
)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle('ToolBar')
        self.show()

    def initUI(self):
        layout = QGridLayout()
        self.setLayout(layout)

        # Create pyqt toolbar
        toolbar = QToolBar()
        layout.addWidget(toolbar)

        # Add buttons to toolbar
        tbtn1 = QToolButton()
        tbtn1.setText('Apple')
        tbtn1.setCheckable(True)
        tbtn1.setAutoExclusive(True)
        toolbar.addWidget(tbtn1)

        tbtn2 = QToolButton()
        tbtn2.setText('Orange')
        tbtn2.setCheckable(True)
        tbtn2.setAutoExclusive(True)
        toolbar.addWidget(tbtn2)

        # Add textfield to window
        tedit = QPlainTextEdit()
        layout.addWidget(tedit)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
