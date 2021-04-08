from db import db
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my_test_app")

def add_restaurant(name, description, address):
	sql = "INSERT INTO restaurants (name, description, address) VALUES (:name, :description, :address)"
	db.session.execute(sql, {"name":name, "description":description, "address":address})
	db.session.commit()

def get_coordinates(name):
	sql = "SELECT address FROM restaurants WHERE name=:name"
	result = db.session.execute(sql, {"name":name})
	address = result.fetchone()[0]
	location = geolocator.geocode(address)
	return location.latitude, location.longitude
