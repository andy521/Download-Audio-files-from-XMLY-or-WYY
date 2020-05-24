#coding:utf-8  
'''
Author: 杜晓峰 HUST-SJTU
Time: 2020.03
summary: 一个集合了网易云和喜马拉雅非会员免费音频下载功能的小程序
'''
import sys
import threading
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QFileDialog
from uipyFile.mainWindow import Ui_MainWindow
from uipyFile.WYYWindow import Ui_WavWindow as Ui_WYYWindow
from uipyFile.XMLYWindow import Ui_MatWindow as Ui_XMLYWindow
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5 import QtCore
from PyQt5.QtGui import QPalette, QCursor, QTextCursor

import xmly as x
import wyy as w


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_Mat.clicked.connect(self.pushButtonProcess)
        self.pushButton_Wav.clicked.connect(self.pushButtonProcess)
        self.pushButton_close.clicked.connect(self.close)  # 关闭窗口
        self.pushButton_mini.clicked.connect(self.showMinimized)  # 最小化窗口
        self.beautiful()

    def show_XMLY(self):
        self.hide()
        XMLYWin.show()

    def show_WYY(self):
        self.hide()
        WYYWin.show()

    def pushButtonProcess(self):
        source = self.sender()
        if source.text() == '喜马拉雅':
            self.hide()
            XMLYWin.show()
        elif source.text() == '网易云':
            self.hide()
            WYYWin.show()

    def beautiful(self):
        # 美化
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setWindowFlag(Qt.FramelessWindowHint)  # 隐藏边框
        pe = QPalette()
        self.setAutoFillBackground(True)
        pe.setColor(QPalette.Window, Qt.lightGray)   # 设置背景色
        # pe.setColor(QPalette.Background,Qt.blue)
        self.setPalette(pe)
        self.pushButton_close.setStyleSheet('''QPushButton{background:#F76677;border-radius:15px;}
QPushButton:hover{background:red;}''')
        self.pushButton_mini.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:15px;}
