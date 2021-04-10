CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT UNIQUE, password TEXT);
CREATE TABLE restaurants (id SERIAL PRIMARY KEY, name TEXT, description TEXT, address TEXT, opening TEXT, closing TEXT);
CREATE TABLE reviews (id SERIAL PRIMARY KEY, restaurant_id INTEGER REFERENCES restaurants, stars INTEGER, comment TEXT);
