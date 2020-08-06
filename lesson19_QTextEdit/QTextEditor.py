from PyQt5.QtWidgets import *
import sys


class QTextEditDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('QTextEdit控件')

        self.textedit = QTextEdit()
        self.buttontext = QPushButton('显示文本')
        self.buttonHTML = QPushButton('显示HTML')
        self.tobuttontext = QPushButton('获取文本')
        self.tobuttonHTML = QPushButton('获取HTML')


        layout = QVBoxLayout()
        layout.addWidget(self.textedit)
        layout.addWidget(self.buttontext)
        layout.addWidget(self.buttonHTML)
        layout.addWidget(self.tobuttontext)
        layout.addWidget(self.tobuttonHTML)

        self.setLayout(layout)
        self.buttontext.clicked.connect(self.onClick_ButtonText)
        self.buttonHTML.clicked.connect(self.onClick_ButtonHTML)
        self.tobuttontext.clicked.connect(self.onClick_toButtonText)
        self.tobuttonHTML.clicked.connect(self.onClick_toButtonHTML)

    def onClick_ButtonText(self):
        self.textedit.setPlainText('hello world')

    def onClick_ButtonHTML(self):
        self.textedit.setHtml('<font color="blue" size="5">hello world</font>')

    def onClick_toButtonText(self):
       print(self.textedit.toPlainText())

    def onClick_toButtonHTML(self):
       print(self.textedit.toHtml())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTextEditDemo()
    main.show()
    sys.exit(app.exec_())