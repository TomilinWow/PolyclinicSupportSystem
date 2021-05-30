from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui_py import patient_ui
from PyQt5.QtCore import QDateTime, Qt
import datetime
from create_table import CreateTable


class Patient(QMainWindow, patient_ui.PatientUi):
    def __init__(self, parent, connection, login):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.connection = connection
        # заполнение выпадающих списков
        self.set_completer(0)
        self.set_completer(1)

        self.btn_69.clicked.connect(self.create_table)
        self.btn_70.clicked.connect(self.show_specialists)

        self.btn_19.clicked.connect(self.back)
        self.btn_20.clicked.connect(self.back)
        self.btn_36.clicked.connect(self.return_back)
        self.btn_2.clicked.connect(self.show_list)

    def back(self):
        self.stackedWidget.setCurrentIndex(0)

    def create_table(self):
        self.stackedWidget.setCurrentIndex(1)

        now = QDateTime.currentDateTime()
        mass_time = now.toString(Qt.ISODate).split('T')
        hour = int(mass_time[1].split(':')[0])
        today = datetime.date.today()

        count_row = 0
        self.table_4.setColumnCount(3)
        self.table_4.insertRow(0)
        for i in range(7):
            item = QTableWidgetItem()
            item.setText(today.strftime('%y-%d-%m'))
            self.table_4.setItem(count_row, 0, item)
            for j in range(hour, 20):
                item = QTableWidgetItem()
                item.setText(f"{j}:00:00 - {j + 1}:00:00")
                self.table_4.setItem(count_row, 1, item)
                count_row += 1
                self.table_4.insertRow(count_row)
            hour = 9
            today += datetime.timedelta(days=1)

    def show_list(self):
        """
        Заполнение таблицы записей конкретного специалиста
        :return:
        """
        print(self.id_specialist())

    def show_specialists(self):
        """
        Заполнение таблицы специалистами
        :return:
        """
        cursor = self.connection.cursor()
        cursor.execute('call show_specialists(%s)',
                       (self.line_6.text()))  # procedure
        self.stackedWidget.setCurrentIndex(2)
        create_table = CreateTable(self.tableWidget, cursor, 4)
        create_table.set_table()

    def id_specialist(self):
        """
        Получение id специалиста
        :return: значение id специалиста
        """
        num_row = self.tableWidget.currentRow()
        name = self.tableWidget.item(num_row, 0)
        surname = self.tableWidget.item(num_row, 1)
        patronymic = self.tableWidget.item(num_row, 2)
        cursor = self.connection.cursor()
        cursor.execute('call specialistid(%s, %s, %s)',
                       (name, surname, patronymic))
        return cursor.fetchall()[0].get('specialty_num')

    def set_completer(self, flag):
        """
        Заполнение выпадающего списка специалистами и специальностями из БД
        """
        words = []  # массив слов для QComleter
        cursor = self.connection.cursor()
        if flag == 0:
            cursor.execute("SELECT * FROM completer_specialist")  # view
        else:
            cursor.execute("SELECT specialty_name FROM specialty")  # view

        row = cursor.fetchone()
        while row is not None:
            word = ''
            mass = list(row.items())
            for i in range(len(mass)):
                word += mass[i][1] + " "
            words.append(word[:-1])
            row = cursor.fetchone()

        if flag == 0:
            completer = QCompleter(words, self.line_5)
            self.line_5.setCompleter(completer)
        else:
            completer = QCompleter(words, self.line_6)
            self.line_6.setCompleter(completer)

    def return_back(self):
        """
        Переход назад на окно с авторизацией
        """
        self.parent.show()
        self.parent.textEdit.setText("")
        self.parent.lineEdit.setText("")
        self.close()
