from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

# Define website
app = Flask(__name__)
app.secret_key = "ILoveMyLittleSister"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'	#users is table name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5)	# Dictates how long a session stays

db = SQLAlchemy(app)
class users(db.Model):
	_id = db.Column("id", db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	email = db.Column(db.String(100))

	def __init__(self, name, email):
		self.name = name
		self.email = email



# Define Pages
@app.route("/")
def home():
    return render_template("index.html")     # Returns inline html

@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		session.permanent = True	# Will last as long as we dictates
		user = request.form["nm"]
		session["user"] = user
		flash("Login Successful")
		return redirect(url_for("user"))
	else:
		if "user" in session:
			flash("Already Logged in")
			return redirect(url_for("user"))
		return render_template("login.html")


@app.route("/user", methods=["POST", "GET"])
def user():
	email = None
	if "user" in session:
		user = session["user"]

		if request.method == "POST":
			email = request.form["email"]
			session["email"] = email
			flash("Email was saved")
		else:
			if "email" in session:
				email = session["email"]
		return render_template("user.html", email=email)
	else:
		flash("You are not logged in.")
		return redirect(url_for("login"))


@app.route("/logout")
def logout():
	if "user" in session:
		user = session["user"]
		flash(f"You have been logged out, {user}")
	session.pop("user", None)
	session.pop("email", None)
	return redirect(url_for("login"))
'''
@app.route("/<name>") # Passes the string in the url to the function parameter
def user(name):
    return f"Hello {name}!"


# Normal Redirect
@app.route("/admin")
def admin():
    return redirect(url_for("home"))    # Redirects to home


@app.route("/admin")
# Redirect to page with parameter
def admin():
    return redirect(url_for("user", name="Ad!"))
'''

if __name__ == "__main__":
	db.create_all()
    app.run(debug=True)