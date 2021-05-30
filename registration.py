from ui_py import registration_ui
from PyQt5.QtWidgets import QDialog
import string
import random

class Registration(QDialog, registration_ui.RegistrationUi):
    def __init__(self, parent, connection):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.connection = connection
        self.char = string.ascii_letters + string.digits
        self.line_2.textChanged.connect(self.clear_line_specialty)
        self.btn_36.clicked.connect(self.return_back)
        self.pushButton.clicked.connect(self.random_login_password)
        self.btn_2.clicked.connect(self.add_patient)

    def random_login_password(self):
        """
        метод генерации случайных пароля и логина
        длиной от 6 до 8 символов
        """
        login = ''
        password = ''
        for i in range(random.randint(6, 8)):
            login += random.choice(self.char)
            password += random.choice(self.char)

        self.line_6.setText(login)
        self.line_3.setText(password)

    def add_patient(self):

        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT count(patient_num) from patient")
        count = self.cursor.fetchall()[0].get('count(patient_num)')
        # Добавление специалиста
        self.cursor.execute("INSERT INTO patient (patient_num, patient_date, "
                            "patient_mail, patient_phone, "
                            "patient_name, patient_surname, "
                            "patient_patronymic) values (%s, %s, %s, %s, %s, %s, %s)",
                            (count + 1,
                            self.line_8.text(),
                             self.line_7.text(),
                             self.line_4.text(),
                             self.line_2.text(),
                             self.line_5.text(),
                             self.line.text())
                            )

        # добавление аккаунта в user
        self.cursor.execute("INSERT INTO user (user_login, user_password, type) values(%s, %s, %s)",
                            (self.line_6.text(), self.line_3.text(), 2))
        self.connection.commit()
        self.label_9.setText("Вы добавлены!!!\nВоспользуйтесь логином и паролем, чтобы войти в систему")
        self.clear_line()

    def return_back(self):
        """
        Переход назад на окно с авторизацией
        """
        self.parent.show()
        self.parent.textEdit.setText("")
        self.parent.lineEdit.setText("")
        self.close()

    def clear_line_specialty(self):
        """
        Очистка поля добавления пациента
        """
        self.label_9.setText("")

    def clear_line(self):
        """
        Очистка полей регистрации
        """
        self.line_8.setText('')
        self.line_7.setText('')
        self.line_4.setText('')
        self.line_2.setText('')
        self.line_5.setText('')
        self.line.setText('')