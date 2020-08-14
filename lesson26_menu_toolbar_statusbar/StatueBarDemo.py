import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class StatueBarDemo(QMainWindow):
    def __init__(self):
        super(StatueBarDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('状态栏实例')
        self.resize(500,500)

        menu = self.menuBar()
        file = menu.addMenu('File')
        file.addAction('show')
        file.triggered.connect(self.processTrigger)

        self.setCentralWidget(QTextEdit())
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)


    def processTrigger(self,q):
        if q.text() == 'show':
            self.statusBar.showMessage(q.text()+'菜单被单击了',5000)









if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = StatueBarDemo()
    main.show()
    sys.exit(app.exec_())