-- 1. Вывести количество преподавателей кафедры 'Department of Philosophy'. 

SELECT 
    COUNT(`teachers`.`id`)
FROM
    `teachers`
        JOIN
    `lectures` ON `lectures`.`TeacherId` = `teachers`.`id`
        JOIN
    `groupslectures` ON `groupslectures`.`LectureId` = `lectures`.`id`
        JOIN
    `groups` ON `groupslectures`.`GroupId` = `groups`.`id`
        JOIN
    `departments` ON `groups`.`DepartmentId` = `departments`.`id`
WHERE
    `departments`.`Name` = 'Department of Philosophy'
    
    
-- 2. Вывести количество лекций, которые читает преподаватель “Dave McQueen”. 

SELECT COUNT(`lectures`.`id`)
FROM `teachers`
        JOIN `lectures` 
        ON `lectures`.`TeacherId` = `teachers`.`id`
WHERE
    `teachers`.`Name` = 'Lareina'
    
    
-- 3.	Вывести количество занятий, проводимых в аудитории “58”.

SELECT COUNT(`lectures`.`LectureRoom`) FROM `lectures`
WHERE `lectures`.`LectureRoom` = '58'


-- 4.	Вывести названия аудиторий и количество лекций, проводимых в них. 

SELECT  `lectures`.`LectureRoom`  AS 'Room', count(*) AS 'Num_lect'
FROM `lectures`
GROUP BY `lectures`.`LectureRoom`


-- 5.	Вывести количество студентов, посещающих лекции преподавателя “Jack Underhill”. 

SELECT COUNT(`students`.`id`)
FROM `students`
	JOIN `groupsstudents` 
		ON `groupsstudents`.`StudentId` = `students`.`id`
	JOIN `groupslectures` 
		ON `groupslectures`.`GroupId` = `groupsstudents`.`id`
	JOIN `lectures` 
		ON `lectures`.`id` = `groupslectures`.`LectureId`
	JOIN `teachers`
		ON `lectures`.`TeacherId` = `teachers`.`id`
WHERE
    `teachers`.`Name` = 'Lareina' AND `teachers`.`Surname` = 'Bauer'
    
    
-- 6.	Вывести среднюю ставку преподавателей факультета “ Faculty of Arts”. 

SELECT 
    AVG(t.`Salary`)
FROM
    `Lectures` AS l,
    `Teachers` AS t,
    `Groups` AS g,
    `Groupslectures` AS gl,
    `Departments` AS d,
    `Faculties` AS f
WHERE
    t.`Id` = l.`TeacherID`
        AND l.`Id` = gl.`LectureID`
        AND g.`Id` = gl.`GroupID`
        AND d.`Id` = g.`DepartmentID`
        AND f.`Id` = d.`FacultyID`
        AND f.`Name` = 'Faculty of Arts'
        
        
-- 7.	Вывести минимальное и максимальное количество студентов среди всех групп. 

SELECT 
    MIN(Num), MAX(Num)
FROM
    (SELECT 
        `groups`.`Name`, COUNT(`students`.`id`) AS 'Num'
    FROM
        `students`
    JOIN `groupsstudents` ON `groupsstudents`.`StudentId` = `students`.`id`
    JOIN `groups` ON `groupsstudents`.`GroupId` = `groups`.`id`
    GROUP BY `groups`.`Name`) AS `num_students`
    
    
-- 8. Вывести средний фонд финансирования кафедр

SELECT AVG(`Financing`) FROM `departments`


--  9. Вывести полные имена преподавателей и количество читаемых ими дисциплин.

SELECT `Name`, `Surname`, COUNT(*) AS 'NUM_Subj' 
FROM `teachers`
JOIN `lectures`
  ON `lectures`.`TeacherId` = `teachers`.`id`
GROUP BY `SubjectId` 


--  10. Вывести количество лекций в каждый день недели. 

SELECT DAYNAME(`Date`) as 'Dayname',  COUNT(*) AS 'Num_lect'
FROM `lectures`
GROUP BY `Dayname`


--  11. Вывести номера аудиторий и количество кафедр, чьи лекции в них читаются.

SELECT `LectureRoom` AS 'Room', `departments`.`Name`, COUNT(`departments`.`id`) AS 'NUM'
FROM `lectures`
	JOIN `groupslectures`
	  ON `groupslectures`.`LectureId` = `lectures`.`id`
	JOIN `groups`
	  ON `groups`.`id` = `groupslectures`.`GroupId`
	JOIN `departments`
	  ON `departments`.`id` = `groups`.`DepartmentId`
GROUP BY `LectureRoom`


--   12. Вывести названия факультетов и количество дисциплин, которые на них читаются. 

SELECT `faculties`.`Name`, COUNT(`SubjectId`) AS 'NUM'
FROM `faculties`
	JOIN `departments`
	  ON `faculties`.`id` = `departments`.`FacultyId`
	JOIN `groups`
	  ON `departments`.`id` = `groups`.`DepartmentId` 
	JOIN `groupslectures`
	  ON `groups`.`id` = `groupslectures`.`GroupId`
	JOIN `lectures`
	  ON `lectures`.`id` = `groupslectures`.`LectureId`
	JOIN `subjects`
	  ON `subjects`.`id` = `lectures`.`SubjectId`
GROUP BY `faculties`.`Name`


--   13. Вывести количество лекций для каждой пары преподаватель-аудитория.

SELECT `lectures`.`TeacherId`, `lectures`.`LectureRoom`, COUNT(`id`) AS 'NUM'
FROM `lectures`
GROUP BY `lectures`.`TeacherId`    
