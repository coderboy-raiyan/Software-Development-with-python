import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456"
)

db_name = "test_db"

cursor = db_connection.cursor()

sqlquery = "CREATE DATABASE " + db_name

cursor.execute(sqlquery)
