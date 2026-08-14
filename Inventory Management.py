import sqlite3
from datetime import datetime
con = sqlite3.connect("inventory.db")
cursor = con.cursor()

cursor.execute("PRAGMA foreign_keys = ON")
# print("Database created")


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
     user_id INTEGER PRIMARY KEY AUTOINCREMENT,
     username TEXT UNIQUE,
     password TEXT,
     role TEXT
)
""")

con.commit()

# print("Users table created")


cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT,
    category TEXT,
    price REAL,
    quantity INTEGER
)
""")

con.commit()

# print("Products table created")

cursor.execute("""
CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    supplier_name TEXT,
    phone TEXT,
    email TEXT
)
""")

con.commit()
def add_supplier():
    print("\n--- ADD SUPPLIER ---")

    try:
        supplier_name = input("Enter supplier name: ").strip()
        phone = input("Enter phone number: ").strip()
        email = input("Enter email: ").strip()

        if supplier_name == "":
            print("Supplier name cannot be empty")
            return

        cursor.execute("""
        INSERT INTO suppliers (supplier_name, phone, email)
        VALUES (?, ?, ?)
        """, (supplier_name, phone, email))

        con.commit()

        print("Supplier added successfully")

    except sqlite3.Error:
         print("Database error")
def view_suppliers():
    print("\n--- SUPPLIER LIST ---")

    cursor.execute("SELECT * FROM suppliers")
    suppliers = cursor.fetchall()

    if not suppliers:
        print("No suppliers found")
        return

    for supplier in suppliers:
        print(supplier)
