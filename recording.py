from PyQt5.QtWidgets import *
from ui_py import recording_ui


class Recording(QDialog, recording_ui.RecordingUi):
    def __init__(self, parent, connection, fio, datetime, id_specialist, id_patient):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.connection = connection
        self.fio = fio
        self.datetime = datetime
        self.id_specialist = id_specialist
        self.id_patient = id_patient
        self.label.setText(fio + " " + datetime)

        self.btn_14.clicked.connect(self.create_record)

    def create_record(self):
        """
        Создание записи приема
        """
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO reception (reception_datetime, "
                            "description, patient_patient_num, specialist_specialist_num"
                            ") values (%s, %s, %s, %s)", (self.datetime,
                                                          self.textEdit.toPlainText(),
                                                          self.id_patient,
                                                          self.id_specialist
                                                          ))
        self.connection.commit()
        self.clear_line()

        # добавление связи специалист-пациент
        cursor.execute('select count(specialist_specialist_num) from '
                       'specialists_patients where (specialist_specialist_num ='
                       ' %s and patient_patient_num = %s)', (self.id_specialist, self.id_patient))

        try:
            cursor.execute("Insert into specialists_patients (specialist_specialist_num, "
                           "patient_patient_num) values(%s, %s)", (self.id_specialist, self.id_patient))
            self.connection.commit()
        except Exception as ex:
            pass
        self.parent.create_table()

    def clear_line(self):

        self.textEdit.setText("")
        self.label.setText("Запись добавлена")