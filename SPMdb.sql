DROP DATABASE IF EXISTS `spm`; 
CREATE DATABASE IF NOT EXISTS `spm`;
USE `spm`;

create table Role
(	Role_ID			int				primary key,
	Role_Name		varchar(20) 	not null
);

create table Staff
(	Staff_ID		int				primary key,
	Staff_Fname		varchar(50)		not null,
	Staff_Lname 	varchar(50) 	not null,
    Dept 			varchar(50) 	not null,
    Email 			varchar(50) 	not null,
	Role_ID			int 			not null,
	constraint Staff_fk foreign key(Role_ID) references Role(Role_ID)
);
/*
insert into Staff (Staff_ID, Staff_Fname, Staff_Lname, Department, Email, Role_ID) values
(1, "John", "Doe", "HR", "johndoe@gmail.com", "2"),
(2, "Marcus", "Lim", "Staff", "marcuslim@gmail.com", "1"),
(3, "Leo", "Lee", "Staff", "leolee@gmail.com", "1"),
(4, "Alex", "Keng", "HR", "alexkeng@gmail.com", "2"),
(5, "Samantha", "Tan", "Manager", "samanthatan@gmail.com", "3");
*/
create table Courses
(	Course_ID		varchar(20)		primary key,
	Course_Name		varchar(50)		not null,
	Course_Desc		varchar(255),
	Course_Status 	varchar(15),
    Course_Type 	varchar(10),
    Course_Category varchar(50)
);
/*
insert into Courses (Course_ID, Course_Name, Course_Desc, Course_Status, Course_Type, Course_Category) values 
("PY1", "Introduction to Python", "Learning about the basics of Python", "Active", "Technical", "Internal"),
("R1", "Introduction to R", "Learning about the basics of R", "Active", "Technical", "Internal"),
("C3", "Introduction to C++", "Learning about the basics of C++", "Active", "Technical", "Internal"),
("ME4", "Introduction to Microsoft Excel", "Learning about the basics of Microsoft Excel", "Active", "Technical", "External"),
("ST5", "Statistics", "Learning about Statistics", "Active", "Statistics", "External");
*/
create table Registration
(	Reg_ID			int				primary key,
	Course_ID		varchar(20)		not null,
	Staff_ID		varchar(255) 	not null,
	Reg_Status 		varchar(20),
    Completion_Status varchar(20),
	constraint Registration_fk1 foreign key(Course_ID) references Courses(Course_ID),
	constraint Registration_fk2 foreign key(Staff_ID) references Staff(Staff_ID)
);

create table JobRoles
(	JobRole_ID		varchar(50)		primary key,
	JobRole_Name 	varchar(50)		not null,
	JobRole_Status 	varchar(50)
);

insert into JobRoles (JobRole_ID, JobRole_Name, JobRole_Status) values 
("DA1", "Data Analyst", "Active"),
("DS2", "Data Scientist", "Active"),
("BA3", "Business Analyst", "Active"),
("SE4", "Software Engineer", "Active"),
("PM5", "Project Manager", "Active"),
("FM6", "Finance Manager", "Active"),
("SE7", "Sales Executive", "Active"),
("HE8", "Hardware Engineer", "Active");

create table Skills
(	Skill_ID 		varchar(50)		primary key,
	Skill_Name		varchar(50)		not null,
	Skill_Desc		varchar(255) 	not null,
	Skill_Status 	varchar(255) 	not null
);

insert into Skills (Skill_ID, Skill_Name, Skill_Desc, Skill_Status) values
("ST1", "Statistics", "Understand the basics of Statistics", "Active"),
("LE2", "Leadership", "Strong sense of leadership", "Active"),
("PY3", "Python", "Able to code in Python", "Active"),
("C4", "C++", "Able to code in C++", "Active"),
("ME5", "Microsoft Excel", "Able to use Microsoft Excel", "Active"),
("COR6", "Staff Core", "To better unerstand the company", "Active"),
("FN7", "Finance Management", "Able to allocate the company's available funds to meet costs", "Active"),
("ST8", "Software Technology", "Able to operate the company's software effectively", "Active"),
("HT9", "Hardware Technology", "Able to operate the company's hardware effectively", "Active"),
("SA10", "Sales Management", "Able to come up with sales strategies", "Active");

create table JobRoleWithSkills
(	JobRole_ID 		varchar(50) 	not null,
	Skill_ID 		varchar(50) 	not null,
	constraint JobRoleWithSkills_pk primary key(JobRole_ID, Skill_ID),
	constraint JobRoleWithSkills_fk1 foreign key(JobRole_ID) references JobRoles(JobRole_ID),
	constraint JobRoleWithSkills_fk2 foreign key(Skill_ID) references Skills(Skill_ID));

