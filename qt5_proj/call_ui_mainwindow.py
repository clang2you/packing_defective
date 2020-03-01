import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui, QtCore, QtWidgets
# from PyQt5.QtCore import QPointF
# from PyQt5.QtChart import QLineSeries, QValueAxis, QChart, QChartView
from mainForm import Ui_MainWindow
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use("Qt5Agg")

# class Figure_Canvas(FigureCanvas):

#     def __init__(self, parent=None, width=11, height=5, dpi=100):
#         fig = Figure(figsize=(width, height), dpi=100)

#         FigureCanvas.__init__(self, fig)
#         self.setParent(parent)
#         self.axes = fig.add_subplot(111)
    
#     def test(self):
#         x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#         y = [23, 21, 32, 13, 3, 132, 13, 3, 1]
#         self.axes.plot(x, y)

class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
    
    def plot_(self):
        ax = self.figure.add_axes([0.1, 0.1, 0.8, 0.8])
        x = ["08:00", '09:00', '10:00', '11:00', '12: 00', '13:00', '14:00', '15:00', '16:00', '17:00']
        y = [105, 165, 143, 201, 225, 264, 312, 305, 270, 120]
        ax.plot(x, y, marker='o')
        for xy in zip(x, y):
            plt.annotate("%s,回收量：%s" % xy, xy=xy, xytext=(-20, 10), textcoords='offset points')
        ax.set_title('各时段回收率',fontsize='18',fontweight='bold', color='black',loc ='left')
        self.canvas.draw()
    # def create_bar_chart(self):
    #     self.m_chart = QChart()
    #     self.m_series = QLineSeries()
    #     self.point_0 = QPointF(0.00, 0.00)
    #     self.point_1 = QPointF(0.80, 6.00)
    #     self.point_2 = QPointF(2.00, 2.00)
    #     self.point_3 = QPointF(4.00, 3.00)
    #     self.point_4 = QPointF(1.00, 3.00)
    #     self.point_5 = QPointF(5.00, 3.00)
    #     self.points_list = [self.point_0, self.point_1, self.point_2,
    #                         self.point_3, self.point_3, self.point_4, self.point_5]
    #     self.m_series.append(self.points_list)
    #     self.m_series.setName("折线一")

    #     self.x_Aix = QValueAxis()  # 定义x轴，实例化
    #     self.x_Aix.setRange(0.00, 5.00)
    #     self.x_Aix.setLabelFormat("%0.2f")  # 设置坐标轴坐标显示方式，精确到小数点后两位
    #     self.x_Aix.setTickCount(6)
    #     self.x_Aix.setMinorTickCount(0)  # 设置每个单元格有几个小的分级

    #     self.y_Aix = QValueAxis()  # 定义y轴
    #     self.y_Aix.setRange(0.00, 6.00)
    #     self.y_Aix.setLabelFormat("%0.2f")
    #     self.y_Aix.setTickCount(7)
    #     self.y_Aix.setMinorTickCount(0)

    #     self.m_chart.addSeries(self.m_series)
    #     self.m_chart.setAxisX(self.x_Aix)
    #     self.m_chart.setAxisY(self.y_Aix)
    #     self.m_chart.createDefaultAxes()
    #     self.m_chart.setTitle("Simple line chart example")
    #     self.m_chart.theme = QChart.ChartThemeDark

    #     return self.m_chart


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
    if height <= 1070:
        form.resize(1000, 700)
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
    # dr = Figure_Canvas()
    # dr.test()
    # graphicscene = QtWidgets.QGraphicsScene()
    # graphicscene.addWidget(dr)
    # mywin.graphicsView.setScene(graphicscene)
    GetSystemDefinitionToChangeFontSizeAndLabelSize(mywin)
    mywin.show()
    mywin.verticalLayout_5.addWidget(mywin.canvas)
    mywin.plot_()
    # mywin.frame_2.addWidget(mywin.canvas)
    # mywin.plot_()
    # charview = QChartView(mywin.create_bar_chart(), mywin.frame_2)
    # charview.setRenderHint(QtGui.QPainter.Antialiasing)
    # charview.setGeometry(0, 0, mywin.frame_2.width(), mywin.frame_2.height())
    # charview.show()
    # print(str(mywin.frame_2.width()) + ":" + str(mywin.frame_2.height()))
    sys.exit(app.exec_())
