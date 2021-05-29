from PyQt5.QtCore import Qt
import specialist_ui
from filter import Filter
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from datetime import *

class Specialist(QMainWindow, specialist_ui.SpecialistUi):
    def __init__(self, parent, connection, login):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.connection = connection
        self.login = login
        self.stackedWidget.setCurrentIndex(1)
        self.get_id()
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
        self.btn_65.clicked.connect(self.show_filter)
        self.btn_68.clicked.connect(self.show_filter)

    def get_id(self):
        """
        Извлечение id специалиста по логину
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT specialist_num from specialist where specialist_login = %s", self.login)
        self.specialist_id = cursor.fetchall()[0].get('specialist_num')
        print(self.specialist_id)

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
        count = 0
        cursor = self.connection.cursor()
        if state_table == 0:
            cursor.execute("SELECT * FROM list_of_records_var_1") # view

        elif state_table == 1:
            cursor.execute("SELECT * FROM list_of_records_ver_2")  # view

        elif state_table == 2:
            cursor.execute("SELECT * FROM list_of_records_ver_3")  # view

        elif state_table == 3:
            cursor.execute('call show_records_beetween(%s, %s)',
                           (first_date, second_date)) # procedure

        j = 0
        self.table_3.setRowCount(0)
        self.table_3.setColumnCount(5)
        self.table_3.insertRow(0)

        row = cursor.fetchone()
        while row is not None:
            mass = list(row.items())
            for i in range(len(mass)):
                item = QTableWidgetItem()
                item.setText(str(mass[i][1]))
                self.table_3.setItem(j, i, item)
            j += 1
            self.table_3.insertRow(j)
            row = cursor.fetchone()

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
        elif sender.text() == "Ваши пациенты":
            self.stackedWidget_2.setCurrentIndex(5)
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
