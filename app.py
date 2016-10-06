from flask import Flask, render_template, request
import utils.login
import hashlib

app = Flask(__name__)

@app.route('/')
def  MainPage():
    return render_template("main.html")

@app.route("/reg", methods=['POST'])
def register():
    encryptor = hashlib.md5()
    Dict = utils.login.Dict()
    if request.form["user"] in Dict:
        return render_template("main.html", message="TAKEN")
    encryptor.update(request.form["password"])
    utils.login.add(request.form["user"], encryptor.hexdigest())
    return render_template("main.html", message="REGISTERED")

@app.route("/authenticate", methods=['POST'])
def authenticateIT():
    Dict = utils.login.Dict()
    users = request.form["user"]
    passwords = request.form["password"]
    encryptor=hashlib.md5()
    encryptor.update(passwords)
    if users not in Dict.keys():
        return render_template("main.html",message="Incorrect")
    elif encryptor.hexdigest() != Dict[users]:
        return render_template("main.html",message="Incorrect")
    else:
        return render_template("main.html", message="YOU WIN")

if(__name__ == "__main__"):
    app.debug = True
    app.run();
