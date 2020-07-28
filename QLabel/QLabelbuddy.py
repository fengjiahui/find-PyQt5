from PyQt5.QtWidgets import *
import sys



class QLabelbuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('QLabel与伙伴控件')

        label1 = QLabel('&name',self)
        linedit1 = QLineEdit(self)
        #设置伙伴控件
        label1.setBuddy(linedit1)

        label2 = QLabel('&password', self)
        linedit2 = QLineEdit(self)
        # 设置伙伴控件
        label2.setBuddy(linedit2)

        btn1 = QPushButton('OK')
        btn2 = QPushButton('Cancel')

        mainlayout = QGridLayout(self)
        mainlayout.addWidget(label1,0,0)
        mainlayout.addWidget(linedit1,0,1,1,2)

        mainlayout.addWidget(label2,1,0)
        mainlayout.addWidget(linedit2,1,1,1,2)

        mainlayout.addWidget(btn1,2,1)
        mainlayout.addWidget(btn2,2,2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelbuddy()
    main.show()
    sys.exit(app.exec_())
