import sqlite3

connection = sqlite3.connect("database.db")

cursor = connection.cursor()

cursor.execute("""
     CREATE TABLE IF NOT EXISTS products(prodid INT PRIMARY KEY , prodlabel TEXT , prodprice FLOT, proddiscount INT)
""")

connection.commit()

#cursor.execute("""
#     INSERT INTO products (prodid, prodlabel, prodprice, proddiscount)
#     VALUES (1, "bread", 29.5, 30), 
#          (2, "cheese", 250, 5), 
#          (3, "milk", 42, 30),
#          (4, "meat", 265, 15),
#          (5, "patato", 42, 1)
#     """)

#connection.commit()




#products = [
#    (6, "tomato", 45, 3),
#    (7, "chicken", 170, 10)
#]

#cursor.executemany("""
#     INSERT INTO droducts(prodid, prodlabel, prodprice, proddiscount) 
#     VALUES (?, ?, ?, ?)""", products)

#connection.commit()

def get_products():
     cursor.execute("SELECT * FROM products;")
     result = cursor.fetchall()
     print(result)

get_products()



