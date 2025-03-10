CREATE TABLE users (
    id INT PRIMARY KEY,
    username VARCHAR UNIQUE,
    email VARCHAR UNIQUE,
    password VARCHAR NOT NULL
);

INSER INTO users (username, password, email) VALUES ("admin", "admin", "admin@email.cz"),
      ("user", "user", "user@email.cz"),
      ("test", "test", "test@email.cz"),