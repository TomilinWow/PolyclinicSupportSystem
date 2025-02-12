from PyQt5 import QtCore, QtGui, QtWidgets
import datetime

class SpecialistUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(982, 668)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("QMainWindow{\n"
"    \n"
"    background-color: white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.btn_36 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_36.setStyleSheet("QPushButton{\n"
"    border-radius: 1px;\n"
"    color:white;\n"
"\n"
"}")
        self.btn_36.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Home-2-2-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_36.setIcon(icon)
        self.btn_36.setIconSize(QtCore.QSize(23, 23))
        self.btn_36.setObjectName("btn_36")
        self.horizontalLayout_26.addWidget(self.btn_36)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem)
        self.verticalLayout_15.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"\n"
"}")
        self.btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/cardiogram.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn.setIcon(icon1)
        self.btn.setIconSize(QtCore.QSize(50, 50))
        self.btn.setObjectName("btn")
        self.horizontalLayout_5.addWidget(self.btn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_15.addLayout(self.horizontalLayout_5)
        self.verticalLayout_16.addLayout(self.verticalLayout_15)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.btn_2 = QtWidgets.QPushButton(self.page)
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
        self.horizontalLayout_2.addWidget(self.btn_2)
        self.btn_15 = QtWidgets.QPushButton(self.page)
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
        self.horizontalLayout_2.addWidget(self.btn_15)
        self.btn_3 = QtWidgets.QPushButton(self.page)
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
        self.horizontalLayout_2.addWidget(self.btn_3)
        self.btn_5 = QtWidgets.QPushButton(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setMinimumSize(QtCore.QSize(91, 31))
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
        self.horizontalLayout_2.addWidget(self.btn_5)
        self.btn_38 = QtWidgets.QPushButton(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_38.sizePolicy().hasHeightForWidth())
        self.btn_38.setSizePolicy(sizePolicy)
        self.btn_38.setMinimumSize(QtCore.QSize(97, 31))
        self.btn_38.setStyleSheet("QPushButton{\n"
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
        self.btn_38.setObjectName("btn_38")
        self.horizontalLayout_2.addWidget(self.btn_38)
        self.btn_40 = QtWidgets.QPushButton(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_40.sizePolicy().hasHeightForWidth())
        self.btn_40.setSizePolicy(sizePolicy)
        self.btn_40.setMinimumSize(QtCore.QSize(97, 31))
        self.btn_40.setStyleSheet("QPushButton{\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/plus_icon-icons.com_61187.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_40.setIcon(icon2)
        self.btn_40.setObjectName("btn_40")
        self.horizontalLayout_2.addWidget(self.btn_40)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(31, 31, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(201, 31))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
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
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: white;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(244, 244, 244);\n"
"}")
        self.pushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QtCore.QSize(21, 24))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.page)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_15 = QtWidgets.QWidget()
        self.page_15.setObjectName("page_15")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_15)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.horizontalLayout_55 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")
        self.btn_37 = QtWidgets.QPushButton(self.page_15)
        self.btn_37.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    color: white;\n"
