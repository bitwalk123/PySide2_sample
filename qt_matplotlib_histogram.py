# reference : https://stackoverflow.com/questions/57367474/how-to-draw-a-histogram-inside-a-frame
import numpy as np

import sys
from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
)

from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar,
)
from matplotlib.figure import Figure


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.resize(800, 400)
        self.show()

    def initUI(self):
        mu, sigma = 100, 15
        x = mu + sigma * np.random.randn(10000)

        canvas = FigureCanvas(Figure(figsize=(5, 3)))
        ax = canvas.figure.subplots()
        n, bins, patches = ax.hist(
            x, 50, density=1, facecolor="green", alpha=0.75
        )

        ax.set_xlabel("Smarts")
        ax.set_ylabel("Probability")
        ax.set_title(r"$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$")
        ax.axis([40, 160, 0, 0.03])
        ax.grid(True)

        self.setCentralWidget(canvas)
        self.addToolBar(
            QtCore.Qt.BottomToolBarArea,
            NavigationToolbar(canvas, self)
        )


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
