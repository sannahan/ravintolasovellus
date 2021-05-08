from werkzeug.security import check_password_hash, generate_password_hash
from flask import session
from db import db
import secrets

def login(username, password):
	sql = "SELECT username, password, role, id FROM users WHERE username=:username"
	result = db.session.execute(sql, {"username":username})
	user = result.fetchone()
	if user == None:
		return False
	else:
		if check_password_hash(user[1], password):
			session["username"] = user[0]
			session["userrole"] = user[2]
			session["user_id"] = user[3]
			session["csrf_token"] = secrets.token_hex(16)
			return True
		else:
			return False

def signup(username, password, role):
	hash_value = generate_password_hash(password)
	try:
		sql = "INSERT INTO users (username, password, role) VALUES (:username, :password, :role)"
		db.session.execute(sql, {"username":username, "password":hash_value, "role":role})
		db.session.commit()
	except:
		return False
	return login(username, password)

def logout():
	del session["username"]
	del session["userrole"]
	del session["user_id"]
	del session["csrf_token"]

def get_id():
	return session.get("user_id")

def get_csrf():
	return session.get("csrf_token")

def is_admin():
	return session.get("userrole") == 2
