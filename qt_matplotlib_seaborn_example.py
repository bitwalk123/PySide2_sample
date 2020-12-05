# reference: https://stackoverflow.com/questions/41671867/embedding-figure-type-seaborn-plot-in-pyqt-pyqtgraph

from PySide2 import QtCore
from PySide2.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QWidget,
)

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")


def seabornplot():
    g = sns.FacetGrid(tips, col="sex", hue="time", palette="Set1",
                      hue_order=["Dinner", "Lunch"])
    g.map(plt.scatter, "total_bill", "tip", edgecolor="w")
    return g.fig


class Example(QMainWindow):
    send_fig = QtCore.Signal(str)

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle('Seaborn example')
        self.show()

    def initUI(self):
        self.fig = seabornplot()
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.canvas.updateGeometry()

        self.button = QPushButton("Button")
        self.label = QLabel("A plot:")
        self.main_widget = QWidget(self)
        self.layout = QGridLayout(self.main_widget)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.canvas)
        self.setCentralWidget(self.main_widget)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
