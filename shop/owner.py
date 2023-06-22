import sqlite3

connection = sqlite3.connect("database.db")

cursor = connection.cursor()

cursor.execute("""
     CREATE TABLE IF NOT EXISTS owner(ownid INT PRIMARY KEY , ownname TEXT , ownposition TEXT)
""")

connection.commit()

#cursor.execute("""
#     INSERT INTO owner (ownid, ownname, ownposition)
#     VALUES (1, "Oleksandr", "owner" ), 
#          (2, "Mike", "manager")
#     """)

#connection.commit()

def get_owner():
     cursor.execute("SELECT ownname FROM owner WHERE ownposition = 'owner' ;")
     result = cursor.fetchall()
     print("The shop owner's name is", result)

def get_manager():
     cursor.execute("SELECT ownname FROM owner WHERE ownposition = 'manager' ;")
     result = cursor.fetchall()
     print("Hello, my name is", result, "How can i help you?")

get_owner()

get_manager()
