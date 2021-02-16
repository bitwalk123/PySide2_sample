#!/usr/bin/env python
# coding: utf-8
# Reference:
# https://stackoverflow.com/questions/22069321/realtime-output-from-a-subprogram-to-stdout-of-a-pyqt-widget

import os
import sys
from PySide2.QtCore import QProcess
from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
    QToolBar,
    QToolButton,
)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle('QProcess')
        self.setGeometry(100, 100, 600, 300)
        self.show()

    def initUI(self):
        tool_run = QToolButton()
        tool_run.setText('Run')
        tool_run.clicked.connect(self.callProgram)

        toolbar = QToolBar()
        self.addToolBar(toolbar)
        toolbar.addWidget(tool_run)

        self.output = QTextEdit()
        self.setCentralWidget(self.output)

        # QProcess object for external app
        self.process = QProcess(self)
        # QProcess emits `readyRead` when there is data to be read
        self.process.readyRead.connect(self.dataReady)

        # Just to prevent accidentally running multiple times
        # Disable the button when process starts, and enable it when it finishes
        self.process.started.connect(lambda: tool_run.setEnabled(False))
        self.process.finished.connect(lambda: tool_run.setEnabled(True))

    def dataReady(self):
        cursor = self.output.textCursor()
        cursor.movePosition(cursor.End)
        content = self.process.readAllStandardOutput()
        cursor.insertText(str(content, 'utf-8'))
        self.output.ensureCursorVisible()

    def callProgram(self):
        # run the process
        # `start` takes the exec and a list of arguments
        if os.name == 'nt':
            self.process.start('ping', ['127.0.0.1'])
        else:
            self.process.start('ping', ['-c', '4', '127.0.0.1'])


def main():
    app: QApplication = QApplication(sys.argv)
    ex: Example = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
