"""
消息对话框 QMessageBox

1、关于对话框
2、错误对话框
3、警告对话框
4、提问对话框
5、消息对话框


有2点差异
1、显示的对话框图标可能不同

2、显示的按钮不一样
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class QMessageBoxDemo(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('消息对话框实例')
        self.resize(700,700)


        layout = QVBoxLayout()
        self.button1 = QPushButton(self)
        self.button1.setText('显示关于对话框')
        self.button1.clicked.connect(self.showdialog)
        layout.addWidget(self.button1)

        self.button2 = QPushButton(self)
        self.button2.setText('显示警告对话框')
        self.button2.clicked.connect(self.showdialog)
        layout.addWidget(self.button2)

        self.button3 = QPushButton(self)
        self.button3.setText('显示错误对话框')
        self.button3.clicked.connect(self.showdialog)
        layout.addWidget(self.button3)

        self.button4 = QPushButton(self)
        self.button4.setText('显示提问对话框')
        self.button4.clicked.connect(self.showdialog)
        layout.addWidget(self.button4)

        self.button5 = QPushButton(self)
        self.button5.setText('显示消息对话框')
        self.button5.clicked.connect(self.showdialog)
        layout.addWidget(self.button5)



        self.setLayout(layout)


    def showdialog(self):
        text = self.sender().text()
        if text == '显示关于对话框':
            QMessageBox.about(self,'关于','这是一个关于对话框')
        elif text == '显示警告对话框':
            QMessageBox.warning(self, '警告', '这是一个警告对话框',QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        elif text == '显示错误对话框':
            QMessageBox.critical(self, '错误', '这是一个错误对话框', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        elif text == '显示提问对话框':
            QMessageBox.question(self, '提问', '这是一个提问对话框', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        elif text == '显示消息对话框':
            repaly = QMessageBox.information(self, '消息', '这是一个消息对话框', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            print(repaly == QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QMessageBoxDemo()
    main.show()
    sys.exit(app.exec_())
