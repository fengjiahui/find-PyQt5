from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp
import sys




class QLineEditValidator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('输入校验器')

        #创建表单布局
        formlayout = QFormLayout()

        #创建3个QlineEdit控件
        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        validatorLineEdit = QLineEdit()


        formlayout.addRow("整数类型",intLineEdit)
        formlayout.addRow("浮点类型",doubleLineEdit)
        formlayout.addRow("数字和字母",validatorLineEdit)

        intLineEdit.setPlaceholderText('整型')
        doubleLineEdit.setPlaceholderText('浮点型')
        validatorLineEdit.setPlaceholderText('字母和数字')

        #设置整数校验器
        intvalidate = QIntValidator(self)
        intvalidate.setRange(1,99)


        #设置浮点数校验器[-360,360],精度：小数点后两位
        doublevalidate = QDoubleValidator(self)
        doublevalidate.setRange(-360,360)
        doublevalidate.setNotation(QDoubleValidator.StandardNotation)

        #设置精度，小数点2位
        doublevalidate.setDecimals(2)

        #设置字符和数字校验器
        reg = QRegExp('[a-zA-z0-9]+$')
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)


        #设置校验器
        intLineEdit.setValidator(intvalidate)
        doubleLineEdit.setValidator(doublevalidate)
        validatorLineEdit.setValidator(validator)

        self.setLayout(formlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditValidator()
    main.show()
    sys.exit(app.exec_())







