"""
对话框  QDilog
QMessageBox   消息对话框
QColorDialog  设置颜色对话框
QFileDialog   设置文件对话框
QFontDialog   设置字体对话框
QInputDialog  用户输入对话框

"""
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class QDialogDemo(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('对话框实例')
        self.resize(300,300)

        self.button = QPushButton(self)
        self.button.setText('弹出对话框')
        self.button.move(100,100)
        self.button.clicked.connect(self.showdialog)





    def showdialog(self):
        dialog = QDialog()
        dialog.setWindowTitle('弹出框')

        button = QPushButton('确定',dialog)
        button.clicked.connect(dialog.close)
        button.move(50,50)

        #设置模式状态(显示时，主窗口不能操作)

        dialog.setWindowModality(Qt.ApplicationModal)


        dialog.exec_()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDialogDemo()
    main.show()
    sys.exit(app.exec_())