insert into JobRoleWithSkills (JobRole_ID, Skill_ID) values
("DA1", "ST1"),
("DA1", "ME5"),
("DA1", "COR6"),
("DS2", "ME5"),
("DS2", "COR6"),
("BA3", "C4"),
("BA3", "LE2"),
("BA3", "PY3"),
("BA3", "COR6"),
("SE4", "COR6"),
("SE4", "PY3"),
("SE4", "ST8"),
("SE4", "C4"),
("PM5", "LE2"),
("PM5", "ST1"),
("PM5", "ME5"),
("PM5", "COR6"),
("FM6", "FN7"),
("FM6", "LE2"),
("FM6", "ST1"),
("FM6", "COR6"),
("SE7", "COR6"),
("SE7", "FN7"),
("SE7", "SA10"),
("SE7", "ST1"),
("HE8", "COR6"),
("HE8", "HT9");


create table SkillsRequiredCourses
(	Course_ID 			varchar(50) 	not null,
	Skill_ID 			varchar(50) 	not null,
	constraint SkillsRequiredCourses_pk primary key(Course_ID, Skill_ID),
	constraint SkillsRequiredCourses_fk1 foreign key(Course_ID) references Courses(Course_ID),
	constraint SkillsRequiredCourses_fk2 foreign key(Skill_ID) references Skills(Skill_ID));

insert into SkillsRequiredCourses (Course_ID, Skill_ID) values 
-- courses under each skill
("FIN001", "ST1"),
("MGT001", "LE2"),
("MGT002", "LE2"),
("MGT003", "LE2"),
("MGT004", "LE2"),
("MGT007", "LE2"),
("COR004", "LE2"),
("COR006", "LE2"),
("tch018", "LE2"),
("tch019", "LE2"),
("COR001", "COR6"),
("COR002", "COR6"),
("COR004", "COR6"),
("COR006", "COR6"),
("FIN001", "FN7"),
("FIN002", "FN7"),
("FIN003", "FN7"),
("SAL001", "FN7"),
("MGT001", "FN7"),
("MGT002", "FN7"),
("MGT003", "FN7"),
("MGT004", "FN7"),
("tch006", "ST8"),
("tch008", "ST8"),
("tch009", "ST8"),
("tch012", "ST8"),
("tch013", "ST8"),
("tch014", "ST8"),
("tch015", "ST8"),
("tch018", "ST8"),
("tch019", "ST8"),
("tch001", "HT9"),
("tch002", "HT9"),
("tch003", "HT9"),
("tch004", "HT9"),
("tch005", "HT9"),
("tch014", "HT9"),
("SAL001", "SA10"),
("SAL002", "SA10"),
("SAL003", "SA10"),
("SAL004", "SA10");
/* OG
("ST5", "ST1"),
("PY1", "ST1"),
("ME4", "ME5");
*/

/* I edited this */
create table LearningJourney
(	LearningJourney_ID int AUTO_INCREMENT primary key,
	JobRole_ID 			varchar(50) 	not null,
	Skill_ID 			varchar(50) 	not null,
	Course_ID 			varchar(50) 	not null,
	Staff_ID 			int 			not null,
	constraint LearningJourney_fk1 foreign key(JobRole_ID) references JobRoles(JobRole_ID),
	constraint LearningJourney_fk2 foreign key(Skill_ID) references Skills(Skill_ID),
	constraint LearningJourney_fk3 foreign key(Course_ID) references Courses(Course_ID),
	constraint LearningJourney_fk4 foreign key(Staff_ID) references Staff(Staff_ID));

/*
insert into LearningJourney (LearningJourney_ID, JobRole_ID, Skill_ID, Course_ID, Staff_ID) values
(1, "DA1", "ST1", "ST5", 2),
(2, "DA1", "ME5", "ME4", 2);
*/

LOAD DATA LOCAL INFILE 'C:/wamp64/www/is212/SPMteam1/RawData/courses.csv' INTO TABLE Courses
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(Course_ID, Course_Name, Course_Desc, Course_Status, Course_Type, Course_Category);

LOAD DATA LOCAL INFILE 'C:/wamp64/www/is212/SPMteam1/RawData/registration.csv' INTO TABLE Registration
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(Reg_ID, Course_ID, Staff_ID, Reg_Status, Completion_Status);

LOAD DATA LOCAL INFILE 'C:/wamp64/www/is212/SPMteam1/RawData/role.csv' INTO TABLE Role
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(Role_ID, Role_Name);

LOAD DATA LOCAL INFILE 'C:/wamp64/www/is212/SPMteam1/RawData/staff.csv' INTO TABLE Staff
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(Staff_ID, Staff_FName, Staff_LName, Dept, Email, Role_ID);