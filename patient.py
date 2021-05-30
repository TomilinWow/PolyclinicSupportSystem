
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui_py import patient_ui

class Patient(QMainWindow, patient_ui.PatientUi):
    def __init__(self, parent, connection, login):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.connection = connection



