import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QCheckBoxDemo(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('复选框实例')
        layout = QHBoxLayout()


        self.checkbox1 = QCheckBox('复选框1')
        self.checkbox1.setChecked(True)
        self.checkbox1.stateChanged.connect(lambda:self.checkboxState(self.checkBox1))
        layout.addWidget(self.checkbox1)

        self.checkbox2 = QCheckBox('复选框2')
        self.checkbox2.stateChanged.connect(lambda: self.checkboxState(self.checkBox2))
        layout.addWidget(self.checkbox2)

        self.checkBox3 = QCheckBox('半选中')
        self.checkBox3.stateChanged.connect(lambda: self.checkboxState(self.checkBox3))
        self.checkBox3.setTristate(True)
        self.checkBox3.setCheckState(Qt.PartiallyChecked)
        layout.addWidget(self.checkBox3)

        self.setLayout(layout)

    def checkboxState(self, cb):
        check1Status = self.checkBox1.text() + ', isChecked=' + str(self.checkBox1.isChecked()) + ',checkState=' + str(self.checkBox1.checkState()) + '\n'
        check2Status = self.checkBox2.text() + ', isChecked=' + str(self.checkBox2.isChecked()) + ',checkState=' + str(self.checkBox2.checkState()) + '\n'
        check3Status = self.checkBox3.text() + ', isChecked=' + str(self.checkBox3.isChecked()) + ',checkState=' + str(self.checkBox3.checkState()) + '\n'
        print(check1Status + check2Status + check3Status)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QCheckBoxDemo()
    main.show()
    sys.exit(app.exec_())




