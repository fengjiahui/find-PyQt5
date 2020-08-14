import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class MenuDemo(QMainWindow):
    def __init__(self):
        super(MenuDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('菜单实例')
        menu = QMenuBar(self)

        file = menu.addMenu('文件')
        file.addAction('新建')

        save = QAction('保存',self)
        #设置快捷键
        save.setShortcut('Ctrl+S')
        file.addAction(save)

        quit = QAction('退出',self)
        file.addAction(quit)


        save.triggered.connect(self.process)

        edit = menu.addMenu('Edit')
        edit.addAction('copy')
        edit.addAction('paste')






    def process(self):
        print(self.sender().text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MenuDemo()
    main.show()
    sys.exit(app.exec_())

