import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

def get_db_connection():
    """
    Create and return a database connection
    """
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            print("Successfully connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

def close_db_connection(connection):
    """
    Close the database connection
    """
    if connection and connection.is_connected():
        connection.close()
        print("Database connection closed") 