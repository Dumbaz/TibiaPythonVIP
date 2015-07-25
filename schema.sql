DROP TABLE IF EXISTS characters;
CREATE TABLE characters ( 
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  sex TEXT NOT NULL,
  vocation TEXT NOT NULL,
  level INTEGER NOT NULL,
  achievement_points INTEGER NOT NULL,
  world TEXT NOT NULL,
  house TEXT,
  last_login DATE NOT NULL,
  comment_id INTEGER,
  account_status TEXT
);

CREATE TABLE comment (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  timestamp DATE NOT NULL,
  content TEXT NOT NULL
  char_id INTEGER NOT NULL
);

