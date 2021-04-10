from db import db

def add_review(restaurant_id, stars, comment):
	sql = "INSERT INTO reviews (restaurant_id, stars, comment) VALUES (:restaurant_id, :stars, :comment)"
	db.session.execute(sql, {"restaurant_id":restaurant_id, "stars":stars, "comment":comment})
	db.session.commit()

def get_list(id):
	sql = "SELECT stars, comment FROM reviews WHERE restaurant_id=:id"
	result = db.session.execute(sql, {"id":id})
	return result.fetchall()
