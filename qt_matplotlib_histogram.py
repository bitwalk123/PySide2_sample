import numpy as np

import sys
from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QMdiArea,
    QMdiSubWindow,
    QVBoxLayout,
    QWidget,
)

from matplotlib.backends.backend_qt5agg import (
    FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar,
)
from matplotlib.figure import Figure


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mdiArea = QMdiArea()
        self.setCentralWidget(self.mdiArea)

        mu, sigma = 100, 15
        x = mu + sigma * np.random.randn(10000)

        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.ax = self.canvas.figure.subplots()
        n, bins, patches = self.ax.hist(
            x, 50, density=1, facecolor="green", alpha=0.75
        )
        self.ax.set_xlabel("Smarts")
        self.ax.set_ylabel("Probability")
        self.ax.set_title(r"$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$")
        self.ax.axis([40, 160, 0, 0.03])
        self.ax.grid(True)

        widget = QMainWindow()
        widget.setCentralWidget(self.canvas)
        widget.addToolBar(
            QtCore.Qt.BottomToolBarArea, NavigationToolbar(self.canvas, self)
        )
        sub_window = QMdiSubWindow()
        sub_window.setWidget(widget)
        self.mdiArea.addSubWindow(sub_window)
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