"    \n"
"}")
        self.btn_37.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/Icons8-Ios7-Arrows-Back.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_37.setIcon(icon4)
        self.btn_37.setObjectName("btn_37")
        self.horizontalLayout_55.addWidget(self.btn_37)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_55.addItem(spacerItem8)
        self.verticalLayout_21.addLayout(self.horizontalLayout_55)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem9)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.horizontalLayout_92 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_92.setObjectName("horizontalLayout_92")
        self.verticalLayout_55 = QtWidgets.QVBoxLayout()
        self.verticalLayout_55.setObjectName("verticalLayout_55")
        self.label_37 = QtWidgets.QLabel(self.page_15)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("QLabel{\n"
"    color: rgb(194, 194, 194)\n"
"    \n"
"}")
        self.label_37.setObjectName("label_37")
        self.verticalLayout_55.addWidget(self.label_37)
        self.label_38 = QtWidgets.QLabel(self.page_15)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_38.setFont(font)
        self.label_38.setText("")
        self.label_38.setObjectName("label_38")
        self.verticalLayout_55.addWidget(self.label_38)
        self.horizontalLayout_92.addLayout(self.verticalLayout_55)
        self.verticalLayout_56 = QtWidgets.QVBoxLayout()
        self.verticalLayout_56.setObjectName("verticalLayout_56")
        self.label_39 = QtWidgets.QLabel(self.page_15)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("QLabel{\n"
"    color: rgb(194, 194, 194)\n"
"    \n"
"}")
        self.label_39.setObjectName("label_39")
        self.verticalLayout_56.addWidget(self.label_39)
        self.label_40 = QtWidgets.QLabel(self.page_15)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_40.setFont(font)
        self.label_40.setText("")
        self.label_40.setObjectName("label_40")
        self.verticalLayout_56.addWidget(self.label_40)
        self.horizontalLayout_92.addLayout(self.verticalLayout_56)
        self.verticalLayout_19.addLayout(self.horizontalLayout_92)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem10)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_41 = QtWidgets.QLabel(self.page_15)
        self.label_41.setObjectName("label_41")
        self.verticalLayout_14.addWidget(self.label_41)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.page_15)
        self.dateTimeEdit_2.setMinimumSize(QtCore.QSize(180, 0))
        self.dateTimeEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.dateTimeEdit_2.setDisplayFormat("yyyy-MM-dd hh:mm:ss")

        self.dateTimeEdit_2.setDateTime(datetime.datetime.now())

        self.verticalLayout_14.addWidget(self.dateTimeEdit_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_14)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem11)
        self.verticalLayout_19.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem12)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_12 = QtWidgets.QLabel(self.page_15)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_20.addWidget(self.label_12)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(180, 0))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_20.addWidget(self.lineEdit_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_20)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem13)
        self.verticalLayout_19.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_8.addLayout(self.verticalLayout_19)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem14)
        self.verticalLayout_21.addLayout(self.horizontalLayout_8)
        self.verticalLayout_60 = QtWidgets.QVBoxLayout()
        self.verticalLayout_60.setObjectName("verticalLayout_60")
        self.horizontalLayout_96 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_96.setObjectName("horizontalLayout_96")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_96.addItem(spacerItem15)
        self.verticalLayout_58 = QtWidgets.QVBoxLayout()
        self.verticalLayout_58.setObjectName("verticalLayout_58")
        self.label_42 = QtWidgets.QLabel(self.page_15)
        self.label_42.setObjectName("label_42")
        self.verticalLayout_58.addWidget(self.label_42)
        self.textEdit_4 = QtWidgets.QTextEdit(self.page_15)
        self.textEdit_4.setMinimumSize(QtCore.QSize(220, 121))
        self.textEdit_4.setObjectName("textEdit_4")
        self.verticalLayout_58.addWidget(self.textEdit_4)
        self.horizontalLayout_96.addLayout(self.verticalLayout_58)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_96.addItem(spacerItem16)
        self.verticalLayout_60.addLayout(self.horizontalLayout_96)
        self.verticalLayout_59 = QtWidgets.QVBoxLayout()
        self.verticalLayout_59.setObjectName("verticalLayout_59")
        self.horizontalLayout_95 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_95.setObjectName("horizontalLayout_95")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_95.addItem(spacerItem17)
        self.label_43 = QtWidgets.QLabel(self.page_15)
        self.label_43.setMinimumSize(QtCore.QSize(171, 20))
        self.label_43.setText("")
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.horizontalLayout_95.addWidget(self.label_43)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_95.addItem(spacerItem18)
        self.verticalLayout_59.addLayout(self.horizontalLayout_95)
        self.horizontalLayout_94 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_94.setObjectName("horizontalLayout_94")
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_94.addItem(spacerItem19)
        self.btn_61 = QtWidgets.QPushButton(self.page_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_61.sizePolicy().hasHeightForWidth())
        self.btn_61.setSizePolicy(sizePolicy)
        self.btn_61.setMinimumSize(QtCore.QSize(91, 31))
        self.btn_61.setStyleSheet("QPushButton{\n"
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
        self.btn_61.setObjectName("btn_61")
        self.horizontalLayout_94.addWidget(self.btn_61)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_94.addItem(spacerItem20)
        self.verticalLayout_59.addLayout(self.horizontalLayout_94)
        self.verticalLayout_60.addLayout(self.verticalLayout_59)
        self.verticalLayout_21.addLayout(self.verticalLayout_60)
        self.gridLayout_3.addLayout(self.verticalLayout_21, 0, 0, 1, 1)
        self.stackedWidget_2.addWidget(self.page_15)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.btn_23 = QtWidgets.QPushButton(self.page_6)
        self.btn_23.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    color: white;\n"
"    \n"
"}")
        self.btn_23.setText("")
        self.btn_23.setIcon(icon4)
        self.btn_23.setObjectName("btn_23")
        self.horizontalLayout_24.addWidget(self.btn_23)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem21)
        self.verticalLayout_13.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem22)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setHorizontalSpacing(20)
        self.gridLayout_8.setVerticalSpacing(6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label = QtWidgets.QLabel(self.page_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"    color: rgb(194, 194, 194)\n"
"    \n"
"}")
        self.label.setObjectName("label")
        self.verticalLayout_9.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.page_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_9.addWidget(self.label_3)
        self.gridLayout_8.addLayout(self.verticalLayout_9, 0, 0, 1, 1)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.page_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("QLabel{\n"
"    color: rgb(194, 194, 194)\n"
"    \n"
"}")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_10.addWidget(self.label_9)
        self.label_8 = QtWidgets.QLabel(self.page_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_10.addWidget(self.label_8)
        self.gridLayout_8.addLayout(self.verticalLayout_10, 0, 1, 1, 1)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_10 = QtWidgets.QLabel(self.page_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("QLabel{\n"
"    color: rgb(194, 194, 194)\n"
"    \n"
"}")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_12.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.page_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_12.addWidget(self.label_11)
        self.gridLayout_8.addLayout(self.verticalLayout_12, 1, 0, 1, 1)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_7 = QtWidgets.QLabel(self.page_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel{\n"
"    color: rgb(194, 194, 194)\n"
"    \n"
"}")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_11.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(self.page_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_11.addWidget(self.label_6)
        self.gridLayout_8.addLayout(self.verticalLayout_11, 1, 1, 1, 1)
        self.horizontalLayout_25.addLayout(self.gridLayout_8)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem23)
        self.verticalLayout_13.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem24)
        self.table_5 = QtWidgets.QTableWidget(self.page_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_5.sizePolicy().hasHeightForWidth())
        self.table_5.setSizePolicy(sizePolicy)
        self.table_5.setMinimumSize(QtCore.QSize(0, 0))
        self.table_5.setMaximumSize(QtCore.QSize(380, 16777215))
        self.table_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table_5.setLineWidth(1)
        self.table_5.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table_5.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_5.setAutoScroll(True)
        self.table_5.setAutoScrollMargin(18)
        self.table_5.setTabKeyNavigation(True)
        self.table_5.setObjectName("table_5")
        self.table_5.setColumnCount(2)
        self.table_5.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_5.setHorizontalHeaderItem(1, item)
        self.table_5.horizontalHeader().setDefaultSectionSize(181)
        self.table_5.horizontalHeader().setMinimumSectionSize(17)
        self.table_5.verticalHeader().setDefaultSectionSize(30)
        self.table_5.verticalHeader().setHighlightSections(True)
        self.table_5.verticalHeader().setMinimumSectionSize(15)
        self.table_5.verticalHeader().setSortIndicatorShown(False)
        self.horizontalLayout_22.addWidget(self.table_5)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem25)
        self.verticalLayout_13.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem26)
        self.btn_16 = QtWidgets.QPushButton(self.page_6)
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
        self.btn_16.setIcon(icon2)
        self.btn_16.setObjectName("btn_16")
        self.horizontalLayout_23.addWidget(self.btn_16)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem27)
        self.verticalLayout_13.addLayout(self.horizontalLayout_23)
        self.gridLayout_9.addLayout(self.verticalLayout_13, 0, 0, 1, 1)
        self.stackedWidget_2.addWidget(self.page_6)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout()
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.horizontalLayout_51 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        self.btn_19 = QtWidgets.QPushButton(self.page_5)
        self.btn_19.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    color: white;\n"
