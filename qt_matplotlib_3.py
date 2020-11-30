#!/usr/bin/env python
# coding: utf-8
# reference: https://discourse.matplotlib.org/t/customizing-the-navigation-toolbar/16032/3

import sys
from PySide2.QtWidgets import (
    QApplication,
    QLineEdit,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar2


class Example(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):
        # create a simple main widget to keep the figure
        self.mainWidget = QWidget()
        self.setCentralWidget(self.mainWidget)

        layout = QVBoxLayout()
        self.mainWidget.setLayout(layout)

        # create a figure
        self.figure_canvas = FigureCanvas(Figure())
        layout.addWidget(self.figure_canvas, 10)

        # and the axes for the figure
        self.axes = self.figure_canvas.figure.add_subplot(111)

        # add a navigation toolbar
        self.navigation_toolbar = NavigationToolbar2(self.figure_canvas, self)
        layout.addWidget(self.navigation_toolbar, 0)

        # create a simple widget to extend the navigation toolbar
        anotherWidget = QLineEdit()
        # add the new widget to the existing navigation toolbar
        self.navigation_toolbar.addWidget(anotherWidget)

        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
