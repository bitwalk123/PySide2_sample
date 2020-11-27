#!/usr/bin/env python3
# reference : https://stackoverflow.com/questions/58075822/pyside2-and-matplotlib-how-to-make-matplotlib-run-in-a-separate-process-as-i

import sys

from PySide2.QtCore import QFile, QObject, Signal, Slot, QTimer
from PySide2.QtWidgets import QApplication, QVBoxLayout, QWidget
from PySide2.QtUiTools import QUiLoader

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import random


class DSL(QObject):
    dataChanged = Signal(list)

    def __init__(self, parent=None):
        # LOAD HMI
        super().__init__(parent)
        designer_file = QFile("userInterface.ui")
        if designer_file.open(QFile.ReadOnly):
            loader = QUiLoader()
            self.ui = loader.load(designer_file)
            designer_file.close()
            self.ui.show()
        # Data to be visualized
        self.data = []

    def mainLoop(self):
        self.data = []
        for i in range(10):
            self.data.append(random.randint(0, 10))
        # Send data to graph
        self.dataChanged.emit(self.data)
        # LOOP repeater
        QTimer.singleShot(10, self.mainLoop)


class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        fig = Figure(figsize=(7, 5), dpi=65, facecolor=(1, 1, 1), edgecolor=(0, 0, 0))
        self.canvas = FigureCanvas(fig)
        self.toolbar = NavigationToolbar(self.canvas, self)
        lay = QVBoxLayout(self)
        lay.addWidget(self.toolbar)
        lay.addWidget(self.canvas)

        self.ax = fig.add_subplot(111)
        self.line, *_ = self.ax.plot([])

    @Slot(list)
    def update_plot(self, data):
        self.line.set_data(range(len(data)), data)

        self.ax.set_xlim(0, len(data))
        self.ax.set_ylim(min(data), max(data))
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dsl = DSL()
    dsl.mainLoop()

    matplotlib_widget = MatplotlibWidget()
    matplotlib_widget.show()

    dsl.dataChanged.connect(matplotlib_widget.update_plot)
    sys.exit(app.exec_())
