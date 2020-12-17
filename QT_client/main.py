#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
sys.path.insert(0, 'forms/');
sys.path.insert(0, 'libs/');



from login import LoginForm
from contacts import Contactslist
from programstatus import ProgramStatus
from program_class import *


import pymysql
from pymysql.cursors import DictCursor



if __name__ == '__main__':
    ap=BRN_program()
    
    app = QApplication(sys.argv)
    if ap.status==0:
        form = LoginForm()
        form.show()
    elif ap.status==1:
        form = Contactslist()
        form.show()
    else:
        form = ProgramStatus(ap)
        form.show()
    sys.exit(app.exec_())
