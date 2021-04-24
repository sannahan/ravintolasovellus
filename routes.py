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
			return render_template("signup.html", errormessage="Rekisteröinti ei onnistunut. Valitse toinen käyttäjätunnus.")

@app.route("/map")
def map():
	info = restaurants.get_info_for_map()
	return render_template("map.html", info=info)

@app.route("/addrestaurant", methods=["GET","POST"])
def add_restaurant():
	if request.method == "GET":
		return render_template("add_restaurant.html")
	if request.method == "POST":
		name = request.form["name"]
		description = request.form["description"]
		address = request.form["address"]
		opening = request.form["opening_hours"] + ":" + request.form["opening_minutes"]
		closing = request.form["closing_hours"] + ":" + request.form["closing_minutes"]
		days = request.form.getlist("days")
		restaurants.add_restaurant(name, description, address, opening, closing, days)
		return redirect("/")

@app.route("/removerestaurant", methods=["GET","POST"])
def remove_restaurant():
	if request.method == "GET":
		restaurantnames = restaurants.get_list()
		return render_template("remove_restaurant.html", restaurants=restaurantnames)
	if request.method == "POST":
		restaurant_id = request.form["restaurant_to_be_removed"]
		restaurants.remove_restaurant(restaurant_id)
		return redirect("/")

@app.route("/restaurant/<int:id>", methods=["GET","POST"])
def restaurant(id):
	if request.method == "POST":
		stars = int(request.form["stars"])
		comment = request.form["comment"]
		reviews.add_review(id, stars, comment)
	info = restaurants.get_info(id)
	reviews_list = reviews.get_list(id)
	return render_template("restaurant.html", info=info[0], open=info[1], id=id, reviews=reviews_list)

@app.route("/restaurantlist")
def restaurantlist():
	restaurant_list = restaurants.get_list()
	return render_template("restaurantlist.html", restaurants=restaurant_list)

@app.route("/search", methods=["GET"])
def search():
	query = request.args["query"]
	restaurant_list = restaurants.search(query)
	return render_template("restaurantlist.html", restaurants=restaurant_list)
