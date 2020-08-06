from PyQt5.QtWidgets import *
import sys

class QPushButtonDemo(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('按键实例')

        layout = QVBoxLayout

        self.button1 = QPushButton('第一个按钮')
        self.button1.setCheckable(True)           #设置按钮可选择
        self.button1.toggle()


    def whichButton(self):