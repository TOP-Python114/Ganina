-- Объединение таблиц использовано в следующих файлах. Здесь попробовала с where.

-- 1. Вывести все возможные пары строк преподавателей и групп.

SELECT t.`Name` AS 'Name', t.`Surname` AS 'Surame', g.`Name` AS 'NameGroup'
FROM `Lectures` AS l, `Teachers` AS t, `Groups` AS g, `Groupslectures` AS gl
WHERE l.`Id` = gl.`LectureID` AND t.`Id` = l.`TeacherID` AND g.`Id` = gl.`GroupID`


-- 2.	Вывести названия факультетов, фонд финансирования кафедр которых превышает фонд финансирования факультета.

SELECT f.`Name` AS 'FacultName', d.`Financing` AS 'FinancingD', f.`Financing` AS 'FinancingF'
FROM `Departments` AS d, `Faculties` AS f
WHERE f.`Id` = d.`FacultyID` AND d.`Financing` > f.`Financing`


-- 3. Вывести фамилии кураторов групп и названия групп, которые они курируют

SELECT c.`Name` AS 'NameCurator', c.`Surname`  AS 'SurameCurator', g.`Name` AS 'NameGroup'
FROM `Curators` AS c, `Groups` AS g, `Groupscurators` AS gc
WHERE c.`Id` = gc.`CuratorID` AND g.`Id` = gc.`GroupID`


--  4. Вывести имена и фамилии преподавателей, которые читают лекции у группы “B010”.

SELECT t.`Name` AS 'Name', t.`Surname` AS 'Surame', g.`Name` AS 'NameGroup'
FROM `Lectures` AS l, `Teachers` AS t, `Groups` AS g, `Groupslectures` AS gl
WHERE l.`Id` = gl.`LectureID` AND t.`Id` = l.`TeacherID` AND g.`Id` = gl.`GroupID`AND g.Name = 'B010'


--  5. Вывести фамилии преподавателей и названия факультетов, на которых они читают лекции.

SELECT 
    t.`Name` AS 'Name',
    t.`Surname` AS 'Surame',
    f.`Name` AS 'FacultName'
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
        
        
-- 6. Вывести названия кафедр и названия групп, которые к ним относятся.

SELECT g.`Name` AS 'NameGr', d.`Name` AS 'NameDep'
FROM `Groups` AS g, `Departments` AS d, `Faculties` AS f
WHERE f.`Id` = d.`FacultyID` AND d.`Id` = g.`DepartmentID`


-- 7. Вывести названия дисциплин, которые читает преподаватель “ Lareina Bauer ”.

SELECT s.`Name` AS 'NameSubj', t.`Name` AS 'Name', t.`Surname`  AS 'Surame'
FROM `Lectures` AS l, `Teachers` AS t, `Subjects` AS s
WHERE t.`Id` = l.`TeacherID` AND s.`Id` = l.`SubjectID` AND t.`Name` = 'Lareina' AND t.`Surname` = 'Bauer'


-- 8. Вывести названия кафедр, на которых читается дисциплина “ Medicine ”.

SELECT 
    s.`Name` AS 'NameSubj', d.`Name` AS 'NameDep'
FROM
    `Departments` AS d,
    `Subjects` AS s,
    `Lectures` AS l,
    `Groupslectures` AS gl,
    `Groups` AS g
WHERE
    s.`Id` = l.`SubjectId`
        AND l.`Id` = gl.`LectureID`
        AND g.`Id` = gl.`GroupID`
        AND d.`Id` = g.`DepartmentID`
        AND s.`Name` = 'Medicine'


-- 9. Вывести названия групп, которые относятся к факультету 'Faculty of Arts'.

SELECT g.`Name` AS 'NameGr', f.`Name` AS 'FacultName'
FROM `Groups` AS g, `Faculties` AS f, `Departments` AS d
WHERE d.`Id` = g.`DepartmentID` AND f.`Id` = d.`FacultyID` AND f.`Name` = 'Faculty of Arts'


-- 10. Вывести названия групп 5-го курса, а также название факультетов, к которым они относятся. 

SELECT g.`Name` AS 'NameGr', f.`Name` AS 'FacultName'
FROM `Groups` AS g, `Faculties` AS f, `Departments` AS d
WHERE d.`Id` = g.`DepartmentID` AND f.`Id` = d.`FacultyID` AND g.`Year` = '5'


-- 11. Вывести полные имена преподавателей и лекции, которые они читают (названия дисциплин и групп), 
-- причем отобрать только те лекции, которые читаются в аудитории “58”

SELECT s.`Name` AS 'NameSubj', t.`Name` AS 'Name', t.`Surname` AS 'Surame', l.`LectureRoom` AS 'NumRoom'
FROM `Lectures` AS l, `Teachers` AS t, `Subjects` AS s
WHERE t.`Id` = l.`TeacherID` AND s.`Id` = l.`SubjectID` AND l.`LectureRoom` = '58'
        