from app import app
from db import db
import users
import restaurants
from flask import redirect, render_template, request, session

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/login",methods=["POST"])
def login():
	username = request.form["username"]
	password = request.form["password"]
	if users.login(username, password):
		return redirect("/")
	else:
		return render_template("error.html", message="Väärä tunnus tai salasana.")

@app.route("/logout")
def logout():
	del session["username"]
	return redirect("/")

@app.route("/signup", methods=["GET","POST"])
def signup():
	if request.method == "GET":
		return render_template("signup.html")
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
		if users.signup(username, password):
			return redirect("/")
		else:
			return render_template("error.html", message="Rekisteröinti ei onnistunut. Valitse toinen käyttäjätunnus.")

@app.route("/map")
def map():
	coordinates = restaurants.get_coordinates("Kinkku & kalkkuna")
	return render_template("map.html", lat=coordinates[0], lng=coordinates[1])

@app.route("/addrestaurant", methods=["GET","POST"])
def add_restaurant():
	if request.method == "GET":
		return render_template("add_restaurant.html")
	if request.method == "POST":
		name = request.form["name"]
		description = request.form["description"]
		address = request.form["address"]
		restaurants.add_restaurant(name, description, address)
		return redirect("/")
