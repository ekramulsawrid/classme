CREATE TABLE "classes" (
	"class_id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"class_name"	VARCHAR(64) NOT NULL,
	"class_section"	VARCHAR(8) NOT NULL,
	"class_year"	INTEGER NOT NULL,
	"class_semester"	VARCHAR(6) NOT NULL
);

CREATE TABLE "users" (
	"user_id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"first_name"	VARCHAR(16) NOT NULL,
	"last_name"	VARCHAR(16),
	"user_name"	VARCHAR(32) NOT NULL UNIQUE,
	"email"	VARCHAR(32) NOT NULL UNIQUE
);

CREATE TABLE "posts" (
	"post_id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"class_id"	INTEGER NOT NULL,
	"user_id"	INTEGER NOT NULL,
	"posted"	TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"reply_to"	INTEGER NOT NULL,
	"message"	VARCHAR(500) NOT NULL,
    FOREIGN KEY("class_id") REFERENCES "classes"("class_id"),
    FOREIGN KEY("user_id") REFERENCES "users"("user_id"),
    FOREIGN KEY("reply_to") REFERENCES "posts"("post_id")

);

CREATE TABLE "ischedule" (
	"user_id"	INTEGER,
	"class_id"	INTEGER,
	PRIMARY KEY("user_id","class_id"),
    FOREIGN KEY("user_id") REFERENCES "users"("user_id"),
    FOREIGN KEY("class_id") REFERENCES "classes"("class_id")
);

CREATE TABLE "login" (
	"user_id"	INTEGER,
	"user_name"	VARCHAR(32) NOT NULL,
	"password"	VARCHAR(24) NOT NULL,
	PRIMARY KEY("user_id"),
	FOREIGN KEY("user_id") REFERENCES "users"("user_id"),
	FOREIGN KEY("user_name") REFERENCES "users"("user_name")
);

INSERT INTO "main"."users"
("user_id", "first_name", "last_name", "user_name", "email")
VALUES(1, 'John', 'Li', 'John1', 'john@gmail.com');
INSERT INTO "main"."users"
("user_id", "first_name", "last_name", "user_name", "email")
VALUES(2, 'Kim', 'Wu', 'Kim1', 'kim@gmail.com');
INSERT INTO "main"."users"
("user_id", "first_name", "last_name", "user_name", "email")
VALUES(3, 'Don', 'Ski', 'Don1', 'don@gmail.com');

INSERT INTO "main"."classes"
("class_id", "class_name", "class_section", "class_year", "class_semester")
VALUES (1, 'CSC 33600: Databases', 'L', 2018, 'Fall');
INSERT INTO "main"."classes"
("class_id", "class_name", "class_section", "class_year", "class_semester")
VALUES (2, 'CSC 22000: Algorithms', 'C', 2019, 'Spring');
INSERT INTO "main"."classes"
("class_id", "class_name", "class_section", "class_year", "class_semester")
VALUES (3, 'SPCH 11100: Speech', 'B1', 2020, 'Fall');


