#显示控件提示信息

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QHBoxLayout,QWidget,QPushButton,QToolTip
from PyQt5.QtGui import QFont

class tooltip(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SanSerif' , 12))
        self.setToolTip('今天是<b>星期五</b>')
        self.setGeometry(300,30,200,300)
        self.setWindowTitle('显示控件提示消息')

        self.button1 = QPushButton('我的按钮')
        self.button1.setToolTip('我是一个可爱的按钮')

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = tooltip()
    main.show()
    sys.exit(app.exec_())