CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username VARCHAR UNIQUE,
    password VARCHAR NOT NULL,
    email VARCHAR UNIQUE,
    phone VARCHAR UNIQUE
);

CREATE TABLE cars (
    id INTEGER PRIMARY KEY,
    brand VARCHAR UNIQUE,
    engine VARCHAR,
    model VARCHAR
);

INSERT INTO users (username, password, email, phone) VALUES
    ("admin", "admin", "admin@email.cz", "123456789"),
    ("user", "user", "user@email.cz", "987654321"),
    ("test", "test", "test@email.cz", "555666777");

INSERT INTO cars (brand, engine, model) VALUES
    ("BMW", "M57", "sedan"),
    ("MERCEDES", "M156", "SUV"),
    ("ADUI", "VR6", "hatchback");