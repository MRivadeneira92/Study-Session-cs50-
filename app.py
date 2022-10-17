from flask import Flask, render_template, request, redirect
from Functions import timer

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/timer_setup")
def timer_setup():

    return render_template("timer_setup.html")

@app.route("/timer")
def timer():
    numb_timers = request.form.get("num_timers")
    hour = 0
    min = 0
    sec = 5
    return render_template("timer.html", hour=hour, min=min, sec=sec)

@app.route("/test")
def test():
    return render_template("test.html")