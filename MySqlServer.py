import mysql.connector

# Replace with your connection details
mydb = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    user="root",
    password="SqHijerker1#")


cursor = mydb.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

print("Database 'alx_book_store' created successfully!")

# Close the cursor and connection
cursor.close()
mydb.close()
print("MySQL connection closed.")