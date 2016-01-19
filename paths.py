import utils, other 
form flask import FLask, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route("/")
def intro():
    return render_template 

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

@app.route("/settings")
def settings:
    return redirect("/login")
@app.route("/settings/<username>", methods = ["GET, POST"]) //make sure to make a pass confirmation
def settings2:
    
    
@app.route("/play")
def play:
    return redirect("/login")
@app.route("/play/<username>", methods = ["GET", "POST"]) //make sure to make a pass confirmation
def play2:

@app.route("/loginfinished/<username>", methods = ["GET", "POST"])
def logfin:


@app.route("/get_functions", methods = ["GET", "POST"])
def get_functions(type, a, b, c, d):
    if type == "get_cityIDs": //username
        hold = utils.getCitiesID(a)
    if type == "get_resources": //cityID
        hold = utils.getResources(a)
        return hold
    if type = "get_multipliers": //cityID
        return "multipliers"
    if type == "get_msgs": //from, to
        hold = utils.getmsgs(a, b)
        return hold
    if type == "get_citymap": //mapx, mapy
        hold = utils.getCity(a, b) 
    if type == "get_city_buildings": //cityID
        hold = utils.getBuildingsIn(a)
    if type == "get_specific_building": //cityID, buildingx, buildingy
        hold = utils.getBuilding(a, b, c)
    if type == "get_friends": //username
        hold = utils.getFriends(a)

@app.route("/set_functions", methods = ["GET", "POST"])
def set_functions(type, a, b, c, d):
    if type == "add_building": //cityID, buildingx, buildingy, buildingtype
        utils.addBuilding(a, b, c, d)
    if type == "set_resources":
        //set the damn resources
    if type == "set_multipliers":
        //set the damn multipliers
    if type == "set_msgs":
        //set the damn msgs
    if type == "set_friends":
        //set the damn friends
    if type == "add_city":
        //add the damn city to the username
    if type == "set_building":
        //update a building

if __name__ = "__main__":
    app.debug = True
    app.run()
