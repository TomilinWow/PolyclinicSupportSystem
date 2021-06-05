from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(315, 137)
        Dialog.setStyleSheet("QDialog{\n"
"\n"
"    background-color: white;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(23)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(17, -1, 17, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.horizontalLayout_2.addWidget(self.dateTimeEdit)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.dateTimeEdit_2.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.horizontalLayout_2.addWidget(self.dateTimeEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Фильтр"))
        self.label.setText(_translate("Dialog", "-"))
        self.pushButton.setText(_translate("Dialog", "Применить"))

class Filter(QDialog, Ui_Dialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent

        self.pushButton.clicked.connect(self.accept_value)

    def accept_value(self):
        """
        Извлечение записей во временном диапазоне (преобразование времен к строковому виду и
        запуск метода создания таблицы)
        """
        first_time  = self.dateTimeEdit.dateTime()
        second_time = self.dateTimeEdit_2.dateTime()
        first_time_string = first_time.toString(self.dateTimeEdit.displayFormat())
        second_time_string = second_time.toString(self.dateTimeEdit_2.displayFormat())

        self.parent.create_list_records(3, first_time_string, second_time_string)
        self.close()