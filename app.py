from flask import Flask, redirect, render_template, request, session #anything you put in the session variable, which iself is a dictionary, will be there again and again when the user comes back. 
#a session is how you implement a shopping cart. If I login to amazon, and you login to amazon, amazon knows which user is which by way of that cookie. If amazon is using flask, they provide 
#the programmer with a dictionary called session. Flask makes sure that, when carter is visiing the site, tthe code uses his session object vs. my session object when I'm visitting the site
from flask_session import Session

#Configure app
app = Flask(__name__)

#Configure session
app.config["SESSION_PERMERNANT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
	if not session.get("name"):
		return redirect("/login")
	return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "POST":
		session["name"] = request.form.get("name")
		return redirect("/")
	return render_template("login.html")

@app.route("/logout")
def logout():
	session["name"] = None
	return redirect("/")
