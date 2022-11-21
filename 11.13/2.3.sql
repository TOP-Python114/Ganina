--   1.	Вывести номера корпусов, если суммарный фонд финансирования расположенных в них кафедр превышает 100000. 

SELECT `Building`
FROM
    (SELECT `Building`, SUM(`Financing`) AS 'Sum_fin'
    FROM `departments`
    GROUP BY `Building`) AS `bild100`
WHERE
    `bild100`.`SumFin` > 100000
    
    
--   2.	Вывести названия групп 5-го курса кафедры “Faculty of Arts”, которые имеют более 10 пар в первую неделю.
 
SELECT `groups`.`Name` AS 'Name_gr', `Date` AS 'Date',  COUNT(`lectures`.`id`) AS 'Lec_num' 
FROM `groups`
	JOIN `departments`
	  ON `departments`.`id` = `groups`.`DepartmentId`
	JOIN `groupslectures`
	  ON `groups`.`id` = `groupslectures`.`GroupId`
	JOIN `lectures`
	  ON `lectures`.`id` = `groupslectures`.`LectureId`
WHERE `groups`.`Year`= '5' AND `departments`.`Name` = 'Faculty of Arts' AND 'Lec_num' > 10
GROUP BY `Name_gr`
ORDER BY `Date` ASC
LIMIT 7


-- 3. Вывести названия групп, имеющих рейтинг (средний рейтинг всех студентов группы) больше, чем рейтинг группы “B002”. 

SELECT `Name_gr`
FROM (SELECT `groups`.`Name` AS 'Name_gr', AVG(`Rating`) AS 'Rat'
		FROM `students`
			JOIN `groupsstudents` ON `students`.`id` = `groupsstudents`.`StudentId`
			JOIN `groups` ON `groups`.`id` = `groupsstudents`.`GroupId`
      GROUP BY `groups`.`Name`) AS `f`
WHERE `Rat` > (SELECT AVG(`Rating`)
			   FROM `students`
                JOIN `groupsstudents` ON `students`.`id` = `groupsstudents`.`StudentId`
                JOIN `groups` ON `groups`.`id` = `groupsstudents`.`GroupId`
			   WHERE `groups`.`Name` = 'B002')


--  4. Вывести фамилии и имена преподавателей, ставка которых выше средней ставки профессоров.

SELECT `Name`, `Surname`, `Salary`
FROM `teachers` AS t
WHERE t.`Salary` > (SELECT AVG(`Salary`)
						FROM `teachers`
						WHERE `IsProfessor` = '1')


--   5. Вывести названия групп, у которых больше одного куратора. 

SELECT `Name` AS 'Name_gr'
FROM
    (SELECT `groups`.`Name`, COUNT(`CuratorId`) AS `NC`
    FROM `groups`
		JOIN `groupscurators` ON `groups`.`id` = `groupscurators`.`GroupId`
    GROUP BY `groups`.`Name`) AS `lot_cur`
WHERE
    `lot_cur`.`NC` > 1


--   6. Вывести названия групп, имеющих рейтинг (средний рейтинг всех студентов группы) меньше или равный, чем минимальный рейтинг групп 5-го курса. 

SELECT `groups`.`Name` AS 'Name_gr', AVG(`Rating`) AS 'Rating_med'
FROM `students`
	JOIN `groupsstudents`
	  ON `students`.`id` = `groupsstudents`.`StudentId`
	JOIN `groups`
	  ON `groups`.`id` = `groupsstudents`.`GroupId`
WHERE `students`.`Rating` <= (SELECT  MIN(`Rating`) 
							  FROM `students`
							  WHERE `Year`='5' 
							  ORDER BY MIN(`Rating`) ASC)
GROUP BY `groups`.`Name`


-- 7. Вывести названия факультетов, суммарный фонд финансирования кафедр которых больше суммарного фонда 
-- финансирования кафедр факультета “ Faculty of Arts”.  (Не придумала как сделать в один запрос)

SELECT f.`Name`, SUM(d.`Financing`) AS 'TFF'
FROM departments AS d
	JOIN `faculties` AS f 
	ON d.`FacultyId` = f.`id`
GROUP BY f.`Name`
HAVING `TFF` > (SELECT SUM(d.`Financing`)
						FROM `departments` AS d
						JOIN `faculties` AS f 
                        ON d.`FacultyId` = f.`id`
						AND f.`Name` = 'Faculty of Arts'
					GROUP BY f.`Name`)


-- 8. Вывести названия дисциплин и полные имена преподавателей, читающих наибольшее количество лекций по ним. 

SELECT 
    `subjects`.`Name` AS 'Name_subj',
    `teachers`.`Name` AS 'Name_teach',
    `teachers`.`Surname` AS 'Sername_teach',
    COUNT(`SubjectId`) AS 'Num_lec'
FROM `lectures`
	JOIN `subjects` ON `subjects`.`id` = `lectures`.`SubjectId`
	JOIN `teachers` ON `teachers`.`id` = `lectures`.`TeacherId`
GROUP BY `SubjectId`
ORDER BY `Num_lec` DESC
LIMIT 5


-- 9. Вывести название дисциплины, по которому читается меньше всего лекций. 

SELECT `Name` AS 'Name', COUNT(`SubjectId`) AS 'Num'
FROM `lectures`
	JOIN `subjects` 
    ON `subjects`.`id` = `lectures`.`SubjectId`
GROUP BY SubjectId
ORDER BY `Num` ASC
LIMIT 1


-- 10. Вывести количество студентов и читаемых дисциплин на кафедре “'Department of Philosophy ”

SELECT 
    COUNT(DISTINCT `Num_Stud`), COUNT(DISTINCT `Num_Lec`)
FROM
    (SELECT 
        `StudentId` AS 'Num_Stud', `LectureId` AS 'Num_Lec'
    FROM `groupsstudents`
		JOIN `groups` ON `groupsstudents`.`GroupId` = `groups`.`id`
		JOIN `departments` ON `groups`.`DepartmentId` = `departments`.`id`
		JOIN `groupslectures` ON `groupslectures`.`GroupId` = `groups`.`id`
		JOIN `lectures` ON `groupslectures`.`LectureId` = `lectures`.`id`
    WHERE
        `departments`.`name` = 'Department of Philosophy') AS `h`  
        