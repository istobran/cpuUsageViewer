# -*- coding: utf-8 -*-
__author__ = 'BangZ'
from PyQt4 import QtCore, QtGui
import progress
import sys
import sysInfo

class MainUiClass(QtGui.QMainWindow, progress.Ui_MainWindow):       #多重继承
    def __init__(self, parent = None):
        super(MainUiClass, self).__init__(parent)
        self.setupUi(self)                      #在不改变自动生成型文件progress.py的条件下进行外部启动
        self.threadclass = ThreadClass()        #创建线程
        self.threadclass.start()                #运行线程
        self.connect(self.threadclass, QtCore.SIGNAL("CPU_VALUE"), self.updateProgressBar)          #把自己的成员方法作为槽连接到threadclass线程的信号

    def updateProgressBar(self, val):
        self.progressBar.setValue(val)          #更新进度条


class ThreadClass(QtCore.QThread):
    def __init__(self, parent = None):
        super(ThreadClass, self).__init__(parent)

    def run(self):
        while True:
            val = sysInfo.getCPU()
            #print val
            self.emit(QtCore.SIGNAL("CPU_VALUE"), val)      #把val作为附带参数，发射CPU_VALUE信号

if __name__ == '__main__':      #从面向过程转向面向对象，相当于面向对象编程
    a = QtGui.QApplication(sys.argv)
    app = MainUiClass()
    app.show()
    a.exec_()