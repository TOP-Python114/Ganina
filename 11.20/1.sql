drop database if exists `phonebook`;

create database if not exists `phonebook`;

use phonebook;

create table if not exists `people` (
	`id` mediumint unsigned not null auto_increment,
    `Name` varchar(50) not null,
    `MiddleName` varchar(50) not null,
    `Surname` varchar(50) not null,
    `BirthDate` date not null,
    `Gender` varchar (1) CHECK (`Gender` in ('F', 'M')),
    `Telephone` varchar(20) unique not null,
    `City` varchar(50) not null,
    `Country` varchar(50) not null,
    `Address` varchar(255) not null,
    constraint `PK_id` primary key(`id`)
);
