DROP PROCEDURE IF EXISTS Medical_Data_Procedure; 
DROP PROCEDURE IF EXISTS NUM_of_diag_Procedure; 
Drop Procedure if exists Hereditary_diseases_Procedure;
Drop Procedure if exists Popular_Medication;
Drop Procedure if exists Area_Diagnosis_Procedure;
Drop Procedure if exists GetDocPatients;
DROP PROCEDURE IF EXISTS getAge; 
DROP FUNCTION IF EXISTS getAge;

DELIMITER //
CREATE FUNCTION getAge(pid varchar(10), dob datetime) RETURNS int NOT DETERMINISTIC 
BEGIN 
DECLARE age int;
SET age = TIMESTAMPDIFF(YEAR,dob,CURDATE());
RETURN (age); 
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE Num_of_diag_Procedure() 
BEGIN 
select count(a.diag_id), b.diag_name from Patient_Diagnosis a JOIN Diagnosis b ON a.diag_id=b.diag_id Group By a.diag_id order by count(a.diag_id) DESC; 
END // 
DELIMITER ; 

call Num_of_diag_Procedure();

DELIMITER //
CREATE PROCEDURE Hereditary_diseases_Procedure(in diagid varchar(10)) 
BEGIN 
select p.first_name, p.last_name from Patient p JOIN Family_Med_History e ON p.pat_id=e.pat_id where e.diag_id=diagid; 
END // 
DELIMITER ; 

Call Hereditary_diseases_Procedure('a20');

DELIMITER //
CREATE PROCEDURE Popular_Medication() 
BEGIN 
select count(m.med_id), Medicine.med_name from Patient_Medicine m JOIN Medicine ON m.med_id=Medicine.med_id Group By m.med_id order by count(m.med_id) DESC; 
END // 
DELIMITER ; 

call Popular_Medication();

DELIMITER //
CREATE PROCEDURE Area_Diagnosis_Procedure(in city varchar(10)) 
BEGIN 
select count(d.diag_id) from Patient_Diagnosis d JOIN Diagnosis ON d.diag_id=Diagnosis.diag_id JOIN Patient_Address a on d.pat_id = a.pat_id Group By city order by count(d.diag_id) DESC; 
END // 
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetDocPatients(in doc_id varchar(10)) 
BEGIN 
select Patient.first_name, Patient.last_name from Patient JOIN Patient_Diagnosis on Patient.pat_id = Patient_Diagnosis.pat_id where Patient_Diagnosis.doc_id = doc_id;
END // 
DELIMITER ; 

call GetDocPatients('D00000');