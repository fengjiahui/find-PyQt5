import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class CalendarDemo(QWidget):
    def __init__(self):
        super(CalendarDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.cal = QCalendarWidget(self)
        self.cal.setMinimumDate(QDate(1966,1,1))
        self.cal.setMaximumDate(QDate(2388,12,31))


        self.cal.setGridVisible(True)   #设置格栅
        self.cal.move(20,20)
        self.cal.clicked.connect(self.showDate)

        self.label = QLabel(self)
        self.label.move(20,300)
        date = self.cal.selectedDate()
        self.label.setText(date.toString('yyyy-MM-dd dddd'))
        self.resize(400,350)




    def showDate(self,date):
        self.label.setText(date.toString('yyyy-MM-dd dddd'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CalendarDemo()
    main.show()
    sys.exit(app.exec_())


