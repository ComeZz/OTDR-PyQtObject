# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Mainwindows.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QTextEdit, QToolButton,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1250, 926)
        MainWindow.setStyleSheet(u"QWidget#centralwidget\n"
"{\n"
"	background-color: rgb(176, 199, 216);	\n"
"}\n"
"QWidget#button_widget,QFrame#tool_frame\n"
"{\n"
"	border:3px solid;\n"
"\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(162, 185, 202, 255), stop:1 rgba(104, 121, 134, 255));	\n"
"	border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(185, 212, 231, 255), stop:1 rgba(189, 213, 229, 255));\n"
"	\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(162, 185, 202, 255), stop:1 rgba(104, 121, 134, 255));\n"
"	\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(185, 212, 231, 255), stop:1 rgba(189, 213, 229, 255));\n"
"}\n"
"\n"
"QWidget#luciol_widget\n"
"{\n"
"	border:2px solid;\n"
"\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(162, 185, 202, 255), stop:1 rgba(104, 121, 134, 255));	\n"
"	border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:"
                        "1, y2:1, stop:0 rgba(185, 212, 231, 255), stop:1 rgba(189, 213, 229, 255));\n"
"	\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(162, 185, 202, 255), stop:1 rgba(104, 121, 134, 255));\n"
"	\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(185, 212, 231, 255), stop:1 rgba(189, 213, 229, 255));\n"
"}\n"
"\n"
"QTableView,QTextEdit\n"
"{\n"
"	border:3px solid;\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(162, 185, 202, 255), stop:1 rgba(104, 121, 134, 255));	\n"
"	border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(185, 212, 231, 255), stop:1 rgba(189, 213, 229, 255));\n"
"	\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(162, 185, 202, 255), stop:1 rgba(104, 121, 134, 255));\n"
"	\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(185, 212, 231, 255), stop:1 rgba(189, 213, 229, 255)"
                        ");\n"
"}\n"
"\n"
"QToolButton\n"
"{\n"
"	border:2px solid;\n"
"	border-radius: 5px;\n"
"	border-color: rgb(178, 178, 178);\n"
"	background-color: qlineargradient(spread:pad, x1:0.477, y1:0, x2:0.5, y2:1, stop:0 rgba(231, 231, 231, 255), stop:1 rgba(206, 206, 206, 255));\n"
"	\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout.addWidget(self.tableView, 2, 1, 1, 1)

        self.tool_frame = QFrame(self.centralwidget)
        self.tool_frame.setObjectName(u"tool_frame")
        self.tool_frame.setMinimumSize(QSize(0, 60))
        self.tool_frame.setFrameShape(QFrame.StyledPanel)
        self.tool_frame.setFrameShadow(QFrame.Raised)
        self.tool_frame.setLineWidth(2)
        self.tool_frame.setMidLineWidth(1)
        self.horizontalLayout = QHBoxLayout(self.tool_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Config_toolButton = QToolButton(self.tool_frame)
        self.Config_toolButton.setObjectName(u"Config_toolButton")
        self.Config_toolButton.setMinimumSize(QSize(100, 40))
        self.Config_toolButton.setBaseSize(QSize(70, 50))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        font.setPointSize(13)
        font.setBold(False)
        self.Config_toolButton.setFont(font)

        self.horizontalLayout.addWidget(self.Config_toolButton)

        self.toolButton_2 = QToolButton(self.tool_frame)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setMinimumSize(QSize(100, 40))
        self.toolButton_2.setBaseSize(QSize(70, 50))
        self.toolButton_2.setFont(font)

        self.horizontalLayout.addWidget(self.toolButton_2)

        self.toolButton_3 = QToolButton(self.tool_frame)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setMinimumSize(QSize(100, 40))
        self.toolButton_3.setBaseSize(QSize(70, 50))
        self.toolButton_3.setFont(font)

        self.horizontalLayout.addWidget(self.toolButton_3)

        self.toolButton_4 = QToolButton(self.tool_frame)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setMinimumSize(QSize(100, 40))
        self.toolButton_4.setBaseSize(QSize(70, 50))
        self.toolButton_4.setFont(font)

        self.horizontalLayout.addWidget(self.toolButton_4)

        self.toolButton_5 = QToolButton(self.tool_frame)
        self.toolButton_5.setObjectName(u"toolButton_5")
        self.toolButton_5.setMinimumSize(QSize(100, 40))
        self.toolButton_5.setBaseSize(QSize(70, 50))
        self.toolButton_5.setFont(font)

        self.horizontalLayout.addWidget(self.toolButton_5)

        self.toolButton_exit = QToolButton(self.tool_frame)
        self.toolButton_exit.setObjectName(u"toolButton_exit")
        self.toolButton_exit.setMinimumSize(QSize(100, 40))
        self.toolButton_exit.setBaseSize(QSize(70, 50))
        self.toolButton_exit.setFont(font)

        self.horizontalLayout.addWidget(self.toolButton_exit)

        self.horizontalSpacer_2 = QSpacerItem(573, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout.addWidget(self.tool_frame, 0, 0, 1, 2)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout.addWidget(self.textEdit, 2, 0, 1, 1)

        self.luciol_widget = QWidget(self.centralwidget)
        self.luciol_widget.setObjectName(u"luciol_widget")
        self.luciol_widget.setMinimumSize(QSize(808, 551))
        self.luciol_widget.setMaximumSize(QSize(809, 552))
        self.luciol_widget.setBaseSize(QSize(825, 568))
        self.gridLayout_3 = QGridLayout(self.luciol_widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(1, 1, 1, 1)

        self.gridLayout.addWidget(self.luciol_widget, 1, 1, 1, 1)

        self.button_widget = QWidget(self.centralwidget)
        self.button_widget.setObjectName(u"button_widget")
        self.button_widget.setMinimumSize(QSize(100, 0))
        self.button_widget.setStyleSheet(u"QPushButton\n"
"{\n"
"	max-width:40px;\n"
"	max-height:40px;\n"
"	min-width:40px;\n"
"	min-height:40px;\n"
"	border:1px solid;\n"
"	border-radius: 20px;\n"
"	border-color: rgb(178, 178, 178);\n"
"	background-color: qlineargradient(spread:pad, x1:0.477, y1:0, x2:0.5, y2:1, stop:0 rgba(231, 231, 231, 255), stop:1 rgba(206, 206, 206, 255));\n"
"	font-weight:bold;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: qradialgradient(spread:pad, cx:0.529851, cy:0.506, radius:0.5, fx:0.532, fy:0.505682, stop:0 rgba(94, 223, 201, 255), stop:1 rgba(105, 193, 194, 255));\n"
"}\n"
"\n"
"QPushButton:checked\n"
"{\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(174, 210, 255, 255), stop:1 rgba(149, 195, 238, 255));\n"
"}\n"
"\n"
"")
        self.layoutWidget = QWidget(self.button_widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 10, 331, 411))
        self.gridLayout_Point = QGridLayout(self.layoutWidget)
        self.gridLayout_Point.setObjectName(u"gridLayout_Point")
        self.gridLayout_Point.setContentsMargins(0, 0, 0, 0)
        self.pushButton_A = QPushButton(self.layoutWidget)
        self.pushButton_A.setObjectName(u"pushButton_A")
        self.pushButton_A.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_A, 0, 0, 1, 1)

        self.pushButton_B = QPushButton(self.layoutWidget)
        self.pushButton_B.setObjectName(u"pushButton_B")
        self.pushButton_B.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_B, 0, 1, 1, 1)

        self.pushButton_C = QPushButton(self.layoutWidget)
        self.pushButton_C.setObjectName(u"pushButton_C")
        self.pushButton_C.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_C, 0, 2, 1, 1)

        self.pushButton_D = QPushButton(self.layoutWidget)
        self.pushButton_D.setObjectName(u"pushButton_D")
        self.pushButton_D.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_D, 0, 3, 1, 1)

        self.pushButton_E = QPushButton(self.layoutWidget)
        self.pushButton_E.setObjectName(u"pushButton_E")
        self.pushButton_E.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_E, 1, 0, 1, 1)

        self.pushButton_F = QPushButton(self.layoutWidget)
        self.pushButton_F.setObjectName(u"pushButton_F")
        self.pushButton_F.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_F, 1, 1, 1, 1)

        self.pushButton_G = QPushButton(self.layoutWidget)
        self.pushButton_G.setObjectName(u"pushButton_G")
        self.pushButton_G.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_G, 1, 2, 1, 1)

        self.pushButton_H = QPushButton(self.layoutWidget)
        self.pushButton_H.setObjectName(u"pushButton_H")
        self.pushButton_H.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_H, 1, 3, 1, 1)

        self.pushButton_J = QPushButton(self.layoutWidget)
        self.pushButton_J.setObjectName(u"pushButton_J")
        self.pushButton_J.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_J, 2, 0, 1, 1)

        self.pushButton_K = QPushButton(self.layoutWidget)
        self.pushButton_K.setObjectName(u"pushButton_K")
        self.pushButton_K.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_K, 2, 1, 1, 1)

        self.pushButton_L = QPushButton(self.layoutWidget)
        self.pushButton_L.setObjectName(u"pushButton_L")
        self.pushButton_L.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_L, 2, 2, 1, 1)

        self.pushButton_M = QPushButton(self.layoutWidget)
        self.pushButton_M.setObjectName(u"pushButton_M")
        self.pushButton_M.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_M, 2, 3, 1, 1)

        self.pushButton_N = QPushButton(self.layoutWidget)
        self.pushButton_N.setObjectName(u"pushButton_N")
        self.pushButton_N.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_N, 3, 0, 1, 1)

        self.pushButton_P = QPushButton(self.layoutWidget)
        self.pushButton_P.setObjectName(u"pushButton_P")
        self.pushButton_P.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_P, 3, 1, 1, 1)

        self.pushButton_R = QPushButton(self.layoutWidget)
        self.pushButton_R.setObjectName(u"pushButton_R")
        self.pushButton_R.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_R, 3, 2, 1, 1)

        self.pushButton_S = QPushButton(self.layoutWidget)
        self.pushButton_S.setObjectName(u"pushButton_S")
        self.pushButton_S.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_S, 3, 3, 1, 1)

        self.pushButton_T = QPushButton(self.layoutWidget)
        self.pushButton_T.setObjectName(u"pushButton_T")
        self.pushButton_T.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_T, 4, 0, 1, 1)

        self.pushButton_U = QPushButton(self.layoutWidget)
        self.pushButton_U.setObjectName(u"pushButton_U")
        self.pushButton_U.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_U, 4, 1, 1, 1)

        self.pushButton_V = QPushButton(self.layoutWidget)
        self.pushButton_V.setObjectName(u"pushButton_V")
        self.pushButton_V.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_V, 4, 2, 1, 1)

        self.pushButton_W = QPushButton(self.layoutWidget)
        self.pushButton_W.setObjectName(u"pushButton_W")
        self.pushButton_W.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_W, 4, 3, 1, 1)

        self.pushButton_X = QPushButton(self.layoutWidget)
        self.pushButton_X.setObjectName(u"pushButton_X")
        self.pushButton_X.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_X, 5, 0, 1, 1)

        self.pushButton_Y = QPushButton(self.layoutWidget)
        self.pushButton_Y.setObjectName(u"pushButton_Y")
        self.pushButton_Y.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_Y, 5, 1, 1, 1)

        self.pushButton_Z = QPushButton(self.layoutWidget)
        self.pushButton_Z.setObjectName(u"pushButton_Z")
        self.pushButton_Z.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_Z, 5, 2, 1, 1)

        self.pushButton_a = QPushButton(self.layoutWidget)
        self.pushButton_a.setObjectName(u"pushButton_a")
        self.pushButton_a.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_a, 5, 3, 1, 1)

        self.pushButton_b = QPushButton(self.layoutWidget)
        self.pushButton_b.setObjectName(u"pushButton_b")
        self.pushButton_b.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_b, 6, 0, 1, 1)

        self.pushButton_c = QPushButton(self.layoutWidget)
        self.pushButton_c.setObjectName(u"pushButton_c")
        self.pushButton_c.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_c, 6, 1, 1, 1)

        self.pushButton_d = QPushButton(self.layoutWidget)
        self.pushButton_d.setObjectName(u"pushButton_d")
        self.pushButton_d.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_d, 6, 2, 1, 1)

        self.pushButton_e = QPushButton(self.layoutWidget)
        self.pushButton_e.setObjectName(u"pushButton_e")
        self.pushButton_e.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_e, 6, 3, 1, 1)

        self.pushButton_f = QPushButton(self.layoutWidget)
        self.pushButton_f.setObjectName(u"pushButton_f")
        self.pushButton_f.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_f, 7, 0, 1, 1)

        self.pushButton_g = QPushButton(self.layoutWidget)
        self.pushButton_g.setObjectName(u"pushButton_g")
        self.pushButton_g.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_g, 7, 1, 1, 1)

        self.pushButton_h = QPushButton(self.layoutWidget)
        self.pushButton_h.setObjectName(u"pushButton_h")
        self.pushButton_h.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_h, 7, 2, 1, 1)

        self.pushButton_j = QPushButton(self.layoutWidget)
        self.pushButton_j.setObjectName(u"pushButton_j")
        self.pushButton_j.setCheckable(True)

        self.gridLayout_Point.addWidget(self.pushButton_j, 7, 3, 1, 1)

        self.widget = QWidget(self.button_widget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 430, 331, 101))
        self.widget.setStyleSheet(u"border-image: url(:/img/GX.png);")

        self.gridLayout.addWidget(self.button_widget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"OTDR\u5149\u7f06\u6d4b\u8bd5\u8bbe\u5907", None))
        self.Config_toolButton.setText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"\u624b\u52a8\u6d4b\u8bd5", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u6d4b\u8bd5", None))
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u4fdd\u5b58", None))
        self.toolButton_5.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.toolButton_exit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u8fd0\u884c\u4e2d...</p></body></html>", None))
        self.pushButton_A.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.pushButton_B.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.pushButton_C.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pushButton_D.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.pushButton_E.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.pushButton_F.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.pushButton_G.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.pushButton_H.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.pushButton_J.setText(QCoreApplication.translate("MainWindow", u"J", None))
        self.pushButton_K.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.pushButton_L.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.pushButton_M.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.pushButton_N.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.pushButton_P.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.pushButton_R.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.pushButton_S.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.pushButton_T.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.pushButton_U.setText(QCoreApplication.translate("MainWindow", u"U", None))
        self.pushButton_V.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.pushButton_W.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.pushButton_X.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.pushButton_Y.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.pushButton_Z.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.pushButton_a.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.pushButton_b.setText(QCoreApplication.translate("MainWindow", u"b", None))
        self.pushButton_c.setText(QCoreApplication.translate("MainWindow", u"c", None))
        self.pushButton_d.setText(QCoreApplication.translate("MainWindow", u"d", None))
        self.pushButton_e.setText(QCoreApplication.translate("MainWindow", u"e", None))
        self.pushButton_f.setText(QCoreApplication.translate("MainWindow", u"f", None))
        self.pushButton_g.setText(QCoreApplication.translate("MainWindow", u"g", None))
        self.pushButton_h.setText(QCoreApplication.translate("MainWindow", u"h", None))
        self.pushButton_j.setText(QCoreApplication.translate("MainWindow", u"j", None))
    # retranslateUi

