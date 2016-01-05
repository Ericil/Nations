import sqlite3

"""THIS FILE IS USED TO CREATE THE BACKEND OF THE PROJECT, IT CREATES THE
DATABASE FILE AND CREATES ITS TABLES. ALL FUNCTIONS REGARDING CHANGING THE
DATABASE IS LOCATED AT database.py"""

conn = sqlite3.connect("data.db")

c = conn.cursor()

q = "CREATE TABLE %s (%S)" #1st string - table name
                           #2nd string - arguments

#And then we make some tables here

#Or was it email? 
c.execute(q %("players", "username TEXT", "password TEXT"))


conn.commit()
conn.close()
