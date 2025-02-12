from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class AdminUi(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1040, 842)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(439, 590))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("free-icon-hospital-sign-883337.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("QDialog{\n"
"    background-color: white;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.btn_36 = QtWidgets.QPushButton(Dialog)
        self.btn_36.setStyleSheet("QPushButton{\n"
"    border-radius: 1px;\n"
"    color:white;\n"
"\n"
"}")
        self.btn_36.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/Home-2-2-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_36.setIcon(icon1)
        self.btn_36.setIconSize(QtCore.QSize(23, 23))
        self.btn_36.setObjectName("btn_36")
        self.horizontalLayout_32.addWidget(self.btn_36)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_32.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_32)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(396, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btn_12 = QtWidgets.QPushButton(Dialog)
        self.btn_12.setStyleSheet("QPushButton{\n"
"\n"
"    border: none;\n"
"    background-color: white;\n"
"\n"
"}")
        self.btn_12.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/hospital-3_icon-icons.com_66075.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_12.setIcon(icon2)
        self.btn_12.setIconSize(QtCore.QSize(50, 50))
        self.btn_12.setObjectName("btn_12")
        self.horizontalLayout_2.addWidget(self.btn_12)
        spacerItem2 = QtWidgets.QSpacerItem(396, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.stackedWidget_6 = QtWidgets.QStackedWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget_6.sizePolicy().hasHeightForWidth())
        self.stackedWidget_6.setSizePolicy(sizePolicy)
        self.stackedWidget_6.setObjectName("stackedWidget_6")
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.page_8)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.btn_2 = QtWidgets.QPushButton(self.page_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setMinimumSize(QtCore.QSize(91, 31))
        self.btn_2.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-color: #a6f7f1;\n"
"       transition: 2s linear; \n"
"    color: #4c4d4d;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #89f0ea;\n"
"}\n"
"\n"
"")
        self.btn_2.setObjectName("btn_2")
        self.horizontalLayout_10.addWidget(self.btn_2)
        self.btn_3 = QtWidgets.QPushButton(self.page_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setMinimumSize(QtCore.QSize(91, 31))
        self.btn_3.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-color: #a6f7f1;\n"
"       transition: 2s linear; \n"
"    color: #4c4d4d;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #89f0ea;\n"
"}\n"
"\n"
"")
        self.btn_3.setObjectName("btn_3")
        self.horizontalLayout_10.addWidget(self.btn_3)
        self.btn_15 = QtWidgets.QPushButton(self.page_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_15.sizePolicy().hasHeightForWidth())
        self.btn_15.setSizePolicy(sizePolicy)
        self.btn_15.setMinimumSize(QtCore.QSize(91, 31))
        self.btn_15.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-color: #a6f7f1;\n"
"       transition: 2s linear; \n"
"    color: #4c4d4d;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #89f0ea;\n"
"}\n"
"\n"
"")
        self.btn_15.setObjectName("btn_15")
        self.horizontalLayout_10.addWidget(self.btn_15)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.gridLayout_11.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.page_8)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.page_5)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.widget_2 = QtWidgets.QWidget(self.tab_3)
        self.widget_2.setObjectName("widget_2")
        self.wid = QVBoxLayout(self.widget_2)
        self.figure = plt.figure()
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self.figure)
        self.wid.addWidget(self.canvas)
        self.gridLayout_14.addWidget(self.widget_2, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_3.setMinimumSize(QtCore.QSize(420, 0))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(4)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.tableWidget_3)
        self.horizontalLayout_21.addLayout(self.verticalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem6)
        self.gridLayout_15.addLayout(self.horizontalLayout_21, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab, "")
        self.gridLayout_13.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_5)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.page)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_39 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.tab_2)
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_7)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.btn_22 = QtWidgets.QPushButton(self.page_7)
        self.btn_22.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    color: white;\n"
