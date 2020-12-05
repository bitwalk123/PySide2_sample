# coding: UTF-8
# reference: https://mojaie.tumblr.com/post/58909785645/pyside-qtablewidget

import sys
# from PySide2 import QtGui, QtCore
from PySide2.QtCore import (
    Qt,
    QModelIndex,
    QAbstractTableModel
)

from PySide2.QtWidgets import (
    QApplication,
    QHeaderView,
    QMainWindow,
    QHBoxLayout,
    QWidget,
    QTableView,
    QTableWidget,
    QTableWidgetItem
)

# Sample Data
title = ["A", "B", "C"]
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


class Example(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        self.show()

    def initUI(self):
        rows = len(data)
        cols = len(data[0])
        self.table = QTableWidget(rows, cols)
        # Header
        vheader = QHeaderView(Qt.Orientation.Vertical)
        # vheader.setResizeMode(QHeaderView.ResizeToContents)
        self.table.setVerticalHeader(vheader)
        hheader = QHeaderView(Qt.Orientation.Horizontal)
        # hheader.setResizeMode(QHeaderView.ResizeToContents)
        self.table.setHorizontalHeader(hheader)
        self.table.setHorizontalHeaderLabels(title)

        # Table Contents
        for i in range(rows):
            for j in range(cols):
                item = QTableWidgetItem(str(data[i][j]))
                self.table.setItem(i, j, item)

        # Layout
        layout = QHBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
