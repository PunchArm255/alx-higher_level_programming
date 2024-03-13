-- creates database hbtn_0d_usa and table states (in the database hbtn_0d_usa) on MySQL server
-- creates a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use a database
USE hbtn_0d_usa;
-- creates a table
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
