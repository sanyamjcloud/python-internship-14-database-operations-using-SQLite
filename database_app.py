import sqlite3
from sqlite3 import Error


DB_NAME = "users.db"


# -------------------------------
# 1. Create Connection
# -------------------------------
def create_connection():
    try:
        conn = sqlite3.connect(DB_NAME)
        return conn
    except Error as e:
        print("Error connecting to database:", e)
        return None


# -------------------------------
# 2. Create Table Programmatically
# -------------------------------
def create_table(conn):
    query = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        age INTEGER
    );
    """
    conn.execute(query)
    conn.commit()


# -------------------------------
# 3. Insert Record (Parameterized)
# -------------------------------
def insert_user(conn, name, email, age):
    query = "INSERT INTO users (name, email, age) VALUES (?, ?, ?)"
    try:
        conn.execute(query, (name, email, age))
        conn.commit()
        print("User added successfully.")
    except Error as e:
        print("Insert Error:", e)


# -------------------------------
# 4. Fetch Records
# -------------------------------
def fetch_users(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    if not rows:
        print("\nNo records found.\n")
        return

    print("\n--- User Records ---")
    print("{:<5} {:<15} {:<25} {:<5}".format("ID", "Name", "Email", "Age"))
    print("-" * 55)

    for row in rows:
        print("{:<5} {:<15} {:<25} {:<5}".format(*row))
    print()


# -------------------------------
# 5. Update Record
# -------------------------------
def update_user(conn, user_id, name, email, age):
    query = """
    UPDATE users
    SET name = ?, email = ?, age = ?
    WHERE id = ?
    """
    cursor = conn.execute(query, (name, email, age, user_id))
    conn.commit()

    if cursor.rowcount:
        print("User updated successfully.")
    else:
        print("User ID not found.")


# -------------------------------
# 6. Delete Record
# -------------------------------
def delete_user(conn, user_id):
    query = "DELETE FROM users WHERE id = ?"
    cursor = conn.execute(query, (user_id,))
    conn.commit()

    if cursor.rowcount:
        print("User deleted successfully.")
    else:
        print("User ID not found.")


# -------------------------------
# 7. Menu UI
# -------------------------------
def menu():
    print("""
========= USER DATABASE =========
1. Add User
2. View Users
3. Update User
4. Delete User
5. Exit
""")


# -------------------------------
# 8. Main App Logic
# -------------------------------
def main():
    conn = create_connection()
    if conn is None:
        return

    create_table(conn)

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            email = input("Email: ")
            age = int(input("Age: "))
            insert_user(conn, name, email, age)

        elif choice == "2":
            fetch_users(conn)

        elif choice == "3":
            user_id = int(input("Enter user ID to update: "))
            name = input("New Name: ")
            email = input("New Email: ")
            age = int(input("New Age: "))
            update_user(conn, user_id, name, email, age)

        elif choice == "4":
            user_id = int(input("Enter user ID to delete: "))
            delete_user(conn, user_id)

        elif choice == "5":
            print("Closing database connection...")
            conn.close()
            break

        else:
            print("Invalid choice. Try again.")


# -------------------------------
# Run Program
# -------------------------------
if __name__ == "__main__":
    main()
