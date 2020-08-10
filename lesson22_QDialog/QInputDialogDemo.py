from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class QInputDialogDemo(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('输入对话框实例')
        self.resize(300,300)
        layout = QFormLayout()

        self.button1 = QPushButton('获取列表的选项')
        self.button1.clicked.connect(self.getItem)
        self.linEdit1 = QLineEdit()
        layout.addRow(self.button1,self.linEdit1)

        self.button2 = QPushButton('获取字符串')
        self.button2.clicked.connect(self.getStr)
        self.linEdit2 = QLineEdit()
        layout.addRow(self.button2, self.linEdit2)

        self.button3 = QPushButton('获取整数')
        self.button3.clicked.connect(self.getInt)
        self.linEdit3 = QLineEdit()
        layout.addRow(self.button3, self.linEdit3)

        self.setLayout(layout)


    def getItem(self):
        items = ('C','C++','Ruby','Python','Java')
        item , ok =QInputDialog.getItem(self,'请选择编程语言','语言列表',items)
        if ok and item:
            self.linEdit1.setText(item)

    def getStr(self):
        text , ok =QInputDialog.getText(self,'文本输入框','输入姓名')
        if ok and text:
            self.linEdit2.setText(text)

    def getInt(self):
        num , ok =QInputDialog.getInt(self,'整数输入框','输入数字')
        if ok and num:
            self.linEdit3.setText(str(num))









if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QInputDialogDemo()
    main.show()
    sys.exit(app.exec_())