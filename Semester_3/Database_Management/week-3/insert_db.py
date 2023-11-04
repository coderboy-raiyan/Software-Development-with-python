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
INSERT INTO students (roll, name) VALUES (
    "0001",
    "Raiyan"
)
'''

cursor.execute(sql_query)
db_connection.commit()
print("Insert done")
