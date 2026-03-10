/*
GRANT ALL PRIVILEGES ON `myl`.* TO 'user'@'%' IDENTIFIED BY 'passroot' WITH GRANT OPTION;
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'user'@'%';
*/

DROP DATABASE IF EXISTS myl;

CREATE DATABASE `myl`;

USE `myl`;

CREATE TABLE `cards` (
    id INT PRIMARY KEY,
    name VARCHAR(30),
    attack INT,
    cost INT,
    effect VARCHAR(1000),
    isUnique BOOLEAN,
    imageUrl VARCHAR(250),
    type VARCHAR(10)
);


