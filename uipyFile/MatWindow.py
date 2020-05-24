# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\PyProjects\ximalaya_qt\uiFile\MatWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MatWindow(object):
    def setupUi(self, MatWindow):
        MatWindow.setObjectName("MatWindow")
        MatWindow.resize(1121, 602)
        self.centralwidget = QtWidgets.QWidget(MatWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_mini = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mini.setGeometry(QtCore.QRect(1030, 10, 31, 28))
        self.pushButton_mini.setText("")
        self.pushButton_mini.setObjectName("pushButton_mini")
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setGeometry(QtCore.QRect(1080, 10, 31, 28))
        self.pushButton_close.setText("")
        self.pushButton_close.setShortcut("")
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_Mat = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Mat.setGeometry(QtCore.QRect(490, 170, 93, 28))
        self.pushButton_Mat.setObjectName("pushButton_Mat")
        self.pushButton_Wav = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Wav.setGeometry(QtCore.QRect(490, 240, 93, 28))
        self.pushButton_Wav.setObjectName("pushButton_Wav")
        MatWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MatWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MatWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MatWindow)
        self.statusbar.setObjectName("statusbar")
        MatWindow.setStatusBar(self.statusbar)
        self.action_Mat = QtWidgets.QAction(MatWindow)
        self.action_Mat.setObjectName("action_Mat")
        self.action_Wav = QtWidgets.QAction(MatWindow)
        self.action_Wav.setObjectName("action_Wav")
        self.menu.addAction(self.action_Mat)
        self.menu.addAction(self.action_Wav)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MatWindow)
        QtCore.QMetaObject.connectSlotsByName(MatWindow)

    def retranslateUi(self, MatWindow):
        _translate = QtCore.QCoreApplication.translate
        MatWindow.setWindowTitle(_translate("MatWindow", "MainWindow"))
        self.pushButton_Mat.setText(_translate("MatWindow", "矩阵计算"))
        self.pushButton_Wav.setText(_translate("MatWindow", "波形观察"))
        self.menu.setTitle(_translate("MatWindow", "功能"))
        self.action_Mat.setText(_translate("MatWindow", "MatCalculate"))
        self.action_Wav.setText(_translate("MatWindow", "WavView"))

