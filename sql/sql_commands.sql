use hospital;

-- DELIMITER //
-- CREATE PROCEDURE insert_sp
--     (num varchar(12), count varchar(10))
-- BEGIN
--     INSERT INTO specialists_specialties (specialty_specialty_num, specialist_specialist_num) values (num, count);
-- END//  

-- DELIMITER //
-- CREATE TRIGGER insert_sp after INSERT ON specialists_specialties
-- FOR EACH ROW
-- BEGIN    
-- 	UPDATE specialty
-- 		set specialty_count = specialty_count + 1 where specialty_num = New.specialty_specialty_num;
--  END//  


-- DELIMITER //
-- CREATE TRIGGER insert_d after INSERT ON reception_result
-- FOR EACH ROW
-- BEGIN    
-- 	UPDATE diagnosis
-- 		set diagnosis_count = diagnosis_count + 1 where diagnosis_num = new.diagnosis_diagnosis_num;
--  END//  


-- DELIMITER //
-- CREATE TRIGGER insert_rr after INSERT ON reception_result
-- FOR EACH ROW
-- BEGIN    
-- 	DELETE FROM reception WHERE reception_datetime = New.reception_result_date;
--  END//  
--  



-- create view completer_specialist as
-- select specialist_surname, specialist_name, specialist_patronymic from specialist;


-- create view completer_specialty as
-- select specialty_name from specialty;


-- -- view and procedure
-- create view show_diagnosis as
-- select rr.patient_patient_num, Concat(CONVERT(p.patient_name, CHAR), " ", CONVERT(p.patient_surname, CHAR), " ", CONVERT(p.patient_patronymic, CHAR)) as Пациент, d.diagnosis_name,
-- Concat(CONVERT(ls.specialist_surname, CHAR), " ", CONVERT(ls.specialist_name, CHAR), " ", CONVERT(ls.specialist_patronymic, CHAR), "\n", CONVERT(ls.specialty_name, CHAR)) as Специалист from
-- reception_result rr, patient p, list_specialists ls, diagnosis d where (rr.patient_patient_num = p.patient_num and rr.specialist_specialist_num = ls.specialist_num and rr.diagnosis_diagnosis_num = d.diagnosis_num);



-- DELIMITER //
-- CREATE PROCEDURE get_specialist
--     (num varchar(32))
-- BEGIN
-- select ls.specialist_surname, ls.specialist_name, ls.specialist_patronymic, ls.specialty_name, ls.specialist_date
-- from list_specialists ls join specialists_patients sp where ls.specialist_num = sp.specialist_specialist_num and sp.patient_patient_num = num;
-- END// 


-- DELIMITER //
-- CREATE PROCEDURE patient_id
--     (name varchar(50), surname varchar(50), patronymic varchar(50))
-- BEGIN
-- select s.patient_num from patient s 
-- where (s.patient_name = name and s.patient_surname = surname and s.patient_patronymic = patronymic);
-- END// 


-- DELIMITER //
-- CREATE PROCEDURE get_patients
--     (num varchar(32))
-- BEGIN
-- 	select patient_surname, patient_name, patient_patronymic, Concat(CONVERT(ls.specialist_surname, CHAR), " ", CONVERT(ls.specialist_name, CHAR), " ", CONVERT(ls.specialist_patronymic, CHAR), 
-- "\n", CONVERT(ls.specialty_name, CHAR)) as Специалист, patient_date, patient_mail, patient_phone from patient p, list_specialists ls, specialists_patients sp where sp.patient_patient_num = p.patient_num and sp.specialist_specialist_num = num and ls.specialist_num = num;
-- END// 


-- DELIMITER //
-- CREATE PROCEDURE r_patient
--     (patient_surn varchar(32), patient_n varchar(32), patient_patr varchar(32))
-- BEGIN
-- 	select patient_num, patient_date, patient_phone, patient_mail from patient where patient_name = patient_n and patient_surname = patient_surn and patient_patr = patient_patronymic;
-- END// 


-- DELIMITER //
-- CREATE PROCEDURE table_filter_specialty
--     (spec varchar(32))
-- BEGIN
-- 	select * from list_specialist where specialty_name = spec;
-- END// 

-- select * from reception;

-- DELIMITER //
-- CREATE PROCEDURE records_patient
--     (id_patient varchar(10), id_specialist varchar(10))
-- BEGIN
-- select reception_datetime, description from reception r where r.patient_patient_num = id_patient and reception_datetime > Now() and id_specialist = r.specialist_specialist_num;
-- END// 

-- select * from patient;

