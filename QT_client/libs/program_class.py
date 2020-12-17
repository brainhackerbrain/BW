#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
import time
connection = sqlite3.connect("projects.db")
# cursor = connection.cursor()
# cursor.execute("CREATE TABLE projects ")
#cursor.execute("INSERT INTO projects ...")
# connection.commit()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
import os
connection = sqlite3.connect("projects.db")
# cursor = connection.cursor()
# cursor.execute("CREATE TABLE projects ")
#cursor.execute("INSERT INTO projects ...")
# connection.commit()

class BRN_program():
	id=1
	login=""
	password=""
	code=""
	status=1
	local_info_file_name="info.db"
	start_type=0
	hash="01234567890123456789012345678912"
	def __init__(self):
		self.load_local_info()
		self.start()
	def load_local_info(self):
		if os.path.isfile(self.local_info_file_name):
			self.__load_local_info()
		else:
			self.__create_local_info()
			print ("NO")

	def __create_local_info(self):
		connection = sqlite3.connect(self.local_info_file_name)
		self.status=2;
		cursor = connection.cursor()
		cursor.execute("CREATE TABLE program (id int, hash VARCHAR(32),status INT, dc INT,ping INT)")
		cursor.execute("CREATE TABLE program_starts (dc INT)")
		cursor.execute("INSERT INTO  program (id,hash, status ,dc,ping) VALUES ("+str(self.id)+",'"+self.hash+"', "+str(self.status)+","+str(int(time.time()))+","+str(int(time.time()))+")")
		# cursor.execute("INSERT INTO  program_starts (dc) VALUES ("+str(int(time.time()))+")")
		connection.commit()


	def start(self):
		connection = sqlite3.connect(self.local_info_file_name)
		cursor = connection.cursor()
		cursor.execute("INSERT INTO  program_starts (dc) VALUES ("+str(int(time.time()))+")")
		connection.commit()

	# def generate_insert_query(self):
	def __save_local_info(self):
		connection = sqlite3.connect(self.local_info_file_name)
		cursor = connection.cursor()
	def __load_local_info(self):
		print ("LOAD LOCAL INFO")
		connection = sqlite3.connect(self.local_info_file_name)
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM program")
		rows = cursor.fetchall()
		self.status= rows[0][2]
		self.dc=rows[0][3]
		self.ping=rows[0][4]
		self.hash=rows[0][1]
		self.id=rows[0][0]
		# for row in rows:
			# print(row)



