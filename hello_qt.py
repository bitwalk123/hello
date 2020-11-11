#!/usr/bin/env python
# coding: utf-8

import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class HelloWorld(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Hello, World!')

        label = QLabel('こんにちは、世界！')
        font = QFont()
        font.setPointSize(16)
        label.setFont(font)
        label.setAlignment(QtCore.Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    hello = HelloWorld()
    sys.exit(app.exec_())
