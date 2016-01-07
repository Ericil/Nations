import sqlite3
""" TABLES:


accounts (account_id INTEGER PRIMARY KEY, uname TEXT, pword TEXT, email TEXT)

cities (city_id INTEGER PRIMARY KEY, account_id INTEGER, city_name TEXT, cx INTEGER, cy INTEGER)

buildings (city_id INTEGER, bx INTEGER, by INTEGER, type INTEGER, level INTEGER)

messages (fromID INTEGER, toID INTEGER, message INTEGER, time INTEGER, seen INTEGER)

"""

#+========================+#
#+=====++ Accounts ++=====+#
#+========================+#

def unameAuth(uname):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    accounts = c.execute("SELECT uname FROM accounts")
    for r in accounts:
        if r[0] == uname:
            return True
    return False

def pwordAuth(uname, pword):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT pword FROM accounts WHERE uname = '%s';", %(uname))
    for r in p:
        return r[0] == pword
    return False


def addAccount(uname, pword, email):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    if uname.find(",") != -1: # it can't have a comma in it
        return "This account name has a character that is not allowed (',')"
    if uname.find("'") != -1: # it can't have an apostrophe in it
        return "This account name has a character that is not allowed (''')"

    accounts = c.execute("SELECT uname FROM accounts")
    for r in accounts:
        if r[0] == uname:
            return "This account name already exists"
    accounts = c.execute("SELECT email FROM accounts")
    for r in accounts:
        if r[0] == email:
            return "There is already an account associated with this email"

    c.execute("INSERT INTO accounts VALUES (?, ?, ?);", (uname, pword, email))
    conn.commit()


def changePword(uname, oldP, newP, cNewP):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT pword FROM accounts WHERE uname = '%s';", %(uname))
    for r in p:
        result = r[0]
    if result != oldP:
        return "The password you input was incorrect."
    if newP != cNewP:
        return "The confirmed new password did not match."
    else:
        c.execute("UPDATE accounts SET pword = '?' WHERE uname = '?';", (newP, uname))
        conn.commit()        
        return "Password successfully updated"

#+========================+#
#+==========Cities========+#
#+========================+#

def getCitiesID(uname):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT account_id FROM accounts WHERE uname = '%s';", %(uname))
    for r in p:
        id = r[0]
    p = c.execute("SELECT city_id FROM cities WHERE account_id = %s;", %(id))
    return p

#+========================+#
#+========Buildings=======+#
#+========================+#

def getBuildingsIn(cityName):
    conn = sqlite3.connect("data.db")
    
