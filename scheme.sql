CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username VARCHAR UNIQUE,
    password VARCHAR NOT NULL,
    email VARCHAR UNIQUE,
    role VARCHAR NOT NULL,
    phone VARCHAR UNIQUE
);

CREATE TABLE cars (
    id INTEGER PRIMARY KEY,
    brand VARCHAR UNIQUE,
    engine VARCHAR,
    model VARCHAR
);

INSERT INTO users (username, password, email, role, phone) VALUES
    ("admin", "admin", "admin@email.cz", "admin", "123456789"),
    ("user", "user", "user@email.cz", "user", "987654321"),
    ("test", "test", "test@email.cz", "user", "555666777");

INSERT INTO cars (brand, engine, model) VALUES
    ("BMW", "M57", "sedan"),
    ("MERCEDES", "M156", "SUV"),
    ("ADUI", "VR6", "hatchback");