"    \n"
"}")
        self.btn_19.setText("")
        self.btn_19.setIcon(icon4)
        self.btn_19.setObjectName("btn_19")
        self.horizontalLayout_51.addWidget(self.btn_19)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_51.addItem(spacerItem28)
        self.verticalLayout_36.addLayout(self.horizontalLayout_51)
        spacerItem29 = QtWidgets.QSpacerItem(20, 31, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_36.addItem(spacerItem29)
        self.verticalLayout_6.addLayout(self.verticalLayout_36)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem30)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_2 = QtWidgets.QLabel(self.page_5)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_13.addWidget(self.label_2)
        self.line_2 = QtWidgets.QLineEdit(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setMinimumSize(QtCore.QSize(179, 25))
        self.line_2.setMaximumSize(QtCore.QSize(179, 16777215))
        self.line_2.setAlignment(QtCore.Qt.AlignCenter)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_13.addWidget(self.line_2)
        self.gridLayout_6.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_4 = QtWidgets.QLabel(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_14.addWidget(self.label_4)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEdit.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit.setSizePolicy(sizePolicy)
        self.dateTimeEdit.setMinimumSize(QtCore.QSize(179, 25))
        self.dateTimeEdit.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.dateTimeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateTimeEdit.setProperty("showGroupSeparator", False)
        self.dateTimeEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit.setDisplayFormat("yyyy-MM-dd hh:mm:ss")

        self.dateTimeEdit.setDateTime(datetime.datetime.now())
        self.horizontalLayout_14.addWidget(self.dateTimeEdit)
        self.gridLayout_6.addLayout(self.horizontalLayout_14, 1, 0, 1, 1)
        self.horizontalLayout_20.addLayout(self.gridLayout_6)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem31)
        self.verticalLayout_6.addLayout(self.horizontalLayout_20)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem32)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem33)
        self.label_5 = QtWidgets.QLabel(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_19.addWidget(self.label_5)
        spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem34)
        self.verticalLayout_5.addLayout(self.horizontalLayout_19)
        self.text_edit = QtWidgets.QTextEdit(self.page_5)
        self.text_edit.setMinimumSize(QtCore.QSize(171, 81))
        self.text_edit.setObjectName("text_edit")
        self.verticalLayout_5.addWidget(self.text_edit)
        self.horizontalLayout_21.addLayout(self.verticalLayout_5)
        spacerItem35 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem35)
        self.verticalLayout_7.addLayout(self.horizontalLayout_21)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem36)
        self.label_34 = QtWidgets.QLabel(self.page_5)
        self.label_34.setMinimumSize(QtCore.QSize(171, 20))
        self.label_34.setText("")
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_18.addWidget(self.label_34)
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem37)
        self.verticalLayout_18.addLayout(self.horizontalLayout_18)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem38 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem38)
        self.btn_4 = QtWidgets.QPushButton(self.page_5)
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
        self.horizontalLayout_15.addWidget(self.btn_4)
        spacerItem39 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem39)
        self.verticalLayout_17.addLayout(self.horizontalLayout_15)
        spacerItem40 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_17.addItem(spacerItem40)
        self.verticalLayout_18.addLayout(self.verticalLayout_17)
        self.verticalLayout_8.addLayout(self.verticalLayout_18)
        self.gridLayout_7.addLayout(self.verticalLayout_8, 0, 0, 1, 1)
        self.stackedWidget_2.addWidget(self.page_5)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_41 = QtWidgets.QVBoxLayout()
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.btn_21 = QtWidgets.QPushButton(self.page_3)
        self.btn_21.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    color: white;\n"
