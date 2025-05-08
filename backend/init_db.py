from backend.database_schema import initialize_database
from backend.database import get_db_connection, close_db_connection

def init_database():
    """
    Initialize the database with all required tables
    """
    print("Initializing database...")
    
    # Initialize new tables
    initialize_database()
    
    # Check if products table has the new columns
    connection = get_db_connection()
    if not connection:
        print("Failed to connect to database")
        return
    
    try:
        cursor = connection.cursor()
        
        # Check if is_active column exists in products table
        cursor.execute("""
            SELECT COUNT(*)
            FROM information_schema.columns
            WHERE table_name = 'products'
            AND column_name = 'is_active'
        """)
        
        if cursor.fetchone()[0] == 0:
            # Add is_active column if it doesn't exist
            cursor.execute("""
                ALTER TABLE products
                ADD COLUMN is_active BOOLEAN DEFAULT 1
            """)
            connection.commit()
            print("Added is_active column to products table")
        
        # Check if category column exists in products table
        cursor.execute("""
            SELECT COUNT(*)
            FROM information_schema.columns
            WHERE table_name = 'products'
            AND column_name = 'category'
        """)
        
        if cursor.fetchone()[0] == 0:
            # Add category column if it doesn't exist
            cursor.execute("""
                ALTER TABLE products
                ADD COLUMN category VARCHAR(50)
            """)
            connection.commit()
            print("Added category column to products table")
        
        # Check if image_url column exists in products table
        cursor.execute("""
            SELECT COUNT(*)
            FROM information_schema.columns
            WHERE table_name = 'products'
            AND column_name = 'image_url'
        """)
        
        if cursor.fetchone()[0] == 0:
            # Add image_url column if it doesn't exist
            cursor.execute("""
                ALTER TABLE products
                ADD COLUMN image_url VARCHAR(255)
            """)
            connection.commit()
            print("Added image_url column to products table")
        
        print("Database initialization completed successfully")
        
    except Exception as e:
        print(f"Error initializing database: {e}")
    finally:
        close_db_connection(connection)

if __name__ == "__main__":
    init_database() 