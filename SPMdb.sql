DROP DATABASE IF EXISTS `spm`; 
CREATE DATABASE IF NOT EXISTS `spm` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spm`;

create table Role
(	Role_ID	int	primary key,
 	Role_Name	varchar(50) not null
);

insert into Role (Role_ID, Role_Name) values 
(1, "Staff"),
(2, "Human Resource"),
(3, "Manager");

create table Staff
(	Staff_ID	int	primary key,
	Staff_Fname	varchar(50)	not null,
 	Staff_Lname varchar(50) not null,
    Department varchar(50) not null,
	-- Department refers to: Staff, HR, Manager
    Email varchar(50) not null,
	Role_ID int not null,
constraint Staff_fk foreign key(Role_ID) references Role(Role_ID)
);

insert into Staff (Staff_ID, Staff_Fname, Staff_Lname, Department, Email, Role_ID) values
(1, "John", "Doe", "HR", "johndoe@gmail.com", "2"),
(2, "Marcus", "Lim", "Staff", "marcuslim@gmail.com", "1"),
(3, "Leo", "Lee", "Staff", "leolee@gmail.com", "1"),
(4, "Alex", "Keng", "HR", "alexkeng@gmail.com", "2"),
(5, "Samantha", "Tan", "Manager", "samanthatan@gmail.com", "3");

create table Courses
(	Course_ID	varchar(50)	primary key,
 	Course_Name	varchar(50)	not null,
 	Course_Desc	varchar(255) not null,
 	Course_Status varchar(15) not null,
    Course_Type varchar(10) not null,
    Course_Category varchar(50) not null
);

insert into Courses (Course_ID, Course_Name, Course_Desc, Course_Status, Course_Type, Course_Category) values 
("PY1", "Introduction to Python", "Learning about the basics of Python", "Active", "Technical", "Internal"),
("R1", "Introduction to R", "Learning about the basics of R", "Active", "Technical", "Internal"),
("C3", "Introduction to C++", "Learning about the basics of C++", "Active", "Technical", "Internal"),
("ME4", "Introduction to Microsoft Excel", "Learning about the basics of Microsoft Excel", "Active", "Technical", "External"),
("ST5", "Statistics", "Learning about Statistics", "Active", "Statistics", "External");


create table JobRoles
(	JobRole_ID	varchar(50)	primary key,
 	JobRole_Name varchar(50)	not null
);

insert into JobRoles (JobRole_ID, JobRole_Name) values 
("DA1", "Data Analyst"),
("DS2", "Data Scientist"),
("BA3", "Business Analyst"),
("SE4", "Software Engineer"),
("PM5", "Project Manager");

create table Skills
(	Skill_ID varchar(50)	primary key,
 	Skill_Name	varchar(50)	not null,
 	Skill_Desc	varchar(255) not null
);

insert into Skills (Skill_ID, Skill_Name, Skill_Desc) values
("ST1", "Statistics", "Understand the basics of Statistics"),
("LE2", "Leadership", "Strong sense of leadership"),
("PY3", "Python", "Able to code in Python"),
("C4", "C++", "Able to code in C++"),
("ME5", "Microsoft Excel", "Able to use Microsoft Excel");

create table JobRoleWithSkills
(JobRole_ID varchar(50) not null,
 Skill_ID varchar(50) not null,
 constraint JobRoleWithSkills_pk primary key(JobRole_ID, Skill_ID),
 constraint JobRoleWithSkills_fk1 foreign key(JobRole_ID) references JobRoles(JobRole_ID),
 constraint JobRoleWithSkills_fk2 foreign key(Skill_ID) references Skills(Skill_ID));

insert into JobRoleWithSkills (JobRole_ID, Skill_ID) values
("DA1", "ST1"),
("DA1", "ME5"),
("DS2", "ME5");

create table SkillsRequiredCourses
(Course_ID varchar(50) not null,
 Skill_ID varchar(50) not null,
 constraint SkillsRequiredCourses_pk primary key(Course_ID, Skill_ID),
 constraint SkillsRequiredCourses_fk1 foreign key(Course_ID) references Courses(Course_ID),
 constraint SkillsRequiredCourses_fk2 foreign key(Skill_ID) references Skills(Skill_ID));

insert into SkillsRequiredCourses (Course_ID, Skill_ID) values 
-- courses under each skill
("ST5", "ST1"),
("PY1", "ST1"),
("ME4", "ME5");

create table LearningJourney
(LearningJourney_ID int not null,
 JobRole_ID varchar(50) not null,
 Skill_ID varchar(50) not null,
 Course_ID varchar(50) not null,
 constraint LearningJourney_pk primary key(JobRole_ID, Skill_ID, Course_ID),
 constraint LearningJourney_fk1 foreign key(JobRole_ID, Skill_ID) references JobRoleWithSkills(JobRole_ID, Skill_ID),
 constraint LearningJourney_fk2 foreign key(Course_ID) references SkillsRequiredCourses(Course_ID));

insert into LearningJourney (LearningJourney_ID, JobRole_ID, Skill_ID, Course_ID) values
(1, "DA1", "ST1", "ST5"),
(1, "DA1", "ME5", "ME4");