from database import get_db_connection, close_db_connection
from mysql.connector import Error

# Product-related database functions

def get_all_products():
    """
    Fetch all products with their category names.
    Returns:
        list of dict: Each dict contains product info and category name.
    """
    connection = get_db_connection()
    products = []
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            # Join products with categories to get category name
            cursor.execute('''
                SELECT p.id, p.name, p.description, p.price, p.stock, p.image_path, c.name AS category
                FROM products p
                LEFT JOIN categories c ON p.category_id = c.id
            ''')
            products = cursor.fetchall()
        except Error as e:
            print(f"Error fetching products: {str(e)}")
        finally:
            close_db_connection(connection)
    return products

def add_product(name, price, stock, description=None, category_id=None, image_path=None):
    """
    Add a new product to the products table.
    Args:
        name (str): Product name (required).
        price (float): Product price (required).
        stock (int): Stock quantity (required).
        description (str, optional): Product description.
        category_id (int, optional): Category ID (foreign key).
        image_path (str, optional): Path or URL to product image.
    Returns:
        tuple: (success (bool), message (str), product_id (int or None))
    """
    connection = get_db_connection()
    product_id = None
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT INTO products (name, description, price, stock, category_id, image_path)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (name, description, price, stock, category_id, image_path)
            )
            connection.commit()
            product_id = cursor.lastrowid
            return True, "Product added successfully", product_id
        except Error as e:
            return False, f"Error: {str(e)}", None
        finally:
            close_db_connection(connection)
    return False, "Database connection failed", None

def get_product_by_id(product_id):
    """
    Fetch a single product by its ID (with category name).
    Args:
        product_id (int): The product's unique ID.
    Returns:
        dict or None: Product info if found, else None.
    """
    connection = get_db_connection()
    product = None
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute('''
                SELECT p.id, p.name, p.description, p.price, p.stock, p.image_path, c.name AS category
                FROM products p
                LEFT JOIN categories c ON p.category_id = c.id
                WHERE p.id = %s
            ''', (product_id,))
            product = cursor.fetchone()
        except Error as e:
            print(f"Error fetching product by ID: {str(e)}")
        finally:
            close_db_connection(connection)
    return product

def search_products_by_name(name):
    """
    Search for products by (partial) name match.
    Args:
        name (str): The search string (case-insensitive, partial match).
    Returns:
        list of dict: Matching products with category names.
    """
    connection = get_db_connection()
    products = []
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute('''
                SELECT p.id, p.name, p.description, p.price, p.stock, p.image_path, c.name AS category
                FROM products p
                LEFT JOIN categories c ON p.category_id = c.id
                WHERE p.name LIKE %s
            ''', (f"%{name}%",))
            products = cursor.fetchall()
        except Error as e:
            print(f"Error searching products by name: {str(e)}")
        finally:
            close_db_connection(connection)
    return products

if __name__ == "__main__":
    # Example usage and testing
    print("All products:")
    all_products = get_all_products()
    for product in all_products:
        print(product)
    print("\nProduct by ID (1):")
    print(get_product_by_id(1))
    print("\nSearch products by name ('shirt'):")
    for product in search_products_by_name('shirt'):
        print(product)

    # Test add_product
    print("\nTesting add_product:")
    success, message, product_id = add_product(
        name="Test Product",
        price=49.99,
        stock=20,
        description="A test product for demonstration.",
        category_id=1,
        image_path="images/test_product.jpg"
    )
    print(f"Add Product Success: {success}, Message: {message}, Product ID: {product_id}")


