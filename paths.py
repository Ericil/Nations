import utils
import json
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route("/")
def intro():
    return "hello"

"""<-------------------------------LOGIN------------------------------->"""
"""route to the home page, will have a LOGIN button and a REGISTER button"""
@app.route("/login", methods = ["GET", "POST"])
def login():
    if str(request.form["button"]) == "Log in!":
        username = str(request.form["username"])
        if utils.pwordAuth(username, str(request.form["password"])): 
            return redirect(url_for('play2', username = username))
        else:
            return render_template("login.html", text = "Username/Password does not match")
    else:
        return render_template("register.html")

"""<-------------------------------REGISTER------------------------------->"""    
@app.route("/register", methods = ["GET", "POST"])
def register():
    if str(request.form["button"]) == "Register!":

        username = str(request.form["username"])
        password = str(request.form["password"])
        first = str(request.form["firstname"])
        last = str(request.form["lastname"])
        text = str(request.form["paragraph_text"])
        
        if not utils.unameAuth(username): 
            utils.addAccount(username, password, first, last)
            utils.editInfo(username, text)
            return redirect(url_for('logfin', username = username))
          
        else:
            return render_template("register.html", text = "This username already exists")
    else:
        return render_template("login.html")

"""<-------------------------------SETTINGS------------------------------->"""
@app.route("/settings")
def settings():
    return redirect(url_for('login'))

@app.route("/settings/<username>", methods = ["GET, POST"])
def settings2(username):
    print 1
    if request.method == "POST":
        print 2
        post = str(request.form["post"])
        if (post == "change"):
            print 3
            the_response = utils.changePword(str(request.form["user"]), str(request.form["oldpass"]), str(request.form["pass1"]), str(request.form["pass2"]))
            return render_template("settings.html", username = username, the_response = the_response, friendslist = utils.friendList(username))
        
        elif (post == "finding"):
            print 4
            utils.addFriend(username, str(request.form["search_for"]))
            return render_template("settings.html", username = username, friendslist = utils.friendList(username))
    else:
        return render_template("settings.html", username = username, friendslist = utils.friendList(username))


#PLAY
@app.route("/play")
def play():
    return redirect(url_for('login'))

@app.route("/play/<username>", methods = ["GET", "POST"]) 
def play2(username):
    return render_template("test.html", username = username)

@app.route("/loginfinished/<username>", methods = ["GET", "POST"])
def logfin(username):
    return "hello"

#GET_FUNCTIONS
@app.route("/get_functions")
def get_functions():
    function_type = request.args.get("type")
    a = request.args.get("a")
    b = request.args.get("b")
    c = request.args.get("c")
    if function_type == "get_accountID":
        """username"""
        hold == utils.findID(a)
        return hold

    if function_type == "get_cityIDs":
        """accountID"""
        accountID = utils.findID(a)
        hold = utils.getCitiesID(a)
        return hold

    if function_type == "get_resources":
        """cityName"""
        cityID = utils.getCityID(a)
        hold = utils.getResources(cityID)
        return hold

    if function_type == "get_multipliers":
        """cityName"""
        cityID = utils.getCityID(a)
        hold = utils.getResourceIncreases(cityID)
        return hold
        
    if function_type == "get_msgs":
        """from, to"""
        accountID = utils.findID(a)
        friendID = utils.findID(b)
        hold = utils.getmsgs(accountID, friendID)
        return hold

    if function_type == "get_city_on_map":
        """mapx, mapy"""
        hold = utils.getCity(a, b)
        return hold
        
    if function_type == "get_city_buildings":
        """cityName"""
        cityID = utils.getCityID(a)
        hold = utils.getBuildingsIn(cityID)
        return hold

    if function_type == "get_specific_building":
        """cityName, buildingx, buildingy"""
        cityID = utils.getCityID(a)
        hold = utils.getBuildingXY(cityID, b, c)
        return hold

    if function_type == "get_specific_building_stat":
        """buildingID"""
        hold = utils.getBuilding(a)
        return hold

    if function_type == "get_friends":
        """username"""
        accountID = utils.findID(a)
        hold = utils.getFriends(accountID)
        return hold

    if function_type == "base_building_stats":
        """returns a list of dictionaries"""
        return json.dumps(utils.allBuildings)    


"""<-------------------------------SET_FUNCTIONS------------------------------->"""
@app.route("/set_functions")
def set_functions():
    function_type = request.args.get("type")
    a = request.args.get("a")
    b = request.args.get("b")
    c = request.args.get("c")
    d = request.args.get("d")
    e = request.args.get("e")
    f = request.args.get("f")
    g = request.args.get("g")
    
    if function_type == "add_building":
        """cityName, buildingx, buildingy, buildingtype"""
        cityID = utils.getCityID(a)
        utils.addBuilding(cityID, b, c, d)

    if function_type == "update_resources":
        """cityName, wood, iron, gold, food, population, soldiers"""
        cityID = utils.getCityID(a)
        utils.updateResources(cityID, b, c, d, e, f, g)

    #if function_type == "set_multipliers":
        

    if function_type == "set_msgs":
        """from, to, messages"""
        accountID = utils.findID(a)
        friendID = utils.findID(b)
        utils.addmsg(accountID, friendID, c)

    if function_type == "set_friends":
        """username, friend"""
        accountID = utils.findID(a)
        friendID = utils.findID(b)
        utils.addFriend(accountID, friendID)

    if function_type == "add_city":
        """cityname, cx, cy, wood, iron, gold, food"""
        utils.addCity(a, b, c, d, e, f, g)

    if function_type == "set_city_owner":
        """username, cityname"""
        accountID = utils.findID(a)
        cityID = utils.getCityID(b)
        utils.setCityOwner(accountID, cityID)

    if function_type == "set_building":
        """buildingID"""
        utils.LevelUpBuilding(a);
        

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8000)
   
