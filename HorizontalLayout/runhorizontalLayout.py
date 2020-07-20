from HorizontalLayout.horizontalLayout import Ui_MainWindow
import sys

from PyQt5.QtWidgets import QApplication,QMainWindow


if __name__ == '__main__':
    # 创建QApplication类的实例
    app = QApplication(sys.argv)

    # 创建一个窗口
    mainWindow = QMainWindow()

    #实例化Qtdesigner界面对象
    ui = Ui_MainWindow()

    #调用对象的方法
    ui.setupUi(mainWindow)

    #展示窗口
    mainWindow.show()
    sys.exit(app.exec_())




