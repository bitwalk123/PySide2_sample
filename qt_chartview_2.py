#!/usr/bin/env python
# coding: utf-8
# reference : https://medium.com/swlh/python-gui-with-pyqt-pyside2-5cca38d739fa

import sys
from PySide2 import QtCore
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

    def initUI(self):

        dataY = [9.030, 8.810, 9.402, 8.664, 8.773, 8.774, 8.416, 9.101, 8.687, 8.767]

        seriesList = []
        series1 = QtCharts.QLineSeries()
        seriesList.append(series1)
        series2 = QtCharts.QScatterSeries()
        seriesList.append(series2)

        for i in range(len(dataY)):
            for series in seriesList:
                series.append(i + 1, dataY[i])

        series1.setColor(QtGui.QColor('blue'))
        series2.setColor(QtGui.QColor('gray'))


        chart = QtCharts.QChart()
        for series in seriesList:
            chart.addSeries(series)

        chart.setTitle('SPC Chart Example')
        chart.setBackgroundBrush(QtGui.QColor("ivory"))
        chart.legend().hide()

        axisX = QtCharts.QValueAxis()
        axisX.setLinePenColor('gray')
        axisX.setTickCount(len(dataY) + 2);
        axisX.setRange(0, len(dataY) + 1);
        axisX.setLabelFormat('%d')

        axisX2 = QtCharts.QValueAxis()
        axisX2.setLinePenColor('gray')
        axisX2.setRange(0, len(dataY) + 1);
        axisX2.setLabelFormat(' ')

        ymax = max(dataY)
        ymin = min(dataY)
        yrange = ymax - ymin
        ydelta = yrange * 0.05

        axisY = QtCharts.QValueAxis()
        axisY.setLinePenColor('gray')
        axisY.setRange(ymin - ydelta, ymax + ydelta);

        axisY2 = QtCharts.QValueAxis()
        axisY2.setLinePenColor('gray')
        axisY2.setRange(ymin - ydelta, ymax + ydelta);

        chart.addAxis(axisX, QtCore.Qt.AlignBottom)
        chart.addAxis(axisX2, QtCore.Qt.AlignTop)
        chart.addAxis(axisY, QtCore.Qt.AlignLeft)
        chart.addAxis(axisY2, QtCore.Qt.AlignRight)

        for series in seriesList:
            #chart.setAxisX(axisX, series)
            #chart.setAxisY(axisY, series)
            series.attachAxis(axisX)
            series.attachAxis(axisY)


        chartView = QtCharts.QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)

        layout = QVBoxLayout()
        layout.addWidget(chartView)
        self.setLayout(layout)
        self.resize(600, 400)
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
