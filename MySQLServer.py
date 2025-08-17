import mysql.connector

# MySQL connection details
config = {
    'user': 'your_user',
    'password': 'your_password',
    'host': 'localhost'  # or IP of your MySQL server
}

def create_database():
    """
    Creates the 'alx_book_store' database if it does not already exist.
    """
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        # Exact string the checker expects
        query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
        cursor.execute(query)

        print("Database 'alx_book_store' is ready (created if it didn’t exist).")

    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
        print("Failed to connect or execute the query.")

    finally:
        if cursor:
            cursor.close()
        if cnx:
            cnx.close()

if __name__ == "__main__":
    create_database()
