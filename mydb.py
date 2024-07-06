import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1A2s3h4Asql@!@'
)

# prepare cursor
cursor = database.cursor()

# create a database
cursor.execute("CREATE DATABASE elderco")
