from Mainwindows_ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QWidget,QMessageBox,QSplashScreen,QButtonGroup,QPushButton
from PyQt5.QtGui import QWindow,QPixmap
from PyQt5.QtCore import QProcess,QFile,Qt
from PyQt5 import QtCore
from SerialPort_Con import SerialPort_Con
from ConfigFileEditClass import ConfigFileEditClass
import time
import sys
import ctypes
import win32gui
import win32con
import win32api
import subprocess

class MyloginMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyloginMainForm, self).__init__(parent)
        self.setupUi(self)
        #self.setWindowFlags(Qt.FramelessWindowHint)  # 设置无边框属性
        self.toolButton_exit.clicked.connect(self.closeEvent)
        #self.serial_port_con = SerialPort_Con("COM4",115200,1000)
        self.Config_toolButton.clicked.connect(self.Config_toolButton_clicked)
        self.set_pushbutton_group(self)
            
    def run_external_app(self):
        #打开第三方应用程序
        programstr ="C:/Program Files (x86)/Luciol Instruments/LOR-200/LOR-200.exe"; 
        #检查文件路径progtamstr是否存在
        if QFile.exists(programstr)==False :
            #弹出提示框提示错误
            QMessageBox.warning(self, "警告", "文件路径不存在")
            return   
        '''
        process = QProcess()
        process.startDetached(programstr)
        '''
        process=subprocess.Popen(programstr,shell=True)
        # 主动等待程序启动
        start_time = time.time()
        while process.poll() is None:
            time.sleep(0.1)  # 小于1秒的间隔检查
            if time.time() - start_time > 5:
                print("程序启动超时，终止等待。")
                process.terminate()
                break
        
        #等待第三方应用程序启动
        #time.sleep(2)
        #获取已打开的第三方应用程序
        hwnd = win32gui.FindWindow(None, "LUCIOL INSTRUMENTS - LOR-220 High Resolution OTDR")    
        self.m_window = QWindow.fromWinId(hwnd)
        time.sleep(1)
        childwidget=QWidget.createWindowContainer(self.m_window, self)
        self.luciol_widget.layout().addWidget(childwidget)
    
    def Config_toolButton_clicked(self):
        #打开配置文件编辑窗口
        self.configForm=ConfigFileEditClass()
        self.configForm.show()

    def closeEvent(self, event):
        #关闭窗口
        self.close()

    #刷新widget控件
    def refresh_widget(self):
        #重绘widget控件
        self.luciol_widget.repaint()
        #强制刷新widget控件
        self.luciol_widget.update()
        #改变widget控件的大小
        self.luciol_widget.resize(826, 569)
        self.luciol_widget.resize(825, 568)
    
    
    #将gridlayout_Point控件中所有pushbutton添加到组中，并设置选中互斥
    def set_pushbutton_group(self,gridlayout_Point):
        #获取gridlayout_Point控件中所有pushbutton
        pushbutton_list=gridlayout_Point.findChildren(QPushButton)
        #将pushbutton添加到组中，并设置选中互斥
        self.group=QButtonGroup()
        for pushbutton in pushbutton_list:
            self.group.addButton(pushbutton)
        self.group.setExclusive(True)
        self.group.buttonClicked.connect(self.pushbutton_clicked)
    
    #pushbutton被点击时触发
    def pushbutton_clicked(self,pushbutton):
        #获取被点击的pushbutton
        self.pushbutton_clicked_pushbutton=pushbutton
        #获取被点击的pushbutton的文本
        self.pushbutton_clicked_text=pushbutton.text()
    

#用一个定时器刷新widget控件
class MyTimer(QtCore.QTimer):
    def __init__(self, parent=None):
        super(MyTimer, self).__init__(parent)
        self.setInterval(1000)
        self.timeout.connect(self.refresh_widget)

    def refresh_widget(self):
        self.parent().refresh_widget()     

if __name__ == '__main__':
    # 自适应分辨率解决窗口错位代码
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    # 每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    app = QApplication(sys.argv)
    
    #启动界面
    splash_pix = QPixmap('splash.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.show()
    app.processEvents()
    # 加载界面
    myWin = MyloginMainForm()
    # 显示在屏幕上
    myWin.show()
    myWin.run_external_app()
    splash.finish(myWin)
    
    # 设置定时器，每隔100毫秒刷新一次widget控件
    myTimer = MyTimer(myWin)
    myTimer.start()
    
    
    
    sys.exit(app.exec_())


