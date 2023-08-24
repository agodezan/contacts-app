DROP TABLE IF EXISTS persons;

CREATE TABLE persons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL ,
    emailaddress TEXT NOT NULL,
    whatsapp INTEGER NOT NULL
);