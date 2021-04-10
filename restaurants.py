from db import db
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my_test_app")

def add_restaurant(name, description, address, opening, closing):
	sql = "INSERT INTO restaurants (name, description, address, opening, closing) VALUES (:name, :description, :address, :opening, :closing)"
	db.session.execute(sql, {"name":name, "description":description, "address":address, "opening":opening, "closing":closing})
	db.session.commit()

def get_coordinates(name):
	sql = "SELECT address FROM restaurants WHERE name=:name"
	result = db.session.execute(sql, {"name":name})
	address = result.fetchone()[0]
	location = geolocator.geocode(address)
	return location.latitude, location.longitude

def get_info(id):
	sql = "SELECT name, description, address, opening, closing FROM restaurants WHERE id=:id"
	result = db.session.execute(sql, {"id":id})
	info = result.fetchone()
	return info

def get_list():
	sql = "SELECT name, id FROM restaurants"
	result = db.session.execute(sql)
	restaurant_list = result.fetchall()
	return restaurant_list
