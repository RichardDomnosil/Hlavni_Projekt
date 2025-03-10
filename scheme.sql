CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username VARCHAR UNIQUE,
    password VARCHAR NOT NULL,
    email VARCHAR UNIQUE
);

INSERT INTO users (username, password, email) VALUES ("admin", "admin", "admin@email.cz"),
      ("user", "user", "user@email.cz"),
      ("test", "test", "test@email.cz");