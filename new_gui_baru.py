import weka.core.jvm as jvm

from weka.classifiers import Classifier
from weka.classifiers import Evaluation
from weka.core.classes import Random
import weka.core.converters as converters
from weka.core.dataset import create_instances_from_lists, Attribute, Instances, Instance

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QMainWindow
from PyQt5.QtGui import QImage, QPixmap
import numpy as np
import cv2
import sys

from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime
from acquisitionKinect import AcquisitionKinect
from frame import Frame

from src.hand_tracker import HandTracker

WINDOW = "Hand Tracking"
PALM_MODEL_PATH = "models/palm_detection_without_custom_op.tflite"
LANDMARK_MODEL_PATH = "models/hand_landmark.tflite"
ANCHORS_PATH = "models/anchors.csv"

POINT_COLOR = (0, 255, 0)
CONNECTION_COLOR = (255, 0, 0)
THICKNESS = 2

connections = [
    (0, 1), (1, 2), (2, 3), (3, 4),
    (5, 6), (6, 7), (7, 8),
    (9, 10), (10, 11), (11, 12),
    (13, 14), (14, 15), (15, 16),
    (17, 18), (18, 19), (19, 20),
    (0, 5), (5, 9), (9, 13), (13, 17), (0, 17)
]

detector = HandTracker(
    PALM_MODEL_PATH,
    LANDMARK_MODEL_PATH,
    ANCHORS_PATH,
    box_shift=0.2,
    box_enlarge=1.3
)

def keypoints(data_frame):
    image = cv2.cvtColor(data_frame, cv2.COLOR_BGR2RGB)
    points_x, points_y = [],[]
    points, _ = detector(image)
    if points is not None:
        for point in points:
            x, y = point
            points_x.append(x)
            points_y.append(y)

    return data_frame, points_x, points_y, points

def create_dataset(list):
    att0 = Attribute.create_numeric("num0")
    att1 = Attribute.create_numeric("num1") 
    att2 = Attribute.create_numeric("num2")
    att3 = Attribute.create_numeric("num3")
    att4 = Attribute.create_numeric("num4")
    att5 = Attribute.create_numeric("num5")
    att6 = Attribute.create_numeric("num6")
    att7 = Attribute.create_numeric("num7")
    att8 = Attribute.create_numeric("num8")
    att9 = Attribute.create_numeric("num9")
    att10 = Attribute.create_numeric("num10")
    att11 = Attribute.create_numeric("num11")
    att12 = Attribute.create_numeric("num12")
    att13 = Attribute.create_numeric("num13")
    att14 = Attribute.create_numeric("num14")
    att15 = Attribute.create_numeric("num15")
    att16 = Attribute.create_numeric("num16")
    att17 = Attribute.create_numeric("num17")
    att18 = Attribute.create_numeric("num18")
    att19 = Attribute.create_numeric("num19")
    att20 = Attribute.create_numeric("num20")
    att21 = Attribute.create_numeric("num21")
    att22 = Attribute.create_numeric("num22")
    att23 = Attribute.create_numeric("num23")
    att24 = Attribute.create_numeric("num24")
    att25 = Attribute.create_numeric("num25")
    att26 = Attribute.create_numeric("num26")
    att27 = Attribute.create_numeric("num27")
    att28 = Attribute.create_numeric("num28")
    att29 = Attribute.create_numeric("num29")
    att30 = Attribute.create_numeric("num30")
    att31 = Attribute.create_numeric("num31")
    att32 = Attribute.create_numeric("num32")
    att33 = Attribute.create_numeric("num33")
    att34 = Attribute.create_numeric("num34")
    att35 = Attribute.create_numeric("num35")
    att36 = Attribute.create_numeric("num36")
    att37 = Attribute.create_numeric("num37")
    att38 = Attribute.create_numeric("num38")
    att39 = Attribute.create_numeric("num39")
    att40 = Attribute.create_numeric("num40")
    att41 = Attribute.create_numeric("num41")

    nom_att = Attribute.create_nominal("char", ["0","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23"])

    dataset = Instances.create_instances("input data", [att0, att1, att2, att3, att4, att5, att6, att7, att8, att9, att10, att11, att12, att13, att14, att15, att16, att17, att18, att19, att20, att21, att22, att23, att24, att25, att26, att27, att28, att29, att30, att31, att32, att33, att34, att35, att36, att37, att38, att39, att40, att41, nom_att], 0)
    inst = Instance.create_instance(list)
    dataset.add_instance(inst)
    dataset.class_is_last()
    return dataset