"    \n"
"}")
        self.btn_22.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/Icons8-Ios7-Arrows-Back.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_22.setIcon(icon3)
        self.btn_22.setObjectName("btn_22")
        self.horizontalLayout_18.addWidget(self.btn_22)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem7)
        self.verticalLayout_7.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.tableWidget = QtWidgets.QTableWidget(self.page_7)
        self.tableWidget.setMinimumSize(QtCore.QSize(321, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(321, 16777215))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(153)
        self.horizontalLayout_7.addWidget(self.tableWidget)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem10)
        self.btn_14 = QtWidgets.QPushButton(self.page_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_14.sizePolicy().hasHeightForWidth())
        self.btn_14.setSizePolicy(sizePolicy)
        self.btn_14.setMinimumSize(QtCore.QSize(91, 31))
        self.btn_14.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-color: #a6f7f1;\n"
"       transition: 2s linear; \n"
"    color: #4c4d4d;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #89f0ea;\n"
"}\n"
"\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/plus_icon-icons.com_61187.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_14.setIcon(icon4)
        self.btn_14.setObjectName("btn_14")
        self.horizontalLayout_19.addWidget(self.btn_14)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem11)
        self.verticalLayout_8.addLayout(self.horizontalLayout_19)
        self.gridLayout_2.addLayout(self.verticalLayout_8, 0, 0, 1, 1)
        self.stackedWidget_3.addWidget(self.page_7)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.page_9)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem12, 0, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem13, 1, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btn_9 = QtWidgets.QPushButton(self.page_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setMinimumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-color: #a6f7f1;\n"
"       transition: 2s linear; \n"
"    color: #4c4d4d;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #89f0ea;\n"
"}\n"
"\n"
"")
        self.btn_9.setObjectName("btn_9")
        self.verticalLayout_6.addWidget(self.btn_9)
        self.btn_10 = QtWidgets.QPushButton(self.page_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_10.sizePolicy().hasHeightForWidth())
        self.btn_10.setSizePolicy(sizePolicy)
        self.btn_10.setMinimumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_10.setFont(font)
        self.btn_10.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-color: #a6f7f1;\n"
"       transition: 2s linear; \n"
"    color: #4c4d4d;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #89f0ea;\n"
"}\n"
"\n"
"")
        self.btn_10.setObjectName("btn_10")
        self.verticalLayout_6.addWidget(self.btn_10)
        self.gridLayout_10.addLayout(self.verticalLayout_6, 1, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem14, 1, 2, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem15, 2, 1, 1, 1)
        self.verticalLayout_40.addLayout(self.gridLayout_10)
        self.stackedWidget_3.addWidget(self.page_9)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.verticalLayout_41 = QtWidgets.QVBoxLayout(self.page_10)
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.btn_20 = QtWidgets.QPushButton(self.page_10)
        self.btn_20.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    color: white;\n"
"    \n"
"}")
        self.btn_20.setText("")
        self.btn_20.setIcon(icon3)
        self.btn_20.setObjectName("btn_20")
        self.horizontalLayout_12.addWidget(self.btn_20)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem16)
        self.verticalLayout_21.addLayout(self.horizontalLayout_12)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_21.addItem(spacerItem17)
        self.verticalLayout_22.addLayout(self.verticalLayout_21)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem18)
        self.line_33 = QtWidgets.QLineEdit(self.page_10)
        self.line_33.setMinimumSize(QtCore.QSize(163, 27))
        self.line_33.setMaximumSize(QtCore.QSize(262, 27))
        self.line_33.setObjectName("line_33")
        self.horizontalLayout_13.addWidget(self.line_33)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem19)
        self.verticalLayout_19.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem20)
        self.btn_7 = QtWidgets.QPushButton(self.page_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setMinimumSize(QtCore.QSize(91, 31))
        self.btn_7.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-color: #a6f7f1;\n"
"       transition: 2s linear; \n"
"    color: #4c4d4d;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #89f0ea;\n"
"}\n"
"\n"
"")
        self.btn_7.setObjectName("btn_7")
        self.horizontalLayout_14.addWidget(self.btn_7)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem21)
        self.verticalLayout_19.addLayout(self.horizontalLayout_14)
        self.verticalLayout_22.addLayout(self.verticalLayout_19)
        self.verticalLayout_23.addLayout(self.verticalLayout_22)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem22)
        self.label_33 = QtWidgets.QLabel(self.page_10)
        self.label_33.setMinimumSize(QtCore.QSize(181, 20))
        self.label_33.setText("")
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_15.addWidget(self.label_33)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem23)
        self.verticalLayout_20.addLayout(self.horizontalLayout_15)
        spacerItem24 = QtWidgets.QSpacerItem(16, 26, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_20.addItem(spacerItem24)
        self.verticalLayout_23.addLayout(self.verticalLayout_20)
        self.verticalLayout_41.addLayout(self.verticalLayout_23)
        self.stackedWidget_3.addWidget(self.page_10)
        self.verticalLayout_39.addWidget(self.stackedWidget_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.widget)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setObjectName("page_11")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_11)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout()
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.horizontalLayout_51 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        self.btn_19 = QtWidgets.QPushButton(self.page_11)
        self.btn_19.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    color: white;\n"
