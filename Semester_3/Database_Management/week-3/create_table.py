import mysql.connector

db_name = "test_db"

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database=db_name
)


cursor = db_connection.cursor()

sql_query = '''
CREATE TABLE students (
    roll CHAR(4),
    name VARCHAR(10) NOT NULL
)
'''

cursor.execute(sql_query)
print("Table created ")
