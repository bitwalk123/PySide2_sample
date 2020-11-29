#!/usr/bin/env python
# coding: utf-8
# reference: https://pc-technique.info/2020/02/207/

import sys
from typing import Any, List
from PySide2.QtCore import (
    Qt,
    QModelIndex,
    QAbstractTableModel
)

from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableView,
    QHeaderView,
)


class SimpleTableModel(QAbstractTableModel):
    def __init__(self, source: list, headers: list):
        QAbstractTableModel.__init__(self)
        self.source: list= source
        self.headers: list = headers

    def data(self, index: QModelIndex, role: int) -> Any:
        if role == Qt.DisplayRole:
            return self.source[index.row()][index.column()]

    def rowCount(self, parent=QModelIndex()) -> int:
        return len(self.source)

    def columnCount(self, parent=QModelIndex()) -> int:
        return len(self.headers)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return
        if orientation == Qt.Horizontal:
            return self.headers[section]
        else:
            return "{}".format(section + 1)


class Example(QMainWindow):
    prefdata: list = [
        ['栃木県', '宇都宮'],
        ['千葉県', '千葉'],
        ['東京都', '東京'],
        ['神奈川県', '横浜'],
    ]
    header: list = ['都道府県', '県庁所在地']

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        table: QTableView = QTableView()
        table.setWordWrap(False)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # set table model
        table.setModel(SimpleTableModel(self.prefdata, self.header))

        self.setCentralWidget(table)
        self.setWindowTitle('TableView')
        self.show()


def main():
    app: QApplication = QApplication(sys.argv)
    ex: QMainWindow = Example()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
