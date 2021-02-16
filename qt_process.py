import sys
from PySide2.QtCore import QProcess
from PySide2.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QTextEdit,
    QWidget,
)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def dataReady(self):
        cursor = self.output.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText(str(self.process.readAll()))
        self.output.ensureCursorVisible()

    def callProgram(self):
        # run the process
        # `start` takes the exec and a list of arguments
        self.process.start('ping', ['127.0.0.1'])

    def initUI(self):
        # Layout are better for placing widgets
        layout = QHBoxLayout()
        self.runButton = QPushButton('Run')
        self.runButton.clicked.connect(self.callProgram)

        self.output = QTextEdit()

        layout.addWidget(self.output)
        layout.addWidget(self.runButton)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

        # QProcess object for external app
        self.process = QProcess(self)
        # QProcess emits `readyRead` when there is data to be read
        self.process.readyRead.connect(self.dataReady)

        # Just to prevent accidentally running multiple times
        # Disable the button when process starts, and enable it when it finishes
        self.process.started.connect(lambda: self.runButton.setEnabled(False))
        self.process.finished.connect(lambda: self.runButton.setEnabled(True))


def main():
    app: QApplication = QApplication(sys.argv)
    ex: Example = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