"    \n"
"}")
        self.btn_21.setText("")
        self.btn_21.setIcon(icon4)
        self.btn_21.setObjectName("btn_21")
        self.horizontalLayout_16.addWidget(self.btn_21)
        spacerItem41 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem41)
        self.verticalLayout_3.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_57 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_57.setObjectName("horizontalLayout_57")
        spacerItem42 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_57.addItem(spacerItem42)
        self.horizontalLayout_56 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_56.setObjectName("horizontalLayout_56")
        self.btn_62 = QtWidgets.QPushButton(self.page_3)
        self.btn_62.setStyleSheet("QPushButton{\n"
"\n"
"    background-color: white;\n"
"\n"
"}")
        self.btn_62.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/az.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_62.setIcon(icon5)
        self.btn_62.setIconSize(QtCore.QSize(25, 25))
        self.btn_62.setObjectName("btn_62")
        self.horizontalLayout_56.addWidget(self.btn_62)
        self.btn_63 = QtWidgets.QPushButton(self.page_3)
        self.btn_63.setStyleSheet("QPushButton{\n"
"\n"
"    background-color: white;\n"
"\n"
"}")
        self.btn_63.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/za.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_63.setIcon(icon6)
        self.btn_63.setIconSize(QtCore.QSize(25, 25))
        self.btn_63.setObjectName("btn_63")
        self.horizontalLayout_56.addWidget(self.btn_63)
        self.btn_64 = QtWidgets.QPushButton(self.page_3)
        self.btn_64.setStyleSheet("QPushButton{\n"
"\n"
"    background-color: white;\n"
"\n"
"}")
        self.btn_64.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/Filter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_64.setIcon(icon7)
        self.btn_64.setIconSize(QtCore.QSize(25, 25))
        self.btn_64.setObjectName("btn_64")
        self.horizontalLayout_56.addWidget(self.btn_64)
        self.horizontalLayout_57.addLayout(self.horizontalLayout_56)
        spacerItem43 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_57.addItem(spacerItem43)
        self.verticalLayout_3.addLayout(self.horizontalLayout_57)
        self.verticalLayout_41.addLayout(self.verticalLayout_3)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem44 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem44)
        self.table_3 = QtWidgets.QTableWidget(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_3.sizePolicy().hasHeightForWidth())
        self.table_3.setSizePolicy(sizePolicy)
        self.table_3.setMinimumSize(QtCore.QSize(0, 0))
        self.table_3.setMaximumSize(QtCore.QSize(770, 16777215))
        self.table_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table_3.setLineWidth(1)
        self.table_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table_3.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_3.setAutoScroll(True)
        self.table_3.setAutoScrollMargin(18)
        self.table_3.setTabKeyNavigation(True)
        self.table_3.setObjectName("table_3")
        self.table_3.setColumnCount(5)
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
        self.table_3.horizontalHeader().setDefaultSectionSize(134)
        self.table_3.horizontalHeader().setMinimumSectionSize(17)
        self.table_3.verticalHeader().setDefaultSectionSize(30)
        self.table_3.verticalHeader().setHighlightSections(True)
        self.table_3.verticalHeader().setMinimumSectionSize(15)
        self.table_3.verticalHeader().setSortIndicatorShown(False)
        self.horizontalLayout_10.addWidget(self.table_3)
        spacerItem45 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem45)
        self.verticalLayout_41.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem46 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem46)
        self.btn_13 = QtWidgets.QPushButton(self.page_3)
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
        self.btn_13.setIcon(icon2)
        self.btn_13.setObjectName("btn_13")
        self.horizontalLayout_11.addWidget(self.btn_13)
        spacerItem47 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem47)
        self.verticalLayout_41.addLayout(self.horizontalLayout_11)
        self.gridLayout_4.addLayout(self.verticalLayout_41, 0, 0, 1, 1)
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setSpacing(13)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.btn_22 = QtWidgets.QPushButton(self.page_4)
        self.btn_22.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    color: white;\n"
