import utils
import json
from threading import Timer
from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)

@app.route("/")
def intro():
    return render_template("login.html")

"""<-------------------------------LOGIN------------------------------->"""
"""route to the home page, will have a LOGIN button and a REGISTER button"""
@app.route("/login", methods = ["GET", "POST"])
def login():
    print request.form["button"]
    if str(request.form["button"]) == "Log in!":
        username = str(request.form["username"])
        if utils.pwordAuth(username, str(request.form["password"])):
            hold2 = utils.findID(username)
            utils.updateStamp(hold2)
            session["username"] = username
            return redirect(url_for('play2', username = username))
        else:
            return render_template("login.html", text = "Username/Password does not match")
    else:
        return render_template("register.html")

@app.route("/login2", methods = ["GET", "POST"])
def login2():
    return render_template("login.html")
    
"""<-------------------------------REGISTER------------------------------->"""    
@app.route("/register", methods = ["GET", "POST"])
def register():
    if str(request.form["button"]) == "Register!":
        username = str(request.form["username"])
        password1 = str(request.form["password1"])
        password2 = str(request.form["password2"])
        email = str(request.form["usermail"])
        if not utils.unameAuth(username):
            if password1 == password2:
                utils.addAccount(username, password1, email)
                session["username"] = username

                return redirect(url_for('play2', username = username))
            else:
                return render_template("register.html", text = "The passwords do not match")
          
        else:
            return render_template("register.html", text = "This username already exists")
    else:
        return render_template("login.html")

"""<-------------------------------SETTINGS------------------------------->"""
@app.route("/settings")
def settings():
    return redirect(url_for('login2'))

@app.route("/settings/<username>", methods = ["GET, POST"])
def settings2(username):
    if "username" not in session:
        return redirect(url_for("login2"))
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
    return redirect(url_for('login2'))

@app.route("/play/<username>", methods = ["GET", "POST"]) 
def play2(username):
    if "username" not in session:
        return redirect(url_for('login2'))
    #utils.addAccount("test", "123", "")
    #print username
    userid = utils.findID(username)
    #print userid
    cityname = utils.getCitiesName(userid)[0]
    return render_template("test.html", username = username, cityname = cityname)

@app.route("/logout", methods = ["GET", "POST"])
def logfin():
    hold = session["username"]
    hold2 = utils.findID(hold)
    utils.saveStamp(hold2)
    session.clear()
    return render_template("login.html")

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

    if function_type == "get_cityNames":
        """username"""
        accountID = utils.findID(a)
        hold = utils.getCitiesName(accountID)
        print hold
        return json.dumps(hold)

    if function_type == "get_resources":
        """cityName"""
        cityID = utils.getCityID(a)
        hold = utils.getResources(cityID)
        
        print hold
        return json.dumps(hold)

    if function_type == "get_multipliers":
        """cityName"""
        cityID = utils.getCityID(a)
        hold = utils.getResourceIncreases(cityID)
        print  hold
        return json.dumps(hold)
        
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
        hold = utils.getFriendsNames(accountID)
        print  hold
        return json.dumps(hold)

    if function_type == "base_building_stats":
        """returns a list of dictionaries"""
        d = {"buildings": utils.allBuildings,
             "prices": utils.prices}
        return json.dumps(d)

    if function_type == "find_build_type":
        """building name"""
        hold = utils.findBuildingType(a)
        return hold


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
        return "success"

    if function_type == "update_resources":
        """cityName"""
        cityID = utils.getCityID(a)
        utils.updateAll(cityID)
        return "success"

    #if function_type == "set_multipliers":
        

    if function_type == "set_msgs":
        """from, to, messages"""
        accountID = utils.findID(a)
        friendID = utils.findID(b)
        utils.addmsg(accountID, friendID, c)
        return "success"

    if function_type == "set_friends":
        """username, friend"""
        accountID = utils.findID(a)
        friendID = utils.findID(b)
        utils.addFriend(accountID, friendID)
        return "success"

    if function_type == "add_city":
        """cityname, cx, cy, wood, iron, gold, food"""
        utils.addCity(a, b, c, d, e, f, g)
        return "success"

    if function_type == "set_city_owner":
        """username, cityname"""
        accountID = utils.findID(a)
        cityID = utils.getCityID(b)
        utils.setCityOwner(accountID, cityID)
        return "success"

    if function_type == "set_building":
        """buildingID"""
        utils.LevelUpBuilding(a);
        return "success"

if __name__ == "__main__":
    app.secret_key= 'OIBO&*(YOMNKIU123!@!@(O'
    app.debug = True
    app.run(host="0.0.0.0", port=8000)
   
