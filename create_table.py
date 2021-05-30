from PyQt5.QtWidgets import QTableWidgetItem

class CreateTable:
    def __init__(self, table, cursor, count_column):
        self.table = table
        self.cursor = cursor
        self.count_column = count_column

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