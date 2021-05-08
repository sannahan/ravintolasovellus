from app import app
from db import db
import users
import restaurants
import reviews
import tags
from flask import redirect, render_template, request, session

@app.route("/")
def index():
	tag_list = tags.get_tags()
	return render_template("index.html", tags=tag_list)

@app.route("/login", methods=["POST"])
def login():
	username = request.form["username"]
	password = request.form["password"]
	if users.login(username, password):
		return redirect("/")
	else:
		tag_list = tags.get_tags()
		return render_template("index.html", errormessage="Väärä tunnus tai salasana.", tags=tag_list)

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
	days_of_the_week = ["Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai", "Sunnuntai"]
	if not users.is_admin():
		return render_template("forbidden.html", message="Sinulla ei ole oikeutta nähdä tätä sivua")
	if request.method == "GET":
		return render_template("add_restaurant.html", days=days_of_the_week)
	if request.method == "POST":
		errormessage = ""
		name = request.form["name"]
		if len(name) < 1:
			errormessage = "Lisääminen ei onnistunut. Ravintolan nimi ei saa olla tyhjä"
		
		description = request.form["description"]
		if len(description) < 1:
			errormessage = "Lisääminen ei onnistunut. Ravintolan kuvaus ei saa olla tyhjä"

		if len(name) > 500 or len(description) > 500:
			errormessage = "Lisääminen ei onnistunut. Nimen ja kuvauksen tulee olla alle 500 merkkiä"

		address = request.form["address"]
		if len(address) < 1:
			errormessage = "Lisääminen ei onnistunut. Ravintolan osoite ei saa olla tyhjä"
		
		if len(errormessage) > 0:
			return render_template("add_restaurant.html", errormessage=errormessage, days=days_of_the_week)

		opening_times = {}
		for day in days_of_the_week:
			key = days_of_the_week.index(day)
			status = request.form["closed_" + day]
			if status == "closed":
				opening_times[key] = ("kiinni", "kiinni")
			elif status == "open":
				opening = request.form["opening_" + day]
				closing = request.form["closing_" + day]
				opening_times[key] = (opening, closing)

		if restaurants.add_restaurant(name, description, address, opening_times):
			return redirect("/")
		else:
			return render_template("add_restaurant.html", errormessage="Lisääminen ei onnistu. Onhan ravintolalla oikea osoite?", days=days_of_the_week)

@app.route("/removerestaurant", methods=["GET","POST"])
def remove_restaurant():
	if not users.is_admin():
		return render_template("forbidden.html", message="Sinulla ei ole oikeutta nähdä tätä sivua")
	if request.method == "GET":
		restaurantnames = restaurants.get_list()
		return render_template("remove_restaurant.html", restaurants=restaurantnames)
	if request.method == "POST":
		restaurant_id = request.form["restaurant_to_be_removed"]
		restaurants.remove_restaurant(restaurant_id)
		return redirect("/")

@app.route("/restaurant/<int:id>", methods=["GET","POST"])
def restaurant(id):
	info = restaurants.get_info(id)
	reviews_list = reviews.get_list(id)
	if request.method == "POST":
		if "lisays" in request.form:
			stars = int(request.form["stars"])
			comment = request.form["comment"]
			if len(comment) > 500:
				return render_template("restaurant.html", errormessage="Arvostelun tulee olla alle 500 merkkiä", info=info[0], open=info[1], id=id, reviews=reviews_list)
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
	restaurant_list = restaurants.get_list_based_on_reviews()
	return render_template("restaurantlist.html", restaurants=restaurant_list)

@app.route("/search", methods=["GET"])
def search():
	query = request.args["query"]
	restaurant_list = restaurants.search(query)
	return render_template("restaurantlist.html", restaurants=restaurant_list)

@app.route("/tagsearch", methods=["GET"])
def tagsearch():
	tag = request.args["tag_list"]
	restaurant_list = tags.searchtag(tag)
	return render_template("restaurantlist.html", restaurants=restaurant_list)

@app.route("/tags", methods=["GET","POST"])
def tagging():
	if not users.is_admin():
		return render_template("forbidden.html", message="Sinulla ei ole oikeutta nähdä tätä sivua")
	restaurants_list = restaurants.get_list()
	tags_list = tags.get_tags()
	if request.method == "GET":	
		return render_template("tags.html", tags=tags_list, restaurants=restaurants_list)
	if request.method == "POST":
		written_tag = request.form["tag"]
		list_tag = request.form["existing_tag"]
		if is_empty(written_tag) and is_empty(list_tag):
			return render_template("tags.html", errormessage="Et lisännyt tägiä", tags=tags_list, restaurants=restaurants_list)
		elif not is_empty(written_tag) and not is_empty(list_tag):
			return render_template("tags.html", errormessage="Lisää yksi tägi kerrallaan", tags=tags_list, restaurants=restaurants_list)
		else:
			tag_to_be_added = ""
			if is_empty(written_tag):
				tag_to_be_added = list_tag
			else:
				tag_to_be_added = written_tag
			if len(tag_to_be_added) > 50:
				return render_template("tags.html", errormessage="Tägi on liian pitkä. Sen tulee olla alle 50 merkkiä", tags=tags_list, restaurants=restaurants_list) 
			if "selected_restaurants" in request.form:
				restaurants_to_be_added = request.form.getlist("selected_restaurants")
				tags.add_tags(restaurants_to_be_added, tag_to_be_added)
			else:
				return render_template("tags.html", errormessage="Et antanut ravintoloita", tags=tags_list, restaurants=restaurants_list)
		return redirect("/")

def is_empty(word):
	return len(word) == 0