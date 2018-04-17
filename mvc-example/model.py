#!/usr/bin/env python3

import sqlite3


class Model:

	def __init__(self,dbname):
		self.connection = sqlite3.connect(dbname)
		self.cursor = self.connection.cursor()

	def cretetables(self,tablename):

		query = 'CREATE TABLE IF NOT EXISTS {}(testid integer, testname text);'
		self.cursor.execute(query)
		self.connection.commit()

connection = None
cursor = None

def createsql():
	global connection, cursor

	connection = sqlite3.connect('example.db')
	cursor = connection.cursor()

def cretetables():
	global connection, cursor

	query = 'CREATE TABLE IF NOT EXISTS test(testid integer, testname text);'
	cursor.execute(query)
	connection.commit()

def insertvalues(arg1,arg2):
	global connection, cursor

	cursor.execute("INSERT INTO test VALUES(?,?);",[arg1,arg2])
	connection.commit()


def getallvalues():
	global connection, cursor

	query = 'SELECT * FROM test;'
	cursor.execute(query)
	t = cursor.fetchall()
	print(t)
	return (t)

def closeconnection():
	global connection, cursor

	connection.commit()
	connection.close()