"    \n"
"}")
        self.btn_19.setText("")
        self.btn_19.setIcon(icon3)
        self.btn_19.setObjectName("btn_19")
        self.horizontalLayout_51.addWidget(self.btn_19)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_51.addItem(spacerItem25)
        self.verticalLayout_36.addLayout(self.horizontalLayout_51)
        spacerItem26 = QtWidgets.QSpacerItem(20, 31, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_36.addItem(spacerItem26)
        self.verticalLayout_3.addLayout(self.verticalLayout_36)
        self.horizontalLayout_52 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_52.setObjectName("horizontalLayout_52")
        self.horizontalLayout_50 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_50.setObjectName("horizontalLayout_50")
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_50.addItem(spacerItem27)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.page_11)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.line_2 = QtWidgets.QLineEdit(self.page_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setMaximumSize(QtCore.QSize(179, 16777215))
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)
        self.gridLayout_7.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_5 = QtWidgets.QLabel(self.page_11)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_11.addWidget(self.label_5)
        self.line_5 = QtWidgets.QLineEdit(self.page_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_5.sizePolicy().hasHeightForWidth())
        self.line_5.setSizePolicy(sizePolicy)
        self.line_5.setMaximumSize(QtCore.QSize(179, 16777215))
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_11.addWidget(self.line_5)
        self.gridLayout_7.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label = QtWidgets.QLabel(self.page_11)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_22.addWidget(self.label)
        self.line = QtWidgets.QLineEdit(self.page_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMaximumSize(QtCore.QSize(179, 16777215))
        self.line.setObjectName("line")
        self.horizontalLayout_22.addWidget(self.line)
        self.gridLayout_7.addLayout(self.horizontalLayout_22, 2, 0, 1, 1)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_6 = QtWidgets.QLabel(self.page_11)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_27.addWidget(self.label_6)
        self.line_8 = QtWidgets.QLineEdit(self.page_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_8.sizePolicy().hasHeightForWidth())
        self.line_8.setSizePolicy(sizePolicy)
        self.line_8.setMaximumSize(QtCore.QSize(179, 16777215))
        self.line_8.setObjectName("line_8")
        self.horizontalLayout_27.addWidget(self.line_8)
        self.gridLayout_7.addLayout(self.horizontalLayout_27, 3, 0, 1, 1)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_4 = QtWidgets.QLabel(self.page_11)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_28.addWidget(self.label_4)
        self.line_4 = QtWidgets.QLineEdit(self.page_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy)
        self.line_4.setMaximumSize(QtCore.QSize(179, 16777215))
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_28.addWidget(self.line_4)
        self.gridLayout_7.addLayout(self.horizontalLayout_28, 4, 0, 1, 1)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_7 = QtWidgets.QLabel(self.page_11)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_29.addWidget(self.label_7)
        self.line_7 = QtWidgets.QLineEdit(self.page_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_7.sizePolicy().hasHeightForWidth())
        self.line_7.setSizePolicy(sizePolicy)
        self.line_7.setMaximumSize(QtCore.QSize(179, 16777215))
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_29.addWidget(self.line_7)
        self.gridLayout_7.addLayout(self.horizontalLayout_29, 5, 0, 1, 1)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.label_3 = QtWidgets.QLabel(self.page_11)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_30.addWidget(self.label_3)
        self.line_6 = QtWidgets.QLineEdit(self.page_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_6.sizePolicy().hasHeightForWidth())
        self.line_6.setSizePolicy(sizePolicy)
        self.line_6.setMaximumSize(QtCore.QSize(179, 16777215))
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_30.addWidget(self.line_6)
        self.gridLayout_7.addLayout(self.horizontalLayout_30, 6, 0, 1, 1)
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_8 = QtWidgets.QLabel(self.page_11)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_31.addWidget(self.label_8)
        self.line_3 = QtWidgets.QLineEdit(self.page_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        self.line_3.setMaximumSize(QtCore.QSize(179, 16777215))
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_31.addWidget(self.line_3)
        self.gridLayout_7.addLayout(self.horizontalLayout_31, 7, 0, 1, 1)
        self.horizontalLayout_50.addLayout(self.gridLayout_7)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_50.addItem(spacerItem28)
        self.horizontalLayout_52.addLayout(self.horizontalLayout_50)
        spacerItem29 = QtWidgets.QSpacerItem(30, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_52.addItem(spacerItem29)
        self.verticalLayout_3.addLayout(self.horizontalLayout_52)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem30)
        self.label_34 = QtWidgets.QLabel(self.page_11)
        self.label_34.setMinimumSize(QtCore.QSize(171, 20))
        self.label_34.setText("")
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_17.addWidget(self.label_34)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem31)
        self.verticalLayout_18.addLayout(self.horizontalLayout_17)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem32)
        self.btn_4 = QtWidgets.QPushButton(self.page_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setMinimumSize(QtCore.QSize(91, 31))
        self.btn_4.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-color: #a6f7f1;\n"
"       transition: 2s linear; \n"
"    color: #4c4d4d;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #89f0ea;\n"
"}\n"
"\n"
"")
        self.btn_4.setObjectName("btn_4")
        self.horizontalLayout_4.addWidget(self.btn_4)
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem33)
        self.verticalLayout_17.addLayout(self.horizontalLayout_4)
        spacerItem34 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_17.addItem(spacerItem34)
        self.verticalLayout_18.addLayout(self.verticalLayout_17)
        self.verticalLayout_5.addLayout(self.verticalLayout_18)
        self.gridLayout_6.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.stackedWidget_2.addWidget(self.page_11)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_38 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem35 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem35, 0, 1, 1, 1)
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem36, 1, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_5 = QtWidgets.QPushButton(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setMinimumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-color: #a6f7f1;\n"
"       transition: 2s linear; \n"
"    color: #4c4d4d;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #89f0ea;\n"
"}\n"
"\n"
"")
        self.btn_5.setObjectName("btn_5")
        self.verticalLayout_4.addWidget(self.btn_5)
        self.btn_6 = QtWidgets.QPushButton(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setMinimumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-color: #a6f7f1;\n"
"       transition: 2s linear; \n"
"    color: #4c4d4d;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #89f0ea;\n"
"}\n"
"\n"
"")
        self.btn_6.setObjectName("btn_6")
        self.verticalLayout_4.addWidget(self.btn_6)
        self.gridLayout_5.addLayout(self.verticalLayout_4, 1, 1, 1, 1)
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem37, 1, 2, 1, 1)
        spacerItem38 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem38, 2, 1, 1, 1)
        self.verticalLayout_38.addLayout(self.gridLayout_5)
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.btn_21 = QtWidgets.QPushButton(self.page_4)
        self.btn_21.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    color: white;\n"
