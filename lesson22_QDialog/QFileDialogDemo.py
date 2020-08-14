from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys



class QFileDialogDemo(QWidget):

    def __init__(self):
        super(QFileDialogDemo, self).__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('文件对话框实例')
        layout = QVBoxLayout()
        self.button1 = QPushButton('加载图片')
        self.button1.clicked.connect(self.loadimage)
        layout.addWidget(self.button1)


        self.imagelabel = QLabel()
        layout.addWidget(self.imagelabel)


        self.button2 = QPushButton('加载文本文件')
        self.button2.clicked.connect(self.loadtext)
        layout.addWidget(self.button2)

        self.textedit = QTextEdit()
        layout.addWidget(self.textedit)

        self.setLayout(layout)


    def loadimage(self):
        fname,_ =QFileDialog.getOpenFileName(self,'打开文件','.','图像文件(*.jpg *.png)')
        self.imagelabel.setPixmap(QPixmap(fname))


    def loadtext(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)


        if dialog.exec_():
            filenames = dialog.selectedFiles()
            f = open(filenames[0],encoding='utf-8',mode='r')
            with f:
                data = f.read()
                self.textedit.setText(data)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFileDialogDemo()
    main.show()
    sys.exit(app.exec_())
