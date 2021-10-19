
import sqlite3
from sqlite3 import Error

def create_connection(path: str):
	connection = None
	try:
		connection = sqlite3.connect(path)
		print("connection to SQL was successful!")
	except Error as e:
		print("the error was: {}".format(e))

	return connection

def write_query(connection: sqlite3.Connection, query: str):
	cursor = connection.cursor()
	try:
		cursor.execute(query)
		connection.commit()
		print("Query executed successfully")
	except Error as e:
		print(f"The error '{e}' occurred")

def read_query(connection: sqlite3.Connection, query: str):
	cursor = connection.cursor()
	try:
		cursor.execute(query)
		result = cursor.fetchall()
		return result
	except Error as e:
		print(f"the error {e} occurred")
		return None