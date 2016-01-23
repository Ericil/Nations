import sqlite3
""" TABLES:


accounts (account_id INTEGER PRIMARY KEY, uname TEXT, pword TEXT, email TEXT)

cities (city_id INTEGER PRIMARY KEY, account_id INTEGER, city_name TEXT, cx INTEGER, cy INTEGER)

buildings (building_id INTEGER PRIMARY KEY, city_id INTEGER, bx INTEGER, by INTEGER, type INTEGER, level INTEGER)

messages (from_id INTEGER, to_id INTEGER, message INTEGER, time INTEGER, seen INTEGER)

"""
import init

#+========================+#
#+===++ Static Vars ++====+#
#+========================+#

timeInterval = 10## In milliseconds

startPop = 100; # a constant that represents how much population the city starts with
startSol = 50; # a constant that represents how many soldiers the city starts with
startHappiness = 100;# a constant that is how happy a city starts out as

allBuildings = [
{"name":"house", "type":1, "peopleHoused":1000},# houses people, increase gold?
{"name":"barracks", "type":2, "soldiers":.5},# makes soldiers
{"name":"city hall", "type":3},# dictates highest level
{"name":"hospital", "type":4, "food":.5},# lowers disease, restores wounded soldiers, increase food?
{"name":"mine", "type":5, "iron":.5},
{"name":"woodmill", "type":6, "wood":.5},
{"name":"farm", "type":7, "food":.5},
{"name":"shop", "type":8, "gold":.5},# increases gold
{"name":"rec building", "type":9, "happiness":.25}# increase happiness
]
# happiness increase is (max(0, peopleHoused total - population)) + (max(0, food - population)) + buildingHappiness

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
    p = c.execute("SELECT pword FROM accounts WHERE uname = '%s';" %(uname))
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

    c.execute("INSERT INTO accounts(uname, pword, email) VALUES (?, ?, ?);", (uname, pword, email))
    conn.commit()

#===============TEST===============
addAccount("milo", "123", "")
addAccount("other", "321", "")
print"Correct login: "+ str(pwordAuth("milo", "123"))
print"Incorrect login: "+str(pwordAuth("bla bla", "321"))
print "\n"
#==================================

def changePword(uname, oldP, newP, cNewP):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT pword FROM accounts WHERE uname = '%s';" %(uname))
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
    p = c.execute("SELECT account_id FROM accounts WHERE uname = '%s';" %(uname))
    for r in p:
        return r[0]
    return -1

