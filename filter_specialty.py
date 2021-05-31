from PyQt5.QtWidgets import QDialog
from ui_py import filter_specialty_ui
from create_table import CreateTable


class FilterSpecialty(QDialog, filter_specialty_ui.FilterUi):
    def __init__(self, parent, connection):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.connection = connection
        self.btn_2.clicked.connect(self.apply)

    def apply(self):
        self.lineEdit.text()
        cursor = self.connection.cursor()
        cursor.execute('call table_filter_specialty(%s)',
                       (self.lineEdit.text()))
        create_table = CreateTable(self.parent.table_3, cursor, 8)
        create_table.set_table()
        self.close()

