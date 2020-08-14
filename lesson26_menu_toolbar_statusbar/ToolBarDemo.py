"""
工具栏默认按钮：只显示图标，将文本作为悬停提示

"""


import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class ToolDemo(QMainWindow):
    def __init__(self):
        super(ToolDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('工具栏实例')
        self.resize(500,500)



        tb1 = self.addToolBar('File')

        new = QAction(QIcon('./icon7.png'),'new',self)
        tb1.addAction(new)

        open = QAction(QIcon('./icon7.png'),'open',self)
        tb1.addAction(open)

        save = QAction(QIcon('./icon7.png'), 'save', self)
        tb1.addAction(save)


        tb2 = self.addToolBar('File1')
        new1 = QAction(QIcon('./icon7.png'), '新建', self)
        tb2.addAction(new1)

        tb2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        tb1.actionTriggered.connect(self.toolbtnpressed)
        tb2.actionTriggered.connect(self.toolbtnpressed)


    def toolbtnpressed(self,a):
        print(a.text())









if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ToolDemo()
    main.show()
    sys.exit(app.exec_())