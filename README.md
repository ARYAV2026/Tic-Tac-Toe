Inventory Management System
1. Project Title

Inventory Management System

2. Project Description

The Inventory Management System is a database-driven command-line application developed using Python and SQLite.

The system is designed to manage products, inventory stock, suppliers, and stock transactions. It provides user authentication and role-based authorization so that administrators and staff members can perform different operations according to their roles.

3. Technologies Used
Python
SQLite
SQL
Command Line Interface (CLI)

4. Main Features
User Authentication
User registration
User login
Username and password verification
Role-based authorization
Admin Features
Add products
View products
Update products
Delete products
View transactions
Add suppliers
View suppliers
Logout
Staff Features
View products
Add stock
Remove stock
Logout
Inventory Management
Add new products
View available products
Update product information
Delete products
Add stock
Remove stock
Record stock transactions
Supplier Management
Add supplier details
View supplier details
5. Database Tables

The application uses four main tables.

Users Table

The Users table stores user login information and user roles.

Fields:

user_id
username
password
role
Products Table

The Products table stores product information and stock quantity.

Fields:

product_id
product_name
category
price
quantity
Suppliers Table

The Suppliers table stores supplier information.

Fields:

supplier_id
supplier_name
phone
email


The Transactions table stores information about inventory stock transactions.

Fields:

transaction_id
product_id
user_id
transaction_type
quantity
transaction_date
6. Database Relationships

The Transactions table is related to the Users and Products tables.

product_id in the Transactions table refers to product_id in the Products table.
user_id in the Transactions table refers to user_id in the Users table.

These foreign-key relationships allow the system to identify which product was involved in a transaction and which user performed the transaction.

The Suppliers table is used to store supplier information separately.

7. How to Set Up the Project
Step 1: Install Python

Install Python on the computer.

Step 2: Open the Project

Open the project folder in PyCharm.

Step 3: Open the Python File

Open:

Inventory Management.py

Step 4: Run the Program

Click the Run button in PyCharm.

The application connects to the SQLite database and creates the required tables if they do not already exist.

The database file is:

inventory.db

8. Login Details
Administrator

Username: admin

Password: admin123

Role: admin

Staff User 1

Username: staff1

Password: staff123

Role: staff

Staff User 2

Username: staff2

Password: staff2123

Role: staff

9. Sample User Records
User ID	Username	Password	Role
1	admin	admin123	admin
2	staff1	staff123	staff
3	staff2	staff2123	staff
10. Sample Product Records

The following product records are currently present in the database:

Product ID	Product Name	Category	Price	Quantity
1	Pen	Stationery	10.00	52
3	Water Bottle	Accessories	250.00	100
4	Bags	Bags	1100.00	17
5	Digital Calculator	Electronics	1000.00	12
6	FileFolder	Stationery	30.00	45
7	USB Cable	Electronics	150.00	27
8	Pencil boxes	Stationery	150.00	8

Note: Product ID 2 is not currently present because that product was deleted. SQLite does not automatically reuse deleted IDs.

11. Sample Supplier Records

Supplier records can be viewed using the View Suppliers option in the Admin Menu.

Enter the supplier details that are currently present in your database in the table below.

Supplier ID	Supplier Name	Phone	Email
1	ABC Stationery	9800000012	abcstationery@gmail.com
2	KERALA Electronics 980000000089 keralaelectronics@gmail.com

12. Admin Menu

The administrator can access the following options:

--- ADMIN MENU ---

1. Add Product
2. View Products
3. Update Product
4. Delete Product
5. View Transactions
6. Add Supplier
7. View Suppliers
8. Logout
13. Staff Menu

Staff members can access the following options:

--- STAFF MENU ---

1. View Products
2. Add Stock
3. Remove Stock
4. Logout
14. CRUD Operations

The project demonstrates CRUD operations.

Create

New users, products, and suppliers can be added to the database.

Read

Users, products, suppliers, and transactions can be viewed.

Update

Existing product information can be updated.

Delete

Products can be deleted from the database.

15. Role-Based Authorization

The system provides different permissions based on the user's role.

Admin

The administrator can:

Add products
View products
Update products
Delete products
View transactions
Add suppliers
View suppliers
Staff

Staff members can:

View products
Add stock
Remove stock

This prevents users from accessing functions that are not available for their role.

16. Exception Handling

The application uses exception handling to manage common errors such as:

Empty username or password
Duplicate username
Invalid product ID
Invalid quantity
Invalid price
Invalid user input
Database errors

This helps prevent the program from terminating unexpectedly.

17. Inventory Transactions

The Transactions table records stock operations performed by users.

Examples of transaction types include:

Add Stock
Remove Stock

Each transaction stores:

Product ID
User ID
Transaction type
Quantity
Transaction date

This helps maintain a record of inventory activities.

18. Example Product List

The application displays product information in a format similar to:

--- PRODUCT LIST ---
-----------------------------------------------------------------
ID   Product Name       Category       Price       Quantity
-----------------------------------------------------------------
1    Pen                Stationery     10.0        52
3    Water Bottle       Accessories    250.0       100
4    Bags               Bags           1100.0      17
5    Digital Calculator Electronics     1000.0      12
6    FileFolder         Stationery     30.0        45
7    USB Cable          Electronics    150.0       27
8    Pencil boxes       Stationery     150.0        8
-----------------------------------------------------------------
19. Project Files

The main project files are:

Inventory Management.py
inventory.db
README.md
Inventory Management.py

Contains the Python source code for the Inventory Management System.

inventory.db

SQLite database file that stores the application data.

README.md

Contains the project description, setup instructions, database information, login details, features, and sample records.

20. Running the Application

After starting the program, the user can:

Register a new user.
Login using an existing account.
Access the appropriate menu according to the user's role.
Manage products and inventory.
Manage suppliers as an administrator.
View inventory transactions.
Logout.
21. Conclusion

The Inventory Management System demonstrates how Python and SQLite can be used to develop a database-driven
command-line application.

The project demonstrates:

Database design
SQLite database connectivity
SQL queries
CRUD operations
User authentication
Role-based authorization
Relationships between tables
Product management
Inventory management
Supplier management
Transaction management
Exception handling
Command-line programming

The system provides a simple and practical way to manage products, stock, suppliers, and inventory transactions 
using Python and SQLite.