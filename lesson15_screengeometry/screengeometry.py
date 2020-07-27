import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QHBoxLayout,QWidget,QPushButton



def onClick_button():
    print('--------')
    print('widget.x(%d)' % widget.x())                      #窗口横坐标
    print('widget.y(%d)' % widget.y())                      #窗口纵坐标
    print('widget.width(%d)' % widget.width())              #工作区宽度
    print('widget.height(%d)' % widget.height())            #工作区高度
    print('-----------------------')
    print('widget.geometry().x(%d)' % widget.geometry().x())            #工作区横坐标
    print('widget.geometry().y(%d)' % widget.geometry().y())            #工作区纵坐标
    print('widget.geometry().width(%d)' % widget.geometry().width())    #工作区宽度
    print('widget.geometry().height(%d)' % widget.geometry().height())  #工作区高度
    print('-------')
    print('widget.frameGeometry().x(%d)' % widget.frameGeometry().x())               #窗口横坐标
    print('widget.frameGeometry().y(%d)' % widget.frameGeometry().y())               #窗口纵坐标
    print('widget.frameGeometry().width(%d)' % widget.frameGeometry().width())       #窗口宽度
    print('widget.frameGeometry().height(%d)' % widget.frameGeometry().height())     #窗口高度






app = QApplication(sys.argv)

widget = QWidget()

btn = QPushButton(widget)
btn.setText('按钮')
btn.clicked.connect(onClick_button)

btn.move(50,50)

#设置工作区的尺寸
widget.resize(400,300)

widget.move(300,300)

widget.setWindowTitle('屏幕坐标系')

widget.show()

sys.exit(app.exec_())


