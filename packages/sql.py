import sqlite3
from sqlite3 import Error

TABLE_CREATION = "CREATE TABLE IF NOT EXISTS {table_name} ({data_str});"
VALUE_INSERTION = "INSERT INTO {table_name}({value_types}) Values {values}"

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
	i = 0
	for column in columns:
		#column = columns[i]
		data_str += "{name} {data_type}".format(name=column, data_type=columns[column])

		#add comma
		if not i == len(columns)-1:
			data_str += ","
		i += 1
	final = TABLE_CREATION.format(table_name=name, data_str=data_str)
	write_query(connection, final)

def insert_data(connection: sqlite3.Connection, table_name: str, value_types: list, values: dict):
	#Generate value types string
	value_types_str = ""
	for i in range(len(value_types)):
		value_type = value_types[i]
		value_types_str += value_type
		#Commas
		if i < len(value_types)-1:
			value_types_str += ", "
	
	#Genrate values string
	values_str = ""
	for i in range(len(values)):
		value = values[i]
		values_str += str(value)
		#Commas
		if i < len(values)-1:
			values_str += ", "

	query = VALUE_INSERTION.format(table_name="test", value_types=value_types_str, values=values_str)
	write_query(connection, query)

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