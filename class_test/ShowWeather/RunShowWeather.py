from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from class_test.ShowWeather.showweather import *
import sys
import requests



class ShowWeather(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('天气查询')
        self.pushButton.clicked.connect(self.checkweather)
        self.pushButton_2.clicked.connect(self.cleartext)



    def checkweather(self):
        dic = {'北京':101010100 , '上海':101020100 , '天津':101030100 , '重庆': 101040100}
        city = self.comboBox.currentText()
        url = 'http://www.weather.com.cn/data/sk/{}.html'.format(dic[city])
        rev = requests.get(url)
        rev.encoding = 'utf-8'
        data = rev.json()
        message1 = '城市：{}\n'.format(data['weatherinfo']['city'])
        message2 = '温度：{}\n'.format(data['weatherinfo']['temp'])
        message3 = '风向：{}\n'.format(data['weatherinfo']['WD'])
        message4 = '风速：{}\n'.format(data['weatherinfo']['WS'])
        message5 = '湿度：{}\n'.format(data['weatherinfo']['SD'])
        message = message1 + message2 + message3 +  message4 + message5
        self.textEdit.setText(message)


    def cleartext(self):
        self.textEdit.clear()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ShowWeather()
    main.show()
    sys.exit(app.exec_())