from db import db

def add_review(restaurant_id, user_id, stars, comment):
	sql = "INSERT INTO reviews (restaurant_id, user_id, stars, comment, visible, sent_at) VALUES (:restaurant_id, :user_id, :stars, :comment, 1, NOW())"
	db.session.execute(sql, {"restaurant_id":restaurant_id, "user_id":user_id, "stars":stars, "comment":comment})
	db.session.commit()

def get_list(id):
	sql = "SELECT R.stars, R.comment, U.username, R.id, R.sent_at FROM reviews AS R, users AS U WHERE R.restaurant_id=:id AND R.user_id=U.id AND R.visible=1 ORDER BY R.id DESC"
	result = db.session.execute(sql, {"id":id})
	return result.fetchall()

def remove_review(id):
	sql = "UPDATE reviews SET visible=0 WHERE id=:id"
	db.session.execute(sql, {"id":id})
	db.session.commit()