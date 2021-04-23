from db import db
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my_test_app")

def add_restaurant(name, description, address, opening, closing):
	sql = "INSERT INTO restaurants (name, description, address, opening, closing) VALUES (:name, :description, :address, :opening, :closing)"
	db.session.execute(sql, {"name":name, "description":description, "address":address, "opening":opening, "closing":closing})
	db.session.commit()

def get_info_for_map():
	sql = "SELECT id, name, address, description FROM restaurants"
	result = db.session.execute(sql)
	infos = result.fetchall()
	info_for_map = []
	for info in infos:
		location = geolocator.geocode(info[2])
		info_for_map.append([info[0], info[1], location.latitude, location.longitude, info[3]])
	return info_for_map

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

def remove_restaurant(id):
	sql = "DELETE FROM restaurants WHERE id=:id"
	db.session.execute(sql, {"id":id})
	db.session.commit()
