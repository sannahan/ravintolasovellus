CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT UNIQUE, password TEXT);
CREATE TABLE restaurants (id SERIAL PRIMARY KEY, name TEXT, description TEXT, address TEXT);
 
