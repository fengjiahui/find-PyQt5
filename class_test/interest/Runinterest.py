from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from class_test.interest.interest import *
import sys



class Runiterest(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('复利计算')
        self.pushButton.clicked.connect(self.cale)



    def cale(self):
        benjin = int(self.doubleSpinBox.value())
        lilv = int(self.doubleSpinBox_2.value())
        year = int(self.spinBox.value())
        money = benjin * ((1 + lilv/100) ** year)
        self.label_5.setText(str(money))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Runiterest()
    main.show()
    sys.exit(app.exec_())
