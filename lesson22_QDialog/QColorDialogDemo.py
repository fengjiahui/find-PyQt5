from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys



class QColorDialogDemo(QWidget):
    def __init__(self):
        super(QColorDialogDemo, self).__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('颜色设置对话框实例')
        layout = QVBoxLayout()

        self.colorbutton = QPushButton('设置颜色')
        self.colorbutton.clicked.connect(self.getcolor)
        layout.addWidget(self.colorbutton)

        self.colorbutton1 = QPushButton('设置背景颜色')
        self.colorbutton1.clicked.connect(self.getbcolor)
        layout.addWidget(self.colorbutton1)


        self.colorlabel = QLabel('Hello')
        layout.addWidget(self.colorlabel)

        self.setLayout(layout)


    def getcolor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.WindowText,color)
        self.colorlabel.setPalette(p)

    def getbcolor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.Window, color)
        self.colorlabel.setAutoFillBackground(True)
        self.colorlabel.setPalette(p)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QColorDialogDemo()
    main.show()
    sys.exit(app.exec_())