-- Create the database if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Select the database to use for subsequent commands
USE hbtn_0d_usa;

-- Create the table if it does not already exist
CREATE TABLE IF NOT EXISTS states (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(256) NOT NULL
);
