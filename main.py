from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

# Define website
app = Flask(__name__)
app.secret_key = "ILoveMyLittleSister"
app.permanent_session_lifetime = timedelta(minutes=5)	# Dictates how long a session stays

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


@app.route("/user")
def user():
	if "user" in session:
		user = session["user"]
		return render_template("user.html", user=user)
	else:
		flash("You are not logged in.")
		return redirect(url_for("login"))


@app.route("/logout")
def logout():
	if "user" in session:
		user = session["user"]
		flash(f"You have been logged out, {user}")
	session.pop("user", None)
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
    app.run(debug=True)