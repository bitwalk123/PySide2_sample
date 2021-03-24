#!/usr/bin/env python
# coding: utf-8
# Reference:
# https://stackoverflow.com/questions/59082375/implement-qthread-with-qprogressbar-in-pyside-or-pyqt-during-calculation

import sys
import time
from PySide2.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QSizePolicy,
    QStatusBar,
)
from PySide2.QtCore import (
    QThread,
    Signal,
)


class Example(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()
        self.task_def()

        self.setWindowTitle('ProgressBar & Thread')
        self.show()

    def initUI(self):
        self.but = QPushButton("Start Job")
        self.but.clicked.connect(self.task_start)
        self.setCentralWidget(self.but)

        status_label = QLabel("Progress")
        status_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.proggress_bar = QProgressBar()
        self.proggress_bar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        status_bar = QStatusBar()
        status_bar.addWidget(status_label, 1)
        status_bar.addWidget(self.proggress_bar, 2)

        self.setStatusBar(status_bar)

    def task_def(self):
        self.task = TaskThread(self)
        self.task.progressChanged.connect(self.proggress_bar.setValue)

    def task_start(self):
        self.task.start()


class TaskThread(QThread):
    progressChanged = Signal(int)

    def run(self):
        for x in range(0, 101):
            time.sleep(0.1)
            self.progressChanged.emit(x)
        self.exit(0)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