"    \n"
"}")
        self.btn_22.setText("")
        self.btn_22.setIcon(icon4)
        self.btn_22.setObjectName("btn_22")
        self.horizontalLayout_17.addWidget(self.btn_22)
        spacerItem48 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem48)
        self.verticalLayout_4.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        spacerItem49 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem49)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.page_4)
        self.calendarWidget.setMaximumSize(QtCore.QSize(302, 183))
        self.calendarWidget.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.horizontalLayout_29.addWidget(self.calendarWidget)
        spacerItem50 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem50)
        self.verticalLayout_4.addLayout(self.horizontalLayout_29)
        self.verticalLayout_22.addLayout(self.verticalLayout_4)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem51 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem51)
        self.table_4 = QtWidgets.QTableWidget(self.page_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_4.sizePolicy().hasHeightForWidth())
        self.table_4.setSizePolicy(sizePolicy)
        self.table_4.setMinimumSize(QtCore.QSize(0, 0))
        self.table_4.setMaximumSize(QtCore.QSize(442, 16777215))
        self.table_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table_4.setLineWidth(1)
        self.table_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table_4.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_4.setAutoScroll(True)
        self.table_4.setAutoScrollMargin(18)
        self.table_4.setTabKeyNavigation(True)
        self.table_4.setObjectName("table_4")
        self.table_4.setColumnCount(2)
        self.table_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_4.setHorizontalHeaderItem(1, item)
        self.table_4.horizontalHeader().setDefaultSectionSize(220)
        self.table_4.horizontalHeader().setMinimumSectionSize(17)
        self.table_4.verticalHeader().setDefaultSectionSize(30)
        self.table_4.verticalHeader().setHighlightSections(True)
        self.table_4.verticalHeader().setMinimumSectionSize(15)
        self.table_4.verticalHeader().setSortIndicatorShown(False)
        self.horizontalLayout_9.addWidget(self.table_4)
        spacerItem52 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem52)
        self.verticalLayout_22.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem53 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem53)
        self.btn_14 = QtWidgets.QPushButton(self.page_4)
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
        self.btn_14.setIcon(icon2)
        self.btn_14.setObjectName("btn_14")
        self.horizontalLayout_12.addWidget(self.btn_14)
        spacerItem54 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem54)
        self.verticalLayout_22.addLayout(self.horizontalLayout_12)
        self.verticalLayout_23.addLayout(self.verticalLayout_22)
        self.stackedWidget_2.addWidget(self.page_4)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.page_7)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.horizontalLayout_54 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_54.setObjectName("horizontalLayout_54")
        self.btn_35 = QtWidgets.QPushButton(self.page_7)
        self.btn_35.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    color: white;\n"
