from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread, QTimer

from splashscreen import Ui_Loading
from howto import Ui_Howto
from new_gui_baru import Ui_MainWindow


class Loading(QtWidgets.QMainWindow, Ui_Loading):
    def __init__(self, parent =None):
        super(Loading, self).__init__(parent)
        self.setupUi(self)

class Howto(QtWidgets.QMainWindow, Ui_Howto):
    def __init__(self, parent =None):
        super(Howto, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.hide)


class Main_Page(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main_Page, self).__init__(parent)
        self.setupUi(self)
        self.actionHow_to_use.triggered.connect(self.hide)

      
class Manager:
    def __init__(self):
        self.first = Loading()
        self.second = Main_Page()
        self.third = Howto()

        self.first.show()

        self.counter = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(30)

        self.second.actionHow_to_use.triggered.connect(self.third.show)
        self.third.pushButton_3.clicked.connect(self.second.show)

    def progress(self):

        self.first.progressBar.setValue(self.counter)

        if self.counter == 100:
            print(self.counter)
            self.timer.stop()
            self.first.hide()
            self.second.show()

        self.counter += 1


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manager = Manager()
    sys.exit(app.exec_())
