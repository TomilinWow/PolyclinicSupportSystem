from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui_py import patient_ui
from PyQt5.QtCore import QDateTime, Qt
import datetime
from create_table import CreateTable
from recording import Recording


class Patient(QMainWindow, patient_ui.PatientUi):
    def __init__(self, parent, connection, login):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.connection = connection
        self.login = login
        # заполнение выпадающих списков
        self.set_completer(0)
        self.set_completer(1)
        # получение id пациента
        self.id_patient()

        self.btn_69.clicked.connect(self.create_table)
        self.btn_70.clicked.connect(self.show_specialists)
        self.btn_2.clicked.connect(self.create_table)

        self.btn_14.clicked.connect(self.recording_window)

        self.btn_19.clicked.connect(self.back)
        self.btn_20.clicked.connect(self.back)
        self.btn_36.clicked.connect(self.return_back)

    def id_patient(self):
        """
        Определение id пациента по логину
        """
        cursor = self.connection.cursor()
        cursor.execute('select patient_num from patient where patient_login = (%s)', (self.login))
        self.id_pt = cursor.fetchall()[0].get('patient_num')

    def recording_window(self):
        """
        Запуск окна подтверждения записи
        :return:
        """
        try:

            datetime = f"{self.table_4.item(self.table_4.currentRow(), 0).text()} " \
                        f"{self.table_4.item(self.table_4.currentRow(), 1).text()}"
            fio = f"{self.surname} {self.name} {self.patronymic}"
            self.recording = Recording(self.connection, fio, datetime, self.id_sp, self.id_pt)
            self.recording.show()
        except Exception as ex:
           print(ex)

    def back(self):
        self.stackedWidget.setCurrentIndex(0)
        self.line_5.setText("")
        self.line_6.setText("")

    def create_table(self):

        mass_datetime = self.datetime_specialist()
        print(mass_datetime)
        self.stackedWidget.setCurrentIndex(1)
        now = QDateTime.currentDateTime()
        mass_time = now.toString(Qt.ISODate).split('T')
        hour = int(mass_time[1].split(':')[0])
        today = datetime.date.today()
        count_row = 0
        self.table_4.setRowCount(0)
        self.table_4.setColumnCount(3)
        self.table_4.insertRow(0)
        current_time = ''
        for i in range(7):
            current_time += today.strftime('%Y-%m-%d') + " "
            for j in range(hour, 20):

                item = QTableWidgetItem()
                item.setText(today.strftime('%Y-%m-%d'))
                self.table_4.setItem(count_row, 0, item)

                item = QTableWidgetItem()
                time = f"{j}:00:00"
                item.setText(time)
                current_time += f"{j}:00:00"
                self.table_4.setItem(count_row, 1, item)
                if current_time in mass_datetime:
                    item = QTableWidgetItem()
                    item.setBackground(Qt.red)
                    self.table_4.setItem(count_row, 2, item)
                count_row += 1
                self.table_4.insertRow(count_row)
                current_time = today.strftime('%Y-%m-%d') + " "
            current_time = ''
            hour = 9
            today += datetime.timedelta(days=1)


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

    def datetime_specialist(self):
        """
        Формирование массива занятости специалиста
        """
        mass_datetime = []
        cursor = self.connection.cursor()
        self.id_sp = self.id_specialist()
        cursor.execute("SELECT reception_datetime from reception where specialist_specialist_num = %s", (self.id_sp))
        row = cursor.fetchone()
        while row is not None:
            mass = list(row.items())
            mass_datetime.append(mass[0][1].strftime('%Y-%m-%d %H:%M:%S'))
            row = cursor.fetchone()
        return mass_datetime

    def id_specialist(self):
        """
        Получение id специалиста
        :return: значение id специалиста
        """
        if self.stackedWidget.currentIndex() == 2:
            num_row = self.tableWidget.currentRow()
            self.name = self.tableWidget.item(num_row, 0).text()
            self.surname = self.tableWidget.item(num_row, 1).text()
            self.patronymic = self.tableWidget.item(num_row, 2).text()
        else:
            fio = self.line_5.text().split(" ")
            self.name = fio[0]
            self.surname = fio[1]
            self.patronymic = fio[2]

        cursor = self.connection.cursor()
        cursor.execute('call specialistid(%s, %s, %s)',
                       (self.name, self.surname, self.patronymic))
        return cursor.fetchall()[0].get('specialist_num')

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
