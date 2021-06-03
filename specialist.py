from PyQt5.QtCore import Qt
from ui_py import specialist_ui
from filter import Filter
from PyQt5.QtWidgets import QMainWindow, QCompleter
from PyQt5.QtCore import *
from create_table import CreateTable
from diagnosis import Diagnosis
from PyQt5.QtCore import QDateTime, Qt
import datetime
from PyQt5.QtWidgets import *

class Specialist(QMainWindow, specialist_ui.SpecialistUi):
    def __init__(self, parent, connection, login):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.connection = connection
        self.login = login
        self.stackedWidget.setCurrentIndex(1)
        self.get_id()
        self.set_completer(0)
        self.set_completer(1)

        #события сортировки списка пациентов
        self.btn_2.clicked.connect(self.create_table_ver_1)
        self.btn_62.clicked.connect(self.create_table_ver_2)
        self.btn_63.clicked.connect(self.create_table_ver_3)
        self.btn_8.clicked.connect(self.create_list_records)

        # кнопки для смены окон
        self.btn_9.clicked.connect(self.change_window)
        self.btn_10.clicked.connect(self.change_window)
        self.btn_34.clicked.connect(self.change_window)
        self.btn_15.clicked.connect(self.change_window)
        self.btn_3.clicked.connect(self.change_window)
        self.btn_5.clicked.connect(self.change_window)
        self.btn_39.clicked.connect(self.change_window)
        self.btn_38.clicked.connect(self.change_window)

        # возврат на начальное меню
        self.btn_19.clicked.connect(self.back)
        self.btn_21.clicked.connect(self.back)
        self.btn_22.clicked.connect(self.back)
        self.btn_23.clicked.connect(self.back)
        self.btn_35.clicked.connect(self.back)
        self.btn_36.clicked.connect(self.return_back)

        # запуск фильтра
        self.btn_64.clicked.connect(self.show_filter)
        self.btn_68.clicked.connect(self.show_filter)

        self.btn_69.clicked.connect(self.patient_guide)
        self.pushButton.clicked.connect(self.patient_guide)

        self.line_5.textChanged.connect(self.fio_patient_line_1)
        self.lineEdit.textChanged.connect(self.fio_patient_line_2)

        self.btn_40.clicked.connect(self.window_diagnosis)
        self.btn_61.clicked.connect(self.create_record)

        self.btn_17.clicked.connect(self.patient_guide)
        self.btn_4.clicked.connect(self.add_record)


    def add_record(self):
        time = self.dateTimeEdit.dateTime()
        time_string = time.toString(self.dateTimeEdit.displayFormat())

        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO reception (reception_datetime, "
                            "description, patient_patient_num, "
                            "specialist_specialist_num) values (%s, %s, %s, %s)",
                            (time_string,
                             self.text_edit.toPlainText(),
                             self.line_2.text(),
                             self.specialist_id
                             ))
        self.connection.commit()
        self.label_34.setText("Запись добавлена")

    """
    Обязательно изменить!!!
    """
    def datetime_specialist(self):
        """
        Формирование массива занятости специалиста
        """
        mass_datetime = []
        cursor = self.connection.cursor()
        cursor.execute("SELECT reception_datetime from reception where specialist_specialist_num = %s", (self.specialist_id))
        row = cursor.fetchone()
        while row is not None:
            mass = list(row.items())
            mass_datetime.append(mass[0][1].strftime('%Y-%m-%d %H:%M:%S'))
            row = cursor.fetchone()
        return mass_datetime

    def create_table(self):

        mass_datetime = self.datetime_specialist()

        self.stackedWidget.setCurrentIndex(0)
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

    def go_to_patient(self):
        try:
            row = self.table_6.currentRow()
            mass = [self.table_6.item(row, 1).text(), self.table_6.item(row, 2).text(), self.table_6.item(row, 3).text()]
        except Exception:
            return False
        return mass

    def show_patients(self):
        cursor = self.connection.cursor()
        cursor.execute('call show_patients_ver_2(%s)',
                       (self.specialist_id))
        create_table = CreateTable(self.table_6, cursor, 4)
        create_table.set_table()

    def diagnosis_id(self):
        cursor = self.connection.cursor()
        cursor.execute('select diagnosis_num from diagnosis where diagnosis_name = %s', (self.lineEdit_2.text()))
        return cursor.fetchall()[0].get('diagnosis_num')

    def create_record(self):

        time = self.dateTimeEdit_2.dateTime()
        time_string = time.toString("yyyy-MM-dd hh:mm:ss")

        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO reception_result (reception_result_date, "
                            "reception_result_info, specialist_specialist_num, "
                            "patient_patient_num, diagnosis_diagnosis_num) values (%s, %s, %s, %s, %s)",
                            (time_string,
                             self.textEdit_4.toPlainText(),
                             self.specialist_id,
                             self.id_patient,
                             self.diagnosis_id(),
                            ))

        self.connection.commit()
        self.label_43.setText("Запись сохранена")


    def window_diagnosis(self):
        self.diagnosis = Diagnosis(self.connection)
        self.diagnosis.show()

    def fio_patient_line_1(self):
        self.fio = self.line_5.text()

    def fio_patient_line_2(self):
        self.fio = self.lineEdit.text()

    def patient_id(self, state):
        """
        Заполнение окна пациента информацией о пациенте
        """
        if self.go_to_patient():
            fio = self.go_to_patient()
        else:
            fio = self.fio.split(" ")
        initials = ' '.join(fio)
        cursor = self.connection.cursor()
        cursor.execute('call r_patient(%s, %s, %s)',
                       (fio[0], fio[1], fio[2]))
        dict = cursor.fetchall()[0]

        self.id_patient = dict.get('patient_num')
        if state == 0:
            self.label_38.setText(initials)
            self.label_40.setText(dict.get('patient_phone'))
        else:
            self.label_3.setText(initials)
            self.label_8.setText(dict.get('patient_date').strftime('%Y-%m-%d'))
            self.label_11.setText(dict.get('patient_phone'))
            self.label_6.setText(dict.get('patient_mail'))

    def patient_guide(self):
        """
        Окно с информацией пациента
        """
        if self.stackedWidget_2.currentIndex() == 0:
            self.patient_id(0)
            return

        self.patient_id(1)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(1)
        cursor = self.connection.cursor()
        cursor.execute('call records_patient(%s, %s)',
                       (self.id_patient, self.specialist_id))
        create_table = CreateTable(self.table_5, cursor, 2)
        create_table.set_table()


    def set_completer(self, flag):
        """
        Заполнение выпадающего списка специалистами и специальностями из БД
        """
        words = []  # массив слов для QComleter
        cursor = self.connection.cursor()
        if flag == 0:
            cursor.execute('call show_patients(%s)',
                               (self.specialist_id)) # view
        else:
            cursor.execute('select diagnosis_name from diagnosis')

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
            completer = QCompleter(words, self.lineEdit)
            self.lineEdit.setCompleter(completer)
        else:
            completer = QCompleter(words, self.lineEdit_2)
            self.lineEdit_2.setCompleter(completer)


    def show_patient(self, state_table, first_date = None, second_date = None):
        """
        Заполнение таблицы записями пациентов
        """
        self.change_window()

        cursor = self.connection.cursor()
        if state_table == 0:
            cursor.execute('call show_patients(%s)',
                           (self.specialist_id))          # procedure

    def get_id(self):
        """
        Извлечение id специалиста по логину
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT specialist_num from specialist where specialist_login = %s", self.login)
        self.specialist_id = cursor.fetchall()[0].get('specialist_num')

    def create_table_ver_1(self):
        """
        Вызов функции построения таблицы записей пациентов
        с флагом 0 - отсортированная таблица по дате
        """
        self.create_list_records(0)

    def create_table_ver_2(self):
        """
        Вызов функции построения таблицы записей пациентов
        с флагом 1 - отсортированная таблица по алфавиту и дате
        """
        self.create_list_records(1)

    def create_table_ver_3(self):
        """
        Вызов функции построения таблицы записей пациентов
        с флагом 2 - отсортированная таблица по алфавиту
        в порядке убывания и по дате
        """
        self.create_list_records(2)

    def create_list_records(self, state_table, first_date = None, second_date = None):
        """
        Заполнение таблицы записями пациентов
        """
        self.change_window()

        cursor = self.connection.cursor()
        if state_table == 0:
            cursor.execute('call list_of_records_1(%s)',
                           (self.specialist_id))          # procedure
        elif state_table == 1:
            cursor.execute('call list_of_records_2(%s)',
                           (self.specialist_id))   # procedure
        elif state_table == 2:
            cursor.execute('call list_of_records_3(%s)',
                           (self.specialist_id))   # procedure
        elif state_table == 3:
            cursor.execute('call show_records_between_datetime(%s, %s, %s)',
                           (first_date, second_date, self.specialist_id))              # procedure

        create_table = CreateTable(self.table_3, cursor, 5)
        create_table.set_table()

    def show_filter(self):
        """
        Запуск окна с фильтром
        """
        self.filter = Filter(self)
        self.filter.show()

    def back(self):
        """
        Кнопка назад (возврат окна меню)
        """
        self.stackedWidget.setCurrentIndex(1)

    def change_window(self):
        """
        Функция смены окна в зависимости от нажатой кнопки
        (sender считывает какую кнопку вы нажали)
        """
        sender = self.sender()
        self.stackedWidget.setCurrentIndex(0) # смена окна в GUI
        if sender.text() == "Список записей":
            self.stackedWidget_2.setCurrentIndex(3)
        elif sender.text() == "График работы":
            self.stackedWidget_2.setCurrentIndex(4)
            self.create_table()
        elif sender.text() == "Ваши пациенты":
            self.stackedWidget_2.setCurrentIndex(5)
            self.show_patients()
        elif sender.text() == "Добавить запись":
            self.stackedWidget_2.setCurrentIndex(2)
        elif sender.text() == "Результат приема":
            self.stackedWidget_2.setCurrentIndex(0)

    def return_back(self):
        """
        Переход назад на окно с авторизацией
        """
        self.parent.show()
        self.parent.textEdit.setText("")
        self.parent.lineEdit.setText("")
        self.close()


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.back()



