DROP DATABASE IF EXISTS classme;
CREATE DATABASE classme;
USE classme;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
	user_id INTEGER PRIMARY KEY AUTO_INCREMENT,
	first_name VARCHAR(16) NOT NULL,
	last_name VARCHAR(16),
	-- we want unique user names (this is display name)
	user_name VARCHAR(32) UNIQUE NOT NULL,
	-- we want only 1 user for each email
	email VARCHAR(24) UNIQUE NOT NULL
);

ALTER TABLE users AUTO_INCREMENT = 10000;

DROP TABLE IF EXISTS classes;
CREATE TABLE classes (
	class_id INTEGER PRIMARY KEY AUTO_INCREMENT,
	class_name VARCHAR(64) NOT NULL,
	class_section VARCHAR (8) NOT NULL,
	class_year INTEGER NOT NULL,
	class_semester ENUM('fall', 'winter', 'spring', 'summer') NOT NULL
);

ALTER TABLE classes AUTO_INCREMENT=20000;

DROP TABLE IF EXISTS posts;
CREATE TABLE posts (
	post_id INTEGER PRIMARY KEY AUTO_INCREMENT,
	class_id INTEGER NOT NULL,
	user_id INTEGER NOT NULL,
	posted DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	-- NULL if it a post. Else it a reply to a post.
	reply_to INTEGER,
	message VARCHAR (500) NOT NULL,
	FOREIGN KEY (class_id) REFERENCES classes(class_id),
	FOREIGN KEY (user_id) REFERENCES users(user_id)
);

ALTER TABLE posts AUTO_INCREMENT = 30000;

DROP TABLE IF EXISTS login;
CREATE TABLE login (
	user_id INTEGER PRIMARY KEY,
	user_name VARCHAR(32) NOT NULL,
	password VARCHAR(24) NOT NULL,
	FOREIGN KEY (user_id) REFERENCES users(user_id),
	FOREIGN KEY (user_name) REFERENCES users(user_name)
);

DROP TABLE IF EXISTS ischedule;
CREATE TABLE ischedule (
	user_id INTEGER,
	class_id INTEGER,
	UNIQUE KEY (user_id, class_id),
	FOREIGN KEY (user_id) REFERENCES users(user_id),
	FOREIGN KEY (class_id) REFERENCES classes(class_id)
);

DELIMITER $$

CREATE FUNCTION get_user_id_form_user_name(user_name_para VARCHAR(32))
RETURNS INTEGER
DETERMINISTIC
BEGIN
	RETURN (SELECT user_id FROM users WHERE user_name = user_name_para);
END $$

DELIMITER ;

INSERT INTO users VALUES (10001, 'John', 'Moore', 'Johnny', 'john.m@gmail.com');
INSERT INTO users VALUES (10002, 'Kim', 'Gates', 'Kimmy', 'kim.g@gmail.com');

INSERT INTO login VALUES (get_user_id_form_user_name('Johnny'), 'Johnny', 'pass00001');
INSERT INTO login VALUES (get_user_id_form_user_name('Kimmy'), 'Kimmy', 'pass00002');

INSERT INTO classes VALUES (20001, 'CSC 33600 - Database Systems', 'L', '2020', 'spring');

INSERT INTO ischedule VALUES (get_user_id_form_user_name('Johnny'), 20001);
INSERT INTO ischedule VALUES (get_user_id_form_user_name('Kimmy'), 20001);

INSERT INTO posts VALUES (30000, 20001, get_user_id_form_user_name('Johnny'), NOW(), NULL, 'Hello peers. This is the first post');
 
