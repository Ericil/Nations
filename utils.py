import sqlite3
import random
import time
import init

## return a dictionary with weather
def getCitiesWeather():
    import urllib2
    import json
    url = 'http://api.openweathermap.org/data/2.5/box/city?bbox=50,-125,25,80,30&cluster=no&APPID=44db6a862fba0b067b1930da0d769e98'

    response = urllib2.urlopen(url)
    html = response.read()
    data = json.loads(html)
    data2 = data["list"]
    hold = {}
    for meh in data2:
        name = meh.get("name")
        themain = meh.get("main")
        temp = abs(round(themain.get("temp")))
        if name != "":
            hold[name] = temp
    return hold

#+========================+#
#+===++ Static Vars ++====+#
#+========================+#

allCities = getCitiesWeather().keys()

timeInterval = 5## in seconds

xMax = 8
yMax = 16
aiCount = 10

# == starting values ==
startPop = 100; # a constant that represents how much population the city starts with
startSol = 50; # a constant that represents how many soldiers the city starts with
startHappiness = 100;# a constant that is how happy a city starts out as
startwood = 2000
startiron = 2000
startgold = 2000
startfood = 2000
# =====================

allBuildings = [
{"name":"house", "type":1, "housed":1000},# houses people, increase gold?
{"name":"barracks", "type":2, "soldiers":2},# makes soldiers
{"name":"city hall", "type":3},# dictates highest level
{"name":"hospital", "type":4, "food":2},# lowers disease, restores wounded soldiers, increase food?
{"name":"mine", "type":5, "iron":2},
{"name":"woodmill", "type":6, "wood":2},
{"name":"farm", "type":7, "food":2},
{"name":"mall", "type":8, "gold":2},# increases gold
{"name":"park", "type":9, "happiness":.25}# increase happiness
]

prices = [
{"type":1, "wood":200, "gold":200},
{"type":2, "wood":200, "iron":200, "gold":200},
{"type":3, "wood":100, "iron":100, "food":100, "gold":100},
{"type":4, "wood":300, "iron":300, "food": 100},
{"type":5, "wood":200, "gold":200},
{"type":6, "iron":200, "gold":200},
{"type":7, "wood":100, "iron":100, "gold":100},
{"type":8, "wood":300, "iron":300},
{"type":9, "wood":400, "iron":400, "gold":400},
]

# Updated at times:

currWeather = getCitiesWeather()

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


    coords = findNewCoords()
    c.execute("INSERT INTO accounts(uname, pword, email) VALUES (?, ?, ?);", (uname, pword, email))
    conn.commit()
    conn.close()
    addCity(uname+"polis", findID(uname), coords[0], coords[1], startwood, startiron, startgold, startfood)
    #linkCity(getCityID(uname+"polis"), allCities[random.randrange(len(allCities))])
    saveStamp(findID(uname))



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
        conn.close()

        return "Password successfully updated"


## finds the account_id with uname uname
def findID(uname):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT account_id FROM accounts WHERE uname = '%s';" %(uname))
    for r in p:
        return r[0]
    return 0

