from flask import Flask, redirect, render_template, session, request


app = Flask(__name__)

def test_printer(value):
    if value == 1:
        return "Turtles"
    if value == 2:
        return "Uno Dos Tres"


@app.route("/")
def index():
    return render_template("page.html", printout = test_printer(1))


app.run(host="0.0.0.0", port=81)
