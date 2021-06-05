from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from ui_py import ui
from admin import Admin
from patient import Patient
from specialist import Specialist
from error import Error
from PyQt5.QtCore import Qt
from registration import Registration
from connect_db import ConnectDb
import sys

class MainWindow(QMainWindow, ui.Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connect = ConnectDb()
        self.connection = self.connect.connect_db()
        # self.clear_db()
        self.pushButton.clicked.connect(self.check_user)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton_4.clicked.connect(self.window_reg)


    # def clear_db(self):
    #     """
    #     Очистка бд
    #     """
    #     with self.connection.cursor() as cursor:
    #         cursor.execute("DELETE FROM user")
    #         cursor.execute("ALTER TABLE user AUTO_INCREMENT = 0")
    #         self.connection.commit()
    #

    def add(self):
        """
        Добавление записи в БД
        """
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO user (user_num, user_login, "\
                            "user_password, type) values (%s, %s, %s, %s)", (1, 'Admin', '',0))
        self.connection.commit()

    def patient_window(self, login):
        """
        запуск окна пациента
        """
        self.patient = Patient(self, self.connection, login)
        self.patient.show()
        self.close()

    def window_reg(self):
        """
        запуск окна регистрации пациента
        """
        self.registration = Registration(self, self.connection)
        self.registration.show()
        self.close()

    def check_user(self):
        """
        Проверка пользователя
        """
        login = self.textEdit.toPlainText()  # считывание логина с поля textEdit
        password = self.lineEdit.text()  # считывание пароля с поля lineEdit
        self.cursor = self.connection.cursor()  # курсор для взаимодейтсвия с БД
        self.cursor.execute("SELECT user_num, user_password, type FROM user WHERE user_login = %s",
                            (login))  # достаем id по введенному логину
        dict = self.cursor.fetchall()
        try:
            dict = dict[0]
            id = dict.get('id')  # значение id пользователя
        except Exception:
            self.error_window(0)  # вызов ошибки, если пользователя не существует
            return
        type = dict.get('type')
        user_password = dict.get('user_password')  # пароль пользователя
        if user_password == password:
            if type == 0:
                self.admin_window()  # запуск окна Админа
            elif type == 1:
                self.specialist_window(login)
            else:
                self.patient_window(login)
        else:
            self.error_window(1)


    def specialist_window(self, login):
        """
        Запуск окна специалиста
        """
        self.specialist = Specialist(self, self.connection, login)
        self.specialist.show()
        self.close()

    def admin_window(self):
        """
        Запуск окна администрации
        """
        self.admin = Admin(self, self.connection)
        self.admin.show()
        self.close()

    def error_window(self, flag):
        """
        Запуск ошибки
        """
        if flag == 1:
            self.error = Error(self, 'Введен неправильный \nпароль, попробуйте снова')
        else:
            self.error = Error(self, 'Пользователя с таким именем \nне существует, попробуйте снова')

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Enter:
            self.check_user()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())