from app import app
from db import db
import users
import restaurants
import reviews
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
	users.logout()
	return redirect("/")

@app.route("/signup", methods=["GET","POST"])
def signup():
	if request.method == "GET":
		return render_template("signup.html")
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
		role = request.form["role"]
		if users.signup(username, password, role):
			return redirect("/")
		else:
			return render_template("signup.html", message="Rekisteröinti ei onnistunut. Valitse toinen käyttäjätunnus.")

@app.route("/map")
def map():
	info = restaurants.get_info_for_map()
	test = [
      		['Bondi Beach', -33.890542, 151.274856],
      		['Coogee Beach', -33.923036, 151.259052],
      		['Cronulla Beach', -34.028249, 151.157507],
      		['Manly Beach', -33.80010128657071, 151.28747820854187],
      		['Maroubra Beach', -33.950198, 151.259302]
    	]
	return render_template("map.html", test=test)

@app.route("/addrestaurant", methods=["GET","POST"])
def add_restaurant():
	if request.method == "GET":
		return render_template("add_restaurant.html")
	if request.method == "POST":
		name = request.form["name"]
		description = request.form["description"]
		address = request.form["address"]
		opening = request.form["opening"]
		closing = request.form["closing"]
		restaurants.add_restaurant(name, description, address, opening, closing)
		return redirect("/")

@app.route("/restaurant/<int:id>", methods=["GET","POST"])
def restaurant(id):
	if request.method == "POST":
		stars = int(request.form["stars"])
		comment = request.form["comment"]
		reviews.add_review(id, stars, comment)
	info = restaurants.get_info(id)
	reviews_list = reviews.get_list(id)
	return render_template("restaurant.html", info=info, id=id, reviews=reviews_list)

@app.route("/restaurantlist")
def restaurantlist():
	restaurant_list = restaurants.get_list()
	return render_template("restaurantlist.html", restaurants=restaurant_list)
