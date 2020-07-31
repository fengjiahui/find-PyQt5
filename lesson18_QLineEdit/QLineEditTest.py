from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys




class QLineEidtTest(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        #edit1--整数校验
        edit1 = QLineEdit()
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(4)  #不超过9999
        edit1.setAlignment(Qt.AlignRight)
        edit1.setFont(QFont('Arial',20))

        #edit2--浮点数校验
        edit2 = QLineEdit()
        edit2.setValidator(QDoubleValidator(0.99,99.99,2))

        #edit3--掩码
        edit3 = QLineEdit()
        edit3.setInputMask('99_9999_999999;#')

        #edit4--
        edit4 = QLineEdit()
        edit4.textChanged.connect(self.textchanged)

        #edit5--
        edit5 = QLineEdit()
        edit5.setEchoMode(QLineEdit.Password)
        edit5.editingFinished.connect(self.enterPress)

        #edit6--
        edit6 = QLineEdit('Hello world')
        edit6.setReadOnly(True)


        formLayout = QFormLayout()
        formLayout.addRow('整数校验',edit1)
        formLayout.addRow('浮点数校验',edit2)
        formLayout.addRow('掩码限制',edit3)
        formLayout.addRow('文本变化',edit4)
        formLayout.addRow('密码',edit5)
        formLayout.addRow('只读',edit6)

        self.setLayout(formLayout)
        self.setWindowTitle('QLineEdit综合案例')

    def textchanged(self,text):
        print('输入的内容：' + text)

    def enterPress(self):
        print('已输入值')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEidtTest()
    main.show()
    sys.exit(app.exec_())