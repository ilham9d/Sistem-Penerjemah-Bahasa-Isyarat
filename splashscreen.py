from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread, QTimer
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QMainWindow
from PyQt5.QtGui import QImage, QPixmap


counter = 0


class Ui_Loading(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 400)

        MainWindow.setWindowFlag(Qt.FramelessWindowHint)
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 700, 400))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 238, 153, 255), stop:1 rgba(240, 145, 50, 255)); border-style:None; border-radius:10px;")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 190, 190))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("lg.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 130, 371, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(195, 78, 18);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 180, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(195, 78, 18);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(50, 320, 601, 23))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    background-color: rgb(255, 238, 153);\n"
"    color: rgb(195, 78, 18);\n"
"    border-style:none;\n"
"    border-radius:10px;\n"
"    text-align:center;\n"
"}\n"
"QProgressBar::chunk{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(240, 145, 50, 255), stop:0.98 rgba(255, 199, 121, 255), stop:1 rgba(0, 0, 0, 0));\n"
"    border-radius:10px;\n"
"    border-style:none;\n"
"}")

        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(240, 344, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(195, 78, 18);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #     self.counter = 0
    #     self.timer = QtCore.QTimer()
    #     self.timer.timeout.connect(self.progress)
    #     self.timer.start(35)

    # def progress(self):

    #     # global counter

    #     self.new = 0

    #     self.progressBar.setValue(self.counter)

    #     if self.counter > 100:
    #         print(self.counter)
    #         self.timer.stop()

    #     self.counter += 1

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>APLIKASI <span style=\" font-weight:400;\">PENERJEMAH</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>BAHASA <span style=\" font-weight:400;\">ISYARAT</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>LOADING <span style=\" font-weight:400;\">APP</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Loading()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())