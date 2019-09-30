
DROP SCHEMA IF EXISTS MicroShop;
CREATE SCHEMA MicroShop;
USE MicroShop;

DROP TABLE IF EXISTS `Customer`;
CREATE TABLE `Customer`
(
    `id` INT (11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255)
);

DROP TABLE IF EXISTS `Order`;
CREATE TABLE `Order`
(
    `id` INT (11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `date` VARCHAR(255),
    `total` INT(11),
    `customer_id` INT(11)
);

DROP TABLE IF EXISTS `OrderLine`;
CREATE TABLE `OrderLine`
(
    `id` INT (11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `order_id` INT(11),
    `product_id` INT(11),
    `count` INT(11),
    `total` INT(11)
);

DROP TABLE IF EXISTS `Product`;
CREATE TABLE `Product`
(
    `id` INT (11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255),
    `price` INT(11)
);