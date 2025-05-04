from database import get_db_connection, close_db_connection
from mysql.connector import Error

def add_category(name, description=None):
    """
    Add a new category to the categories table.
    Args:
        name (str): Category name (required, must be unique).
        description (str, optional): Category description.
    Returns:
        tuple: (success (bool), message (str), category_id (int or None))
    """
    connection = get_db_connection()
    category_id = None
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO categories (name, description) VALUES (%s, %s)",
                (name, description)
            )
            connection.commit()
            category_id = cursor.lastrowid
            return True, "Category added successfully", category_id
        except Error as e:
            return False, f"Error: {str(e)}", None
        finally:
            close_db_connection(connection)
    return False, "Database connection failed", None

if __name__ == "__main__":
    # Example usage
    success, message, category_id = add_category(
        name="Test Category2",
        description="A test category for demonstration."
    )
    print(f"Add Category Success: {success}, Message: {message}, Category ID: {category_id}") 