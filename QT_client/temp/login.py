
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login Form')
        self.resize(500, 120)

        layout = QGridLayout()

        label_name = QLabel('<font size="4"> Login </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('Login')
        button_login.clicked.connect(self.check_password)
        layout.addWidget(button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)

    def check_password(self):
        msg = QMessageBox()

        self.db = QSqlDatabase.addDatabase('QMYSQL')
        self.db.setHostName("localhost")
        self.db.setUserName("root")
        self.db.setPassword("svetac")
        self.db.setDatabaseName("brain")
        self.db.open()
        query = QSqlQuery()
        query.prepare("SELECT * FROM users WHERE login = :login AND password = :password")
        if self.lineEdit_username.text() == 'Usernmae' and self.lineEdit_password.text() == '000':
            msg.setText('Success')
            msg.exec_()
            app.quit()
        else:
            msg.setText('Incorrect Password')
            msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = LoginForm()
    form.show()

    sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QMessageBox, QLabel, QPushButton, QLineEdit, QSpinBox
# from PyQt5 import uic
# from PyQt5.QtSql import QSqlDatabase, QSqlQuery
# class Dialogo(QDialog):
#     def __init__(self):
#         QDialog.__init__(self)
#         uic.loadUi("login.ui", self)
#         self.setWindowTitle("Авторизация") # Title
#         self.resize(250, 250) # Размер окна
#         self.setMinimumSize(250, 150) # Минимальный размер окна
#         self.setMaximumSize(250, 250) # Максимальный размер окна
#         self.db_ok.clicked.connect(self.getDb) # Переход на getDb при нажатии на ОК
#         self.db_cancel.clicked.connect(self.dbCancel)
  
#     def getDb(self):
#         useDb = self.db_combobox.currentText() # Выбор базы
#         login = self.db_login.text() # Логин
#         password = self.db_password.text() # Пароль
#         self.db = QSqlDatabase.addDatabase('QMYSQL') # Драйвер для Mysql
#         self.db.setHostName("localhost")
#         self.db.setUserName("root")
#         self.db.setPassword("root")
#         self.db.setDatabaseName(useDb)
#         self.db.open()
#         query = QSqlQuery()
#         query.prepare("SELECT * FROM users WHERE login = :login AND password = :password")
#         query.bindValue(":login", login)
#         query.bindValue(":password", password)
#         query.exec_()
#         if query.next():
#             return True
#         return False
#     def dbCancel(self):
#         self.close()
  
# app = QApplication(sys.argv)
# dialogo = Dialogo()
# dialogo.show()
# app.exec_()