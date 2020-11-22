#!/usr/bin/env python
# coding: utf-8
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog


class Example(QMainWindow):

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        # openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile = QAction('開く', self)

        openFile.setShortcut('Ctrl+O')

        openFile.setStatusTip('新しいファイルを開く')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('ファイル(&F)')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):
        dialog = QFileDialog()
        if dialog.exec_():
            fname = dialog.selectedFiles()[0]
            f = open(fname, 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()