-- DELIMITER //
-- CREATE PROCEDURE list_of_records_1
--     (num varchar(10))
-- BEGIN
-- 	sELECT patient_surname, patient_name, patient_patronymic, reception_datetime, description
-- 	FROM reception r JOIN patient p ON r.patient_patient_num=p.patient_num and r.specialist_specialist_num = num ORDER BY 4;
-- END// 


-- CREATE PROCEDURE list_of_records_2
--     (num varchar(10))
-- BEGIN
-- 	sELECT patient_surname, patient_name, patient_patronymic, reception_datetime, description
-- 	FROM reception r JOIN patient p ON r.patient_patient_num=p.patient_num and r.specialist_specialist_num = num ORDER BY 1, 4 ;
-- END// 


-- CREATE PROCEDURE list_of_records_3
--     (num varchar(10))
-- BEGIN
-- 	sELECT patient_surname, patient_name, patient_patronymic, reception_datetime, description
-- 	FROM reception r JOIN patient p ON r.patient_patient_num=p.patient_num and r.specialist_specialist_num = num ORDER BY 1 DESC, 4;
-- END// 


-- DELIMITER //
-- CREATE PROCEDURE show_records_between_datetime
--     (datetime_1 DATETIME, datetime_2 DATETIME, num varchar(10))
-- BEGIN
-- 	SELECT patient_surname, patient_name, patient_patronymic, reception_datetime, description
--     FROM (sELECT patient_surname, patient_name, patient_patronymic, reception_datetime, description
-- 	FROM reception r JOIN patient p ON r.patient_patient_num=p.patient_num and r.specialist_specialist_num = num ORDER BY 4) as t
--     WHERE t.reception_datetime BETWEEN datetime_1 AND datetime_2;
-- END// 


-- DELIMITER //
-- CREATE PROCEDURE specialistid
-- 	(name varchar(50), surname varchar(50), patronymic varchar(50))
-- BEGIN
-- select s.specialist_num from specialist s 
-- where (s.specialist_name = name and s.specialist_surname = surname and s.specialist_patronymic = patronymic);
-- END// 

-- DELIMITER //
-- CREATE PROCEDURE patient_id
-- 	(name varchar(50), surname varchar(50), patronymic varchar(50))
-- BEGIN
-- select s.patient_num from patient s 
-- where (s.patient_name = name and s.patient_surname = surname and s.patient_patronymic = patronymic);
-- END// 

-- select * from salary

-- DELIMITER //
-- CREATE PROCEDURE show_specialists
-- 	(specialty_ varchar(50))
-- BEGIN
-- SELECT specialist_surname, specialist_name, specialist_patronymic, specialty_name
--     FROM list_specialist ls where ls.specialty_name = specialty_;
-- END// 


-- DELIMITER //
-- CREATE PROCEDURE show_patients
-- 	(num varchar(50))
-- BEGIN
-- select patient_surname, patient_name, patient_patronymic from patient p join specialists_patients sp on sp.patient_patient_num = p.patient_num and specialist_specialist_num = num;
-- END// 


-- DELIMITER //
-- CREATE PROCEDURE show_patients_ver_2
-- 	(num varchar(50))
-- BEGIN
-- select patient_num, patient_surname, patient_name, patient_patronymic from patient p join specialists_patients sp on sp.patient_patient_num = p.patient_num and specialist_specialist_num = num;
-- END// 


-- create view list_specialists as
-- select s.specialist_num, s.specialist_surname, s.specialist_name, s.specialist_patronymic, s.specialist_date, 
-- s.specialist_login, s.specialist_password, sp.specialty_name, sa.salary
-- FROM specialist s join salary sa on s.salary_salary_num=sa.salary_num
-- join specialists_specialties ssp on ssp.specialist_specialist_num = s.specialist_num
-- join specialty sp on sp.specialty_num = ssp.specialty_specialty_num;

-- select * from specialist
-- create view list_specialist as
-- select s.specialist_surname, s.specialist_name, s.specialist_patronymic, s.specialist_date, 
-- s.specialist_login, s.specialist_password, sp.specialty_name, sa.salary, sa.premium
-- FROM specialist s join salary sa on s.salary_salary_num=sa.salary_num
-- join specialists_specialties ssp on ssp.specialist_specialist_num = s.specialist_num
-- join specialty sp on sp.specialty_num = ssp.specialty_specialty_num 

-- DELIMITER //
-- CREATE PROCEDURE premium_value (percent INT, id varchar(12))
-- BEGIN
-- DECLARE per INT;
--   IF percent > 0 AND percent < 100 THEN             
-- 		UPDATE salary
--            SET premium = salary * (percent / 100)
--              WHERE salary_num = id;
--      END IF;
-- END//


-- create view list_specialist_ver_2 as 
-- select * from list_specialist ORDER BY 1;

-- create view list_specialist_ver_3 as 
-- select * from list_specialist ORDER BY 1 desc;