"    \n"
"}")
        self.btn_21.setText("")
        self.btn_21.setIcon(icon3)
        self.btn_21.setObjectName("btn_21")
        self.horizontalLayout_16.addWidget(self.btn_21)
        spacerItem39 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem39)
        self.verticalLayout_9.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem40 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem40)
        self.btn_66 = QtWidgets.QPushButton(self.page_4)
        self.btn_66.setStyleSheet("QPushButton{\n"
"\n"
"    background-color: white;\n"
"\n"
"}")
        self.btn_66.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/az.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_66.setIcon(icon5)
        self.btn_66.setIconSize(QtCore.QSize(25, 25))
        self.btn_66.setObjectName("btn_66")
        self.horizontalLayout_5.addWidget(self.btn_66)
        self.btn_67 = QtWidgets.QPushButton(self.page_4)
        self.btn_67.setStyleSheet("QPushButton{\n"
"\n"
"    background-color: white;\n"
"\n"
"}")
        self.btn_67.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/za.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_67.setIcon(icon6)
        self.btn_67.setIconSize(QtCore.QSize(25, 25))
        self.btn_67.setObjectName("btn_67")
        self.horizontalLayout_5.addWidget(self.btn_67)
        spacerItem41 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem41)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem42 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem42)
        self.table_3 = QtWidgets.QTableWidget(self.page_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_3.sizePolicy().hasHeightForWidth())
        self.table_3.setSizePolicy(sizePolicy)
        self.table_3.setMinimumSize(QtCore.QSize(0, 0))
        self.table_3.setMaximumSize(QtCore.QSize(863, 16777215))
        self.table_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table_3.setLineWidth(1)
        self.table_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table_3.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_3.setAutoScroll(True)
        self.table_3.setAutoScrollMargin(18)
        self.table_3.setTabKeyNavigation(True)
        self.table_3.setObjectName("table_3")
        self.table_3.setColumnCount(9)
        self.table_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_3.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_3.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_3.setHorizontalHeaderItem(8, item)
        self.table_3.horizontalHeader().setDefaultSectionSize(96)
        self.table_3.horizontalHeader().setMinimumSectionSize(17)
        self.table_3.verticalHeader().setDefaultSectionSize(30)
        self.table_3.verticalHeader().setHighlightSections(True)
        self.table_3.verticalHeader().setMinimumSectionSize(15)
        self.table_3.verticalHeader().setSortIndicatorShown(False)
        self.horizontalLayout_8.addWidget(self.table_3)
        spacerItem43 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem43)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem44 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem44)
        self.btn_13 = QtWidgets.QPushButton(self.page_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_13.sizePolicy().hasHeightForWidth())
        self.btn_13.setSizePolicy(sizePolicy)
        self.btn_13.setMinimumSize(QtCore.QSize(91, 31))
        self.btn_13.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-color: #a6f7f1;\n"
