from database import get_db_connection, close_db_connection
from mysql.connector import Error

class Auth:
    def __init__(self):
        self.connection = get_db_connection()
        
    def __del__(self):
        if self.connection:
            close_db_connection(self.connection)
    
    def signup(self, user_name, password_, email, user_phone=None, addr_city=None, addr_street=None, addr_bn=None):
        """
        Register a new user with the correct columns
        Returns: (success, message)
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO user (user_name, password_, email, user_phone, addr_city, addr_street, addr_bn) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (user_name, password_, email, user_phone, addr_city, addr_street, addr_bn)
            )
            self.connection.commit()
            return True, "User registered successfully"
        except Error as e:
            return False, f"Error: {str(e)}"
    
    def login(self, user_name, password_):
        """
        Simple user login with correct columns
        Returns: (success, message)
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "SELECT user_id FROM user WHERE user_name = %s AND password_ = %s",
                (user_name, password_)
            )
            if cursor.fetchone():
                return True, "Login successful"
            return False, "Invalid username or password"
        except Error as e:
            return False, f"Error: {str(e)}" 