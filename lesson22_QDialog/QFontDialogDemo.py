from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys



class QFontDialogDemo(QWidget):
    def __init__(self):
        super(QFontDialogDemo, self).__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('字体设置对话框实例')
        layout = QVBoxLayout()

        self.fontbutton = QPushButton('设置字体')
        self.fontbutton.clicked.connect(self.getfont)
        layout.addWidget(self.fontbutton)

        self.fontlabel = QLabel('Hello')
        layout.addWidget(self.fontlabel)

        self.setLayout(layout)


    def getfont(self):
        font ,ok = QFontDialog.getFont()
        if ok :
            self.fontlabel.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFontDialogDemo()
    main.show()
    sys.exit(app.exec_())

