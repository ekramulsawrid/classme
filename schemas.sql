PRAGMA foreign_keys = ON;

CREATE TABLE "classes" (
	"class_id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"class_name"	TEXT NOT NULL,
	"class_section"	TEXT NOT NULL,
	"class_year"	INTEGER NOT NULL,
	"class_semester"	TEXT NOT NULL,
	CHECK(
		typeof("class_name") = "text" AND
		length("class_name") <= 64 AND
		typeof("class_section") = "text" AND
		length("class_section") <=  8 AND
		typeof("class_year") = "integer" AND
		typeof("class_semester") = "text" AND
		length("class_semester") <= 6
	)
);

CREATE TABLE "users" (
	"user_id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"first_name"	TEXT NOT NULL,
	"last_name"	TEXT,
	"user_name"	TEXT NOT NULL,
	"email"		TEXT NOT NULL,
	CHECK(
		typeof("first_name") = "text" AND
		length("first_name") <= 16 AND
		typeof("last_name") = "text" AND
		length("last_name") <= 16 AND
		typeof("user_name") = "text" AND
		length("user_name") <= 32 AND
		typeof("email") = "text" AND
		length("email") <= 32
	)
);

CREATE UNIQUE INDEX PK_user_name ON "users"("user_name");
CREATE UNIQUE INDEX PK_email ON "users"("email");

CREATE TABLE "posts" (
	"post_id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"user_id"	INTEGER NOT NULL,
	"class_id"	INTEGER NOT NULL,
	"posted"	TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"message"	TEXT NOT NULL,
	FOREIGN KEY("user_id", "class_id") REFERENCES "ischedule"("user_id", "class_id"),
	CHECK (
		typeof("message") = "text" AND
		length("message") <= 500
	)
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
	"password"	TEXT NOT NULL,
	PRIMARY KEY("user_id"),
	FOREIGN KEY("user_id") REFERENCES "users"("user_id"),
	CHECK (
		typeof("password") = "text" AND
		length("password") <= 24
	)
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
VALUES (1, 'CSC 33600: Databases', 'L', 2018, 'fall');
INSERT INTO "main"."classes"
("class_id", "class_name", "class_section", "class_year", "class_semester")
VALUES (2, 'CSC 22000: Algorithms', 'C', 2019, 'spring');
INSERT INTO "main"."classes"
("class_id", "class_name", "class_section", "class_year", "class_semester")
VALUES (3, 'MATH 20100: Calculus I', 'B1', 2020, 'fall');

INSERT INTO "main"."ischedule"
("user_id", "class_id")
VALUES(1, 1);
INSERT INTO "main"."ischedule"
("user_id", "class_id")
VALUES(1, 2);
INSERT INTO "main"."ischedule"
("user_id", "class_id")
VALUES(2, 1);
INSERT INTO "main"."ischedule"
("user_id", "class_id")
VALUES(2, 3);
INSERT INTO "main"."ischedule"
("user_id", "class_id")
VALUES(3, 3);

INSERT INTO "main"."posts"
("post_id","user_id", "class_id", "posted", "message")
VALUES (1, 1, 1, "2020-04-19 01:06:18", "Hello everyone. First message here");
INSERT INTO "main"."posts"
("post_id","user_id", "class_id", "posted", "message")
VALUES (2, 2, 1, "2020-04-19 01:08:14", "Hi. I hope we have a good semester.");
INSERT INTO "main"."posts"
("post_id","user_id", "class_id", "posted", "message")
VALUES (3, 1, 1, "2020-04-19 01:14:12", "Yea.");
INSERT INTO "main"."posts"
("post_id","user_id", "class_id", "posted", "message")
VALUES (4, 3, 3, "2020-04-19 01:20:34", "Hello. Is this MATH 20100?");
INSERT INTO "main"."posts"
("post_id","user_id", "class_id", "posted", "message")
VALUES (5, 2, 3, "2020-04-19 01:22:14", "Yes. This is MATH 20100: Calculus I");
INSERT INTO "main"."posts"
("post_id","user_id", "class_id", "posted", "message")
VALUES (6, 3, 3, "2020-04-19 01:22:45", "Thank you.");

INSERT INTO "main"."login"
("user_id", "password")
VALUES(1, "pass123");
INSERT INTO "main"."login"
("user_id", "password")
VALUES(2, "password1");
INSERT INTO "main"."login"
("user_id", "password")
VALUES(3, "12345");




