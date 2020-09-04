from flask import Flask, redirect, url_for

# Define website
app = Flask(__name__)

# Define Pages
@app.route("/")
def home():
    return "<h1>Main Page</h1>"     # Returns inline html

@app.route("/<name>") # Passes the string in the url to the function parameter
def user(name):
    return f"Hello {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))    # Redirects to home

if __name__ == "__main__":
    app.run()