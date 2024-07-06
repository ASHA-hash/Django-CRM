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
#
# import mysql.connector
# from mysql.connector import errorcode
#
# try:
#     # Establish a connection to the MySQL server
#     database = mysql.connector.connect(
#         host='localhost',
#         user='root',
#         password='1A2s3h4Asql@!@'
#     )
#     # Prepare cursor
#     cursor = database.cursor()
#
#     # Try to create the database
#     cursor.execute("CREATE DATABASE elderco")
#     print("Database 'elderco' created successfully.")
#
# except mysql.connector.Error as err:
#     if err.errno == errorcode.ER_DB_CREATE_EXISTS:
#         print("Database 'elderco' already exists.")
#     elif err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#         print("Something is wrong with your user name or password")
#     else:
#         print(err)
# else:
#     # If the database already exists or is created successfully, use it
#     cursor.execute("USE elderco")
#     print("Using the 'elderco' database.")

# # Close the cursor and database connection
# cursor.close()
# database.close()
