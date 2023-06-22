import sqlite3

connection = sqlite3.connect("database.db")

cursor = connection.cursor()

cursor.execute("""
     CREATE TABLE IF NOT EXISTS customers(custid INT PRIMARY KEY , custname TEXT , custmoney INT, customer_code INT)
""")

connection.commit()

#cursor.execute("""
#     INSERT INTO customers (custid, custname, custmoney, customer_code)
#     VALUES (1, "Bob", 1000, 1234), 
#          (2, "Marc", 1500, 2345), 
#          (3, "Dora", 2000, 3456),
#          (4, "John", 250, 4567),
#          (5, "Vika", 800, 5678)
#     """)

#connection.commit()

def get_customers():
     cursor.execute("SELECT custname FROM customers ;")
     result = cursor.fetchall()
     print(result)

get_customers()