QPushButton:hover{background:green;}''')

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True  # move flag
            self.m_Position = event.globalPos()-self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos()-self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


# 喜马拉雅下载线程
class XMLYThread(QThread):
    _signal = pyqtSignal(str)
    threadPool = []
    def __int__(self):
        super(XMLYThread, self).__init__()
        self.ID_num = None
        self.page_num = None
        self.save_path = None

    def __del__(self):
        self.wait()

    def set_value(self, ID_num, page_num, path):
        self.ID_num = ID_num
        self.page_num = page_num
        self.save_path = path

    def run(self):
        self.Creat_Thread()
        self.Run_Thread()

    def signal_download(self, url):
        mp3Name = str(x.download(url, self.save_path))
        self._signal.emit(mp3Name)

    def Creat_Thread(self):
        for url in x.get_EpisodeId(self.ID_num, self.page_num):
            print(url)
            t = threading.Thread(target=self.signal_download, args=(str(url),))
            self.threadPool.append(t)

    def Run_Thread(self):
        for i in self.threadPool:
            i.start()
        for i in self.threadPool:
            i.join()   

# 喜马拉雅搜索线程
class XMLYThread_search(QThread):
    _signal = pyqtSignal(str)

    def __int__(self):
        super(XMLYThread_search, self).__init__()
        self.keyword = None

    def __del__(self):
        self.wait()

    def set_value(self, keyword):
        self.keyword = keyword

    def run(self):
        for i in x.getid(self.keyword):
            self._signal.emit(str(i))

# 喜马拉雅线程监听
class XMLYThread_listen(QThread):
    _signal = pyqtSignal(str)

    def __int__(self):
        super(XMLYThread_search, self).__init__()
        self.OtherThread = None

    def __del__(self):
        self.wait()

    def set_value(self, OtherThread):
        self.OtherThread = OtherThread
        self.isRunning
        self.isFinished

    def run(self):
        while True:
            if self.OtherThread.isFinished():
                self._signal.emit('下载线程结束')
                break
# 喜马拉雅界面
class XMLYWindow(QMainWindow, Ui_XMLYWindow):

    def __init__(self, parent=None):
        super(XMLYWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_back.clicked.connect(self.pushButtonProcess)

        self.pushButton_download.clicked.connect(self.pushButtonProcess)
        self.pushButton_getid.clicked.connect(self.pushButtonProcess)
        self.pushButton_OpenPath.clicked.connect(self.pushButtonProcess)
        self.pushButton_close.clicked.connect(self.programClose)  # 关闭窗口
        self.pushButton_mini.clicked.connect(self.showMinimized)  # 最小化窗口
        self.beautiful()
        self.download_TH = None
        self.search_TH = None
        self.listen_TH = None

    def pushButtonProcess(self):
        source = self.sender()
        if source.text() == '查询':
            self.textBrowser.setText('正在查询... 请稍后\n')
            self.search_TH = XMLYThread_search()
            self.search_TH._signal.connect(self.call_backlog)
            keyword = self.lineEdit_Keyword.text()
            self.search_TH.set_value(keyword)
            self.search_TH.start()

        elif source.text() == '...':
            filename = QFileDialog.getExistingDirectory(self)
            self.lineEdit_Path.setText(filename)

        elif source.text() == '下载':
            self.textBrowser.setText('开始下载\n')

            self.download_TH = XMLYThread()
            self.download_TH._signal.connect(self.call_backlog)

            self.listen_TH = XMLYThread_listen()
            self.listen_TH._signal.connect(self.call_backlog)
            self.listen_TH.set_value(self.download_TH)
            self.listen_TH.start()
            ID = self.lineEdit_ID.text()
            num = self.lineEdit_Num.text()
            
            path = self.lineEdit_Path.text()
            if os.path.exists(path):
                self.download_TH.set_value(ID, num, path)
                self.download_TH.start()
            else:
                os.mkdir(path)
                self.download_TH.set_value(ID, num, path)
                self.download_TH.start()

        elif source.text() == '返回':
            MainWin.show()
            self.close()
    def call_backlog(self, msg):
        self.textBrowser.append(msg)
        # 将线程的参数传入进度条
    def beautiful(self):
        # 美化
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setWindowFlag(Qt.FramelessWindowHint)  # 隐藏边框
        pe = QPalette()
        self.setAutoFillBackground(True)
        pe.setColor(QPalette.Window, Qt.lightGray)   # 设置背景色
        # pe.setColor(QPalette.Background,Qt.blue)
        self.setPalette(pe)
        self.pushButton_close.setStyleSheet('''QPushButton{background:#F76677;border-radius:15px;} QPushButton:hover{background:red;}''')
        self.pushButton_mini.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:15px;} QPushButton:hover{background:green;}''')

    def programClose(self):
        self.close()
        MainWin.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True  # move flag
            self.m_Position = event.globalPos()-self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos()-self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

# 网易云线程
class WYYThread(QThread):
    _signal = pyqtSignal(str)

    def __int__(self):
        super(WYYThread, self).__init__()
        self.list_ID = None
        self.list_path = None
    def __del__(self):
        self.wait()

    def set_value(self, list_ID, list_path):
        self.list_ID = list_ID
        self.list_path = list_path

    def run(self):
        for i in w.get_list(self.list_ID, self.list_path):
            self._signal.emit(str(i))

# 网易云界面
class WYYWindow(QMainWindow, Ui_WYYWindow):

    def __init__(self, parent=None):
        super(WYYWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_back.clicked.connect(self.pushButtonProcess)
        self.pushButton_downloadsong.clicked.connect(self.pushButtonProcess)
        self.pushButton_listDownload.clicked.connect(self.pushButtonProcess)
        self.pushButton_openPathList.clicked.connect(self.pushButtonProcess)
        self.pushButton_openPathsong.clicked.connect(self.pushButtonProcess)

        self.pushButton_close.clicked.connect(self.programClose)  # 关闭窗口
        self.pushButton_mini.clicked.connect(self.showMinimized)  # 最小化窗口
        self.beautiful()
        self.TH = None

    def pushButtonProcess(self):
        source = self.sender() 
        if source.text() == '返回':
            MainWin.show()
            self.close()

        elif source.text() == '...':
            filename = QFileDialog.getExistingDirectory(self)
            self.lineEdit_listPath.setText(filename)
            self.lineEdit_songPath.setText(filename)

        elif source.text() == '单曲下载':
            song_ID = self.lineEdit_songID.text()
            song_path = self.lineEdit_songPath.text()
            self.call_backlog(w.get_song(song_ID, song_path))

        elif source.text() == '歌单下载':
            self.TH = WYYThread()
            self.TH._signal.connect(self.call_backlog)
            song_ID = self.lineEdit_listID.text()
            song_path = self.lineEdit_listPath.text()
            self.TH.set_value(song_ID, song_path)
            self.TH.start()

    def call_backlog(self, msg):
        self.textBrowser.append(msg)
        # 将线程的参数传入进度条
         
    def beautiful(self):
        # 美化
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setWindowFlag(Qt.FramelessWindowHint)  # 隐藏边框
        pe = QPalette()
        self.setAutoFillBackground(True)
        pe.setColor(QPalette.Window, Qt.lightGray)   # 设置背景色
        # pe.setColor(QPalette.Background,Qt.blue)
        self.setPalette(pe)
        self.pushButton_close.setStyleSheet('''QPushButton{background:#F76677;border-radius:15px;} QPushButton:hover{background:red;}''')
        self.pushButton_mini.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:15px;} QPushButton:hover{background:green;}''')

    def programClose(self):
        self.close()
        MainWin.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True  # move flag
            self.m_Position = event.globalPos()-self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos()-self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWin = MainWindow()
    XMLYWin = XMLYWindow()
    WYYWin = WYYWindow()
    MainWin.show()
    sys.exit(app.exec_())
