from flask import Flask, redirect, url_for, render_template, request

# Define website
app = Flask(__name__)

# Define Pages
@app.route("/")
def home():
    return render_template("index.html")     # Returns inline html

@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		user = request.form["nm"]
		return redirect(url_for("user", usr=user))
	else:
		return render_template("login.html")


@app.route("/<usr>")
def user(usr):
	return f"<h1>{usr}</h1>"
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