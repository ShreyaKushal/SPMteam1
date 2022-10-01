create table Role
(	Role_ID	int	primary key,
 	Role_Name	varchar(50) not null
);

create table Staff
(	Staff_ID	int	primary key,
	Staff_Fname	varchar(50)	not null,
 	Staff_Lname varchar(50) not null,
    Department varchar(50) not null,
    Email varchar(50) not null,
constraint Staff_fk foreign key(Role_ID) references Role(Role_ID)
);

create table Courses
(	Course_ID	varchar(50)	primary key,
 	Course_Name	varchar(50)	not null,
 	Course_Desc	varchar(255) not null,
 	Course_Status varchar(15) not null,
    Course_Type varchar(10) not null,
    Course_Category varchar(50) not null
);

create table JobRoles
(	JobRole_ID	varchar(50)	primary key,
 	JobRole_Name varchar(50)	not null
);

create table Skills
(	Skill_ID varchar(50)	primary key,
 	Skill_Name	varchar(50)	not null,
 	Skill_Desc	varchar(255) not null
);

create table JobRoleWithSkills
(JobRole_ID varchar(50) not null,
 Skill_ID varchar(50) not null,
 constraint JobRoleWithSkills_pk primary key(JobRole_ID, Skill_ID),
 constraint JobRoleWithSkills_fk1 foreign key(JobRole_ID) references JobRoles(JobRole_ID),
 constraint JobRoleWithSkills_fk2 foreign key(Skill_ID) references Skills(Skill_ID));

create table SkillsRequiredCourses
(Course_ID varchar(50) not null,
 Skill_ID varchar(50) not null,
 constraint SkillsRequiredCourses_pk primary key(Course_ID, Skill_ID),
 constraint SkillsRequiredCourses_fk1 foreign key(Course_ID) references Courses(Course_ID),
 constraint SkillsRequiredCourses_fk2 foreign key(Skill_ID) references Skills(Skill_ID));

create table LearningJourney
(JobRole_ID varchar(50) not null,
 Skill_ID varchar(50) not null,
 Course_ID varchar(50) not null,
 constraint LearningJourney_pk primary key(JobRole_ID, Skill_ID, Course_ID),
 constraint LearningJourney_fk1 foreign key(JobRole_ID, Skill_ID) references JobRoleWithSkills(JobRole_ID, Skill_ID),
 constraint LearningJourney_fk2 foreign key(Course_ID) references SkillsRequiredCourses(Course_ID));







