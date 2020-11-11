#!/usr/bin/env python
# coding: utf-8

import sys
from PySide2 import QtCore
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class HelloWorld(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle('Hello, World!')

        label = QLabel('こんにちは、世界！')
        font = QFont()
        font.setPointSize(24)
        label.setFont(font)
        label.setAlignment(QtCore.Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    hello = HelloWorld()
    sys.exit(app.exec_())
