#!/usr/bin/env python
# coding: utf-8

import math
import queue
import re
import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import (
    QApplication,
    QGridLayout,
    QLayout,
    QLCDNumber,
    QPushButton,
    QSizePolicy,
    QWidget,
)


class Calculator(QWidget):
    # Key Layout
    list_key = (
        ('Ｃ', 1, 0, 'func'),
        ('％', 1, 1, 'func'),
        ('√', 1, 2, 'func'),
        ('÷', 1, 3, 'ope'),
        ('７', 2, 0, 'num'),
        ('８', 2, 1, 'num'),
        ('９', 2, 2, 'num'),
        ('×', 2, 3, 'ope'),
        ('４', 3, 0, 'num'),
        ('５', 3, 1, 'num'),
        ('６', 3, 2, 'num'),
        ('－', 3, 3, 'ope'),
        ('１', 4, 0, 'num'),
        ('２', 4, 1, 'num'),
        ('３', 4, 2, 'num'),
        ('＋', 4, 3, 'func'),
        ('０', 5, 0, 'num'),
        ('・', 5, 1, 'num'),
        ('±', 5, 2, 'func'),
        ('＝', 5, 3, 'ope'),
    )
    # initial display
    display_initial = "0."
    # max length
    max_chars = 12

    # operation flag
    flag_dot = False
    flag_operation = False
    flag_error = False

    # register for calculation
    reg = queue.Queue()

    # regular expression
    re1 = re.compile("([\-0-9]+)\.$")
    re2 = re.compile("([\-0-9]+\.)0$")

    def __init__(self):
        super().__init__()
        # self.setWhatsThis("Help on widget")
        self.initUI()
        self.setWindowTitle('Calculator')
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        # This can be used for Windows
        # self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
        self.show()

    def initUI(self):
        grid = QGridLayout()
        grid.setHorizontalSpacing(2)
        grid.setVerticalSpacing(2)
        # Reference
        # https://stackoverflow.com/questions/16673074/how-can-i-fully-disable-resizing-a-window-including-the-resize-icon-when-the-mou
        grid.setSizeConstraint(QLayout.SetFixedSize)
        self.setLayout(grid)

        self.lcd = QLCDNumber(self)
        self.lcd.setDigitCount(self.max_chars)
        # lcd.display(0.)
        value = 0.123456789
        self.lcd.display(value)
        self.lcd.setStyleSheet("QLCDNumber {color:darkgreen;}")
        self.lcd.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(self.lcd, 0, 0, 1, 4)
        grid.setRowMinimumHeight(0, 48)

        for key in self.list_key:
            self.gen_key_pad(grid, key)

    def gen_key_pad(self, grid, info):
        label = info[0]
        y = info[1]
        x = info[2]
        button = QPushButton(label)
        button.setStyleSheet("QPushButton {font-size:12pt; padding:5px 20px; color:#666;}")
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(button, y, x)

    # -------------------------------------------------------------------------
    #  get_display_string
    #
    #  argument
    #    value : value to display
    #
    #  return
    #    string to display
    # -------------------------------------------------------------------------
    def get_display_string(self, value):
        str_display = str(value)

        result = self.re2.match(str_display)
        if result:
            str_display = result.group(1)
            return str_display

        return str_display

    # -------------------------------------------------------------------------
    #  get_function_result
    #
    #  arguments
    #    text  : function operator
    #    value : value of function parameter
    #
    #  return
    #    value calculated specified function
    # -------------------------------------------------------------------------
    def get_function_result(self, text, value):
        # sign
        if text == "±":
            return value * -1
        # square root
        if text == "√":
            try:
                return math.sqrt(value)
            except Exception as e:
                self.flag_error = True
                return e

    # -------------------------------------------------------------------------
    #  get_operator
    #
    #  argument
    #    text : label string of calculator key pad
    #
    #  return
    #    operator string
    # -------------------------------------------------------------------------
    def get_operator(self, text):
        if text == "＋":
            return "+"
        if text == "−":
            return "-"
        if text == "×":
            return "*"
        if text == "÷":
            return "/"

    # -------------------------------------------------------------------------
    #  set_display
    #
    #  argument
    #    text : string to display
    # -------------------------------------------------------------------------
    def set_display(self, text):
        length = len(text)
        self.ent.set_text(text)
        self.ent.set_position(length)

    # -------------------------------------------------------------------------
    #  zenkaku_to_hankaku
    #
    #  argument
    #    text : zenkaku string
    #
    #  return
    #    hankaku (ascii) string
    # -------------------------------------------------------------------------
    def zenkaku_to_hankaku(self, text):
        # ref: https://qiita.com/YuukiMiyoshi/items/6ce77bf402a29a99f1bf
        return text.translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)}))

    # =========================================================================
    #  BINDINGS
    # =========================================================================
    # -------------------------------------------------------------------------
    #  on_clear
    # -------------------------------------------------------------------------
    def on_clear(self, button):
        # display
        self.set_display(self.display_initial)

        # clear flag
        self.flag_dot = False
        self.flag_operation = False
        self.flag_error = False

    # -------------------------------------------------------------------------
    #  on_dot
    # -------------------------------------------------------------------------
    def on_dot(self, button):
        if self.flag_error:
            return

        # flag
        self.flag_dot = True

    # -------------------------------------------------------------------------
    #  on_equal
    # -------------------------------------------------------------------------
    def on_equal(self, button):
        if self.flag_error:
            return

        expr = ""
        while not self.reg.empty():
            expr += self.reg.get()

        expr += self.ent.get_text()

        try:
            result = eval(expr)
        except Exception as e:
            result = e
            self.flag_error = True

        disp_new = self.get_display_string(result)

        # display
        self.set_display(disp_new)

        # flag
        self.flag_operation = True

    # -------------------------------------------------------------------------
    #  on_function
    # -------------------------------------------------------------------------
    def on_function(self, button):
        if self.flag_error:
            return

        # get current value displayed
        value_current = float(self.ent.get_text())

        # get string from key label
        text = button.get_label()

        value_new = self.get_function_result(text, value_current)
        disp_new = self.get_display_string(value_new)

        # display
        self.set_display(disp_new)

        # flag
        self.flag_operation = True

    # -------------------------------------------------------------------------
    #  on_operation
    # -------------------------------------------------------------------------
    def on_operation(self, button):
        if self.flag_error:
            return

        # get current string displayed
        disp_current = self.ent.get_text()
        self.reg.put(disp_current)

        # get string from key label
        text = button.get_label()
        self.reg.put(self.get_operator(text))

        # flag
        self.flag_operation = True

    # -------------------------------------------------------------------------
    #  on_number
    # -------------------------------------------------------------------------
    def on_number(self, button):
        if self.flag_error:
            return

        # get current string displayed
        disp_current = self.ent.get_text()

        # get string from key label
        text = button.get_label()
        text_ascii = self.zenkaku_to_hankaku(text)

        # update string to display
        if self.flag_operation:
            disp_new = text_ascii + "."
            self.flag_operation = False
        else:
            if disp_current == "0.":
                if self.flag_dot:
                    disp_new = disp_current + text_ascii
                else:
                    disp_new = text_ascii + "."
            else:
                # check charcter length (digit)
                if len(disp_current) > self.max_chars:
                    return

                if self.flag_dot:
                    disp_new = disp_current + text_ascii
                else:
                    result = self.re1.match(disp_current)
                    if result:
                        disp_new = result.group(1) + text_ascii + "."
                    else:
                        disp_new = disp_current + text_ascii

        self.set_display(disp_new)


def main():
    app = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
