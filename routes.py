from app import app
from db import db
import users
import restaurants
import reviews
from flask import redirect, render_template, request, session

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
	username = request.form["username"]
	password = request.form["password"]
	if users.login(username, password):
		return redirect("/")
	else:
		return render_template("index.html", errormessage="Väärä tunnus tai salasana.")

@app.route("/logout")
def logout():
	users.logout()
	return redirect("/")

@app.route("/signup", methods=["GET","POST"])
def signup():
	if request.method == "GET":
		return render_template("signup.html")
	if request.method == "POST":
		errormessage = ""

		username = request.form["username"]
		if len(username) < 1:
			errormessage = "Rekisteröinti ei onnistunut. Käyttäjänimi ei saa olla tyhjä"

		password = request.form.getlist("password")
		if len(password[0]) < 1:
			errormessage = "Rekisteröinti ei onnistunut. Salasana ei saa olla tyhjä"
		if password[0] != password[1]:
			errormessage = "Rekisteröinti ei onnistunut. Salasanat eivät täsmää."

		role = request.form["role"]
		if role != "1" and role != "2":
			errormessage = "Rekisteröinti ei onnistunut. Tuntematon rooli."
		
		if len(errormessage) > 0:
			return render_template("signup.html", errormessage=errormessage)

		if users.signup(username, password[0], role):
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
		errormessage = ""
		name = request.form["name"]
		if len(name) < 1:
			errormessage = "Lisääminen ei onnistunut. Ravintolan nimi ei saa olla tyhjä"
		
		description = request.form["description"]
		if len(description) < 1:
			errormessage = "Lisääminen ei onnistunut. Ravintolan kuvaus ei saa olla tyhjä"

		address = request.form["address"]
		if len(address) < 1:
			errormessage = "Lisääminen ei onnistunut. Ravintolan osoite ei saa olla tyhjä"
		
		if len(errormessage) > 0:
			return render_template("add_restaurant.html", errormessage = errormessage)

		opening = request.form["opening_hours"] + ":" + request.form["opening_minutes"]
		closing = request.form["closing_hours"] + ":" + request.form["closing_minutes"]
		days = request.form.getlist("days")

		if restaurants.add_restaurant(name, description, address, opening, closing, days):
			return redirect("/")
		else:
			return render_template("add_restaurant.html", errormessage="Lisääminen ei onnistu. Onhan ravintolalla oikea osoite?")

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
		if "lisays" in request.form:
			stars = int(request.form["stars"])
			comment = request.form["comment"]
			user_id = users.get_id()
			reviews.add_review(id, user_id, stars, comment)
		if "poisto" in request.form:
			review_id = request.form["review_id"]
			reviews.remove_review(review_id)
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
