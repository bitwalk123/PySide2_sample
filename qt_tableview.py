#!/usr/bin/env python
# coding: utf-8
# reference: https://pc-technique.info/2020/02/207/

import sys
import dataclasses

from typing import Any, List
from PySide2.QtCore import (
    Qt,
    QModelIndex,
    QAbstractTableModel
)

# For Sample
from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QTableView
)


# custom Data class
@dataclasses.dataclass
class CustomData:
    name: str
    age: int
    country: str

    def toList(self) -> list:
        return [self.name, self.age, self.country]

    @classmethod
    def toHeaderList(cls) -> List[str]:
        return ["NAME", "AGE", "COUNTRY"]


class SimpleTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.custom_data: List[CustomData] = [
            CustomData(name="Taro", age=24, country="Japan"),
            CustomData(name="Jiro", age=20, country="Japan"),
            CustomData(name="David", age=32, country="USA"),
            CustomData(name="Wattson", age=15, country="US")
        ]  # prepare table's source data (TEST)

    def data(self, index: QModelIndex, role: int) -> Any:
        if role == Qt.DisplayRole:
            # The QTableView wants a cell text of 'index'
            # BE CAREFUL about IndexError (rowCount() and/or columnCount() are incorrect.)
            return self.custom_data[index.row()].toList()[index.column()]

    def rowCount(self, parent=QModelIndex()) -> int:
        # = data count
        return len(self.custom_data)

    def columnCount(self, parent=QModelIndex()) -> int:
        return len(CustomData.toHeaderList())

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.DisplayRole):
        if role == Qt.DisplayRole:
            # The QTableView wants a header text
            if orientation == Qt.Horizontal:
                # BE CAREFUL about IndexError
                return CustomData.toHeaderList()[section]

            return ""  # There is no vertical header


class Example(QMainWindow):
    def initUI(self):
        self.root_widget: QWidget = QWidget()
        self.layout: QVBoxLayout = QVBoxLayout()
        self.table: QTableView = QTableView()
        self.layout.addWidget(self.table)
        self.root_widget.setLayout(self.layout)

        # create model and set
        self.table.setModel(SimpleTableModel())

        self.setCentralWidget(self.root_widget)
        self.setWindowTitle('TableView')
        self.show()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
