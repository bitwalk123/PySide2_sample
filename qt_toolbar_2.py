#!/usr/bin/env python
# coding: utf-8
# reference : https://pythonbasics.org/pyqt-toolbar/

import sys
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QToolBar,
    QToolButton,
    QGridLayout,
    QPlainTextEdit,
    QSizePolicy,
)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle("ToolBar")
        self.show()

    def initUI(self):
        layout = QGridLayout()
        self.setLayout(layout)

        # Create pyqt toolbar
        toolbar = QToolBar()
        layout.addWidget(toolbar)

        # Add buttons to toolbar
        but_open = QToolButton()
        but_open.setIcon(QIcon.fromTheme('document-open'))
        but_open.setCheckable(True)
        but_open.setAutoExclusive(True)
        toolbar.addWidget(but_open)

        # spacer
        spacer: QWidget = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        toolbar.addWidget(spacer)

        but_exit = QToolButton()
        but_exit.setIcon(QIcon.fromTheme('application-exit'))
        but_exit.setCheckable(True)
        but_exit.setAutoExclusive(True)
        toolbar.addWidget(but_exit)

        # Add textfield to window
        tedit = QPlainTextEdit()
        layout.addWidget(tedit)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
