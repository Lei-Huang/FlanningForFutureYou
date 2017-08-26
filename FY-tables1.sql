DROP TABLE IF EXISTS UserEvent CASCADE;
DROP TABLE IF EXISTS UserProfile CASCADE;
DROP TABLE IF EXISTS UserMilestone CASCADE;
DROP TABLE IF EXISTS Badge CASCADE;
DROP TABLE IF EXISTS BadgeInfo CASCADE;
DROP TABLE IF EXISTS Incentive CASCADE;
DROP TABLE IF EXISTS Points CASCADE;
DROP TABLE IF EXISTS MainEvent CASCADE;
DROP TABLE IF EXISTS Student CASCADE;
DROP TABLE IF EXISTS Staff CASCADE;



create TABLE Student
(ID varchar (20) PRIMARY KEY,
 FirstName varchar(50) NOT NULL,
 LastName varchar(50) NOT NULL,
 Major varchar(100) NOT NULL,
 DOB varchar(20) NOT NULL,
 Email varchar(100) check(Email like '%@%.com'),
 PhoneNo varchar(20),
 Nationality varchar(100),
 GraduateDate varchar(20),
 StudentType varchar(20),
 YearOfStudy varchar(20)
);


create table BadgeInfo
( ID varchar(20) primary key,
  BadgeName varchar(20),
  Description varchar(100),
  Relation varchar(100),
  Imageurl varchar(200)
);


create table Badge 
( ID varchar(20) primary key,
  BadgeStatus varchar(20),
  BadgeInfoID varchar(20),
  foreign key (BadgeInfoID) references BadgeInfo(ID)
);

create table Incentive
( ID varchar(20) primary key,
  IncentiveType varchar(20),
  Description varchar(100)
);


create table Points
( ID varchar(20) primary key,
  CurrentPoints varchar(100)
);


create TABLE UserMilestone 
( StudentID VARCHAR (20) primary KEY,
  BadgeID varchar (20),
  IncentiveID varchar(20),
  PointID varchar(20),
  foreign key (StudentID) references Student(ID),
  foreign key (BadgeID) references Badge(ID),
  foreign key (IncentiveID) references Incentive(ID),
  foreign key (PointID) references Points(ID)
);


CREATE TABLE MainEvent(
EventID VARCHAR(20) PRIMARY KEY,
EventType VARCHAR(20) Not NULL,
EventDate VARCHAR(20) Not NULL,
EventContent VARCHAR(20) Not NULL
);

CREATE TABLE UserEvent(
StudentID VARCHAR(20),
UserEventID VARCHAR(20),
UserEventType VARCHAR(20) Not NULL,
UserEventDate VARCHAR(20) Not NULL,
UserEventContent VARCHAR(20) Not NULL,
PRIMARY KEY (StudentID, UserEventID),
FOREIGN KEY (UserEventID) REFERENCES MainEvent(EventID)
);


CREATE TABLE UserProfile(
StudentID VARCHAR(20),
ProfileYear VARCHAR(5),
ProfileType VARCHAR(20) Not NULL,
NetworkTree VARCHAR(30) Not NULL DEFAULT '0',
SkillTree VARCHAR(30) Not NULL DEFAULT '0',
ExperienceTree VARCHAR(30) Not NULL DEFAULT '0',
PreparationTree VARCHAR(30) Not NULL DEFAULT '0',
Network VARCHAR(1000),
Skill VARCHAR(1000),
Experience VARCHAR(1000),
Preparation VARCHAR(1000),
Notes VARCHAR(1000),
PRIMARY KEY(StudentID, ProfileYear),
FOREIGN KEY (StudentID) REFERENCES Student(ID)
);


create table Staff
( ID varchar(20) primary key,
  StaffType varchar(20),
  FirstName varchar(50) NOT NULL,
  LastName varchar(50) NOT NULL,
  Email varchar(100) check(Email like '%@%.com'),
  PhoneNo varchar(20),
  Optiondate Date,
  StudentID varchar (20),
  UserProfileYear varchar (5),
  MainEventID varchar(20) not null,
  UserEventID varchar(20) not null,
  foreign key (StudentID) references Student(ID),
  foreign key (MainEventID) references MainEvent(EventID),
  foreign key (UserEventID) references UserEvent(UserEventID),
  foreign key (UserProfileYear) references UserProfile(ProfileYear)
);