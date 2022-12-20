CREATE TABLE Students (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  surname TEXT NOT NULL,
  phone TEXT NOT NULL
);

INSERT INTO Students VALUES (0001, 'Clark', 'D', '11');
INSERT INTO Students VALUES (0002, 'Dave', 'G', '22');
INSERT INTO Students VALUES (0003, 'Ava', 'B', '33');

ALTER TABLE Students ADD COLUMN address TEXT NOT NULL;

DESCRIBE Students;
SELECT * FROM Students;