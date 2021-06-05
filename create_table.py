from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt


class CreateTable:
    def __init__(self, table, cursor=None, count_column=None, id_specialist=None, connection=None):
        self.table = table
        self.cursor = cursor
        self.count_column = count_column
        self.id = id_specialist
        self.connection = connection

    def set_table(self):
        """
        метод заполнения таблицы данными
        """
        j = 0
        self.table.setRowCount(0)
        self.table.setColumnCount(self.count_column)
        self.table.insertRow(0)

        row = self.cursor.fetchone()
        while row is not None:
            mass = list(row.items())
            for i in range(len(mass)):
                item = QTableWidgetItem()
                item.setText(str(mass[i][1]))
                self.table.setItem(j, i, item)
            j += 1
            self.table.insertRow(j)
            row = self.cursor.fetchone()

    def create_table(self, today):

        mass_datetime = self.datetime_specialist()  # массив занятости специалиста

        hour = 8
        count_row = 0
        self.table.setRowCount(0)
        self.table.setColumnCount(2)
        self.table.insertRow(0)

        current_time = today

        for j in range(hour, 20):
            item = QTableWidgetItem()
            time = f"{j}:00:00"
            item.setText(time)
            current_time += ' ' + time
            self.table.setItem(count_row, 0, item)
            if current_time in mass_datetime:
                item = QTableWidgetItem()
                item.setText("Занят")
                item.setBackground(Qt.red)
                self.table.setItem(count_row, 1, item)
            count_row += 1
            self.table.insertRow(count_row)
            current_time = today

    def datetime_specialist(self):
        """
        Формирование массива занятости специалиста
        """
        mass_datetime = []
        cursor = self.connection.cursor()
        cursor.execute("SELECT reception_datetime from reception where specialist_specialist_num = %s", (self.id))
        row = cursor.fetchone()
        while row is not None:
            mass = list(row.items())
            mass_datetime.append(mass[0][1].strftime('%Y-%m-%d %H:%M:%S'))
            row = cursor.fetchone()
        return mass_datetime