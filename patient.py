from PyQt5.QtWidgets import QMainWindow, QCompleter
from ui_py import patient_ui
from create_table import CreateTable
from recording import Recording
from error import Error


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

        # кнопки поиска специалистов
        self.btn_69.clicked.connect(self.search_specialist)
        self.btn_70.clicked.connect(self.show_specialists)
        self.btn_2.clicked.connect(self.search_specialist)
        # смена графика специалиста при нажатии на дату календаря
        self.calendarWidget.clicked['QDate'].connect(self.create_table)

        # запуск окна записи
        self.btn_14.clicked.connect(self.recording_window)

        # кнопки возвращения назад
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
        """
        try:

            datetime = f"{self.date_string} " \
                       f"{self.table_4.item(self.table_4.currentRow(), 0).text()}"
            fio = f"{self.surname} {self.name} {self.patronymic}"
            self.recording = Recording(self, self.connection, fio, datetime, self.id_sp, self.id_pt)
            self.recording.show()
        except Exception as ex:
            print(ex)

    def back(self):
        """
        Возрат на начальное меню
        """
        self.stackedWidget.setCurrentIndex(0)
        self.line_5.setText("")
        self.line_6.setText("")

    def search_specialist(self):
        """
        Извлечение id специалиста
        """
        try:
            self.id_sp = self.id_specialist()
        except Exception:
            self.error = Error(self, 'Поиск ничего не нашел, попробуйте снова')
            return
        self.create_table()

    def create_table(self):
        """
        создание таблицы занятости специалиста
        :param today: выбранное время на календаре
        """
        date = self.calendarWidget.selectedDate()
        self.date_string = date.toString('yyyy-MM-dd')
        self.stackedWidget.setCurrentIndex(1)
        create_table = CreateTable(self.table_4, id_specialist=self.id_sp, connection=self.connection)
        create_table.create_table(self.date_string)

    def show_specialists(self):
        """
        Заполнение таблицы специалистами
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute('call show_specialists(%s)',
                           (self.line_6.text()))  # procedure
        except Exception:
            self.error = Error(self, 'Поиск ничего не нашел, попробуйте снова')
            return
        self.stackedWidget.setCurrentIndex(2)
        create_table = CreateTable(self.tableWidget, cursor, 4)
        create_table.set_table()

    def id_specialist(self):
        """
        Получение id специалиста
        :return: значение id специалиста
        """
        if self.stackedWidget.currentIndex() == 2:
            num_row = self.tableWidget.currentRow()
            self.surname = self.tableWidget.item(num_row, 0).text()
            self.name = self.tableWidget.item(num_row, 1).text()
            self.patronymic = self.tableWidget.item(num_row, 2).text()
        else:
            fio = self.line_5.text().split(" ")
            self.surname = fio[0]
            self.name = fio[1]
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
