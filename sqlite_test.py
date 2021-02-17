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
import sqlite3
import tempfile


class Example(QMainWindow):
    dbname = "test.sqlite"

    def __init__(self):
        super().__init__()
        if not os.path.exists(self.dbname):
            self.initDB()

        self.initUI()
        self.setGeometry(100, 100, 600, 1)
        self.setWindowTitle('SQLite Test')
        self.show()

    def initUI(self):
        # menu in
        openFile = QAction('Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open New File')
        openFile.triggered.connect(self.showDialog)

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
        but_file.clicked.connect(lambda: self.on_click_open(combo_file))
        grid.addWidget(combo_file, 0, 0)
        grid.addWidget(but_file, 0, 1)

    def showDialog(self):
        dialog = QFileDialog()
        if dialog.exec_():
            fname = dialog.selectedFiles()[0]
            name_file = os.path.basename(fname)
            f = open(fname, 'rb')
            with f:
                content = f.read()
                con = sqlite3.connect(self.dbname)
                cur = con.cursor()
                cur.execute("INSERT INTO file VALUES(?, ?);", [name_file, content])
                con.commit()
                con.close()

    def get_filelist(self, combo: QComboBox):
        combo.clear()
        combo.clearEditText()

        con = sqlite3.connect(self.dbname)
        cur = con.cursor()
        cur.execute("SELECT name_file FROM file;")
        out = cur.fetchall()
        con.close()

        for name_file in out:
            combo.addItem(name_file[0])

    def on_click_open(self, combo: QComboBox):
        name_file = combo.currentText()
        out_file = os.path.join(tempfile.gettempdir(), name_file)
        print(out_file)

        con = sqlite3.connect(self.dbname)
        cur = con.cursor()
        cur.execute("SELECT content FROM file WHERE name_file = ?;", [name_file])
        out = cur.fetchall()
        con.close()

        with open(out_file, 'wb') as f:
            f.write(out[0][0])

        os.startfile(out_file)

    def initDB(self):
        init_sql = [
            'CREATE TABLE file (name_file TEXT UNIQUE, content BLOB)',
        ]
        con = sqlite3.connect(self.dbname)
        cur = con.cursor()

        for sql in init_sql:
            cur.execute(sql)

        con.commit()
        con.close()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
