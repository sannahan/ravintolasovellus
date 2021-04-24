CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT UNIQUE, password TEXT);
CREATE TABLE restaurants (id SERIAL PRIMARY KEY, name TEXT, description TEXT, address TEXT, visible INTEGER);
CREATE TABLE reviews (id SERIAL PRIMARY KEY, restaurant_id INTEGER REFERENCES restaurants, stars INTEGER, comment TEXT);
CREATE TABLE opening_times (id SERIAL PRIMARY KEY, restaurant_id INTEGER REFERENCES restaurants, day INTEGER, opening TEXT, closing TEXT);
