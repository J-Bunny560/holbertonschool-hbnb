-- Create and use the specified database
CREATE DATABASE IF NOT EXISTS hbnb_part3_db;
USE hbnb_part3_db;
DROP TABLE IF EXISTS `place_amenity`;
DROP TABLE IF EXISTS `reviews`;
DROP TABLE IF EXISTS `amenities`;
DROP TABLE IF EXISTS `places`;
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
    id CHAR(36) PRIMARY KEY NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    is_admin BOOL DEFAULT FALSE
);
CREATE TABLE `places` (
    id CHAR(36) PRIMARY KEY NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    owner_id CHAR(36) NOT NULL, 
    FOREIGN KEY (owner_id) REFERENCES users(id)
);
CREATE TABLE `reviews` (
    id CHAR(36) PRIMARY KEY NOT NULL,
    `text` TEXT NOT NULL,
    rating INT NOT NULL CHECK (rating >= 1 AND rating <= 5),
    user_id CHAR(36) NOT NULL,
    place_id CHAR(36) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (place_id) REFERENCES places(id),
    CONSTRAINT UC UNIQUE (user_id, place_id)
);
CREATE TABLE `amenities` (
    id CHAR(36) PRIMARY KEY NOT NULL,
    name VARCHAR(255) UNIQUE NOT NULL
);
CREATE TABLE `place_amenity` (
    place_id CHAR(36) NOT NULL,
    amenity_id CHAR(36) NOT NULL,
    PRIMARY KEY (place_id, amenity_id),
    FOREIGN KEY (place_id) REFERENCES places(id),
    FOREIGN KEY (amenity_id) REFERENCES amenities(id)
);


-- Insert Initial Data into the tables
INSERT INTO users (id, email, first_name, last_name, password, is_admin)
VALUES (
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1',
    'admin@hbnb.io',
    'Admin',
    'HBnB',
    '5319c237fd4e9e3896ebac929552c4e8',
    1
),
(
    '46c9050e-ddd3-4c3b-9731-9f487208bbc1',
    'notadmin@hbnb.ii',
    'Notadmin',
    'HBnB',
    '5319c237fd4e9e3896ebac929552c4e8',
    0
);
INSERT INTO amenities (id, name)
VALUES 
("a0d0ccf7-ee4e-4a33-879b-34a16d398c1b", "WiFi"),
("b0d0ccf7-ee4e-4a33-879b-34a16d398c1b", "Swimming Pool"),
("c0d0ccf7-ee4e-4a33-879b-34a16d398c1b", "Air Conditioning");
SELECT * FROM amenities;

-- Delete a value
DELETE FROM amenities WHERE name="WiFi";
SELECT * FROM amenities;

-- Try to update a user's email to one that's already in (unique constraint test)
-- Uncomment to test dupes
-- UPDATE users SET email = "admin@hbnb.io" WHERE id = '46c9050e-ddd3-4c3b-9731-9f487208bbc1';
SELECT * FROM users;

-- update a value to a value that was previously taken to test integrity
UPDATE amenities
SET id = "a0d0ccf7-ee4e-4a33-879b-34a16d398c1b"
WHERE id = "b0d0ccf7-ee4e-4a33-879b-34a16d398c1b";


SELECT * FROM amenities;
