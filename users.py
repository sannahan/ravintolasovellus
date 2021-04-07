from werkzeug.security import check_password_hash, generate_password_hash
from flask import session
from db import db

def login(username, password):
	sql = "SELECT username, password FROM users WHERE username=:username"
	result = db.session.execute(sql, {"username":username})
	user = result.fetchone()
	if user == None:
		return False
	else:
		if check_password_hash(user[1], password):
			session["username"] = user[0]
			return True
		else:
			return False

def signup(username, password):
	hash_value = generate_password_hash(password)
	try:
		sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
		db.session.execute(sql, {"username":username, "password":hash_value})
		db.session.commit()
	except:
		return False
	return login(username, password)
