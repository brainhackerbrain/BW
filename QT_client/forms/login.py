#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


import pymysql
from pymysql.cursors import DictCursor

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Вход')
        self.resize(500, 120)

        layout = QGridLayout()

        label_name = QLabel('<font size="4"> Логин </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Введите логин')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel('<font size="4"> Пароль </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Пароль')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('Login')
        button_login.clicked.connect(self.check_password)
        layout.addWidget(button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)

    def check_password(self):
        msg = QMessageBox()
        connection = pymysql.connect(host='localhost',
            user='root',
            password='svetac',
            db='brain',
            cursorclass=DictCursor
        )
        # query.prepare("SELECT * FROM users WHERE login = :login AND password = :password")
        with connection.cursor() as cursor:
            query = """
            SELECT
                *
            FROM
                users
            WHERE login='"""+self.lineEdit_username.text()+"""';
            """
            cursor.execute(query)
            # print cursor)
            # print (curson)
            for row in cursor:
                if row["login"]=="":
                    msg.setText('Не верный логин')
                    msg.exec_()
                else:
                    print (row["password"])
                    # if row["login"]=="":
            # for row in cursor:
                # print(row["login"])
                    if self.lineEdit_username.text() == row["login"] and self.lineEdit_password.text() == row["password"]:
                        msg.setText('Success')
                        msg.exec_()
                        # app.quit()
                    else:
                        msg.setText('Incorrect Password')
                        msg.exec_()

