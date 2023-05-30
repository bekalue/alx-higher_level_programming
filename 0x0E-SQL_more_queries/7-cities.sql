-- Create a database that doesnot overwrite the pre-existing versions
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- switch to that database
USE hbtn_0d_usa;
-- create a table named cities
CREATE TABLE IF NOT EXISTS cities(
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	UNIQUE(id),
	FOREIGN KEY(state_id) REFERENCES states(id)
	);
