#!/usr/bin/env python
# coding: utf-8
# reference : https://medium.com/swlh/python-gui-with-pyqt-pyside2-5cca38d739fa

import sys
from PySide2 import QtGui
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
)
from PySide2.QtCharts import QtCharts
from random import randint


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Initialize chart
        chart = QtCharts.QChart()
        lineSeries = QtCharts.QLineSeries()

        # Make some random data points
        dataSeries = [(i + 1, randint(0, 99999)) for i in range(200)]

        # load data into chart:
        for point in dataSeries:
            lineSeries.append(point[0], point[1])

        # Add Some Chart Options
        chart.addSeries(lineSeries)
        chart.setTitle("Random Numbers from 0-9000")
        chart.createDefaultAxes()

        # Create a container (similar to a widget)
        chartView = QtCharts.QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)

        # Some Chart Styling
        lineSeries.setColor(QtGui.QColor("darkgray"))
        chartView.chart().setBackgroundBrush(QtGui.QColor("ivory"))
        layout.addWidget(chartView)
        self.setLayout(layout)
        self.resize(600, 400)
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
