from db import db
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my_test_app")

def add_restaurant(name, description, address, opening, closing):
	sql = "INSERT INTO restaurants (name, description, address, opening, closing) VALUES (:name, :description, :address, :opening, :closing)"
	db.session.execute(sql, {"name":name, "description":description, "address":address, "opening":opening, "closing":closing})
	db.session.commit()

def get_info_for_map():
	sql = "SELECT name, address FROM restaurants"
	result = db.session.execute(sql)
	addresses = result.fetchall()
	coordinates = []
	for address in addresses:
		location = geolocator.geocode(address[1])
		coordinates.append([address[0], location.latitude, location.longitude])
	return coordinates

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
