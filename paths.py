import utils
form flask import FLask, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route("/")
def intro():

@app.route("/login", methods = ["GET", "POST"])
def login():
    if str(request.form["button"]) == "Log in!":
        username = str(request.form["username"])
        if utils.pwordAuth(username, str(request.form["password"])): //need a utils.pwordAuth
            return redirect('/play/' + username)
        else:
            return render_template("/home.html", text = "Username/Password does not match")
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
@app.route("/settings/<username>", methods = ["GET, POST"])
def settings2:
    
    
@app.rouet("/play")
def play:
    return redirect("/login")
@app.route("/play/<username>", methods = ["GET", "POST"])
def play2:

@app.route("/loginfinished/<username>", methods = ["GET", "POST"])
def logfin:
    

if __name__ = "__main__":
    app.debug = True
    app.run()
