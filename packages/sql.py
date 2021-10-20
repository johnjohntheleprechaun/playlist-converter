
import sqlite3
from sqlite3 import Error

TABLE_CREATION = """
CREATE TABLE IF NOT EXISTS {table_name} (
	{data_str}
);
"""

def create_connection(path: str):
	connection = None
	try:
		connection = sqlite3.connect(path)
		print("connection to SQL was successful!")
	except Error as e:
		print("the error was: {}".format(e))

	return connection

def create_table(connection: sqlite3.Connection, name: str, columns: dict):
	data_str = ""
	for column in columns:
		data_str += "{name} {data_type}".format(name=column, data_type=columns[column])
	print(data_str)

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