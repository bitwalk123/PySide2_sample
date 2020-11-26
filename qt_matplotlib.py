#!/usr/bin/env python
# coding: utf-8

import sys
from PySide2.QtWidgets import QApplication, QVBoxLayout, QWidget

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import pandas as pd


class Example(QWidget):

    def initUI(self):
        # example dataframe
        df = pd.DataFrame({
            'Sample': list(range(1, 11)),
            'Y': [9.030, 8.810, 9.402, 8.664, 8.773, 8.774, 8.416, 9.101, 8.687, 8.767]
        })
        # SPC metrics
        spec_usl = 9.97
        spec_target = 8.70
        spec_lsl = 7.43

        # spc chart
        fig = Figure(dpi=100)
        splot = fig.add_subplot(111, title='SPC Chart Example', ylabel='Value')
        splot.grid(True)

        # horizontal lines
        splot.axhline(y=spec_usl, linewidth=1, color='red', label='USL')
        splot.axhline(y=spec_target, linewidth=1, color='blue', label='Target')
        splot.axhline(y=spec_lsl, linewidth=1, color='red', label='LSL')

        # trend
        splot.plot(df['Sample'], df['Y'], color='gray', marker='o', markersize=10)

        # text label
        x_label = splot.get_xlim()[1]
        splot.text(x_label, spec_usl, ' USL', color='red')
        splot.text(x_label, spec_target, ' Target', color='blue')
        splot.text(x_label, spec_lsl, ' LSL', color='red')

        canvas = FigureCanvas(fig)
        toolbar = NavigationToolbar(canvas, self)

        layout = QVBoxLayout(self)
        layout.addWidget(toolbar)
        layout.addWidget(canvas)

        self.setWindowTitle('SPC Chart')
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
