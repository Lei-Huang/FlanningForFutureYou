INSERT INTO Student
(ID,FirstName,LastName,Major,DOB,Email,PhoneNo,Nationality ,GraduateDate,StudentType,YearOfStudy) VALUES
('u123456', 'Wei', 'Wei','CS','29/02/02','qwer@gmail.com','0407098477','American','31/07/18','Current','1');
INSERT INTO Student
(ID,FirstName,LastName,Major,DOB,Email,PhoneNo,Nationality ,GraduateDate,StudentType,YearOfStudy) VALUES
('u123321', 'Mei', 'Wei','CS','22/02/03','asdf@gmail.com','0402432423','Chinese','31/07/18','Current','1');
INSERT INTO Student
(ID,FirstName,LastName,Major,DOB,Email,PhoneNo,Nationality ,GraduateDate,StudentType,YearOfStudy) VALUES
('u221133', 'Uei', 'Wei','CS','20/05/01','zxcv@gmail.com','0422829929','Australian','31/07/18','Current','1');


INSERT INTO Badgeinfo
(ID,BadgeName,Description,relation,imageurl) VALUES
('101','GainIntern','acquire the internship once','Point','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFTyhmxWJlG3tLCxSNUcUjoy64HfSnXY05MN5GBUaBvAPGIaXh');
INSERT INTO Badgeinfo
(ID,BadgeName,Description,relation,imageurl) VALUES
('110','FinishCV','user complete their resume','Badge','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwcfm_LxbmfqlyaOBg233JJy1GKm-y1s_ZasS9UXWSH2PjLxuqiw');


INSERT INTO Badge
(ID,BadgeStatus,BadgeInfoID) VALUES ('starOne', '1010', '101');
INSERT INTO Badge
(ID,BadgeStatus,BadgeInfoID) VALUES ('starTwo', '0101', '110');


INSERT INTO Incentive
(ID,IncentiveType,Description) VALUES ('incentiveOne', 'Badge', 'HelloWorld');
INSERT INTO Incentive
(ID,IncentiveType,Description) VALUES ('incentiveTwo', 'Point', 'GoodByeWorld');


INSERT INTO Points
(ID,CurrentPoints) VALUES ('pointOne', '27');
INSERT INTO Points
(ID,CurrentPoints) VALUES ('pointTwo', '72');


INSERT INTO UserMilestone
(StudentID,BadgeID,IncentiveID,PointID) VALUES ('u123456', 'starOne', 'incentiveOne', 'pointOne');
INSERT INTO UserMilestone
(StudentID,BadgeID,IncentiveID,PointID) VALUES ('u123321', 'starOne', 'incentiveTwo', 'pointTwo');
INSERT INTO UserMilestone
(StudentID,BadgeID,IncentiveID,PointID) VALUES ('u221133', 'starTwo', 'incentiveOne', 'pointTwo');


INSERT INTO MainEvent
(EventID,EventType,EventDate,EventContent) VALUES ('eventOne', 'typeOne', '21/02/10', 'Hello');
INSERT INTO MainEvent
(EventID,EventType,EventDate,EventContent) VALUES ('eventTwo', 'typeTwo', '12/07/10', 'Bye');


INSERT INTO UserEvent
(StudentID,UserEventID,UserEventType,UserEventDate,UserEventContent) VALUES ('u123456', 'eventOne', 'userIncentiveOne', '21/02/10','Thanks');
INSERT INTO UserEvent
(StudentID,UserEventID,UserEventType,UserEventDate,UserEventContent) VALUES ('u123321', 'eventTwo', 'userIncentiveTwo', '12/07/10','Yea');
INSERT INTO UserEvent
(StudentID,UserEventID,UserEventType,UserEventDate,UserEventContent) VALUES ('u221133', 'eventOne', 'userIncentiveOne', '21/07/10','Oooh');


INSERT INTO UserProfile
(StudentID,ProfileYear,ProfileType,NetworkTree,SkillTree,ExperienceTree,PreparationTree,Network,Skill,Experience,Preparation,Notes) 
VALUES ('u123456','year1','userProfileTypeOne','1010','1010','1010','1010','networkDesc','skillDesc','experienceDesc','preparationDesc','notesDesc');
INSERT INTO UserProfile
(StudentID,ProfileYear,ProfileType,NetworkTree,SkillTree,ExperienceTree,PreparationTree,Network,Skill,Experience,Preparation,Notes) 
VALUES ('u123321','year2','userProfileTypeTwo','0101','0101','0101','0101','networkDesc','skillDesc','experienceDesc','preparationDesc','notesDesc');
INSERT INTO UserProfile
(StudentID,ProfileYear,ProfileType,NetworkTree,SkillTree,ExperienceTree,PreparationTree,Network,Skill,Experience,Preparation,Notes) 
VALUES ('u221133','year3','userProfileTypeThree','1010','0101','1010','0101','networkDesc','skillDesc','experienceDesc','preparationDesc','notesDesc');


INSERT INTO Staff
(ID,StaffType,FirstName,LastName,Email,PhoneNo,Optiondate,StudentID,UserProfileYear,MainEventID,UserEventID) 
VALUES ('s1','staff','Tom','Tim','zxcv@cc.com','0407098476','21/02/10','u123456','year1','eventOne','eventOne');
INSERT INTO Staff
(ID,StaffType,FirstName,LastName,Email,PhoneNo,Optiondate,StudentID,UserProfileYear,MainEventID,UserEventID) 
VALUES ('s2','manager','Judy','Law','abcd@cc.com','0406098477','27/07/10','u123321','year2','eventTwo','eventTwo');
INSERT INTO Staff
(ID,StaffType,FirstName,LastName,Email,PhoneNo,Optiondate,StudentID,UserProfileYear,MainEventID,UserEventID) 
VALUES ('s3','admin','Linda','Fox','defg@cc.com','0406098777','21/07/10','u221133','year3','eventTwo','eventOne');