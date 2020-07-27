import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QHBoxLayout,QWidget,QPushButton



class quitApplication(QMainWindow):
    def __init__(self):
        super(quitApplication,self).__init__()

        self.resize(400,300)
        self.setWindowTitle('按键退出应用程序')

        #添加按钮

        self.button1 = QPushButton('退出应用程序')

        #将信号与槽关联
        self.button1.clicked.connect(self.onClick_button)
        #添加水平布局，在布局中加入按钮
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        #创建主界面，将布局放进主界面
        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)


    #按钮单机事件的方法（自定义的槽）
    def onClick_button(self):
        sender = self.sender()
        print(sender.text()+'按钮被按下')
        app  = QApplication.instance()
        #退出应用程序
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = quitApplication()
    main.show()
    sys.exit(app.exec_())
