import sqlite3

"""THIS FILE IS USED TO CREATE THE BACKEND OF THE PROJECT, IT CREATES THE
DATABASE FILE AND CREATES ITS TABLES. ALL FUNCTIONS REGARDING CHANGING THE
DATABASE IS LOCATED AT database.py"""



conn = sqlite3.connect("data.db")
c = conn.cursor()

q = "DROP TABLE IS EXISTS %s"

c.execute(q, %("accounts"))
c.execute(q, %("cities"))
c.execute(q, %("buildings"))


q = "CREATE TABLE %s (%S)"

# Create all tables

c.execute(q, %("accounts" , 'account_id INTEGER, uname TEXT, pword TEXT, email TEXT'))

c.execute(q, %("cities", 'city_id INTEGER, account_id INTEGER, city_name TEXT, cx INTEGER, cy INTEGER'))

c.execute(q, %("buildings", 'city_id INTEGER, bx INTEGER, by INTEGER, type INTEGER, level INTEGER'))

conn.commit()
conn.close()
