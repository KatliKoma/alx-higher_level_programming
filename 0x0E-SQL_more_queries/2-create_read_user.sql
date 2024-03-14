-- Attempt to create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Attempt to create the user if they don't already exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on the hbtn_0d_2 database to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply the changes made by the GRANT statement
FLUSH PRIVILEGES;
