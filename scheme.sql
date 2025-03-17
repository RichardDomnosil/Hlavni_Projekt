CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username VARCHAR UNIQUE,
    password VARCHAR NOT NULL,
    email VARCHAR UNIQUE,
    phone VARCHAR UNIQUE
);

INSERT INTO users (username, password, email, phone) VALUES
    ("admin", "admin", "admin@email.cz", "123456789"),
    ("user", "user", "user@email.cz", "987654321"),
    ("test", "test", "test@email.cz", "555666777");