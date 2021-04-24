from db import db
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my_test_app")

def add_restaurant(name, description, address, opening, closing, days):
	try:
		# testing to see if address is valid
		location = geolocator.geocode(address)
		if location == None:
			return False

		sql = "INSERT INTO restaurants (name, description, address, visible) VALUES (:name, :description, :address, 1) RETURNING id"
		result = db.session.execute(sql, {"name":name, "description":description, "address":address})
		restaurant_id = result.fetchone()[0]
		for day in days:
			sql = "INSERT INTO opening_times (restaurant_id, day, opening, closing) VALUES (:restaurant_id, :day, :opening, :closing)"
			db.session.execute(sql, {"restaurant_id":restaurant_id, "day":day, "opening":opening, "closing":closing})
		db.session.commit()
		return True
	except:
		return False

def get_info_for_map():
	sql = "SELECT id, name, address, description FROM restaurants WHERE visible=1"
	result = db.session.execute(sql)
	restaurants = result.fetchall()
	info_for_map = []
	for restaurant in restaurants:
		location = geolocator.geocode(restaurant[2])
		info_for_map.append([restaurant[0], restaurant[1], location.latitude, location.longitude, restaurant[3]])
	return info_for_map

def get_info(id):
	return get_restaurant_details(id), get_opening_times(id)

def get_restaurant_details(id):
	sql = "SELECT name, description, address FROM restaurants WHERE id=:id AND visible=1"
	result = db.session.execute(sql, {"id":id})
	restaurant_details = result.fetchone()
	return restaurant_details

def get_opening_times(id):
	sql = "SELECT day, opening, closing FROM opening_times WHERE restaurant_id=:id"
	result = db.session.execute(sql, {"id":id})
	opening_times = result.fetchall()
	days_of_the_week = ["Oletus", "Ma", "Ti", "Ke", "To", "Pe", "La", "Su"]
	open = []
	for o in opening_times:
		open.append([days_of_the_week[o[0]], o[1], o[2]])
	return open

def get_list():
	sql = "SELECT name, id FROM restaurants WHERE visible=1"
	result = db.session.execute(sql)
	restaurant_list = result.fetchall()
	return restaurant_list

def remove_restaurant(id):
	sql = "UPDATE restaurants SET visible=0 WHERE id=:id"
	db.session.execute(sql, {"id":id})
	db.session.commit()

def search(query):
	sql = "SELECT name, id FROM restaurants WHERE description LIKE :query AND visible=1"
	result = db.session.execute(sql, {"query":"%"+query+"%"})
	restaurant_list = result.fetchall()
	return restaurant_list
