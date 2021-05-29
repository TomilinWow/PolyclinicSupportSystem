from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation

class Dialog(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(572, 388)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 541, 351))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.frame.setFont(font)
        self.frame.setStyleSheet("QFrame{\n"
                                 "    border-radius: 5px;\n"
                                 "    background-color: rgb(255, 255, 255);\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(160, 120, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("QTextEdit{\n"
                                    "    padding-top: 8px;\n"
                                    "    text-align: center;\n"
                                    "    background-color: #a6f7f1;\n"
                                    "       transition: 2s linear; \n"
                                    "    color: black;\n"
                                    "}\n"
                                    "\n"
                                    "QTextEdit:hover{\n"
                                    "    background-color:#89f0ea;\n"
                                    "}\n"
                                    "")
        self.textEdit.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.textEdit.setAcceptRichText(True)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(235, 220, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
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
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 0, 41, 41))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "    background-color: white;\n"
                                        "    border-radius: 5px;\n"
                                        "}")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/1487086345-cross_81577.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(17, 17))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 21, 151, 81))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "    background-color: white;\n"
                                        "border: none;\n"
                                        "}")
        self.pushButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/medicine_icon-icons.com_66070.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(160, 170, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                    "    padding-top: 0px;\n"
                                    "    padding-left: 3px;\n"
                                    "    text-align: center;\n"
                                    "    background-color: #a6f7f1;\n"
                                    "    border-radius: 5px;\n"
                                    "       transition: 2s linear; \n"
                                    "    color: black;\n"
                                    "}\n"
                                    "\n"
                                    "QLineEdit:hover{\n"
                                    "    background-color: #89f0ea;\n"
                                    "}    ")
        self.lineEdit.setFrame(False)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.show()
        # Класс анимации прозрачности окна
        self.animation = QPropertyAnimation(self, b'windowOpacity')
        self.animation.setDuration(1000)  # Продолжительность: 1 секунда
        self.doShow()

    def doShow(self):
        try:
            self.animation.finished.disconnect(self.close)
        except:
            pass
        self.animation.stop()
        # Диапазон прозрачности постепенно увеличивается от 0 до 1.
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Введите логин..."))
        self.pushButton.setText(_translate("MainWindow", "Войти"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Введите пароль..."))
