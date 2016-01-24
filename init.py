import sqlite3

"""THIS FILE IS USED TO CREATE THE BACKEND OF THE PROJECT, IT CREATES THE
DATABASE FILE AND CREATES ITS TABLES. ALL FUNCTIONS REGARDING CHANGING THE
DATABASE IS LOCATED AT database.py"""



conn = sqlite3.connect("data.db")
c = conn.cursor()

q = "DROP TABLE IF EXISTS %s;"

c.execute(q %("accounts"))
c.execute(q %("cities"))
c.execute(q %("buildings"))
c.execute(q %("messages"))
c.execute(q %("friends"))
c.execute(q %("citylinks"))


q = "CREATE TABLE %s (%s);"

# Create all tables

# Resources: food, wood, iron, population, gold

c.execute(q %("accounts" , 'account_id INTEGER PRIMARY KEY AUTOINCREMENT, uname TEXT, pword TEXT, email TEXT'))

c.execute(q %("cities",
'city_id INTEGER PRIMARY KEY AUTOINCREMENT, account_id INTEGER, city_name TEXT, cx INTEGER, cy INTEGER, wood INTEGER, iron INTEGER, gold INTEGER, food INTEGER, population INTEGER, soldiers INTEGER, happiness INTEGER'))

c.execute(q %("buildings", 'building_id INTEGER PRIMARY KEY AUTOINCREMENT, city_id INTEGER, bx INTEGER, by INTEGER, type INTEGER, level INTEGER'))

c.execute(q %("messages", 'from_id INTEGER, to_id INTEGER, message TEXT, time INTEGER, seen INTEGER'))

c.execute(q %("friends", 'you INTEGER, them INTEGER'))

c.execute(q %("citylinks", 'city_id INTEGER, place TEXT'))

conn.commit()
conn.close()
