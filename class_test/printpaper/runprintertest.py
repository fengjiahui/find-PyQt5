import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from class_test.printpaper.printertest import *



class runprintertest(QWidget,Ui_Form):
    help_singer = pyqtSignal(str)
    print_singer = pyqtSignal(list)
    preview_singer = pyqtSignal([int,str],[str])


    def __init__(self):
        super(runprintertest,self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.help_singer.connect(self.ShowHelpMessage)
        self.print_singer.connect(self.printPaper)
        self.preview_singer[str].connect(self.previewPaper)
        self.preview_singer[int,str].connect(self.previewPaperWithArgs)

        self.printpushButton.clicked.connect(self.emitPrintSinger)
        self.preiviewpushButton.clicked.connect(self.emitPreviwSinger)



    def emitPreviwSinger(self):
        if self.checkBox.isChecked() == True:
            self.preview_singer[int,str].emit(1080,'Full Screen')
        else:
            self.preview_singer[str].emit('Preview')


    def emitPrintSinger(self):
        pList = []
        pList.append(self.numberspinBox.value())
        pList.append(self.stylecomboBox.currentText())
        self.print_singer.emit(pList)


    def printPaper(self,list):
        self.resultlabel.setText("打印：" + "份数：" + str(list[0]) + "纸张：" + str(list[1]))


    def previewPaperWithArgs(self,style,text):
        self.resultlabel.setText(str(style)+ text)

    def previewPaper(self,text):
        self.resultlabel.setText(text)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F1:
            self.help_singer.emit('help message')

    def ShowHelpMessage(self,message):
        self.resultlabel.setText(message)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = runprintertest()
    demo.show()
    sys.exit(app.exec_())


