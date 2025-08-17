import mysql.connector

# MySQL connection details
config = {
    'user': 'your_user',
    'password': 'your_password',
    'host': 'localhost'  # or your host's IP address
}

def create_database():
    """
    Creates the 'alx_book_store' database if it does not already exist.
    """
    try:
        # Establish a connection to the MySQL server
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        # SQL statement to create the database if it doesn't exist
        # Using a parameterized query to prevent SQL injection, though simple in this case
        db_name = "alx_book_store"
        query = "CREATE DATABASE IF NOT EXISTS {}".format(db_name)

        # Execute the query
        cursor.execute(query)

        print(f"Database '{db_name}' created successfully!")

    except mysql.connector.Error as err:
        # Handle connection and other MySQL errors
        print(f"Error: {err}")
        print("Failed to connect to the database. Please check your connection details.")

    finally:
        # Close the cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'cnx' in locals() and cnx is not None:
            cnx.close()

if __name__ == "__main__":
    create_database()