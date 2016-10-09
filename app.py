from flask import Flask, render_template, request, url_for, session, redirect
import utils.login
import hashlib

app = Flask(__name__)
app.secret_key = '\xcfUB\x0c\x897\xca\xb9\xb1\x9c\xc5\xd6)B\xe8\xd6rc\x0c.\xc2\xe0s\xb3\x9d\xb7<"\x1coe\xd2'



@app.route('/')
def  MainPage():
    return render_template("main.html", message = "Welcome " + session['user'])

@app.route("/reg", methods=['POST'])
def register():
    Dict = utils.login.Dict()
    encryptor = hashlib.md5()
    if request.form["user"] in Dict:
        return render_template("login.html", message="TAKEN")
    encryptor.update(request.form["password"])
    utils.login.add(request.form["user"], encryptor.hexdigest())
    return render_template("login.html", message="REGISTERED")

@app.route("/authenticate", methods=['POST'])
def authenticateIT():
    Dict = utils.login.Dict()
    encryptor = hashlib.md5()
    user = request.form["user"]
    password = request.form["password"]
    encryptor.update(password)
    if user not in Dict.keys():
        return render_template("login.html",message="Incorrect")
    elif encryptor.hexdigest() != Dict[user]:
        return render_template("login.html",message="Incorrect")
    else:
        session['user'] = user
        return redirect(url_for('MainPage'))

@app.route("/login")
def login():
    #print request.headers
    if 'user' in session:
        return redirect(url_for('main'))
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop('user')
    return redirect(url_for('login'))

if(__name__ == "__main__"):
    app.debug = True
    app.run();
