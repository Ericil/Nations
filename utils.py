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

## finds the account_id with uname uname
def findID(uname):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()


#+========================+#
#+==========Cities========+#
#+========================+#

## Returns a list of city_ids of that uname
def getCitiesID(uname):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT account_id FROM accounts WHERE uname = '%s';", %(uname))
    for r in p:
        id = r[0]
    p = c.execute("SELECT city_id FROM cities WHERE account_id = %s;", %(id))
    return p

## returns the cityID based on x and y
def getCity(cx, cy):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT city_id FROM cities WHERE cx = ? AND cy = ?;", (cx, cy))
    for r in p:
        return r[0]

## adds a city owned by no one in place cx, cy named city_name
def addCity(cityName, cx, cy, wood, iron, gold, food):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    startPop = 100; # a constant that represents how much population the city starts with
    startSol = 50; # a constant that represents how many soldiers the city starts with

    c.execute("INSERT INTO cities (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (0, cityName, cx, cy, wood, iron, gold, food, startPop, startSol))
    conn.commit()

def getResources(cityID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT wood, iron, gold, food, population, soldiers FROM cities WHERE city_id = %s;", %(cityID))
    for r in p:
        return r[0]

#+========================+#
#+========Buildings=======+#
#+========================+#

# gets a list of dictionaries, gathering all info about all buildings in city with cityID
def getBuildingsIn(cityID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT FROM buildings WHERE city_id = %s;", %(cityID))
    return p

## returns the BuildingID based on city_id, bx and by
def getBuilding(cityID, bx, by):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT building_id FROM buildings WHERE city_id = ? AND cx = ? AND cy = ?;", (cityID, bx, by))
    for r in p:
        return r[0]

## add a building in cityID at bx, by, with type
def addBuilding(cityID, bx, by, type):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("INSERT INTO buildings (?, ?, ?, ?, ?)", (cityID, bx, by, 1))
    conn.commit()

## ?
def getBuilding(buildingID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT city_id, bx, by, type, level FROM buildings WHERE building_id = %s;", %(buildingID))
    for r in p:
        return r[0]

## returns a list of dictionaries of messages between fromUser and toUser (fromUser is logged in)
def getmsgs(fromUser, toUser):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    list = []
    p = c.execute("SELECT from_id, message, time FROM messages WHERE from_user = ? AND to_user = ?;", (fromUser, toUser))
    for r in p:
        list.add(r)
    p = c.execute("SELECT from_id, message, time FROM messages WHERE from_user = ? AND to_user = ?;", (toUser, fromUser))
    for r in p:
        list.add(r)
    return list

## gets all friends of account with uname = uname
def getFriends(uname):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT them FROM friends WHERE you = %s;", %(uname))
    for r in p:
        return r[0]

# getMultipliers(city_id)
# updateResources(city_id)
