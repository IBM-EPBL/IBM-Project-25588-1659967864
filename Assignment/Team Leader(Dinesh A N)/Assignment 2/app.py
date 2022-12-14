from flask import Flask, redirect, url_for, render_template

app = Flask(_name_)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/about")
def about():
    return render_template("about.html")

if _name_ == "_main_":
    app.run()