"    \n"
"}")
        self.btn_35.setText("")
        self.btn_35.setIcon(icon4)
        self.btn_35.setObjectName("btn_35")
        self.horizontalLayout_54.addWidget(self.btn_35)
        spacerItem55 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_54.addItem(spacerItem55)
        self.gridLayout_10.addLayout(self.horizontalLayout_54, 0, 0, 1, 1)
        self.horizontalLayout_60 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_60.setObjectName("horizontalLayout_60")
        spacerItem56 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_60.addItem(spacerItem56)
        self.horizontalLayout_61 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_61.setObjectName("horizontalLayout_61")
        self.btn_66 = QtWidgets.QPushButton(self.page_7)
        self.btn_66.setStyleSheet("QPushButton{\n"
"\n"
"    background-color: white;\n"
"\n"
"}")
        self.btn_66.setText("")
        self.btn_66.setIcon(icon5)
        self.btn_66.setIconSize(QtCore.QSize(25, 25))
        self.btn_66.setObjectName("btn_66")
        self.horizontalLayout_61.addWidget(self.btn_66)
        self.btn_67 = QtWidgets.QPushButton(self.page_7)
        self.btn_67.setStyleSheet("QPushButton{\n"
"\n"
"    background-color: white;\n"
"\n"
"}")
        self.btn_67.setText("")
        self.btn_67.setIcon(icon6)
        self.btn_67.setIconSize(QtCore.QSize(25, 25))
        self.btn_67.setObjectName("btn_67")
        self.horizontalLayout_61.addWidget(self.btn_67)
        self.btn_68 = QtWidgets.QPushButton(self.page_7)
        self.btn_68.setStyleSheet("QPushButton{\n"
"\n"
"    background-color: white;\n"
"\n"
"}")
        self.btn_68.setText("")
        self.btn_68.setIcon(icon7)
        self.btn_68.setIconSize(QtCore.QSize(25, 25))
        self.btn_68.setObjectName("btn_68")
        self.horizontalLayout_61.addWidget(self.btn_68)
        self.horizontalLayout_60.addLayout(self.horizontalLayout_61)
        spacerItem57 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_60.addItem(spacerItem57)
        self.gridLayout_10.addLayout(self.horizontalLayout_60, 1, 0, 1, 1)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        spacerItem58 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem58)
        self.table_6 = QtWidgets.QTableWidget(self.page_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_6.sizePolicy().hasHeightForWidth())
        self.table_6.setSizePolicy(sizePolicy)
        self.table_6.setMinimumSize(QtCore.QSize(0, 0))
        self.table_6.setMaximumSize(QtCore.QSize(770, 16777215))
        self.table_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table_6.setLineWidth(1)
        self.table_6.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table_6.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_6.setAutoScroll(True)
        self.table_6.setAutoScrollMargin(18)
        self.table_6.setTabKeyNavigation(True)
        self.table_6.setObjectName("table_6")
        self.table_6.setColumnCount(4)
        self.table_6.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_6.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_6.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_6.setHorizontalHeaderItem(3, item)
        self.table_6.horizontalHeader().setDefaultSectionSize(157)
        self.table_6.horizontalHeader().setMinimumSectionSize(17)
        self.table_6.verticalHeader().setDefaultSectionSize(30)
        self.table_6.verticalHeader().setHighlightSections(True)
        self.table_6.verticalHeader().setMinimumSectionSize(15)
        self.table_6.verticalHeader().setSortIndicatorShown(False)
        self.horizontalLayout_27.addWidget(self.table_6)
        spacerItem59 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem59)
        self.gridLayout_10.addLayout(self.horizontalLayout_27, 2, 0, 1, 1)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        spacerItem60 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_28.addItem(spacerItem60)
        self.btn_17 = QtWidgets.QPushButton(self.page_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_17.sizePolicy().hasHeightForWidth())
        self.btn_17.setSizePolicy(sizePolicy)
        self.btn_17.setMinimumSize(QtCore.QSize(91, 31))
        self.btn_17.setStyleSheet("QPushButton{\n"
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
        self.btn_17.setObjectName("btn_17")
        self.horizontalLayout_28.addWidget(self.btn_17)
        spacerItem61 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_28.addItem(spacerItem61)
        self.gridLayout_10.addLayout(self.horizontalLayout_28, 3, 0, 1, 1)
        self.gridLayout_20.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        self.stackedWidget_2.addWidget(self.page_7)
        self.gridLayout_2.addWidget(self.stackedWidget_2, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.verticalLayout_54 = QtWidgets.QVBoxLayout()
        self.verticalLayout_54.setObjectName("verticalLayout_54")
        self.verticalLayout_53 = QtWidgets.QVBoxLayout()
        self.verticalLayout_53.setObjectName("verticalLayout_53")
        spacerItem62 = QtWidgets.QSpacerItem(20, 72, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_53.addItem(spacerItem62)
        self.horizontalLayout_91 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_91.setObjectName("horizontalLayout_91")
        spacerItem63 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_91.addItem(spacerItem63)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_8 = QtWidgets.QPushButton(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setMinimumSize(QtCore.QSize(251, 51))
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
        self.verticalLayout.addWidget(self.btn_8)
        self.btn_10 = QtWidgets.QPushButton(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_10.sizePolicy().hasHeightForWidth())
        self.btn_10.setSizePolicy(sizePolicy)
        self.btn_10.setMinimumSize(QtCore.QSize(251, 51))
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
        self.verticalLayout.addWidget(self.btn_10)
        self.btn_9 = QtWidgets.QPushButton(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setMinimumSize(QtCore.QSize(251, 51))
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
        self.verticalLayout.addWidget(self.btn_9)
        self.btn_34 = QtWidgets.QPushButton(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_34.sizePolicy().hasHeightForWidth())
        self.btn_34.setSizePolicy(sizePolicy)
        self.btn_34.setMinimumSize(QtCore.QSize(251, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_34.setFont(font)
        self.btn_34.setStyleSheet("QPushButton{\n"
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
        self.btn_34.setObjectName("btn_34")
        self.verticalLayout.addWidget(self.btn_34)
        self.btn_39 = QtWidgets.QPushButton(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_39.sizePolicy().hasHeightForWidth())
        self.btn_39.setSizePolicy(sizePolicy)
        self.btn_39.setMinimumSize(QtCore.QSize(251, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_39.setFont(font)
        self.btn_39.setStyleSheet("QPushButton{\n"
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
        self.btn_39.setObjectName("btn_39")
        self.verticalLayout.addWidget(self.btn_39)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem64 = QtWidgets.QSpacerItem(18, 36, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem64)
        self.horizontalLayout_91.addLayout(self.verticalLayout_2)
        spacerItem65 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_91.addItem(spacerItem65)
        self.verticalLayout_53.addLayout(self.horizontalLayout_91)
        self.verticalLayout_54.addLayout(self.verticalLayout_53)
        self.verticalLayout_52 = QtWidgets.QVBoxLayout()
        self.verticalLayout_52.setObjectName("verticalLayout_52")
        self.horizontalLayout_90 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_90.setObjectName("horizontalLayout_90")
        spacerItem66 = QtWidgets.QSpacerItem(150, 16, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_90.addItem(spacerItem66)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.line_5 = QtWidgets.QLineEdit(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_5.sizePolicy().hasHeightForWidth())
        self.line_5.setSizePolicy(sizePolicy)
        self.line_5.setMinimumSize(QtCore.QSize(251, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_5.setFont(font)
        self.line_5.setStyleSheet("QLineEdit{\n"
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
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_6.addWidget(self.line_5)
        self.btn_69 = QtWidgets.QPushButton(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_69.sizePolicy().hasHeightForWidth())
        self.btn_69.setSizePolicy(sizePolicy)
        self.btn_69.setMinimumSize(QtCore.QSize(51, 51))
        self.btn_69.setStyleSheet("QPushButton{\n"
"    background-color: white;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(244, 244, 244);\n"
"}")
        self.btn_69.setText("")
        self.btn_69.setIcon(icon3)
        self.btn_69.setIconSize(QtCore.QSize(30, 30))
        self.btn_69.setObjectName("btn_69")
        self.horizontalLayout_6.addWidget(self.btn_69)
        self.horizontalLayout_90.addLayout(self.horizontalLayout_6)
        spacerItem67 = QtWidgets.QSpacerItem(89, 17, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_90.addItem(spacerItem67)
        self.verticalLayout_52.addLayout(self.horizontalLayout_90)
        spacerItem68 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_52.addItem(spacerItem68)
        self.verticalLayout_54.addLayout(self.verticalLayout_52)
        self.gridLayout_28.addLayout(self.verticalLayout_54, 0, 0, 2, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_16.addWidget(self.stackedWidget)
        self.gridLayout.addLayout(self.verticalLayout_16, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 982, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Специалист"))
        self.btn_2.setText(_translate("MainWindow", "Список записей"))
        self.btn_15.setText(_translate("MainWindow", "График работы"))
        self.btn_3.setText(_translate("MainWindow", "Ваши пациенты"))
        self.btn_5.setText(_translate("MainWindow", "Добавить запись"))
        self.btn_38.setText(_translate("MainWindow", "Результат приема"))
        self.btn_40.setText(_translate("MainWindow", "Диагноз"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Введите ФИО пациента..."))
        self.label_37.setText(_translate("MainWindow", "ФИО пациента"))
        self.label_39.setText(_translate("MainWindow", "Номер телефона"))
        self.label_41.setText(_translate("MainWindow", "Время записи:"))
        self.label_12.setText(_translate("MainWindow", "Диагноз:"))
        self.label_42.setText(_translate("MainWindow", "Рекомендации"))
        self.btn_61.setText(_translate("MainWindow", "Сохранить"))
        self.label.setText(_translate("MainWindow", "ФИО пациента"))
        self.label_9.setText(_translate("MainWindow", "Дата рождения"))
        self.label_10.setText(_translate("MainWindow", "Номер телефона"))
        self.label_7.setText(_translate("MainWindow", "Почта"))
        item = self.table_5.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Дата записи"))
        item = self.table_5.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Описание"))
        self.btn_16.setText(_translate("MainWindow", "Запись"))
        self.label_2.setText(_translate("MainWindow", "ID пациента:"))
        self.label_4.setText(_translate("MainWindow", "Дата и время:"))
        self.label_5.setText(_translate("MainWindow", "Описание:"))
        self.btn_4.setText(_translate("MainWindow", "Добавить"))
        item = self.table_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Фамилия"))
        item = self.table_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.table_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Отчество"))
        item = self.table_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Дата записи"))
        item = self.table_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Описание"))
        self.btn_13.setText(_translate("MainWindow", "Запись"))
        item = self.table_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Время"))
        item = self.table_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Занятость"))
        self.btn_14.setText(_translate("MainWindow", "Запись"))
        item = self.table_6.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID пациента"))
        item = self.table_6.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Фамилия"))
        item = self.table_6.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.table_6.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Отчество"))
        self.btn_17.setText(_translate("MainWindow", "Подробнее"))
        self.btn_8.setText(_translate("MainWindow", "Список записей"))
        self.btn_10.setText(_translate("MainWindow", "График работы"))
        self.btn_9.setText(_translate("MainWindow", "Ваши пациенты"))
        self.btn_34.setText(_translate("MainWindow", "Добавить запись"))
        self.btn_39.setText(_translate("MainWindow", "Результат приема"))
        self.line_5.setPlaceholderText(_translate("MainWindow", "Введите ФИО пациента..."))