## finds the uname for account with ID
def findUname(ID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT uname FROM accounts WHERE account_id = '%s';" %(ID))
    for r in p:
        return r[0]



#+========================+#
#+==========Cities========+#
#+========================+#

## adds all the computer cities
def createWorld():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    addAccount("AI", "", "AI@NOTAREAL.COM")
    count = 0
    while count < aiCount:
        coords = findNewCoords()
        city = allCities[random.randrange(len(allCities))]
        addCity(city, 1, coords[0], coords[1], 200, 200, 200, 200)
        linkCity(getCityID(city), city)
        count += 1

## finds a place on the map for a city
def findNewCoords():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    done = False
    while (not done):
        x = random.randrange(xMax)
        y = random.randrange(yMax)
        p = c.execute("SELECT cx, cy FROM cities;")
        done = True
        for r in p:
            cx = r[0]
            cy = r[1]
            if x >= cx-1 and x <= cx+1 and y >= cy-1 and y <= cy+1:
                done = False
    return [x, y]

def generateMap(x, y):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT city_name, cx, cy FROM cities")
    cities = []
    for r in p:
        cities.append({"name":r[0], "cx":r[1], "cy":r[2]})
    x -= 4# [["x,y", "x,y+1", "x,y+2", "x,y+3", "x,y+4", "x,y+5", "x,y+6"]]
    y -= 8
    map = []
    currX = 0
    while currX < 8:
        map.append([])
        currY = 0
        while currY < 16:
            map[currX].append("")
            for city in cities:
                if city["cx"] == x+currX and city["cy"] == y+currY:
                    map[currX][currY] = city["name"]
            currY += 1
        currX += 1
    return map


## adds a city owned by no one in place cx, cy named city_name
def addCity(cityName, accountID, cx, cy, wood, iron, gold, food):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    c.execute("INSERT INTO cities(account_id, city_name, cx, cy, wood, iron, gold, food, population, soldiers, happiness) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (accountID, cityName, cx, cy, wood, iron, gold, food, startPop, startSol, startHappiness))
    p = c.execute("SELECT city_id FROM cities;")
    for r in p:
        cityID = r[0]
    c.execute("INSERT INTO buildings(city_id, bx, by, type, level) VALUES (?, ?, ?, ?, ?);", (cityID, 0, 0, 3, 1))
    conn.commit()
    conn.close()



## links cityID to the city with the cityName
def linkCity(cityID, cityLinkName):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("INSERT INTO citylinks VALUES (?, ?)", (cityID, cityLinkName))
    conn.commit()
    conn.close()


## gets the linked city's weather
def getWeatherOf(cityID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT place FROM citylinks WHERE city_id = %s;" %(cityID))
    for r in p:
        return currWeather[r[0]]


## makes the owner of the cityID accountID
def setCityOwner(accountID, cityID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    c.execute("UPDATE cities SET account_id = ? WHERE city_id = ?;", (accountID, cityID))
    conn.commit()
    conn.close()

## get the x and y values of a city in a dictionary
def getCityCoords(cityID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT cx, cy FROM cities WHERE city_id = %s" %(cityID))
    for r in p:
        return {"cx": r[0], "cy": r[1]}

## Returns a list of city_ids of that accountID
def getCitiesID(accountID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT city_id FROM cities WHERE account_id = %s;" %(accountID))
    cities = []
    for r in p:
        cities.append(r[0])
    return cities



## gets the names of cities with accountID
def getCitiesName(accountID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = getCitiesID(accountID)
    cities = []
    for r in p:
        cities.append(getCityName(r))
    return cities

## gets the id of the owner of city with cityID
def getCityOwner(cityID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT account_id FROM cities WHERE city_id = %s;" %(cityID))
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
    p = c.execute("SELECT city_name FROM cities WHERE city_id = %s;" %(cityID))
    for r in p:
        return r[0]


# gets the city id from the name
def getCityID(cityName):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT city_id FROM cities WHERE city_name = '%s';" %(cityName))
    for r in p:
        return r[0]


## Returns dictionary with all resources in the city
def getResources(cityID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = []
    p = c.execute("SELECT wood, iron, gold, food, population, soldiers, happiness FROM cities WHERE city_id = %s;" %(cityID))
    for r in p:
        ret = {"wood":r[0], "iron":r[1], "gold":r[2],"food":r[3], "population":r[4], "soldiers":r[5], "happiness":r[6]}
        conn.close()
        return ret

## Updates all resources with the cityID
def updateResources(cityID, wood, iron, gold, food, population, soldiers, happiness):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("UPDATE cities SET wood = ?, iron = ?, gold = ?, food = ?, population = ?, soldiers = ?, happiness = ? WHERE city_id = ?;",
    (wood, iron, gold, food, population, soldiers, happiness, cityID))
    conn.commit()
    conn.close()

## get the increases in all resources
def getResourceIncreases(cityID):
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
            peopleHoused += allBuildings[0]["housed"]*b["level"]
        if b["type"] == 2:# barracks
            soldiers += allBuildings[1]["soldiers"]*b["level"]
        if b["type"] == 4:# hospital
            # do the hospital stuff
            food += allBuildings[3]["food"]*b["level"]
        if b["type"] == 5:# mine
            iron += allBuildings[4]["iron"]*b["level"]
        if b["type"] == 6:# woodmill
            wood += allBuildings[5]["wood"]*b["level"]
        if b["type"] == 7:# farm
            food += allBuildings[6]["food"]*b["level"]
        if b["type"] == 8:# mall
            gold += allBuildings[7]["gold"]*b["level"]
        if b["type"] == 9:# park
            happiness += allBuildings[8]["happiness"]*b["level"]
    r = getResources(cityID)
    # happiness calculation:
    happiness += (max(0, peopleHoused - r["population"])) + (r["food"] - r["population"])
    # population growth calculation:
    population = (r["food"] - r["population"]) + (r["happiness"] - r["population"])
    #weatherMult = int(getWeatherOf(cityID)/10)
    return {"wood":wood, "iron":iron, "gold":gold, "food":food, "population":population, "soldiers":soldiers, "happiness":happiness}


## automatically update all values in cityID
def updateCity(cityID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    r = getResources(cityID)
    rInc = getResourceIncreases(cityID)
    updateResources(cityID,
    r["wood"]+rInc["wood"],
    r["iron"]+rInc["iron"],
    r["gold"]+rInc["gold"],
    r["food"]+rInc["food"],
    r["population"]+rInc["population"],
    r["soldiers"]+rInc["soldiers"],
    r["happiness"]+rInc["happiness"])
    conn.commit()
    conn.close()
    print r


## update all cities
def updateAll():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT city_id FROM cities;")
    cities = []
    for r in p:
        cities.append(r[0])
    conn.close()
    for city in cities:
        updateCity(city)

#+========================+#
#+========Buildings=======+#
#+========================+#

def findBuildingType(name):
    for r in allBuildings:
        if r["name"] == name:
            return r["type"]
    return 0

def findBuildingName(buildType):
    for r in allBuildings:
        if r["type"] == buildType:
            return r["name"]
    return 0

## returns a dictionary of prices (can include wood, iron, gold, or food)
def upgradePrice(buildingID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT type, level FROM buildings WHERE building_id = %s" %(buildingID))
    type = 0
    level = 0
    for r in p:
        type = r[0]
        level = r[1]
    conn.close()
    price = {}
    for key in prices[type-1].keys():
        if (key != "type"):
            price[key] = prices[type-1][key]*(level+1)# multiplied by level
    print price
    return price


## returns a dictionary of prices (can include wood, iron, gold, or food)
def buildingPrice(type):
    price = {}
    for key in prices[type-1].keys():
        if (key != "type"):
            price[key] = prices[type-1][key]
    return price



## add a building in cityID at bx, by, with type
def addBuilding(cityID, bx, by, type):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    if type == 3:
        return False
    resources = getResources(cityID)
    price = buildingPrice(type)
    for key in price.keys():
        if price[key] > resources[key]:
            return False

    for key in price.keys():
        c.execute("UPDATE cities SET %s = ? WHERE city_id = ?;" %(key), (resources[key]-price[key], cityID))
    c.execute("INSERT INTO buildings(city_id, bx, by, type, level) VALUES (?, ?, ?, ?, ?);", (cityID, bx, by, type, 1))
    conn.commit()
    conn.close()
    return True


## gets a list of dictionaries, gathering all info about all buildings in city with cityID
def getBuildingsIn(cityID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    buildings = []
    p = c.execute("SELECT city_id, bx, by, type, level FROM buildings WHERE city_id = %s;" %(cityID))
    for r in p:
        buildings.append({"city_id":r[0], "bx":r[1], "by":r[2],"type":r[3], "level":r[4], "upgradePrice":upgradePrice(buildingID)})
    conn.close()
    return buildings


## returns the BuildingID based on city_id, bx and by
def getBuildingXY(cityID, bx, by):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT building_id FROM buildings WHERE city_id = ? AND bx = ? AND by = ?;", (cityID, bx, by))
    for r in p:
        return r[0]
    conn.close()
    return 0


## returns a dictionary with the stats of building with buildingID
def getBuilding(buildingID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT city_id, bx, by, type, level FROM buildings WHERE building_id = %s;" %(buildingID))
    for r in p:
        return {"city_id":r[0], "bx":r[1], "by":r[2],"type":r[3], "level":r[4], "upgradePrice":upgradePrice(buildingID)}
        conn.close()
    return {}

## increases level of a building if its level is less than cityhall level and if there is enough of the resources
def levelUpBuilding(buildingID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    p = c.execute("SELECT city_id FROM buildings WHERE building_id = %s" %(buildingID))
    cityID = 0
    for r in p:
        cityID = r[0]
    resources = getResources(cityID)
    price = upgradePrice(buildingID)
    for key in price.keys():
        if price[key] > resources[key]:
            print "False: Not enough resources"
            return False

    for key in price.keys():
        c.execute("UPDATE cities SET %s = ? WHERE city_id = ?;" %(key), (resources[key]-price[key], cityID))
    p = c.execute("SELECT city_id, level, type FROM buildings WHERE building_id = %s;" %(buildingID))
    for r in p:
        cityID = r[0]
        level = r[1]
        type = r[2]

    p = c.execute("SELECT level FROM buildings WHERE city_id = %s AND type = 3;" %(cityID))
    for r in p:
        cityLevel = r[0]
    if cityLevel > level or type == 3:# it can be the same after it is set
        # Check for price
        c.execute("UPDATE buildings SET level = ? WHERE building_id = ?;", (level+1, buildingID))
        conn.commit()
        conn.close()
        print "True"
        return True
    print "False: City level not high enough"
    return False
    # returns false if the price is too high or the level is too high


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
    conn.close()




#+========================+#
#+========Messages========+#
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
    conn.close()



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
    conn.close()
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
    conn.close()
    return unseen

## set all of the messages from fromID to userID to seen
def setAllSeenFrom(userID, fromID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("UPDATE messages SET seen = 1 WHERE from_id = ? AND to_id = ?;", (fromID, userID))
    conn.commit()
    conn.close()


## adds the friendID to the userID friend list
def addFriend(userID, friendID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("INSERT INTO friends VALUES (?, ?);", (userID, friendID))
    conn.commit()
    conn.close()


## gets all friends of account with uname = uname
def getFriends(userID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT them FROM friends WHERE you = %s;" %(userID))
    list = []
    for r in p:
        list.append(r[0])
    conn.close()
    return list


## find the names of all non-friend accounts of accountID
def findAllNonFriends(userID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT uname FROM accounts")
    friends = getFriendsNames(userID)
    nonfriends = []
    for r in p:
        if (not userID == findID(r[0])) and friends.count(r[0]) == 0:
            nonfriends.append(r[0])
    conn.close()
    return nonfriends



# get all friends of userID names
def getFriendsNames(userID):
    f = getFriends(userID)
    list = []
    for r in f:
        list.append(findUname(r))
    return list



#+========================+#
#+=========Action=========+#
#+========================+#

# have one city attack another (takes cityIDs)
def attack(defendingCity, attackingCity):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    updateStamp(getCityOwner(attackingCity))
    aSoldiers = getResources(attackingCity)["soldiers"]
    dSoldiers = int(getResources(defendingCity)["soldiers"]*1.2)# defending cities get a bonus
    # if attackers have more
        # defenders lose everything
    # if defenders have more
        # attackers lose half
        # defenders lose the amount attackers lost
    if aSoldiers > dSoldiers:
        aSoldiers -= dSoldiers
        attacker = getCityOwner(attackingCity)
        setCityOwner(defendingCity, attacker)
    else:
        loss = max(aSoldiers - dSoldiers, aSoldiers/2)
        aSoldiers -= loss
        dSoldiers -= min(loss, dSoldiers)
        c.execute("UPDATE cities SET soldiers = ? WHERE city_id = ?;", (dSoldiers, defendingCity))
    c.execute("UPDATE cities SET soldiers = ? WHERE city_id = ?;", (aSoldiers, attackingCity))
    conn.commit()


## Saves a timestamp for the last time that player's data was updated
def saveStamp(userID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT account_id FROM updatetimes")
    b = False
    for r in p:
        if r[0] == userID:
            b = True
    conn.close()
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    if b:
        c.execute("UPDATE updatetimes SET time = ? WHERE account_id = ?;", (int(time.time()), userID))
    else:
        c.execute("INSERT INTO updatetimes VALUES (?, ?);", (userID, int(time.time())))
    conn.commit()
    conn.close()

## gets the time the player was last updated, updates, and saves the timestamp
def updateStamp(userID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    p = c.execute("SELECT time FROM updatetimes WHERE account_id = %s" %(userID))
    updateTimes = 0
    for r in p:
        updateTimes = (int(time.time())-r[0])/5
    conn.close()
    x = 0
    while x < updateTimes:
        updateAll()
        x += 1
    saveStamp(userID)


#createWorld()

#addAccount("test", "123", "")
#addBuilding(getCityID("testpolis"), 1, 1, 7)
#addAccount("milo", "123", " ")
#levelUpBuilding(getBuildingXY(getCityID("testpolis"), 1, 1))
#print getResources(getCityID("testpolis"))
#updateStamp(getCityID("testpolis"))
#print getResources(getCityID("testpolis"))
