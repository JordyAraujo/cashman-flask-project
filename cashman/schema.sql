DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS transact;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE transact (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  transaction_type VARCHAR(10) NOT NULL,
  value REAL NOT NULL
);