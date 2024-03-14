--creates the table unique_id
-- creates the table unique_id
   -- unique_id description:
      -- id INT - default value 1, must be unique
      -- name
   -- The database name will be passed as an argument
   -- If the table unique_id already exists.
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