class Thread(QThread):
    changePixmap = pyqtSignal(QImage)
    changePixCrop=pyqtSignal(QImage)
    charresult=pyqtSignal(str)
    kinect = AcquisitionKinect()
    frame = Frame()
    def run(self):
        jvm.start()
        # run karena QThread fungsi default
        while True:
            self.kinect.get_frame(self.frame)
            self.kinect.get_color_frame()
            image = self.kinect._frameRGB
            # OpenCv uses RGB image, kinect returns type RGBA, remove extra dim.
            image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
            image, points_x, points_y, points = keypoints(image)
            
            h, w, ch = image.shape
            bytesPerLine = ch * w
            convertToQtFormat = QImage(image.data, w, h, bytesPerLine, QImage.Format_BGR888)
            
            p1 = convertToQtFormat.scaled(853, 480, Qt.KeepAspectRatio)
            # p1 = convertToQtFormat.scaled(140, 140, Qt.KeepAspectRatio)
            # print(p1)

            self.changePixmap.emit(p1)

            # h, w, ch = image2.shape
            # bytesPerLine = ch * w
            convertToQtFormat2 = QImage(image.data, w, h, bytesPerLine, QImage.Format_BGR888)
            # convertToQtFormat2 = convertToQtFormat2[10:40, 10:40]

            try:
                pointY_max = points[0][1].astype(int) + 450
                pointY_min = points[0][1].astype(int) - 450
                pointX_max = points[0][0].astype(int) + 450
                pointX_min = points[0][0].astype(int) - 450

                if (pointY_min < 0):
                    pointY_max = pointY_max + abs(pointY_min)
                    pointY_min = 0

                if (pointY_max) > 1080:
                    pointY_min = pointY_min - (pointY_max - 1080)

                if (pointX_min < 0):
                    pointX_max = pointX_max + abs(pointX_min)
                    pointX_min = 0

                if (pointX_max) > 1920:
                    pointX_min = pointX_min - (pointX_max - 1920)

                convertToQtFormat2 = convertToQtFormat2.copy(QtCore.QRect(pointX_min, pointY_min, 900, 900))

                cropped = image[pointY_min:pointY_max, pointX_min:pointX_max]

                
                input_points = [] #data koordinat input
                _, points_x, points_y, points = keypoints(cropped)

                for i in range(len(points_x)):
                    input_points.append(round(points_x[i], 3))
                    input_points.append(round(points_y[i], 3))
                
                ###Backpropagation                
                input_points.append(0)

                data = create_dataset(input_points)

                cls, _ = Classifier.deserialize("model/model-01-01-700.model")

                for inst in data:
                    # print(inst)
                    pred = cls.classify_instance(inst)

                    pred_class = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
                    a = int(pred)
                    print(pred_class[a])
                    print("-")
                    self.charresult.emit(pred_class[a])
                ###backpropagation

            except Exception as e:
                print(e)
                self.charresult.emit("-")

            p2 = convertToQtFormat2.scaled(200, 200, Qt.KeepAspectRatio)
            self.changePixCrop.emit(p2)

            # myword += 1
            # self.changeKata.emit(word)
        jvm.stop()


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1121, 593)
        MainWindow.setStyleSheet("QMainWindow{color: rgb(64, 68, 64);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.maincam = QtWidgets.QLabel(self.centralwidget)
        self.maincam.setGeometry(QtCore.QRect(20, 70, 853, 480))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.maincam.setFont(font)
        self.maincam.setMouseTracking(False)
        self.maincam.setStyleSheet("background-color: rgb(255, 255, 255); border-style: solid; border-width: 5px; border-color: #D35B18; border-radius:10px;")
        self.maincam.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.maincam.setFrameShadow(QtWidgets.QFrame.Plain)
        self.maincam.setLineWidth(1)
        self.maincam.setText("")
        self.maincam.setObjectName("maincam")

        self.cropcam = QtWidgets.QLabel(self.centralwidget)
        self.cropcam.setGeometry(QtCore.QRect(900, 70, 200, 200))
        self.cropcam.setStyleSheet("background-color: rgb(255, 255, 255); border-style: solid; border-width: 5px; border-color: #D35B18; border-radius:10px;")
        self.cropcam.setFrameShape(QtWidgets.QFrame.Box)
        self.cropcam.setLineWidth(1)
        self.cropcam.setText("")
        self.cropcam.setObjectName("cropcam")
        self.text2 = QtWidgets.QLabel(self.centralwidget)
        self.text2.setGeometry(QtCore.QRect(900, 20, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)

        self.text2.setFont(font)
        self.text2.setStyleSheet("color: rgb(211, 91, 24);")
        self.text2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text2.setAlignment(QtCore.Qt.AlignCenter)
        self.text2.setObjectName("text2")

        self.text3 = QtWidgets.QLabel(self.centralwidget)
        self.text3.setGeometry(QtCore.QRect(900, 300, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)

        self.text3.setFont(font)
        self.text3.setStyleSheet("color: rgb(211, 91, 24);")
        self.text3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text3.setAlignment(QtCore.Qt.AlignCenter)
        self.text3.setObjectName("text3")

        self.textframe = QtWidgets.QLabel(self.centralwidget)
        self.textframe.setGeometry(QtCore.QRect(900, 350, 200, 200))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(70)
        font.setBold(True)
        font.setWeight(75)
        self.textframe.setFont(font)
        self.textframe.setStyleSheet("background-color: rgb(255, 255, 255); border-style: solid; border-width: 5px; border-color: #D35B18; border-radius:10px; color:#D35B18;")
        self.textframe.setFrameShape(QtWidgets.QFrame.Box)
        self.textframe.setTextFormat(QtCore.Qt.AutoText)
        self.textframe.setScaledContents(False)
        self.textframe.setAlignment(QtCore.Qt.AlignCenter)
        self.textframe.setWordWrap(False)
        self.textframe.setObjectName("textframe")

        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 1121, 571))
        self.background.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 238, 153, 1), stop:1 rgba(240, 145, 50, 1));")
        self.background.setText("")
        self.background.setObjectName("background")

        self.text1 = QtWidgets.QLabel(self.centralwidget)
        self.text1.setGeometry(QtCore.QRect(20, 20, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.text1.setFont(font)
        self.text1.setStyleSheet("color: rgb(211, 91, 24);")
        self.text1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text1.setAlignment(QtCore.Qt.AlignCenter)
        self.text1.setObjectName("text1")

        self.background.raise_()
        self.text2.raise_()
        self.text3.raise_()
        self.textframe.raise_()
        self.text1.raise_()
        # self.dropshadow1.raise_()
        self.maincam.raise_()
        # self.dropshadow2.raise_()
        self.cropcam.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 21))
        self.menubar.setObjectName("menubar")

        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.actionHow_to_use = QtWidgets.QAction(MainWindow)
        self.actionHow_to_use.setObjectName("actionHow_to_use")

        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.menuHelp.addAction(self.actionHow_to_use)
        self.menuHelp.addAction(self.actionAbout)

        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        

        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        # th.changePixmap.connect(self.keypoints)
        th.changePixCrop.connect(self.input_Cropped)
        th.charresult.connect(self.inputKata)
        th.start()

    @pyqtSlot(QImage)
    def setImage(self, image):
        self.maincam.setPixmap(QPixmap.fromImage(image))

    # menampilkan hasil crop
    @pyqtSlot(QImage)
    def input_Cropped(self, image):
        # self.inputCrop = image
        self.cropcam.setPixmap(QPixmap.fromImage(image))

    @pyqtSlot(str)
    def inputKata(self, result):
        self.textframe.setText(result)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.text2.setText(_translate("MainWindow", "<strong>CROP</strong> SCREEN"))
        self.text3.setText(_translate("MainWindow", "<strong>TEXT</strong> SCREEN"))
        self.textframe.setText(_translate("MainWindow", "-"))
        self.text1.setText(_translate("MainWindow", "<strong>MAIN</strong> SCREEN"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionHow_to_use.setText(_translate("MainWindow", "How to use"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())