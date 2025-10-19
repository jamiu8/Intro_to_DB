import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server (no database specified since we’re creating one)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",           # change this to your MySQL username
        password="yourpassword"  # change this to your MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if connection.is_connected():
        connection.close()
        print("MySQL connection closed.")
