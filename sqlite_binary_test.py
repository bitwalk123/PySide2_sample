import sys
from PySide2.QtWidgets import (
    QAction,
    QApplication,
    QComboBox,
    QFileDialog,
    QGridLayout,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QWidget,
)
import os
import platform
import sqlite3
import subprocess
import tempfile


class Example(QMainWindow):
    dbname = "test.sqlite"

    def __init__(self):
        super().__init__()
        if not os.path.exists(self.dbname):
            self.initDB()

        self.initUI()
        self.setWindowTitle('SQLite Test')
        self.show()
        self.setGeometry(100, 100, 300, 0)

    def initUI(self):
        # menu in
        openFile = QAction('Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open New File')

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File(&F)')
        fileMenu.addAction(openFile)

        # Main Window
        base = QWidget()
        base.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setCentralWidget(base)
        grid = QGridLayout()
        base.setLayout(grid)

        combo_file = QComboBox()
        self.get_filelist(combo_file)
        but_file = QPushButton('Open')
        but_file.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        grid.addWidget(combo_file, 0, 0)
        grid.addWidget(but_file, 0, 1)

        openFile.triggered.connect(lambda: self.showDialog(combo_file))
        but_file.clicked.connect(lambda: self.on_click_open(combo_file))

    def showDialog(self, combo: QComboBox):
        dialog = QFileDialog()
        dialog.setNameFilters(['PDF files (*.pdf)'])
        if dialog.exec_():
            fname = dialog.selectedFiles()[0]
            name_file = os.path.basename(fname)
            f = open(fname, 'rb')
            with f:
                content = f.read()

                # SQLite
                con = sqlite3.connect(self.dbname)
                cur = con.cursor()
                cur.execute("INSERT INTO file VALUES(?, ?);", [name_file, content])
                con.commit()
                con.close()

                # update list of QComboBox
                self.get_filelist(combo)

    def get_filelist(self, combo: QComboBox):
        combo.clear()
        combo.clearEditText()

        # SQLite
        con = sqlite3.connect(self.dbname)
        cur = con.cursor()
        cur.execute("SELECT name_file FROM file;")
        out = cur.fetchall()
        con.close()

        # add list of file to QComboBox
        for name_file in out:
            combo.addItem(name_file[0])

    def on_click_open(self, combo: QComboBox):
        name_file = combo.currentText()
        if len(name_file) == 0:
            return

        # set temporary location where to save name_file
        out_file = os.path.join(tempfile.gettempdir(), name_file)

        # SQLite
        con = sqlite3.connect(self.dbname)
        cur = con.cursor()
        cur.execute("SELECT content FROM file WHERE name_file = ?;", [name_file])
        out = cur.fetchall()
        con.close()

        # save out_file
        with open(out_file, 'wb') as f:
            f.write(out[0][0])

        # open out_file with application
        if platform.system() == 'Linux':
            subprocess.Popen(['xdg-open', out_file])
        elif platform.system() == 'Darwin':
            subprocess.Popen(['open', out_file])
        else:
            os.startfile(out_file)

    def initDB(self):
        init_query = [
            'CREATE TABLE file (name_file TEXT UNIQUE, content BLOB)',
        ]

        con = sqlite3.connect(self.dbname)
        cur = con.cursor()

        for query in init_query:
            cur.execute(query)

        con.commit()
        con.close()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
