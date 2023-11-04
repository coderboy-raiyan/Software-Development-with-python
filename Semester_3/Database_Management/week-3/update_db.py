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
    UPDATE students
    SET name = "RR"
    WHERE roll = "0001"
'''

cursor.execute(sql_query)
db_connection.commit()
print("update done")