"       transition: 2s linear; \n"
"    color: #4c4d4d;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #89f0ea;\n"
"}\n"
"\n"
"")
        self.btn_13.setIcon(icon4)
        self.btn_13.setObjectName("btn_13")
        self.horizontalLayout_6.addWidget(self.btn_13)
        self.btn_16 = QtWidgets.QPushButton(self.page_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_16.sizePolicy().hasHeightForWidth())
        self.btn_16.setSizePolicy(sizePolicy)
        self.btn_16.setMinimumSize(QtCore.QSize(91, 31))
        self.btn_16.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-color: #a6f7f1;\n"
"       transition: 2s linear; \n"
"    color: #4c4d4d;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #89f0ea;\n"
"}\n"
"\n"
"")
        self.btn_16.setIcon(icon4)
        self.btn_16.setObjectName("btn_16")
        self.horizontalLayout_6.addWidget(self.btn_16)
        spacerItem45 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem45)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        self.gridLayout_8.addLayout(self.verticalLayout_9, 0, 0, 1, 1)
        self.stackedWidget_2.addWidget(self.page_4)
        self.gridLayout_4.addWidget(self.stackedWidget_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.widget, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_53 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_53.setObjectName("horizontalLayout_53")
        self.btn_23 = QtWidgets.QPushButton(self.page_2)
        self.btn_23.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    color: white;\n"
"    \n"
"}")
        self.btn_23.setText("")
        self.btn_23.setIcon(icon3)
        self.btn_23.setObjectName("btn_23")
        self.horizontalLayout_53.addWidget(self.btn_23)
        spacerItem46 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_53.addItem(spacerItem46)
        self.verticalLayout_14.addLayout(self.horizontalLayout_53)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        spacerItem47 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem47)
        self.label_35 = QtWidgets.QLabel(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_23.addWidget(self.label_35)
        spacerItem48 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem48)
        self.verticalLayout_13.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        spacerItem49 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem49)
        spacerItem50 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem50)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setSpacing(7)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.line_9 = QtWidgets.QLineEdit(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_9.sizePolicy().hasHeightForWidth())
        self.line_9.setSizePolicy(sizePolicy)
        self.line_9.setMinimumSize(QtCore.QSize(230, 33))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.line_9.setFont(font)
        self.line_9.setStyleSheet("QLineEdit{\n"
"    padding-top: 0px;\n"
"    padding-left: 3px;\n"
"    text-align: center;\n"
"    background-color: rgb(235, 235, 235);\n"
"    border-radius: 5px;\n"
"    border: 4px double black;\n"
"       transition: 2s linear; \n"
"    color: black;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    background-color: rgb(207, 207, 207);\n"
"}    ")
        self.line_9.setObjectName("line_9")
        self.horizontalLayout_26.addWidget(self.line_9)
        self.btn_69 = QtWidgets.QPushButton(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_69.sizePolicy().hasHeightForWidth())
        self.btn_69.setSizePolicy(sizePolicy)
        self.btn_69.setMinimumSize(QtCore.QSize(35, 28))
        self.btn_69.setStyleSheet("QPushButton{\n"
"    background-color: white;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(244, 244, 244);\n"
"}")
        self.btn_69.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_69.setIcon(icon7)
        self.btn_69.setIconSize(QtCore.QSize(25, 25))
        self.btn_69.setObjectName("btn_69")
        self.horizontalLayout_26.addWidget(self.btn_69)
        self.verticalLayout_10.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.line_10 = QtWidgets.QLineEdit(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_10.sizePolicy().hasHeightForWidth())
        self.line_10.setSizePolicy(sizePolicy)
        self.line_10.setMinimumSize(QtCore.QSize(230, 33))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.line_10.setFont(font)
        self.line_10.setStyleSheet("QLineEdit{\n"
"    padding-top: 0px;\n"
"    padding-left: 3px;\n"
"    text-align: center;\n"
"    background-color: rgb(235, 235, 235);\n"
"    border-radius: 5px;\n"
"    border: 4px double black;\n"
"       transition: 2s linear; \n"
"    color: black;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    background-color: rgb(207, 207, 207);\n"
"}    ")
        self.line_10.setObjectName("line_10")
        self.horizontalLayout_24.addWidget(self.line_10)
        self.btn_70 = QtWidgets.QPushButton(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_70.sizePolicy().hasHeightForWidth())
        self.btn_70.setSizePolicy(sizePolicy)
        self.btn_70.setMinimumSize(QtCore.QSize(35, 28))
        self.btn_70.setStyleSheet("QPushButton{\n"
"    background-color: white;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(244, 244, 244);\n"
"}")
        self.btn_70.setText("")
        self.btn_70.setIcon(icon7)
        self.btn_70.setIconSize(QtCore.QSize(25, 25))
        self.btn_70.setObjectName("btn_70")
        self.horizontalLayout_24.addWidget(self.btn_70)
        self.verticalLayout_10.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_25.addLayout(self.verticalLayout_10)
        spacerItem51 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem51)
        self.verticalLayout_13.addLayout(self.horizontalLayout_25)
        self.verticalLayout_14.addLayout(self.verticalLayout_13)
        self.verticalLayout_16.addLayout(self.verticalLayout_14)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        spacerItem52 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_15.addItem(spacerItem52)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem53 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem53)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.page_2)
        self.tableWidget_2.setMinimumSize(QtCore.QSize(700, 0))
        self.tableWidget_2.setMaximumSize(QtCore.QSize(702, 16777215))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(7)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        self.horizontalLayout_9.addWidget(self.tableWidget_2)
        spacerItem54 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem54)
        self.verticalLayout_15.addLayout(self.horizontalLayout_9)
        self.verticalLayout_16.addLayout(self.verticalLayout_15)
        self.gridLayout_9.addLayout(self.verticalLayout_16, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout_11.addWidget(self.stackedWidget, 1, 0, 1, 1)
        self.stackedWidget_6.addWidget(self.page_8)
        self.page_15 = QtWidgets.QWidget()
        self.page_15.setObjectName("page_15")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.page_15)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        spacerItem55 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem55)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem56 = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem56)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_8 = QtWidgets.QPushButton(self.page_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setMinimumSize(QtCore.QSize(151, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-color: #a6f7f1;\n"
"       transition: 2s linear; \n"
"    color: #4c4d4d;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #89f0ea;\n"
"}\n"
"\n"
"")
        self.btn_8.setObjectName("btn_8")
        self.horizontalLayout.addWidget(self.btn_8)
        spacerItem57 = QtWidgets.QSpacerItem(8, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem57)
        self.btn_11 = QtWidgets.QPushButton(self.page_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_11.sizePolicy().hasHeightForWidth())
        self.btn_11.setSizePolicy(sizePolicy)
        self.btn_11.setMinimumSize(QtCore.QSize(151, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_11.setFont(font)
        self.btn_11.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-color: #a6f7f1;\n"
"       transition: 2s linear; \n"
"    color: #4c4d4d;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #89f0ea;\n"
"}\n"
"\n"
"")
        self.btn_11.setObjectName("btn_11")
        self.horizontalLayout.addWidget(self.btn_11)
        spacerItem58 = QtWidgets.QSpacerItem(8, 18, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem58)
        self.btn_18 = QtWidgets.QPushButton(self.page_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_18.sizePolicy().hasHeightForWidth())
        self.btn_18.setSizePolicy(sizePolicy)
        self.btn_18.setMinimumSize(QtCore.QSize(151, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_18.setFont(font)
        self.btn_18.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-color: #a6f7f1;\n"
"       transition: 2s linear; \n"
"    color: #4c4d4d;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #89f0ea;\n"
"}\n"
"\n"
"")
        self.btn_18.setObjectName("btn_18")
        self.horizontalLayout.addWidget(self.btn_18)
        self.horizontalLayout_20.addLayout(self.horizontalLayout)
        spacerItem59 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem59)
        self.verticalLayout_11.addLayout(self.horizontalLayout_20)
        spacerItem60 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem60)
        self.gridLayout_12.addLayout(self.verticalLayout_11, 0, 0, 1, 1)
        self.stackedWidget_6.addWidget(self.page_15)
        self.gridLayout.addWidget(self.stackedWidget_6, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.stackedWidget_6.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)
        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Администрация"))
        self.btn_2.setText(_translate("Dialog", "Специалисты"))
        self.btn_3.setText(_translate("Dialog", "Пациенты"))
        self.btn_15.setText(_translate("Dialog", "Диагнозы"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("Dialog", "Статистика"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Пациент"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Диагноз"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Специалист"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("Dialog", "Список"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Специальность"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Количество специалистов"))
        self.btn_14.setText(_translate("Dialog", "Специальность"))
        self.btn_9.setText(_translate("Dialog", "Показать список\n"
"специальностей"))
        self.btn_10.setText(_translate("Dialog", "Добавить новую \n"
"специальность"))
        self.btn_7.setText(_translate("Dialog", "Добавить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Специальности"))
        self.label_2.setText(_translate("Dialog", "Имя:"))
        self.label_5.setText(_translate("Dialog", "Фамилия:"))
        self.label.setText(_translate("Dialog", "Отчество:"))
        self.label_6.setText(_translate("Dialog", "Дата рождения:"))
        self.label_4.setText(_translate("Dialog", "Специальность:"))
        self.label_7.setText(_translate("Dialog", "Логин:"))
        self.label_3.setText(_translate("Dialog", "Пароль"))
        self.label_8.setText(_translate("Dialog", "Первонач. ЗП:"))
        self.btn_4.setText(_translate("Dialog", "Добавить"))
        self.btn_5.setText(_translate("Dialog", "Показать список\n"
"специалистов"))
        self.btn_6.setText(_translate("Dialog", "Добавить специалиста"))
        item = self.table_3.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Фамилия"))
        item = self.table_3.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Имя"))
        item = self.table_3.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Отчество"))
        item = self.table_3.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Дата рождения"))
        item = self.table_3.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Логин"))
        item = self.table_3.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Пароль"))
        item = self.table_3.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Специальность"))
        item = self.table_3.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "Зарплата"))
        item = self.table_3.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "Премия"))
        self.btn_13.setText(_translate("Dialog", "Специалист"))
        self.btn_16.setText(_translate("Dialog", "Премия"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("Dialog", "Специалисты"))
        self.label_35.setText(_translate("Dialog", "Поиск пациентов:"))
        self.line_9.setPlaceholderText(_translate("Dialog", "Введите ФИО специалиста..."))
        self.line_10.setPlaceholderText(_translate("Dialog", "Введите ФИО пациента..."))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Имя"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Фамилия"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Отчество"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Врач"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Дата рождения"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Почта"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Телефон"))
        self.btn_8.setText(_translate("Dialog", "Специалисты"))
        self.btn_11.setText(_translate("Dialog", "Пациенты"))
        self.btn_18.setText(_translate("Dialog", "Диагнозы"))
