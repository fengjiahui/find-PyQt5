import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self):
        # super(FirstMainWin,self).__init__()
        super().__init__()

        #设置主窗口标题
        self.setWindowTitle('第一个主窗口应用')

        #设置窗口尺寸
        self.resize(400,300)

        self.status  = self.statusBar()
        self.status.showMessage('只存在5秒',5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./icon1.png'))
    main = FirstMainWin()
    main.show()
    sys.exit(app.exec_())


