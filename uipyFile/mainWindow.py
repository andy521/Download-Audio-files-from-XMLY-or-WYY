# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\PyProjects\ximalaya_qt\uiFile\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(296, 327)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Mat = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Mat.setGeometry(QtCore.QRect(90, 60, 111, 41))
        self.pushButton_Mat.setObjectName("pushButton_Mat")
        self.pushButton_Wav = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Wav.setGeometry(QtCore.QRect(90, 140, 111, 41))
        self.pushButton_Wav.setObjectName("pushButton_Wav")
        self.pushButton_mini = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mini.setGeometry(QtCore.QRect(190, 10, 31, 28))
        self.pushButton_mini.setText("")
        self.pushButton_mini.setObjectName("pushButton_mini")
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setGeometry(QtCore.QRect(250, 10, 31, 28))
        self.pushButton_close.setText("")
        self.pushButton_close.setObjectName("pushButton_close")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 210, 256, 61))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 296, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_XMLY = QtWidgets.QAction(MainWindow)
        self.action_XMLY.setObjectName("action_XMLY")
        self.action_WYY = QtWidgets.QAction(MainWindow)
        self.action_WYY.setObjectName("action_WYY")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Mat.setText(_translate("MainWindow", "喜马拉雅"))
        self.pushButton_Wav.setText(_translate("MainWindow", "网易云"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">多线程版</p></body></html>"))
        self.action_XMLY.setText(_translate("MainWindow", "audio download"))
        self.action_WYY.setText(_translate("MainWindow", "MP3 download"))