## finds the uname for account with ID
def findUname(ID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT uname FROM accounts WHERE account_id = '%s';" %(ID))
    for r in p:
        return r[0]

#===============TEST===============
print "FindID('milo'): "+str(findID("milo"))
#==================================

#+========================+#
#+==========Cities========+#
#+========================+#


## adds a city owned by no one in place cx, cy named city_name
def addCity(cityName, cx, cy, wood, iron, gold, food):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    c.execute("INSERT INTO cities(account_id, city_name, cx, cy, wood, iron, gold, food, population, soldiers, happiness) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (0, cityName, cx, cy, wood, iron, gold, food, startPop, startSol, startHappiness))
    p = c.execute("SELECT city_id FROM cities;")
    for r in p:
        cityID = r[0]
    c.execute("INSERT INTO buildings(city_id, bx, by, type, level) VALUES (?, ?, ?, ?, ?);", (cityID, 0, 0, 3, 1))
    conn.commit()

#===============TEST===============
addCity("Milopolis", 3, 4, 100, 50, 50, 50)
#==================================

def setCityOwner(accountID, cityID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    c.execute("UPDATE cities SET account_id = ? WHERE city_id = ?;", (accountID, cityID))
    conn.commit()

#===============TEST===============
setCityOwner(1, 1)
#==================================

## Returns a list of city_ids of that accountID
def getCitiesID(accountID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT city_id FROM cities WHERE account_id = %s;" %(accountID))
    cities = []
    for r in p:
        cities.append(r[0])
    return cities

#===============TEST===============
print "getCitiesID(1): "+str(getCitiesID(1))
#==================================

## returns the cityID based on x and y
def getCity(cx, cy):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT city_id FROM cities WHERE cx = ? AND cy = ?;", (cx, cy))
    for r in p:
        return r[0]

## gets the id of the owner of city with cityID
def getCityOwner(cityID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT account_id FROM cities WHERE city_id = %s;" %(cityID))
    for r in p:
        return r[0]

# gets the city id from the name
def getCityID(cityName):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT city_id FROM cities WHERE city_name = %s;" %(cityName))
    for r in p:
        return r[0]

# gets the city id from the coordinates
def getCityXY(cx, cy):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT city_id FROM cities WHERE cx = ? AND cy = ?;", (cx, cy))
    for r in p:
        return r[0]
    return 0

# gets the name from the city id
def getCityName(cityID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT city_name FROM cities WHERE city_id = %s;", (cityID))
    for r in p:
        return r[0]

#===============TEST===============
print "getCity(2, 1): "+str(getCity(2, 1))
print "getCity(3, 4): "+str(getCity(3, 4))
#==================================

## Returns dictionary with all resources in the city
def getResources(cityID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT wood, iron, gold, food, population, soldiers, happiness FROM cities WHERE city_id = %s;" %(cityID))
    for r in p:
        return {"wood":r[0], "iron":r[1], "gold":r[2],"food":r[3], "population":r[4], "soldiers":r[5], "happiness":r[6]}

## Updates all resources with the cityID
def updateResources(cityID, wood, iron, gold, food, population, soldiers, happiness):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("UPDATE cities SET wood = ?, iron = ?, gold = ?, food = ?, population = ?, soldiers = ?, happiness = ? WHERE city_id = ?;",
    (wood, iron, gold, food, population, soldiers, happiness, cityID))
    conn.commit()

## get the increases in all resources
def getResourceIncreases(cityID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    buildings = getBuildingsIn(cityID)
    peopleHoused = 0
    soldiers = 0
    food = 0
    iron = 0
    wood = 0
    gold = 0
    happiness = 0
    for b in buildings:
        if b["type"] == 1:# house
            peopleHoused += allBuildings[0]["peopleHoused"]*b["level"]
        if b["type"] == 2:# barracks
            soldiers += allBuildings[1]["soldiers"]*b["level"]
        if b["type"] == 3:# city hall
            # city hall stuff
            break
        if b["type"] == 4:# hospital
            # do the hospital stuff
            break
        if b["type"] == 5:# mine
            iron += allBuildings[4]["iron"]*b["level"]
        if b["type"] == 6:# woodmill
            wood += allBuildings[5]["wood"]*b["level"]
        if b["type"] == 7:# farm
            food += allBuildings[6]["food"]*b["level"]
        if b["type"] == 8:# shop
            gold += allBuildings[7]["shop"]*b["level"]
        if b["type"] == 9:# rec building
            happiness += allBuildings[8]["happiness"]*b["level"]
    r = getResources(cityID)
    # happiness calculation:
    happiness += (max(0, peopleHoused - r["population"])) + (r["food"] - r["population"])
    # population growth calculation:
    population = (food - r["population"]) + (r["happiness"] - r["population"])
    return {"wood":wood, "iron":iron, "gold":gold, "food":food, "population":population, "soldiers":soldiers, "happiness":happiness}


## automatically update all values
def updateAll(cityID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    r = getResourceIncreases(cityID)
    updateResources(cityID,
    r["wood"]+r["wood"],
    r["iron"]+r["iron"],
    r["gold"]+r["gold"],
    r["food"]+r["food"],
    r["population"]+r["population"],
    r["soldiers"]+r["soldiers"],
    r["happiness"]+r["happiness"])

#+========================+#
#+========Buildings=======+#
#+========================+#

## add a building in cityID at bx, by, with type
def addBuilding(cityID, bx, by, type):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("INSERT INTO buildings(city_id, bx, by, type, level) VALUES (?, ?, ?, ?, ?);", (cityID, bx, by, type, 1))
    conn.commit()

#===============TEST===============
addBuilding(1, 5, 5, 0)
#==================================

## gets a list of dictionaries, gathering all info about all buildings in city with cityID
def getBuildingsIn(cityID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT city_id, bx, by, type, level FROM buildings WHERE city_id = %s;" %(cityID))
    buildings = []
    for r in p:
        buildings.append({"city_id":r[0], "bx":r[1], "by":r[2],"type":r[3], "level":r[4]})
    return buildings

#===============TEST===============
print "getBuildingsIn(1): "+str(getBuildingsIn(1))
#==================================

## returns the BuildingID based on city_id, bx and by
def getBuildingXY(cityID, bx, by):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT building_id FROM buildings WHERE city_id = ? AND bx = ? AND by = ?;", (cityID, bx, by))
    for r in p:
        return r[0]
    return 0

#===============TEST===============
print "getBuildingXY(1, 5, 5): "+str(getBuildingXY(1, 5, 5))
print "getBuildingXY(1, 3, 5): "+str(getBuildingXY(1, 3, 5))


## returns a dictionary with the stats of building with buildingID
def getBuilding(buildingID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT city_id, bx, by, type, level FROM buildings WHERE building_id = %s;" %(buildingID))
    for r in p:
        return {"city_id":r[0], "bx":r[1], "by":r[2],"type":r[3], "level":r[4]}
    return {}

## increases level of a building if its level is less than cityhall level
def levelUpBuilding(buildingID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT city_id, level, type FROM buildings WHERE building_id = %s;" %(buildingID))
    for r in p:
        cityID = r[0]
        level = r[1]
        type = r[2]
    p = c.execute("SELECT level FROM buildings WHERE city_id = %s AND type = 3;", (cityID))
    for r in p:
        cityLevel = r[0]
    if cityLevel > level:# it can be the same after it is set
        # Check for price
        c.execute("UPDATE buildings SET level = ? WHERE building_id = ?;", (level+1, buildingID))
    conn.commit()

## gets the building type name
def getBuildingName(buildingID):
    b = getBuilding(buildingID)
    type = b["type"]
    return allBuildings[type]["name"]

## remove the building with that ID
def deleteBuilding(buildingID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("DELETE FROM buildings WHERE building_id = %s;" %(buildingID))
    conn.commit()

#===============TEST===============
print "getBuilding(getBuildingXY(1, 5, 5)): "+str(getBuilding(getBuildingXY(1, 5, 5)))
#==================================

#+========================+#
#+========Buildings=======+#
#+========================+#

## returns the current date and time
def getTime():
    import datetime
    d = str(datetime.datetime.now())
    d = d.split(" ")
    date = ""

    time = d[1].split(":")
    day = d[0].split("-")

    date += day[1]+"/"+day[2]+"/"+day[0]+" at "
    date += time[0]+":"+time[1]
    return date

## add message between fromUser and toUser
def addmsg(fromID, toID, message):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    time = getTime()
    c.execute("INSERT INTO messages VALUES (?, ?, ?, ?, ?)", (fromID, toID, message, time, 0))
    conn.commit()

#===============TEST===============
addmsg(1, 2, "Hey, just wondering how it's going")
addmsg(2, 1, "It's going well! Can I attack you?")
addmsg(1, 2, "No.")


## returns a list of dictionaries of messages between fromUser and toUser (fromUser is logged in)
def getmsgs(fromUser, toUser):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    list = []
    p = c.execute("SELECT from_id, message, time, seen FROM messages WHERE from_id = ? AND to_id = ?;", (fromUser, toUser))
    for r in p:
        list.append({"from_id":r[0], "message":r[1], "timestamp":r[2], "seen":r[3]})
    p = c.execute("SELECT from_id, message, time, seen FROM messages WHERE from_id = ? AND to_id = ?;", (toUser, fromUser))
    for r in p:
        list.append({"from_id":r[0], "message":r[1], "timestamp":r[2], "seen":r[3]})
    return list

## returns all friends who have unseen messages
def getUnseenFriends(userID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    msgs = c.execute("SELECT from_id, seen FROM messages WHERE to_id = %s;" %(userID))
    unseen = []
    for r in msgs:
        if r[1] == 0:
            if unseen.count(r[0]) == 0:
                unseen.append(r[0])
    return unseen

## set all of the messages from fromID to userID to seen
def setAllSeenFrom(userID, fromID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("UPDATE messages SET seen = 1 WHERE from_id = ? AND to_id = ?;", (fromID, userID))
    conn.commit()

#===============TEST===============
print "getmsgs(1, 2): "+str(getmsgs(1, 2))
print "getUnseenFriends(2)"+str(getUnseenFriends(2))
setAllSeenFrom(2, 1)
print "getUnseenFriends(2)"+str(getUnseenFriends(2))
#==================================

## adds the friendID to the userID friend list
def addFriend(userID, friendID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("INSERT INTO friends VALUES (?, ?);", (userID, friendID))
    conn.commit()

#===============TEST===============
addFriend(1, 2)
addFriend(1, 3)
#==================================

## gets all friends of account with uname = uname
def getFriends(userID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT them FROM friends WHERE you = %s;" %(userID))
    list = []
    for r in p:
        list.append(r[0])
    return list

#===============TEST===============
print "getFriends(1): "+str(getFriends(1))
#==================================


#+========================+#
#+=========Action=========+#
#+========================+#

# have one city attack another (takes cityIDs)
def attack(defendingCity, attackingCity):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()


#===============TEST===============
print "getResources: "+str(getResources(getCity(3, 4)))
updateAll(getCity(3, 4))
print "getResources: "+str(getResources(getCity(3, 4)))
updateAll(getCity(3, 4))
print "getResources: "+str(getResources(getCity(3, 4)))
updateAll(getCity(3, 4))
print "getResources: "+str(getResources(getCity(3, 4)))
#==================================
