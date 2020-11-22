#!/usr/bin/env python
# coding: utf-8

import sys
from PySide2.QtWidgets import QMainWindow, QApplication, QAction


class Example(QMainWindow):

    def initUI(self):
        exitAction = QAction('終了', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('アプリケーションの修了')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("ファイル(&F)")
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('MenuBar')
        self.statusBar().showMessage("準備完了")
        self.show()

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()