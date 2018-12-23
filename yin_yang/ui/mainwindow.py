# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yin_yang/ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(260, 270)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(260, 270))
        MainWindow.setMaximumSize(QtCore.QSize(260, 270))
        MainWindow.setBaseSize(QtCore.QSize(260, 270))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("yin_yang/ui/assets/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 20, 221, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.yinyangimg = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.yinyangimg.setText("")
        self.yinyangimg.setTextFormat(QtCore.Qt.RichText)
        self.yinyangimg.setPixmap(QtGui.QPixmap("yin_yang/ui/assets/icon.png"))
        self.yinyangimg.setAlignment(QtCore.Qt.AlignCenter)
        self.yinyangimg.setObjectName("yinyangimg")
        self.verticalLayout.addWidget(self.yinyangimg)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.light_push = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.light_push.setObjectName("light_push")
        self.horizontalLayout.addWidget(self.light_push)
        self.dark_push = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.dark_push.setEnabled(False)
        self.dark_push.setObjectName("dark_push")
        self.horizontalLayout.addWidget(self.dark_push)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.schedule_radio = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.schedule_radio.setObjectName("schedule_radio")
        self.verticalLayout.addWidget(self.schedule_radio)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setHorizontalSpacing(40)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.light_time = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.light_time.setEnabled(False)
        self.light_time.setTime(QtCore.QTime(8, 0, 0))
        self.light_time.setObjectName("light_time")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.light_time)
        self.dark_time = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.dark_time.setEnabled(False)
        self.dark_time.setTime(QtCore.QTime(20, 0, 0))
        self.dark_time.setObjectName("dark_time")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dark_time)
        self.verticalLayout.addLayout(self.formLayout)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Yin & Yang"))
        self.light_push.setText(_translate("MainWindow", "Light"))
        self.dark_push.setText(_translate("MainWindow", "Dark"))
        self.schedule_radio.setText(_translate("MainWindow", "scheduled"))
        self.label.setText(_translate("MainWindow", "Light:"))
        self.label_2.setText(_translate("MainWindow", "Dark:"))
        self.light_time.setDisplayFormat(_translate("MainWindow", "HH:mm"))
        self.dark_time.setDisplayFormat(_translate("MainWindow", "HH:mm"))

