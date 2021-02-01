#!/usr/bin/env python
# coding: utf-8

import sys
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QSizePolicy,
    QToolBar,
    QToolButton,
    QWidget,
)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle("ToolBar")
        self.show()

    def initUI(self):
        # Create pyqt toolbar
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        # Add buttons to toolbar
        but_open = QToolButton()
        but_open.setIcon(QIcon.fromTheme('document-open'))
        toolbar.addWidget(but_open)

        # spacer
        spacer: QWidget = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        toolbar.addWidget(spacer)

        but_exit = QToolButton()
        but_exit.setIcon(QIcon.fromTheme('application-exit'))
        toolbar.addWidget(but_exit)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