# print("Suppliers table created")

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    user_id INTEGER,
    transaction_type TEXT,
    quantity INTEGER,
    transaction_date TEXT,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
)
""")

con.commit()

# print("Transactions table created")


cursor.execute("SELECT * FROM users")

users = cursor.fetchall()

# print("\nUsers:")

# for user in users:
#      print(user)

def register():
    print("\n--- USER REGISTRATION ---")
    try:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        role = input("Enter role (admin/staff): ").strip().lower()

        if username == "" or password == "":
            print("Username and password cannot be empty")
            return

        if role != "admin" and role != "staff":
            print("Invalid role")
            return

        cursor.execute("""
        INSERT INTO users (username, password, role)
        VALUES (?, ?, ?)
        """, (username, password, role))

        con.commit()

        print("Registration successful")

    except sqlite3.IntegrityError:
        print("Username already exists")

    except sqlite3.Error:
        print("Database error")

def add_product():
    print("\n--- ADD PRODUCT ---")

    try:
        product_name = input("Enter product name: ").strip()
        category = input("Enter category: ").strip()

        if product_name == "" or category == "":
            print("Product name and category cannot be empty")
            return

        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        if price < 0:
            print("Price cannot be negative")
            return

        if quantity < 0:
            print("Quantity cannot be negative")
            return

        cursor.execute("""
        INSERT INTO products
        (product_name, category, price, quantity)
        VALUES (?, ?, ?, ?)
        """, (product_name, category, price, quantity))

        con.commit()

        print("Product added successfully")

    except ValueError:
         print("Please enter valid numbers for price and quantity")

    except sqlite3.Error:
        print("Database error")

def view_products():
    print("\n--- PRODUCT LIST ---")

    try:
        cursor.execute("""
        SELECT product_id, product_name, category, price, quantity
        FROM products
        ORDER BY product_id
        """)

        products = cursor.fetchall()

        if not products:
            print("No products found")
            return

        print("-" * 65)
        print("ID   Product Name       Category       Price       Quantity")
        print("-" * 65)

        for product in products:
            print(
                product[0],
                product[1],
                product[2],
                product[3],
                product[4]
            )

        print("-" * 65)

    except sqlite3.Error:
        print("Database error")

def update_product():
    print("\n--- UPDATE PRODUCT ---")

    try:
        product_id = int(input("Enter product ID: "))

        cursor.execute("""
        SELECT * FROM products
        WHERE product_id = ?
        """, (product_id,))

        product = cursor.fetchone()

        if product is None:
            print("Product not found")
            return

        print("Current product:", product)

        product_name = input("Enter new product name: ").strip()
        category = input("Enter new category: ").strip()
        price = float(input("Enter new price: "))
        quantity = int(input("Enter new quantity: "))

        if product_name == "" or category == "":
            print("Product name and category cannot be empty")
            return

        if price < 0 or quantity < 0:
            print("Price and quantity cannot be negative")
            return
        cursor.execute("""
        UPDATE products
        SET product_name = ?,
            category     = ?,
            price        = ?,
            quantity     = ?
        WHERE product_id = ?
        """, (product_name, category, price, quantity, product_id))

        con.commit()

        print("Product updated successfully")

    except ValueError:
        print("Please enter valid values")

    except sqlite3.Error:
        print("Database error")

def delete_product():
    print("\n--- DELETE PRODUCT ---")

    try:
        product_id = int(input("Enter product ID: "))

        cursor.execute("""
        SELECT * FROM products
        WHERE product_id = ?
        """, (product_id,))

        product = cursor.fetchone()

        if product is None:
            print("Product not found")
            return

        print("Product:", product)

        confirm = input("Are you sure you want to delete? (yes/no): ").lower()

        if confirm != "yes":
            print("Delete cancelled")
            return
        cursor.execute("""
        SELECT transaction_id
        FROM transactions
        WHERE product_id = ?
        """, (product_id,))

        transaction = cursor.fetchone()

        if transaction:
            print("Cannot delete this product because transactions exist")
            return

        cursor.execute("""
        DELETE FROM products
        WHERE product_id = ?
        """, (product_id,))

        con.commit()

        print("Product deleted successfully")

    except ValueError:
        print("Please enter a valid product ID")

    except sqlite3.Error:
         print("Database error")


# ==========================================
# ADD STOCK
# ==========================================

def add_stock(user_id):
    print("\n--- ADD STOCK ---")

    try:
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity to add: "))

        if quantity <= 0:
            print("Quantity must be greater than zero")
            return

        cursor.execute("""
        SELECT product_id
        FROM products
        WHERE product_id = ?
        """, (product_id,))

        product = cursor.fetchone()

        if product is None:
            print("Product not found")
            return

        cursor.execute("""
        UPDATE products
        SET quantity = quantity + ?
        WHERE product_id = ?
        """, (quantity, product_id))

        transaction_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("""
        INSERT INTO transactions
        (product_id, user_id, transaction_type, quantity, transaction_date)
        VALUES (?, ?, ?, ?, ?)
        """, (
            product_id,
            user_id,
            "Add Stock",
            quantity,
            transaction_date
        ))

        con.commit()

        print("Stock added successfully")

    except ValueError:
        print("Please enter  numbers")

    except sqlite3.Error as e:
        print("Database error:",e)


# ==========================================
# REMOVE STOCK
# ==========================================

def remove_stock(user_id):
    print("\n--- REMOVE STOCK ---")

    try:
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity to remove: "))

        if quantity <= 0:
            print("Quantity must be greater than zero")
            return

        cursor.execute("""
        SELECT quantity
        FROM products
        WHERE product_id = ?
        """, (product_id,))

        product = cursor.fetchone()

        if product is None:
            print("Product not found")
            return

        current_quantity = product[0]

        if quantity > current_quantity:
            print("Not enough stock available")
            return

        cursor.execute("""
        UPDATE products
        SET quantity = quantity - ?
        WHERE product_id = ?
        """, (quantity, product_id))

        transaction_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("""
        INSERT INTO transactions
        (product_id, user_id, transaction_type, quantity, transaction_date)
        VALUES (?, ?, ?, ?, ?)
        """, (
            product_id,
            user_id,
            "REMOVE STOCK",
            quantity,
            transaction_date
         ))

        con.commit()

        print("Stock removed successfully")

    except ValueError:
        print("Please enter valid numbers")

    except sqlite3.Error as e:
        print("Database error:",e)


# ==========================================
# VIEW TRANSACTIONS
# ==========================================

def view_transactions():
    print("\n--- TRANSACTIONS ---")

    try:
        cursor.execute("""
        SELECT 
            transactions.transaction_id,
            products.product_name,
            users.username,
            transactions.transaction_type,
            transactions.quantity,
            transactions.transaction_date
        FROM transactions
        JOIN products
        ON transactions.product_id = products.product_id
        JOIN users
        ON transactions.user_id = users.user_id
        ORDER BY transactions.transaction_id
        """)

        transactions = cursor.fetchall()

        if not transactions:
            print("No transactions found")
            return

        print("-" * 90)

        for transaction in transactions:
            print(
                "ID:", transaction[0],
                "| Product:", transaction[1],
                "| User:", transaction[2],
                "| Type:", transaction[3],
                "| Quantity:", transaction[4],
                "| Date:", transaction[5]
            )

        print("-" * 90)

    except sqlite3.Error:
        print("Database error")


# ==========================================
# ADMIN MENU
# ==========================================

def admin_menu():
    while True:

        print("\n--- ADMIN MENU ---")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. View Transactions")
        print("6. Add Supplier")
        print("7. View Suppliers")
        print("8. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            update_product()

        elif choice == "4":
            delete_product()

        elif choice == "5":
            view_transactions()

        elif choice == "6":
            add_supplier()

        elif choice == "7":
            view_suppliers()

        elif choice == "8":
            print("Logged out successfully")
            break
        else:
            print("Invalid choice. Please enter 1 to 6.")


# ==========================================
# STAFF MENU
# ==========================================

def staff_menu(user_id):
    while True:

        print("\n--- STAFF MENU ---")
        print("1. View Products")
        print("2. Add Stock")
        print("3. Remove Stock")
        print("4. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_products()

        elif choice == "2":
            add_stock(user_id)

        elif choice == "3":
            remove_stock(user_id)

        elif choice == "4":
            print("Logged out successfully")
            break

        else:
            print("Invalid choice. Please enter 1 to 4.")


# ==========================================
# LOGIN
# ==========================================

def login():
    print("\n--- LOGIN ---")

    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    try:
        cursor.execute("""
        SELECT user_id, username, role
        FROM users
        WHERE username = ?AND password = ?
        """, (username, password))

        user = cursor.fetchone()

        if user:

            print("\nLogin successful")
            print("Welcome", user[1])
            print("Role:", user[2])

            if user[2] == "admin":
                admin_menu()

            elif user[2] == "staff":
                staff_menu(user[0])

        else:
            print("Invalid username or password")

    except sqlite3.Error:
        print("Database error")


# ==========================================
# MAIN MENU
# ==========================================

def main_menu():
    while True:

        print("\n================================")
        print("   INVENTORY MANAGEMENT SYSTEM")
        print("================================")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register()

        elif choice == "2":
            login()

        elif choice == "3":
            print("Thank you for using Inventory Management System")
            break

        else:
            print("Invalid choice. Please enter 1, 2 or 3.")
main_menu()

con.close()

