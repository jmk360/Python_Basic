BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username text,     email text, phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'KIM','kim@naver.com','010-0000-0000','www@naver.com','2021-12-13 23:54:23');
INSERT INTO "users" VALUES(2,'Park','Park@daum.net','010-1111-1111','Park.com','2021-12-13 23:54:23');
INSERT INTO "users" VALUES(3,'Lee','Lee@naver.com','010-2222-2222','Lee.com','2021-12-13 23:54:23');
INSERT INTO "users" VALUES(4,'Cho','Cho@daum.net','010-3333-3333','Cho.com','2021-12-13 23:54:23');
INSERT INTO "users" VALUES(5,'Yoo','Yoo@google.com','010-4444-4444','Yoo.net','2021-12-13 23:54:23');
COMMIT;
