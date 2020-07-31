import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
from PyQt5.QtGui import QPalette,QPixmap
from PyQt5.QtCore import Qt

class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #生成4个QLabel控件

        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)
        #label1设置文本内容
        label1.setText('<font color=yellow>这是一个文本标签.</font>')
        #label1设备背景颜色
        label1.setAutoFillBackground(True)
        patette = QPalette()
        patette.setColor(QPalette.Window,Qt.lightGray)
        label1.setPalette(patette)
        #设置文本居中
        label1.setAlignment(Qt.AlignCenter)


        #label2设置文本，文本是超链接形式的
        label2.setText("<a href='#'>欢迎使用python GUI程序</a> ")



        #label3设置居中，设置控件提示信息，设置图片
        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap('./icon2.png'))

        #label4超链接打开
        label4.setOpenExternalLinks(True)
        label4.setText("<a href='https://www.jd.com'>欢迎来到京东</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是京东的超链接')

        #设置垂直布局
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        #槽的绑定
        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)
        self.setWindowTitle('QLabel控件演示')

    def linkHovered(self):
        print('当鼠标划过label2标签时，触发时间')


    def linkClicked(self):
        print("当鼠标单机label4标签时，触发事件")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())