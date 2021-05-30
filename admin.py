
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.QtCore import Qt
import sys
from ui_py import admin_ui
from create_table import CreateTable
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Admin(QMainWindow, admin_ui.AdminUi):
    def __init__(self, parent, connection):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.connection = connection

        #обновление окон специалистов и специальностей
        self.tabWidget.currentChanged.connect(self.update_window)

        #переключение между специалистами и пациентами(меню)
        self.btn_2.clicked.connect(self.change_window)
        self.btn_3.clicked.connect(self.change_window)

        #возврат на авторизацию
        self.btn.clicked.connect(self.return_back)

        #смена содержимого окна (специальности, специалисты)
        self.btn_8.clicked.connect(self.change_window)
        self.btn_11.clicked.connect(self.change_window)

        #смена внутреннего tabwidget
        self.btn_5.clicked.connect(self.update_tabwidget)
        self.btn_6.clicked.connect(self.update_tabwidget)
        self.btn_9.clicked.connect(self.update_tabwidget)
        self.btn_10.clicked.connect(self.update_tabwidget)
        self.btn_14.clicked.connect(self.update_tabwidget)
        self.btn_13.clicked.connect(self.update_tabwidget)

        #кнопка назад
        self.btn_19.clicked.connect(self.back)
        self.btn_20.clicked.connect(self.back)
        self.btn_21.clicked.connect(self.back)
        self.btn_22.clicked.connect(self.back)

        #добавление записей в бд
        self.btn_7.clicked.connect(self.add_specialty)
        self.line_33.textChanged.connect(self.clear_line_specialty)
        self.btn_4.clicked.connect(self.add_specialist)

        #кнопка показа специалистов
        self.btn_5.clicked.connect(self.show_specialist)

        # кнопка показа специальностей
        self.btn_9.clicked.connect(self.show_list_specialty)


    def list_specialty(self):
        """
        Метод для формирования массива специальностей
        :return: массив специальностей из бд
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT count(specialty_num) from specialty")
        count = cursor.fetchall()[0].get('count(specialty_num)')
        mass_specialty = []
        for i in range(1, count + 1):
            cursor.execute("SELECT specialty_name FROM specialty WHERE specialty_num = %s", (i))
            dict = cursor.fetchall()[0]
            mass = list(dict.items())
            mass_specialty.append(mass[0][1])
        return mass_specialty


    def show_list_specialty(self):
        """
        Заполнение таблицы специальностями
        """
        cursor = self.connection.cursor()
        mass_specialty = self.list_specialty()
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(len(mass_specialty))
        for i in range(1, len(mass_specialty)+1):
            cursor.execute("SELECT specialty_name FROM specialty WHERE specialty_num = %s", (i))
            dict = cursor.fetchall()[0]
            dict_2 = list(dict.items())

            for j in range(0, len(dict)):
                item = QTableWidgetItem()
                item.setText(str(dict_2[j][1]))
                self.tableWidget.setItem(i - 1, j, item)

        # заполнение столбца количества специалистов
        cursor = self.connection.cursor()
        cursor.execute("SELECT specialty_specialty_num FROM specialists_specialties")
        dict = cursor.fetchall()
        dict_3 = []
        for item in dict:
            dict_3.append(item.get('specialty_specialty_num'))
        for item in set(dict_3):
            item2 = QTableWidgetItem()
            item2.setText(str(dict_3.count(item)))
            self.tableWidget.setItem(item-1, 1, item2)


    def add_specialty(self):
        """
        Добавление новых специальностей в БД
        """
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO specialty (specialty_name) values (%s)", (self.line_33.text()))
        self.connection.commit()
        self.label_33.setText("Специальность добавлена")

    def clear_line_specialty(self):
        """
        Очистка поля добавления специальности
        """
        self.label_33.setText("")

    def clear_line_specialist(self):
        """
        Очистка полей после добавление специалиста
        """
        self.line_2.setText('')
        self.line_5.setText('')
        self.line.setText('')
        self.line_8.setText('')
        self.line_7.setText('')
        self.line_6.setText('')
        self.line_3.setText('')

    def show_specialist(self):
        """
        Заполнение таблицы со специалистами
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT * from list_specialist")
        self.create_table = CreateTable(self.table_3, cursor, 8)
        self.create_table.set_table()

    def add_specialist(self):
        """
        Добавление нового специалиста в БД
        """
        self.cursor = self.connection.cursor()

        # Первоначальная ЗП
        self.cursor.execute("SELECT count(salary_num) from salary")
        count = self.cursor.fetchall()[0].get('count(salary_num)')
        self.cursor.execute("INSERT INTO salary (salary_num, salary) values (%s, %s)", (count+1, self.line_3.text()))
        self.connection.commit()

        # Добавление специалиста
        self.cursor.execute("INSERT INTO specialist (specialist_num, specialist_name, "
                            "specialist_surname, specialist_patronymic, "
                            "specialist_date, specialist_login, "
                            "specialist_password, salary_salary_num) values (%s, %s, %s, %s, %s, %s, %s, %s)",
                            (count + 1,
                            self.line_2.text(),
                             self.line_5.text(),
                             self.line.text(),
                             self.line_8.text(),
                             self.line_7.text(),
                             self.line_6.text(),
                             count + 1)
                            )

        self.connection.commit()
        self.label_34.setText("Специалист добавлен")
        self.cursor.execute("SELECT count(specialist_num) from specialist")
        count_specialist = self.cursor.fetchall()[0].get('count(specialist_num)')

        # добавление аккаунта в user
        self.cursor.execute("INSERT INTO user (user_login, user_password, type) values(%s, %s, %s)",
                            (self.line_7.text(), self.line_6.text(), 1))
        self.connection.commit()

        # блок для соответствия специальностей с сотрудником
        mass = self.list_specialty()
        mass_specialty = self.line_4.text().split(', ')
        for specialty in mass_specialty:
            try:
                index = mass.index(specialty) + 1
            except Exception:
                print('Такой специальности не существует')
                return

            self.cursor.execute("INSERT INTO specialists_specialties (specialty_specialty_num, "
                                "specialist_specialist_num) values (%s, %s)", (index, count_specialist))
            self.connection.commit()
        self.clear_line_specialist()

    def back(self):
        """
        Кнопка назад(возврат окна меню)
        """
        if self.tabWidget.currentIndex() == 1:
            self.stackedWidget_2.setCurrentIndex(1)
        else:
            self.stackedWidget_3.setCurrentIndex(1)

    def update_tabwidget(self):
        """
        смена содержимого вкладки tabwidget
        """
        sender = self.sender().text()
        if self.tabWidget.currentIndex() == 1:
            if sender == "Показать список\nспециалистов":
                self.stackedWidget_2.setCurrentIndex(2)
            else:
                self.stackedWidget_2.setCurrentIndex(0)
        else:
            if sender == "Показать список\nспециальностей":
                self.stackedWidget_3.setCurrentIndex(0)
            else:
                self.stackedWidget_3.setCurrentIndex(2)

    def update_window(self):
        """
        Обновление содержимого окон Специальности и Специалисты при переключении
        вкладок tabWidget
        """
        self.stackedWidget_3.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(1)

    def change_window(self):
        """
        Функция смены окна в зависимости от нажатой кнопки
        (sender считывает какую кнопку вы нажали)
        """
        sender = self.sender()
        self.stackedWidget_6.setCurrentIndex(0) # смена окна в GUI
        if sender.text() == "Специалисты":
            self.stackedWidget.setCurrentIndex(0)
        else:
            self.stackedWidget.setCurrentIndex(1)

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
