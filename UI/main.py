#!/usr/bin/env python3
# coding=utf-8

import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main.ui', self)

        self.setWindowTitle('Работа с текстом в PyQt5')
        self.setWindowIcon(QtGui.QIcon('logo.png'))

        self.pushButton_execute.clicked.connect(self.solve)
        self.pushButton_clear.clicked.connect(self.clear)
        self.pushButton_exit.clicked.connect(self.close)

    def solve(self):

        new_list = []
        source_text = self.lineEdit.text()
        for i, symbol in enumerate(source_text):
            if i % 60 == 0:
                new_list += '\n$'
            new_list += symbol
        new_list = ''.join(new_list[1:])
        self.textEdit.insertPlainText(''.join(map(str, new_list)))

    def clear(self):
        self.lineEdit.clear()
        self.textEdit.clear()


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
