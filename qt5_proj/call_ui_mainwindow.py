import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainForm import Ui_MainWindow

class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywin = MyMainForm()
    mywin.show()
    sys.exit(app.exec_())