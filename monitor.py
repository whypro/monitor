# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import os
import sys
import cv2
import numpy as np
from PyQt4.QtGui import QMainWindow, QImage, QPixmap, QApplication, QSound
from PyQt4.QtCore import QTimer
import datetime
from ui_monitor import Ui_MainWindow
from time import clock


def CV_FOURCC(c1, c2, c3, c4):
    return (c1 & 255) + ((c2 & 255) << 8) + ((c3 & 255) << 16) + ((c4 & 255) << 24)


class MainWindow(QMainWindow, Ui_MainWindow):
    INTERVAL = 1000/24  # 单位为毫秒

    MHI_DURATION = 0.5
    DEFAULT_THRESHOLD = 32
    MAX_TIME_DELTA = 0.25
    MIN_TIME_DELTA = 0.05

    VIDEO_FOLDER = 'video'
    PHOTO_FOLDER = 'photo'

    DEFAULT_MONITOR_DELAY = 5   # 单位为秒

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.timer = QTimer(self)
        self.timer.setInterval(self.INTERVAL)
        self.timer.timeout.connect(self.capture)

        self.camera = cv2.VideoCapture()
        self.image = None
        self.sound = QSound('alert.wav')
        self.sound.setLoops(2)

        self.monitor_last_shoot = None

        self.frame = None
        self.video = None
        self.prev_frame = None
        self.motion_history = None
        self.hsv = None

        self.is_recording = False
        self.is_monitoring = False

        self.threshold_spin.setValue(self.DEFAULT_THRESHOLD)
        self.shoot_delay_spin.setValue(self.DEFAULT_MONITOR_DELAY)

        self.shoot_button.setEnabled(False)
        self.record_button.setEnabled(False)
        self.monitor_button.setEnabled(False)
        self.visual_radio_1.setEnabled(False)
        self.visual_radio_2.setEnabled(False)
        self.visual_radio_3.setEnabled(False)
        self.visual_radio_4.setEnabled(False)
        self.threshold_label.setEnabled(False)
        self.threshold_spin.setEnabled(False)
        self.threshold_slider.setEnabled(False)
        self.record_check.setEnabled(False)
        self.shoot_check.setEnabled(False)
        self.shoot_delay_label.setEnabled(False)
        self.shoot_delay_spin.setEnabled(False)
        self.shoot_delay_slider.setEnabled(False)
        self.sound_check.setEnabled(False)

        self.open_button.clicked.connect(self.open_camera)
        self.shoot_button.clicked.connect(self.shoot)
        self.record_button.clicked.connect(self.start_record)
        self.monitor_button.clicked.connect(self.start_monitor)
        self.record_check.toggled.connect(self.record_toggled)
        self.shoot_check.toggled.connect(self.shoot_toggled)

    def record_toggled(self):
        if self.record_check.isChecked() and self.shoot_check.isChecked():
            self.shoot_check.setChecked(False)
            self.monitor_last_shoot = clock()
            self.shoot_delay_label.setText('录像最短时间')
        if not self.record_check.isChecked() and self.is_recording:
            self.stop_record()

    def shoot_toggled(self):
        # if not self.shoot_check.isChecked():
        #     self.shoot_delay_spin.setEnabled(False)
        #     self.shoot_delay_slider.setEnabled(False)
        if self.shoot_check.isChecked():
            self.shoot_delay_spin.setEnabled(True)
            self.shoot_delay_slider.setEnabled(True)
            self.shoot_delay_label.setText('拍照间隔')
            if self.record_check.isChecked():
                self.record_check.setChecked(False)

    def open_camera(self):
        self.camera.open(0)
        assert self.camera.isOpened()
        self.timer.start()

        self.open_button.setText('关闭摄像头(&O)')

        self.shoot_button.setEnabled(True)
        self.record_button.setEnabled(True)
        self.monitor_button.setEnabled(True)

        self.open_button.clicked.disconnect(self.open_camera)
        self.open_button.clicked.connect(self.close_camera)

    def close_camera(self):
        if self.is_recording:
            self.stop_record()
        if self.is_monitoring:
            self.stop_monitor()
        self.timer.stop()
        self.camera.release()
        self.image = QImage()
        self.screen.setPixmap(QPixmap.fromImage(self.image))

        self.open_button.setText('打开摄像头(&O)')

        self.shoot_button.setEnabled(False)
        self.record_button.setEnabled(False)
        self.monitor_button.setEnabled(False)

        self.open_button.clicked.disconnect(self.close_camera)
        self.open_button.clicked.connect(self.open_camera)
        #self.open_button.setWindowTitle('打开摄像头')

    def shoot(self):
        filename = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.jpg'
        filepath = os.path.join(self.PHOTO_FOLDER, filename)
        if not os.path.exists(self.PHOTO_FOLDER):
            os.makedirs(self.PHOTO_FOLDER)
        if cv2.imwrite(filepath, self.frame):
            print('saved to %s' % filepath)

    def start_record(self):
        filename = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.avi'
        filepath = os.path.join(self.VIDEO_FOLDER, filename)
        if not os.path.exists(self.VIDEO_FOLDER):
            os.makedirs(self.VIDEO_FOLDER)
        fourcc = CV_FOURCC(ord('X'), ord('2'), ord('6'), ord('4'))
        self.video = cv2.VideoWriter(filepath, fourcc, 6, (640, 480))
        print('start recording...')
        print('saving to %s' % filepath)
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
        if self.is_monitoring:
            frame = self.detect()

            if self.is_recording:
                delay = self.shoot_delay_spin.value()
                print(clock() - self.monitor_last_shoot)
                if clock() - self.monitor_last_shoot >= delay:
                    self.stop_record()

        self.display(frame)

    def display(self, frame):
        height, width, bytes_per_component = frame.shape
        bytes_per_line = bytes_per_component * width
        #print(width, height)
        self.image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        self.screen.setPixmap(QPixmap.fromImage(self.image))

    def start_monitor(self):
        height, width = self.frame.shape[:2]
        self.prev_frame = self.frame.copy()
        self.motion_history = np.zeros((height, width), np.float32)
        self.hsv = np.zeros((height, width, 3), np.uint8)
        self.hsv[:, :, 1] = 255
        print('start monitor...')
        self.is_monitoring = True
        self.monitor_button.setText('停止监控(&M)')

        self.record_button.setEnabled(False)
        self.visual_radio_1.setEnabled(True)
        self.visual_radio_2.setEnabled(True)
        self.visual_radio_3.setEnabled(True)
        self.visual_radio_4.setEnabled(True)
        self.threshold_label.setEnabled(True)
        self.threshold_spin.setEnabled(True)
        self.threshold_slider.setEnabled(True)
        self.record_check.setEnabled(True)
        self.shoot_check.setEnabled(True)
        self.shoot_delay_label.setEnabled(True)
        self.shoot_delay_spin.setEnabled(True)
        self.shoot_delay_slider.setEnabled(True)
        self.sound_check.setEnabled(True)

        self.monitor_button.clicked.disconnect(self.start_monitor)
        self.monitor_button.clicked.connect(self.stop_monitor)

    def stop_monitor(self):
        print('stop monitor...')
        self.is_monitoring = False
        if self.is_recording:
            self.stop_record()

        self.monitor_button.setText('开始监控(&M)')

        self.record_button.setEnabled(True)
        self.visual_radio_1.setEnabled(False)
        self.visual_radio_2.setEnabled(False)
        self.visual_radio_3.setEnabled(False)
        self.visual_radio_4.setEnabled(False)
        self.threshold_label.setEnabled(False)
        self.threshold_spin.setEnabled(False)
        self.threshold_slider.setEnabled(False)
        self.record_check.setEnabled(False)
        self.shoot_check.setEnabled(False)
        self.shoot_delay_label.setEnabled(False)
        self.shoot_delay_spin.setEnabled(False)
        self.shoot_delay_slider.setEnabled(False)
        self.sound_check.setEnabled(False)

        self.monitor_button.clicked.disconnect(self.stop_monitor)
        self.monitor_button.clicked.connect(self.start_monitor)

    def detect(self):
        # print('detect...')
        visuals = ['input', 'frame_diff', 'motion_hist', 'grad_orient']
        #cv2.createTrackbar('visual', 'motempl', 2, len(visuals)-1, nothing)
        #cv2.createTrackbar('threshold', 'motempl', DEFAULT_THRESHOLD, 255, nothing)
        height, width = self.frame.shape[:2]
        frame_diff = cv2.absdiff(self.frame, self.prev_frame)
        gray_diff = cv2.cvtColor(frame_diff, cv2.COLOR_BGR2GRAY)
        thrs = self.threshold_spin.value()
        # thrs = cv2.getTrackbarPos('threshold', 'motempl')
        ret, motion_mask = cv2.threshold(gray_diff, thrs, 1, cv2.THRESH_BINARY)
        timestamp = clock()
        cv2.updateMotionHistory(motion_mask, self.motion_history, timestamp, self.MHI_DURATION)
        mg_mask, mg_orient = cv2.calcMotionGradient(self.motion_history, self.MAX_TIME_DELTA, self.MIN_TIME_DELTA, apertureSize=5)
        seg_mask, seg_bounds = cv2.segmentMotion(self.motion_history, timestamp, self.MAX_TIME_DELTA)

        for radio in (self.visual_radio_1, self.visual_radio_2, self.visual_radio_3, self.visual_radio_4):
            if radio.isChecked():
                visual_name = str(radio.text())
                break

        # visual_name = visuals[cv2.getTrackbarPos('visual', 'motempl')]
        # visual_name = 'input'
        if visual_name == 'input':
            vis = self.frame.copy()
        elif visual_name == 'frame_diff':
            vis = frame_diff.copy()
        elif visual_name == 'motion_hist':
            vis = np.uint8(np.clip((self.motion_history-(timestamp-self.MHI_DURATION)) / self.MHI_DURATION, 0, 1)*255)
            vis = cv2.cvtColor(vis, cv2.COLOR_GRAY2BGR)
        elif visual_name == 'grad_orient':
            self.hsv[:, :, 0] = mg_orient/2
            self.hsv[:, :, 2] = mg_mask*255
            vis = cv2.cvtColor(self.hsv, cv2.COLOR_HSV2BGR)

        for i, rect in enumerate([(0, 0, width, height)] + list(seg_bounds)):
            x, y, rw, rh = rect
            area = rw*rh
            if area < 64**2:
                continue
            silh_roi = motion_mask[y:y+rh, x:x+rw]
            orient_roi = mg_orient[y:y+rh, x:x+rw]
            mask_roi = mg_mask[y:y+rh, x:x+rw]
            mhi_roi = self.motion_history[y:y+rh, x:x+rw]
            if cv2.norm(silh_roi, cv2.NORM_L1) < area*0.05:
                continue
            angle = cv2.calcGlobalOrientation(orient_roi, mask_roi, mhi_roi, timestamp, self.MHI_DURATION)
            color = ((255, 0, 0), (0, 0, 255))[i == 0]
            self.draw_motion_comp(vis, rect, angle, color)
            if i == 0:
                # 检测到目标运动
                if self.record_check.isChecked():
                    self.monitor_last_shoot = clock()
                    if not self.is_recording:
                        self.start_record()
                elif self.shoot_check.isChecked():
                    # print(self.monitor_last_shoot)
                    # print(clock())
                    delay = self.shoot_delay_spin.value()
                    if (not self.monitor_last_shoot) or (clock() - self.monitor_last_shoot >= delay):
                        self.shoot()
                        self.monitor_last_shoot = clock()
                if self.sound_check.isChecked():
                    self.play_sound()

        self.draw_str(vis, (20, 20), visual_name)

        self.prev_frame = self.frame.copy()
        return vis

    @staticmethod
    def draw_motion_comp(vis, (x, y, w, h), angle, color):
        cv2.rectangle(vis, (x, y), (x+w, y+h), (0, 255, 0))
        r = min(w/2, h/2)
        cx, cy = x+w/2, y+h/2
        angle = angle*np.pi/180
        cv2.circle(vis, (cx, cy), r, color, 3)
        cv2.line(vis, (cx, cy), (int(cx+np.cos(angle)*r), int(cy+np.sin(angle)*r)), color, 3)

    @staticmethod
    def draw_str(dst, (x, y), s):
        cv2.putText(dst, s, (x+1, y+1), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 0), thickness = 2, lineType=cv2.CV_AA)
        cv2.putText(dst, s, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 255, 255), lineType=cv2.CV_AA)

    def play_sound(self):
        if self.sound.isFinished():
            self.sound.play()
        # media_obj = Phonon.MediaObject()
        # audio_output = Phonon.AudioOutput(Phonon.MusicCategory)
        # Phonon.createPath(media_obj, audio_output)
        # media_obj.setCurrentSource(Phonon.MediaSource("alert.wav"))
        # print('play')
        # media_obj.play()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()