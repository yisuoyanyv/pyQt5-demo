import sys
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from Weather_ui import *

import requests


class MainDailog(QDialog):
    def __init__(self, parent=None) -> None:
        super(QDialog,self).__init__(parent)
        self.ui =Ui_Dialog()
        self.ui.setupUi(self)
    def queryWeather(self):
        cityName = self.ui.comboBox.currentText()
        cityCode = self.getCode(cityName)
        key="d5a45fa3b3de96cc42f7c43c3833e675"
        url="https://restapi.amap.com/v3/weather/weatherInfo?key={}&city={}".format(

                key,cityCode)
        print(url)
        r = requests.get(url)
        if r.status_code == 200:
            print(r.json())
            data = r.json()['lives'][0]
            weatherMsg = '城市：{}\n天气：{}\n温度：{}\n风向：{}\n风力：{}\n湿度：{}\n发布时间：{}\n'.format(

                data['city'],

                data['weather'],

                data['temperature'],

                data['winddirection'],

                data['windpower'],

                data['humidity'],

                data['reporttime'],

            )

        else:
             weatherMsg = '天气查询失败，请稍后再试！'
        self.ui.textEdit.setText(weatherMsg)
    def getCode(self, cityName):
        cityDict = {
                    "嘉定区":"310114",                   
                    "上海": "310000",
                    "苏州": "320500",
                    "北京": "110000"}
        return cityDict.get(cityName,'101010100')
    def clearText(self):
        self.ui.textEdit.clear()
        
def window():
    app = QApplication(sys.argv)
    
    myDlg = MainDailog()
    myDlg.show()
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    window()
