DROP DATABASE IF EXISTS classme;
CREATE DATABASE classme;
USE classme;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
	user_id INTEGER PRIMARY KEY,
	first_name VARCHAR(16) NOT NULL,
	last_name VARCHAR(16),
	-- we want unique user names (this is display name)
	user_name VARCHAR(32) UNIQUE NOT NULL,
	-- we want only 1 user for each email
	email VARCHAR(24) UNIQUE NOT NULL,
);

DROP TABLE IF EXISTS classes;
CREATE TABLE classes (
	class_id INTEGER PRIMARY KEY,
	class_name VARCHAR(64) NOT NULL,
	class_section VARCHAR (8) NOT NULL,
	class_year INTEGER NOT NULL,
	class_semester ENUM('fall', 'winter', 'spring', 'summer') NOT NULL
);

DROP TABLE IF EXISTS posts;
CREATE TABLE posts (
	post_id INTEGER PRIMARY KEY,
	class_id INTEGER NOT NULL,
	user_id INTEGER NOT NULL,
	posted DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	reply_to INTEGER,
	message VARCHAR (500) NOT NULL,
	FOREIGN KEY (class_id) REFERENCES class(class_id),
	FOREIGN KEY (user_id) REFERENCES users(user_id)
);

DROP TABLE IF EXISTS login;
CREATE TABLE login (
	user_id INTEGER PRIMARY KEY,
	user_name VARCHAR(32) NOT NULL,
	password VARCHAR(24) NOT NULL,
	FOREIGN KEY (user_id) REFERENCES users(user_id),
	FOREIGN KEY (user_name) REFERENCES users(user_id)
);

INSERT INTO users VALUES (00001, 'John', 'Moore', 'Johnny', 'john.m@gmail.com');
INSERT INTO users VALUES (00002, 'Kim', 'Gates', 'Kimmy', 'kim.g@gmail.com');

