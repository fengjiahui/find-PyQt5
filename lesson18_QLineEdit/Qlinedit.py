from PyQt5.QtWidgets import *
import sys


class QLinEditEchoMode(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('文本输入框的回显模式')

        formlayout = QFormLayout()
        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnEditLineEdit = QLineEdit()

        formlayout.addRow('Normal',normalLineEdit)
        formlayout.addRow('NoEcho',noEchoLineEdit)
        formlayout.addRow('Password',passwordLineEdit)
        formlayout.addRow('PasswordEchoOnEdit',passwordEchoOnEditLineEdit)

        #输入框中显示内容
        normalLineEdit.setPlaceholderText('Normal')
        noEchoLineEdit.setPlaceholderText('NoEcho')
        passwordLineEdit.setPlaceholderText('Password')
        passwordEchoOnEditLineEdit.setPlaceholderText('PasswordEchoOnEdit')


        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)


        self.setLayout(formlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLinEditEchoMode()
    main.show()
    sys.exit(app.exec_())
