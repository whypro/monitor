# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monitor.ui'
#
# Created: Tue May 06 00:35:26 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(822, 606)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.open_button = QtGui.QPushButton(self.centralwidget)
        self.open_button.setObjectName(_fromUtf8("open_button"))
        self.verticalLayout.addWidget(self.open_button)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.shoot_button = QtGui.QPushButton(self.centralwidget)
        self.shoot_button.setObjectName(_fromUtf8("shoot_button"))
        self.verticalLayout.addWidget(self.shoot_button)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.record_button = QtGui.QPushButton(self.centralwidget)
        self.record_button.setObjectName(_fromUtf8("record_button"))
        self.verticalLayout.addWidget(self.record_button)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.monitor_button = QtGui.QPushButton(self.centralwidget)
        self.monitor_button.setObjectName(_fromUtf8("monitor_button"))
        self.verticalLayout.addWidget(self.monitor_button)
        self.visual_radio_1 = QtGui.QRadioButton(self.centralwidget)
        self.visual_radio_1.setChecked(True)
        self.visual_radio_1.setObjectName(_fromUtf8("visual_radio_1"))
        self.verticalLayout.addWidget(self.visual_radio_1)
        self.visual_radio_2 = QtGui.QRadioButton(self.centralwidget)
        self.visual_radio_2.setObjectName(_fromUtf8("visual_radio_2"))
        self.verticalLayout.addWidget(self.visual_radio_2)
        self.visual_radio_3 = QtGui.QRadioButton(self.centralwidget)
        self.visual_radio_3.setObjectName(_fromUtf8("visual_radio_3"))
        self.verticalLayout.addWidget(self.visual_radio_3)
        self.visual_radio_4 = QtGui.QRadioButton(self.centralwidget)
        self.visual_radio_4.setObjectName(_fromUtf8("visual_radio_4"))
        self.verticalLayout.addWidget(self.visual_radio_4)
        self.threshold_label = QtGui.QLabel(self.centralwidget)
        self.threshold_label.setObjectName(_fromUtf8("threshold_label"))
        self.verticalLayout.addWidget(self.threshold_label)
        self.threshold_spin = QtGui.QSpinBox(self.centralwidget)
        self.threshold_spin.setMinimum(1)
        self.threshold_spin.setMaximum(255)
        self.threshold_spin.setObjectName(_fromUtf8("threshold_spin"))
        self.verticalLayout.addWidget(self.threshold_spin)
        self.threshold_slider = QtGui.QSlider(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.threshold_slider.sizePolicy().hasHeightForWidth())
        self.threshold_slider.setSizePolicy(sizePolicy)
        self.threshold_slider.setMinimum(1)
        self.threshold_slider.setMaximum(255)
        self.threshold_slider.setOrientation(QtCore.Qt.Horizontal)
        self.threshold_slider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.threshold_slider.setObjectName(_fromUtf8("threshold_slider"))
        self.verticalLayout.addWidget(self.threshold_slider)
        self.record_check = QtGui.QCheckBox(self.centralwidget)
        self.record_check.setObjectName(_fromUtf8("record_check"))
        self.verticalLayout.addWidget(self.record_check)
        self.shoot_check = QtGui.QCheckBox(self.centralwidget)
        self.shoot_check.setChecked(True)
        self.shoot_check.setObjectName(_fromUtf8("shoot_check"))
        self.verticalLayout.addWidget(self.shoot_check)
        self.shoot_delay_label = QtGui.QLabel(self.centralwidget)
        self.shoot_delay_label.setObjectName(_fromUtf8("shoot_delay_label"))
        self.verticalLayout.addWidget(self.shoot_delay_label)
        self.shoot_delay_spin = QtGui.QSpinBox(self.centralwidget)
        self.shoot_delay_spin.setMinimum(1)
        self.shoot_delay_spin.setMaximum(10)
        self.shoot_delay_spin.setObjectName(_fromUtf8("shoot_delay_spin"))
        self.verticalLayout.addWidget(self.shoot_delay_spin)
        self.shoot_delay_slider = QtGui.QSlider(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shoot_delay_slider.sizePolicy().hasHeightForWidth())
        self.shoot_delay_slider.setSizePolicy(sizePolicy)
        self.shoot_delay_slider.setMinimum(1)
        self.shoot_delay_slider.setMaximum(10)
        self.shoot_delay_slider.setPageStep(1)
        self.shoot_delay_slider.setOrientation(QtCore.Qt.Horizontal)
        self.shoot_delay_slider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.shoot_delay_slider.setObjectName(_fromUtf8("shoot_delay_slider"))
        self.verticalLayout.addWidget(self.shoot_delay_slider)
        self.sound_check = QtGui.QCheckBox(self.centralwidget)
        self.sound_check.setChecked(True)
        self.sound_check.setObjectName(_fromUtf8("sound_check"))
        self.verticalLayout.addWidget(self.sound_check)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.exit_button = QtGui.QPushButton(self.centralwidget)
        self.exit_button.setObjectName(_fromUtf8("exit_button"))
        self.verticalLayout.addWidget(self.exit_button)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.screen = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screen.sizePolicy().hasHeightForWidth())
        self.screen.setSizePolicy(sizePolicy)
        self.screen.setMinimumSize(QtCore.QSize(640, 480))
        self.screen.setFrameShape(QtGui.QFrame.Panel)
        self.screen.setFrameShadow(QtGui.QFrame.Sunken)
        self.screen.setAlignment(QtCore.Qt.AlignCenter)
        self.screen.setObjectName(_fromUtf8("screen"))
        self.horizontalLayout.addWidget(self.screen)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 822, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.file_menu = QtGui.QMenu(self.menubar)
        self.file_menu.setObjectName(_fromUtf8("file_menu"))
        self.tool_menu = QtGui.QMenu(self.menubar)
        self.tool_menu.setObjectName(_fromUtf8("tool_menu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.open_action = QtGui.QAction(MainWindow)
        self.open_action.setObjectName(_fromUtf8("open_action"))
        self.shoot_action = QtGui.QAction(MainWindow)
        self.shoot_action.setObjectName(_fromUtf8("shoot_action"))
        self.record_action = QtGui.QAction(MainWindow)
        self.record_action.setObjectName(_fromUtf8("record_action"))
        self.exit_action = QtGui.QAction(MainWindow)
        self.exit_action.setObjectName(_fromUtf8("exit_action"))
        self.file_menu.addAction(self.exit_action)
        self.tool_menu.addAction(self.open_action)
        self.tool_menu.addAction(self.shoot_action)
        self.tool_menu.addAction(self.record_action)
        self.menubar.addAction(self.file_menu.menuAction())
        self.menubar.addAction(self.tool_menu.menuAction())
        self.threshold_label.setBuddy(self.threshold_spin)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.exit_button, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.threshold_spin, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.threshold_slider.setValue)
        QtCore.QObject.connect(self.threshold_slider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.threshold_spin.setValue)
        QtCore.QObject.connect(self.shoot_delay_spin, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.shoot_delay_slider.setValue)
        QtCore.QObject.connect(self.shoot_delay_slider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.shoot_delay_spin.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "视频监控异常处理系统", None))
        self.open_button.setText(_translate("MainWindow", "打开摄像头(&C)", None))
        self.shoot_button.setText(_translate("MainWindow", "拍照(&S)", None))
        self.record_button.setText(_translate("MainWindow", "录像(&R)", None))
        self.monitor_button.setText(_translate("MainWindow", "开始监控(&M)", None))
        self.visual_radio_1.setText(_translate("MainWindow", "input", None))
        self.visual_radio_2.setText(_translate("MainWindow", "frame_diff", None))
        self.visual_radio_3.setText(_translate("MainWindow", "motion_hist", None))
        self.visual_radio_4.setText(_translate("MainWindow", "grad_orient", None))
        self.threshold_label.setText(_translate("MainWindow", "阈值", None))
        self.record_check.setText(_translate("MainWindow", "录像", None))
        self.shoot_check.setText(_translate("MainWindow", "拍照", None))
        self.shoot_delay_label.setText(_translate("MainWindow", "拍照间隔", None))
        self.shoot_delay_spin.setSuffix(_translate("MainWindow", " 秒", None))
        self.sound_check.setText(_translate("MainWindow", "播放警报", None))
        self.exit_button.setText(_translate("MainWindow", "退出(&X)", None))
        self.screen.setText(_translate("MainWindow", "1", None))
        self.file_menu.setTitle(_translate("MainWindow", "文件(&F)", None))
        self.tool_menu.setTitle(_translate("MainWindow", "工具(&T)", None))
        self.open_action.setText(_translate("MainWindow", "打开摄像头(&C)", None))
        self.shoot_action.setText(_translate("MainWindow", "拍照(&S)", None))
        self.record_action.setText(_translate("MainWindow", "录像(&R)", None))
        self.exit_action.setText(_translate("MainWindow", "退出(&X)", None))

