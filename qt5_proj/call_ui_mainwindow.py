import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtChart import QBarSet,QBarCategoryAxis,QBarSeries,QChart,QChartView
from mainForm import Ui_MainWindow


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
    
    def create_bar_chart(self):
        set0 = QBarSet('Jane')
        set1 = QBarSet('John')
        series = QBarSeries()
        axis = QBarCategoryAxis()
        chart = QChart()
        
        categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

        set0.append([1, 2, 3, 4, 5, 6])
        set1.append([5, 0, 0, 4, 0, 7])
        series.append(set0)
        series.append(set1)
        chart.addSeries(series)
        axis.append(categories)

        chart.setTitle('Simple barchart example')
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)
        return chart

def GetSystemDefinitionToChangeFontSizeAndLabelSize(form):
    # 获取系统分辨率更改 label 尺寸及字体大小
    # 先设定各个 label 字体不同颜色
    form.label_2.setStyleSheet("QLabel{color: red}")
    form.label_4.setStyleSheet("QLabel{color:blue}")
    form.label_6.setStyleSheet("QLabel{color:pink}")
    form.label_9.setStyleSheet("QLabel{color:green}")
    form.label_7.setStyleSheet("QLabel{color:purple}")
    # 从系统分辨率中提取桌面高度
    height = QApplication.desktop().screenGeometry().height()
    # 高度小于 800，字体及高度都修改为20
    if height <= 800:
        form.frame.setMinimumSize(QtCore.QSize(230, 520))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(50)
        labels = ('label_2', 'label_4', 'label_6', 'label_7', 'label_9')
        for label_name in labels:
            label = form.frame.findChild((QtWidgets.QLabel), label_name)
            label.setFont(font)
            label.setMinimumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        labels = ('label', 'label_3', 'label_5', 'label_8')
        for label_name in labels:
            label = form.frame.findChild((QtWidgets.QLabel), label_name)
            label.setFont(font)
            label.setMinimumSize(QtCore.QSize(16777215, 20))

# def AddQtChartsIntoMainForm(form):
#     # 增加图表项目到主窗口
#     # main code here

#     # example code here



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywin = MyMainForm()
    GetSystemDefinitionToChangeFontSizeAndLabelSize(mywin)
    charview = QChartView(mywin.create_bar_chart(), mywin.frame_2)
    print(str(mywin.tab_3.height()) + " width:" + str(mywin.tab_3.width()))
    charview.setGeometry(0,0, mywin.tab_3.width(),mywin.tab_3.height())
    mywin.show()
    sys.exit(app.exec_())
