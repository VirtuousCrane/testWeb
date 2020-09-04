from flask import Flask, redirect, url_for, render_template

# Define website
app = Flask(__name__)

# Define Pages
@app.route("/")
def home():
    return render_template("index.html")     # Returns inline html

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
    app.run()