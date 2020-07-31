import sys
from PyQt5.QtWidgets import *

class QLinEditMask(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('用掩码限制QLineEdit控件的输入')
        formlayout = QFormLayout()


        ipLineEdit = QLineEdit()
        macLineEdit = QLineEdit()
        dateLineEdit = QLineEdit()
        licenseLineEdit = QLineEdit()

        #192.168.1.100
        ipLineEdit.setInputMask('000.000.000.000;_')
        macLineEdit.setInputMask('HH:HH:HH:HH:HH:H;_')
        dateLineEdit.setInputMask('0000-00-00')
        licenseLineEdit.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#')

        formlayout.addRow('ip掩码',ipLineEdit)
        formlayout.addRow('Mac掩码',macLineEdit)
        formlayout.addRow('日期掩码',dateLineEdit)
        formlayout.addRow('许可证掩码',licenseLineEdit)

        
        self.setLayout(formlayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLinEditMask()
    main.show()
    sys.exit(app.exec_())