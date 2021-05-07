from db import db

def get_tags():
    sql = "SELECT tag FROM tags GROUP BY tag"
    result = db.session.execute(sql)
    return result.fetchall()

def add_tags(restaurants, tag):
    for restaurant in restaurants:
        sql = "INSERT INTO tags (restaurant_id, tag) VALUES (:restaurant_id, :tag)"
        db.session.execute(sql, {"restaurant_id":restaurant, "tag":tag})
    db.session.commit()

def searchtag(tag):
    sql = "SELECT r.name, r.id FROM restaurants AS r, tags AS t WHERE r.id = t.restaurant_id AND r.visible = 1 AND t.tag=:tag"
    result = db.session.execute(sql, {"tag":tag})
    return result.fetchall()
