from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime
from acquisitionKinect import AcquisitionKinect
from frame import Frame
import matplotlib as plt
import matplotlib.pyplot as cm


# import ctypesd
import _ctypes
import cv2
import sys
import numpy as np
import time


# def timestamp(): #mengambil waktu data untuk filename
#     now = time.time()
#     localtime = time.localtime(now)
#     milliseconds = '%03d' % int((now - int(now)) * 1000)
#     return str(time.strftime('%Y%m%d%H-%M-%S-', localtime) + milliseconds)

jalankan=True
kinect = AcquisitionKinect()
frame = Frame()
while True:
    if(jalankan):
        # taaking exatc time to be file name
        now = time.time()
        localtime = time.localtime(now)
        milliseconds = '%03d' % int((now - int(now)) * 1000)
        timename = str(time.strftime('%Y%m%d%H-%M-%S-', localtime) + milliseconds)

        # start access kinect and taking frame
        kinect.get_frame(frame)
        kinect.get_color_frame()
        image = kinect._frameRGB

        # OpenCv uses RGB image, kinect returns type RGBA, remove extra dim.
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)

        if not image is None:
            cv2.namedWindow("Output-Keypoints", cv2.WINDOW_KEEPRATIO)
            cv2.imshow("Output-Keypoints", image)
            print(kinect._frameDepth)
            filename = "depthdata/" + timename + ".txt"
            filename2 = "colordata/" + timename + ".jpg"


            # list = kinect._frameDepth.tolist()
            # print(list)

            # writing/saving img file
            # cv2.imwrite(filename2, image)
            # print(filename)

            # # datadepth = np.loadtxt("depthdata/2020102613-37-15-511.txt")
            datadepth = kinect._frameDepth
            print("==========================================")
            print(datadepth)
            print("==========================================")
            # datadepth = (datadepth / datadepth.max()) * 255
            # max = np.amax(datadepth)
            # datadepth = (datadepth / max) * 255
            # b = np.zeros([424, 512, 3])
            # b[:, :, 0] = datadepth
            # b[:, :, 1] = datadepth
            # b[:, :, 2] = datadepth
            # print(b[:, :, 0])
            # cv2.imshow('Color image', b)

            # try:
            #     # saving depth data file
            #     np.savetxt(filename, kinect._frameDepth)
            #     #plt.
            # except:
            #     pass

        # cv2.waitKey(30)
        # time.sleep(0.5)
    else:
        pass

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(1) & 0xFF == ord('p'):
        jalankan=False
    elif cv2.waitKey(1) & 0xFF == ord('t'):
        jalankan=True