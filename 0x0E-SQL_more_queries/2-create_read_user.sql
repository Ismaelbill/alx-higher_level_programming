-- script that creates the database hbtn_0d_2 and the user user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'user_0d_2'@'localhost';
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
USE hbtn_0d_2;
