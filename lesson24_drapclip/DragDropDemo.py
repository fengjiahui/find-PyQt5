"""
让控件支持拖拽动作
A.setDragEnabled(True)

B.setAcceptDrops(True)

B需要2个事件
1、dragEnterEvent    将A拖到B触发
2、dropEvent         在B的区域放下A时触发
"""

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class MycomboBox(QComboBox):
    def __init__(self):
        super(MycomboBox,self).__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        print(e)
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()


    def dropEvent(self, e):
        self.addItem(e.mimeData().text())


class DragDropDemo(QWidget):
    def __init__(self):
        super(DragDropDemo,self).__init__()
        layout = QFormLayout()
        layout.addRow(QLabel('请将左边的文本框拖拽到右边的下拉列表中'))
        linedit = QLineEdit()

        #让控件可拖动
        linedit.setDragEnabled(True)

        combo = MycomboBox()
        layout.addRow(linedit,combo)
        self.setLayout(layout)
        self.setWindowTitle('拖拽案例')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DragDropDemo()
    main.show()
    sys.exit(app.exec_())




