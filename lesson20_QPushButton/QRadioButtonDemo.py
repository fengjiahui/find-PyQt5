from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class QRadioButtonDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('选择框按钮实例')
        layout = QHBoxLayout()
        self.radiobutton1 = QRadioButton('单选按钮1')
        self.radiobutton1.setChecked(True)

        self.radiobutton1.toggled.connect(self.buttonstate)
        layout.addWidget(self.radiobutton1)

        self.radiobutton2 = QRadioButton('单选按钮2')


        self.radiobutton2.toggled.connect(self.buttonstate)
        layout.addWidget(self.radiobutton2)

        self.setLayout(layout)


    def buttonstate(self):
        radiobutton = self.sender()

        if radiobutton.isChecked() == True:
            print('<'+radiobutton.text()+'>被选中')
        else:
            print('<' + radiobutton.text() + '>被取消')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QRadioButtonDemo()
    main.show()
    sys.exit(app.exec_())


