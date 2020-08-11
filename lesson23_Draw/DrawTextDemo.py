from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys



class QDrawTextDemo(QWidget):
    def __init__(self):
        super(QDrawTextDemo, self).__init__()
        self.setWindowTitle('颜色设置对话框实例')
        self.resize(300,300)
        self.text = 'hello'

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.begin(self)
        print('aaaa')
        painter.setPen(QColor(150,43,5))
        painter.setFont(QFont('SimSun',25))

        painter.drawText(event.rect(),Qt.AlignCenter,self.text)
        painter.end()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDrawTextDemo()
    main.show()
    sys.exit(app.exec_())