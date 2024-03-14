-- Create the database if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Select the database to use for subsequent commands
USE hbtn_0d_usa;

-- Create the states table if it doesn't exist (assuming you may not have run previous scripts)
CREATE TABLE IF NOT EXISTS states (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(256) NOT NULL
);

-- Create the cities table if it does not already exist
CREATE TABLE IF NOT EXISTS cities (
  id INT AUTO_INCREMENT PRIMARY KEY,
  state_id INT NOT NULL,
  name VARCHAR(256) NOT NULL,
  CONSTRAINT fk_state_id FOREIGN KEY (state_id) REFERENCES states(id)
);
