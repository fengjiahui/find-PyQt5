from lesson12_singalslot.singal import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow




if __name__ == '__main__':


    # 实例化QApplication对象
    app = QApplication(sys.argv)

    # 实例化主窗口对象
    mainWindow = QMainWindow()

    # 实例化Qtdesigner界面对象
    ui = Ui_MainWindow()
    # 调用对象的方法
    ui.setupUi(mainWindow)

    # 展示窗口
    mainWindow.show()
    sys.exit(app.exec_())