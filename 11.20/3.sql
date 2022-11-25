drop database if exists `musical_collection`;

create database if not exists `musical_collection`;

use musical_collection;

create table if not exists `MusicalDisks` (
    `Id` mediumint unsigned not null auto_increment,
    `NameDisk` varchar(30) not null,
	`ArtistsId` mediumint unsigned not null,
    `DateRelease` date not null,
    `StylesId` smallint unsigned not null,
    `PublishersId` mediumint unsigned not null,
    constraint `PK_id` primary key (`id`)
);

create table if not exists `Styles` (
    `Id` smallint unsigned not null auto_increment,
    `StyleName` varchar(30) not null,
    constraint `PK_id` primary key (`id`)
);

create table if not exists `Artists` (
    `Id` mediumint unsigned not null auto_increment,
    `ArtistName` varchar(50) not null,
    constraint `PK_id` primary key (`id`)
);

create table if not exists `Publishers` (
    `Id` mediumint unsigned not null auto_increment,
    `PublisherName` varchar(50) not null,
    `Сountry` varchar(50) not null,
    constraint `PK_id` primary key (`id`)
);

create table if not exists `Songs` (
    `Id` mediumint unsigned not null auto_increment,
    `SongName` varchar(50) not null,
    `DisksId` mediumint unsigned not null,
    `Duration` time not null,
    `StylesId` smallint unsigned not null,
    `ArtistsId` mediumint unsigned not null,
    constraint `PK_id` primary key (`id`)
);

alter table `MusicalDisks` 
	add constraint `FK_MusicalDisks_ArtistsId` foreign key(`ArtistsId`) 
								  references `Artists`(`id`),
	add constraint `FK_MusicalDisks_StylesId` foreign key(`StylesId`) 
								references `Styles`(`id`),
	add constraint `FK_MusicalDisks_PublishersId` foreign key(`PublishersId`) 
								references `Publishers`(`id`);
                                
alter table `Songs` 
	add constraint `FK_Songs_DisksId` foreign key(`DisksId`) 
								  references `MusicalDisks`(`id`),
	add constraint `FK_Songs_StylesId` foreign key(`StylesId`) 
								references `Styles`(`id`),
	add constraint `FK_Songs_ArtistsId` foreign key(`ArtistsId`) 
								references `Artists`(`id`);
