drop database if exists `orders`;

create database if not exists `orders`;

use orders;

create table if not exists `Sellers` (
	`Id` mediumint unsigned not null auto_increment,
    `Name` varchar(50) not null,
    `MiddleName` varchar(50) not null,
    `Surname` varchar(50) not null,
	`Email` varchar(50) not null,
    `Telephone` varchar(20) unique not null,
    constraint `PK_id` primary key(`id`)
);

create table if not exists `Buyers` (
	`Id` mediumint unsigned not null auto_increment,
    `Name` varchar(50) not null,
    `MiddleName` varchar(50) not null,
    `Surname` varchar(50) not null,
	`Email` varchar(50) not null,
    `Telephone` varchar(20) unique not null,
    constraint `PK_id` primary key(`id`)
);

create table if not exists `Sales` (
	`id` int unsigned not null auto_increment,
    `SellersId` mediumint unsigned not null,
    `BuyersId` mediumint unsigned not null,
    `NameGoods` varchar(50) not null,
    `Price` decimal(10, 2) not null,
    `Date` date not null,
    constraint `PK_id` primary key(`id`)
);

alter table `Sales` 
	add constraint `FK_Sales_SellersId` foreign key(`SellersId`) 
								  references `Sellers`(`id`),
	add constraint `FK_Buyers_BuyersId` foreign key(`BuyersId`) 
								references `Buyers`(`id`);
                                