from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QLabel, QVBoxLayout,QListWidgetItem,QTableView
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import * 

import numpy as np

class ProgramStatus(QWidget):
    def __init__(self,prog): 
        super().__init__()
        self.prog=prog 
        self.title = 'Статус'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
   
        self.setWindowTitle(self.title) 
        self.setGeometry(self.left, self.top, self.width, self.height) 
   
        self.createTable() 
   
        self.layout = QVBoxLayout() 
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 
   
        #Show window 
        self.show() 
   
    #Create table 
    def createTable(self): 
        self.tableWidget = QTableWidget() 
  
        #Row count 
        self.tableWidget.setRowCount(4)  
  
        #Column count 
        self.tableWidget.setColumnCount(2)   
  
        self.tableWidget.setItem(0,0, QTableWidgetItem("id")) 
        self.tableWidget.setItem(0,1, QTableWidgetItem(str(self.prog.id))) 

        self.tableWidget.setItem(1,0, QTableWidgetItem("hash")) 
        self.tableWidget.setItem(1,1, QTableWidgetItem(str(self.prog.hash))) 
        
        self.tableWidget.setItem(2,0, QTableWidgetItem("Статус")) 
        self.tableWidget.setItem(2,1, QTableWidgetItem("Статус")) 
        self.tableWidget.setItem(3,0, QTableWidgetItem("Дата запуска")) 
        # self.tableWidget.setItem(2,0, QTableWidgetItem("Alan")) 
        self.tableWidget.setItem(3,1, QTableWidgetItem(str(self.prog.dc))) 
        # self.tableWidget.setItem(4,0, QTableWidgetItem(str(self.prog.dc))) 
        # self.tableWidget.setItem(4,1, QTableWidgetItem(str(self.prog.dc))) 
        # self.tableWidget.setItem(3,0, QTableWidgetItem("Arnavi")) 
        # self.tableWidget.setItem(3,1, QTableWidgetItem("Mandsaur"))   
   
        #Table will fit the screen horizontally 
        self.tableWidget.horizontalHeader().setStretchLastSection(True) 
        self.tableWidget.horizontalHeader().setSectionResizeMode( 
            QHeaderView.Stretch) 
   
