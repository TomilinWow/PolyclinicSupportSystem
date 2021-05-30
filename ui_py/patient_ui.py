from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QCompleter
from PyQt5.QtCore import Qt


class PatientUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(948, 637)
        MainWindow.setStyleSheet("QMainWindow{\n"
"\n"
"    background-color: white;\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
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
        self.verticalLayout.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btn_12 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_12.setStyleSheet("QPushButton{\n"
"\n"
"    border: none;\n"
"    background-color: white;\n"
"\n"
"}")
        self.btn_12.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/medicine.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_12.setIcon(icon1)
        self.btn_12.setIconSize(QtCore.QSize(50, 50))
        self.btn_12.setObjectName("btn_12")
        self.horizontalLayout_2.addWidget(self.btn_12)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout = QtWidgets.QGridLayout(self.page)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.line_5 = QtWidgets.QLineEdit(self.page)
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
        self.horizontalLayout_3.addWidget(self.line_5)
        self.btn_69 = QtWidgets.QPushButton(self.page)
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_69.setIcon(icon2)
        self.btn_69.setIconSize(QtCore.QSize(30, 30))
        self.btn_69.setObjectName("btn_69")
        self.horizontalLayout_3.addWidget(self.btn_69)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line_6 = QtWidgets.QLineEdit(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_6.sizePolicy().hasHeightForWidth())
        self.line_6.setSizePolicy(sizePolicy)
        self.line_6.setMinimumSize(QtCore.QSize(251, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_6.setFont(font)
        self.line_6.setStyleSheet("QLineEdit{\n"
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
        self.line_6.setObjectName("line_6")
        self.horizontalLayout.addWidget(self.line_6)
        self.btn_70 = QtWidgets.QPushButton(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_70.sizePolicy().hasHeightForWidth())
        self.btn_70.setSizePolicy(sizePolicy)
        self.btn_70.setMinimumSize(QtCore.QSize(51, 51))
        self.btn_70.setStyleSheet("QPushButton{\n"
"    background-color: white;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(244, 244, 244);\n"
"}")
        self.btn_70.setText("")
        self.btn_70.setIcon(icon2)
        self.btn_70.setIconSize(QtCore.QSize(30, 30))
        self.btn_70.setObjectName("btn_70")
        self.horizontalLayout.addWidget(self.btn_70)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_52 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_52.setObjectName("horizontalLayout_52")
        self.btn_20 = QtWidgets.QPushButton(self.page_3)
        self.btn_20.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    color: white;\n"
"    \n"
"}")
        self.btn_20.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/Icons8-Ios7-Arrows-Back.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_20.setIcon(icon3)
        self.btn_20.setObjectName("btn_20")
        self.horizontalLayout_52.addWidget(self.btn_20)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_52.addItem(spacerItem8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_52)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem9)
        self.table_4 = QtWidgets.QTableWidget(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_4.sizePolicy().hasHeightForWidth())
        self.table_4.setSizePolicy(sizePolicy)
        self.table_4.setMinimumSize(QtCore.QSize(0, 0))
        self.table_4.setMaximumSize(QtCore.QSize(662, 16777215))
        self.table_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table_4.setLineWidth(1)
        self.table_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table_4.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_4.setAutoScroll(True)
        self.table_4.setAutoScrollMargin(18)
        self.table_4.setTabKeyNavigation(True)
        self.table_4.setObjectName("table_4")
        self.table_4.setColumnCount(3)
        self.table_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_4.setHorizontalHeaderItem(2, item)
        self.table_4.horizontalHeader().setDefaultSectionSize(220)
        self.table_4.horizontalHeader().setMinimumSectionSize(17)
        self.table_4.verticalHeader().setDefaultSectionSize(30)
        self.table_4.verticalHeader().setHighlightSections(True)
        self.table_4.verticalHeader().setMinimumSectionSize(15)
        self.table_4.verticalHeader().setSortIndicatorShown(False)
        self.horizontalLayout_8.addWidget(self.table_4)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem10)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem11)
        self.btn_14 = QtWidgets.QPushButton(self.page_3)
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
        self.btn_14.setObjectName("btn_14")
        self.horizontalLayout_7.addWidget(self.btn_14)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem12)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.gridLayout_4.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_51 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        self.btn_19 = QtWidgets.QPushButton(self.page_2)
        self.btn_19.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    color: white;\n"
"    \n"
"}")
        self.btn_19.setText("")
        self.btn_19.setIcon(icon3)
        self.btn_19.setObjectName("btn_19")
        self.horizontalLayout_51.addWidget(self.btn_19)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_51.addItem(spacerItem13)
        self.verticalLayout_4.addLayout(self.horizontalLayout_51)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem14)
        self.tableWidget = QtWidgets.QTableWidget(self.page_2)
        self.tableWidget.setMinimumSize(QtCore.QSize(411, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(411, 16777215))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.horizontalLayout_5.addWidget(self.tableWidget)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem15)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem16)
        self.btn_2 = QtWidgets.QPushButton(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setMinimumSize(QtCore.QSize(91, 31))
        self.btn_2.setLayoutDirection(QtCore.Qt.LeftToRight)
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
        self.horizontalLayout_6.addWidget(self.btn_2)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem17)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout_2.addWidget(self.stackedWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 948, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.line_5.setPlaceholderText(_translate("MainWindow", "Введите ФИО специалиста..."))
        self.line_6.setPlaceholderText(_translate("MainWindow", "Введите специальность..."))
        item = self.table_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Дата"))
        item = self.table_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Время"))
        item = self.table_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Занятость"))
        self.btn_14.setText(_translate("MainWindow", "Записаться"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Фамилия"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Отчество"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Специальность"))
        self.btn_2.setText(_translate("MainWindow", "Выбрать"))
