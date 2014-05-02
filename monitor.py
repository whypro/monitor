# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import sys
import time
import hashlib

import cv2
import cv2.cv as cv


def CV_FOURCC(c1, c2, c3, c4):
    return (c1 & 255) + ((c2 & 255) << 8) + ((c3 & 255) << 16) + ((c4 & 255) << 24)

from PyQt4.QtGui import QMainWindow, QImage, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QPixmap, QApplication
from PyQt4.QtCore import SIGNAL, SLOT, QByteArray, QThread, QMutex, QMutexLocker, QTimer
import datetime

from ui_monitor import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    interval = 1000/24

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.timer = QTimer(self)
        self.timer.setInterval(self.interval)
        self.timer.timeout.connect(self.capture)

        self.camera = cv2.VideoCapture()
        self.image = None

        self.frame = None
        self.video = None
        self.is_recording = False

        self.shoot_button.setEnabled(False)
        self.record_button.setEnabled(False)
        self.monitor_button.setEnabled(False)
        self.open_button.clicked.connect(self.open_camera)
        self.shoot_button.clicked.connect(self.shoot)
        self.record_button.clicked.connect(self.start_record)
        self.monitor_button.clicked.connect(self.start_monitor)

    def open_camera(self):
        self.camera.open(0)
        assert self.camera.isOpened()
        self.timer.start()

        self.open_button.setText('关闭摄像头(&O)')
        self.monitor_button.setEnabled(True)
        self.shoot_button.setEnabled(True)
        self.record_button.setEnabled(True)
        self.open_button.clicked.disconnect(self.open_camera)
        self.open_button.clicked.connect(self.close_camera)

    def close_camera(self):
        self.timer.stop()
        self.camera.release()
        self.image = QImage()
        self.screen.setPixmap(QPixmap.fromImage(self.image))

        self.open_button.setText('打开摄像头(&O)')
        self.shoot_button.setEnabled(False)
        self.record_button.setEnabled(False)
        self.open_button.clicked.disconnect(self.close_camera)
        self.open_button.clicked.connect(self.open_camera)
        #self.open_button.setWindowTitle('打开摄像头')

    def shoot(self):
        filename = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.jpg'
        if cv2.imwrite(filename, self.frame):
            print('saved to %s' % filename)

    def start_record(self):
        fourcc = CV_FOURCC(ord('X'), ord('2'), ord('6'), ord('4'))
        self.video = cv2.VideoWriter('record.avi', fourcc, 6, (640, 480))
        print('start recording...')
        self.is_recording = True

        self.record_button.setText('停止(&R)')
        self.record_button.clicked.disconnect(self.start_record)
        self.record_button.clicked.connect(self.stop_record)

    def stop_record(self):
        print('stop record')
        self.is_recording = False
        self.video.release()

        self.record_button.setText('录像(&R)')
        self.record_button.clicked.disconnect(self.stop_record)
        self.record_button.clicked.connect(self.start_record)

    def capture(self):
        ret, frame = self.camera.read()
        self.frame = frame
        if self.is_recording:
            #frame = cv2.flip(frame, 0)
            self.video.write(frame)
        height, width, bytesPerComponent = frame.shape
        bytesPerLine = bytesPerComponent * width
        #print(width, height)
        self.image = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        self.screen.setPixmap(QPixmap.fromImage(self.image))

    def start_monitor(self):
        self.monitor_button.setText('停止监控(&M)')
        self.monitor_button.clicked.disconnect(self.start_monitor)
        self.monitor_button.clicked.connect(self.stop_monitor)

    def stop_monitor(self):
        self.monitor_button.setText('开始监控(&M)')
        self.monitor_button.clicked.disconnect(self.stop_monitor)
        self.monitor_button.clicked.connect(self.start_monitor)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()