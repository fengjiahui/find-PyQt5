import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class huashua(QWidget):
    def __init__(self):
        super(huashua,self).__init__()
        self.resize(800,800)
        self.setWindowTitle('用画刷填充图形区域')


    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        brush = QBrush(Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawRect(100,100,100,100)

        brush = QBrush(Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawRect(200, 200, 100, 100)

        brush = QBrush(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRect(300, 300, 100, 100)

        brush = QBrush(Qt.Dense3Pattern)
        qp.setBrush(brush)
        qp.drawRect(400, 400, 100, 100)

        brush = QBrush(Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawRect(500, 500, 100, 100)

        qp.end()







if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = huashua()
    main.show()
    sys.exit(app.exec_())