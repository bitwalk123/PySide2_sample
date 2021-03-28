#!/usr/bin/env python
# coding: utf-8
# Reference
# https://www.learnpyqt.com/tutorials/example-browser/

import sys
from PySide2.QtCore import QUrl
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
)


class Example(QMainWindow):
    url = 'http://www.google.com'

    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        browser = QWebEngineView()
        browser.setUrl(QUrl(self.url))
        self.setCentralWidget(browser)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
