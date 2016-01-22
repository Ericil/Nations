import utils, other 
form flask import FLask, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route("/")
def intro():
    return render_template 



"""<-------------------------------LOGIN------------------------------->"""
"""route to the home page, will have a LOGIN button and a REGISTER button"""
@app.route("/login", methods = ["GET", "POST"])
def login():
    if str(request.form["button"]) == "Log in!":
        username = str(request.form["username"])
        if utils.pwordAuth(username, str(request.form["password"])): //need a utils.pwordAuth
            return redirect('/play/' + username)
        else:
            return render_template("/login.html", text = "Username/Password does not match")
    else:
        return render_template("/register.html")

"""<-------------------------------REGISTER------------------------------->"""    
@app.route("/register", methods = ["GET", "POST"])
def register:
    if str(request.form["button"]) == "Register!":
        if utils.unameAuth(str(request.form["username"])) != True: //need a utils.unameAuth
            utils.addAccount(str(request.form["username"]), str(request.form["password"]), str(request.form["firstname"]), str(request.form["lastname"])) //need utils.addAccount
            utils.editInfo(str(request.form["username"]), str(request.form["paragraph_text"])) //need utils.addAcount
            return redirect('/loginfinished/' + str(request.form["username"]))
        else:
            return render_template("/register.html", text = "this username already exists")
    else:
        return render_template("/login.html")

"""<-------------------------------SETTINGS------------------------------->"""
@app.route("/settings")
def settings:
    return redirect("/login")
@app.route("/settings/<username>", methods = ["GET, POST"]) //make sure to make a pass confirmation
def settings2:
    print("1")
    if request.method == "POST":
        print("2")
        if (str(request.form["post"]) == "change"):
            print("3")
            the_response = utils.changePword(str(request.form["user"]), str(request.form["oldpass"]), str(request.form["pass1"]), str(request.form["pass2"]))
            return render_template("settings.html", username = username, the_response = the_response, friendslist = utils.friendList(username))
        elif (str(request.form["post"]) == "finding"):
            print("4")
            utils.addFriend(username, str(request.form["search_for"]))
            return render_template("settings.html", username = username, friendslist = utils.friendList(username))
    else:
        return render_template("settings.html", username = username, friendslist = utils.friendList(username))


"""<-------------------------------PLAY------------------------------->"""
@app.route("/play")
def play:
    return redirect("/login")
@app.route("/play/<username>", methods = ["GET", "POST"]) //make sure to make a pass confirmation
def play2:
    return render_template("/test.html", username = username)

@app.route("/loginfinished/<username>", methods = ["GET", "POST"])
def logfin:

"""<-------------------------------GET_FUNCTIONS------------------------------->"""
@app.route("/get_functions", methods = ["GET", "POST"])
def get_functions(type, a, b, c, d):
    if type == "get_accountID":
        """username""":
        hold == utils.findID(a)
        return hold

    if type == "get_cityIDs"
        """accountID"""
        hold = utils.getCitiesID(a)
        return hold

    if type == "get_resources":
        """cityID"""
        hold = utils.getResources(a)
        return hold

    if type = "get_multipliers":
        """cityID"""
        return "multipliers"

    if type == "get_msgs":
        """from, to"""
        hold = utils.getmsgs(a, b)
        return hold

    if type == "get_citymap":
        """mapx, mapy"""
        hold = utils.getCity(a, b) 
        
    if type == "get_city_buildings":
        """cityID"""
        hold = utils.getBuildingsIn(a)

    if type == "get_specific_building":
        """cityID, buildingx, buildingy"""
        hold = utils.getBuildingXY(a, b, c)
        return hold

    if type == "get_specific_building_stat":
        """buildingID"""
        hold = utils.getBuilding(a)
        return hold

    if type == "get_friends":
        """username"""
        hold = utils.getFriends(a)
        return hold

    if type == "base_building_stats":
        """returns a list of dictionaries"""
        return utils.allBuildings    


"""<-------------------------------SET_FUNCTIONS------------------------------->"""
@app.route("/set_functions", methods = ["GET", "POST"])
def set_functions(type, a, b, c, d, e, f, g):
    if type == "add_building":
        """cityID, buildingx, buildingy, buildingtype"""
        utils.addBuilding(a, b, c, d)

    if type == "update_resources":
        """cityid, wood, iron, gold, food, population, soldiers"""
       utils.updateResources(a, b, c, d, e, f, g)

    if type == "set_multipliers":
        

    if type == "set_msgs":
        """fromID, toID, messages"""
        utils.addmsg(a, b, c)

    if type == "set_friends":
        """userID, friendID"""
        utils.addFriend(a, b)

    if type == "add_city":
        """cityname, cx, cy, wood, iron, gold, food"""
        utils.addCity(a, b, c, d, e, f, g)

    if type == "set_city_owner":
        """accountID, cityID"""
        utils.setCityOwner(a, b)

    if type == "set_building":
        //update a building

if __name__ = "__main__":
    app.debug = True
    app.run()
