from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

"""
下拉列表控件
1、如何将列表添加到QComboBox控件中
2、如何获取选中的列表项
"""






class QComboBoxDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('下拉列表控件实例')
        self.resize(300,100)

        layout = QVBoxLayout()

        self.label = QLabel('请选择变成语言')
        self.cb = QComboBox()
        self.cb.addItem('c++')
        self.cb.addItem('python')
        self.cb.addItems(['java','ruby','go'])

        self.cb.currentIndexChanged.connect(self.selectionChange)

        layout.addWidget(self.label)
        layout.addWidget(self.cb)

        self.setLayout(layout)



    def selectionChange(self,i):
        self.label.setText(self.cb.currentText())
        self.label.adjustSize()


        for count in range(self.cb.count()):
            print('item' + str(count) + '=' + self.cb.itemText(count))

        print('current index', i, 'selection changed', self.cb.currentText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QComboBoxDemo()
    main.show()
    sys.exit(app.exec_())




