-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: hospital
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Temporary view structure for view `completer_specialist`
--

DROP TABLE IF EXISTS `completer_specialist`;
/*!50001 DROP VIEW IF EXISTS `completer_specialist`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `completer_specialist` AS SELECT 
 1 AS `specialist_surname`,
 1 AS `specialist_name`,
 1 AS `specialist_patronymic`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `completer_specialty`
--

DROP TABLE IF EXISTS `completer_specialty`;
/*!50001 DROP VIEW IF EXISTS `completer_specialty`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `completer_specialty` AS SELECT 
 1 AS `specialty_name`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `diagnosis`
--

DROP TABLE IF EXISTS `diagnosis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `diagnosis` (
  `diagnosis_num` int NOT NULL AUTO_INCREMENT,
  `diagnosis_name` varchar(45) DEFAULT NULL,
  `diagnosis_count` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`diagnosis_num`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diagnosis`
--

LOCK TABLES `diagnosis` WRITE;
/*!40000 ALTER TABLE `diagnosis` DISABLE KEYS */;
INSERT INTO `diagnosis` VALUES (1,'Астма','2'),(2,'Аритмия сердца','0'),(3,'Аллергическое заболевание','0'),(4,'Алкоголизм','1'),(5,'Аденоиды','0'),(6,'Альцгеймер','0'),(7,'Склероз','2'),(8,'ВИЧ','0'),(9,'СПИД','0'),(10,'Гепатит','0'),(11,'Деменция','0'),(12,'Ожирение','0'),(13,'Меланома','0'),(14,'Мастопатия','0'),(15,'Отит','0'),(16,'ОРВИ','0'),(17,'Плоскостопие','1'),(18,'Рак простаты','3'),(19,'Рак молочной железы','0'),(20,'Сколиоз','0'),(21,'Сахарный диабет','0'),(22,'Тонзилит','1'),(23,'Туберкулез','1'),(24,'Шизофрения','0'),(25,'Целиакия','0'),(26,'Цистит','0'),(27,'Головная боль','2'),(28,'Пульпит зубов','1'),(29,'Пародонтит','2'),(30,'Мастит','1'),(31,'Рентгенография','1');
/*!40000 ALTER TABLE `diagnosis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `list_specialist`
--

DROP TABLE IF EXISTS `list_specialist`;
/*!50001 DROP VIEW IF EXISTS `list_specialist`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `list_specialist` AS SELECT 
 1 AS `specialist_surname`,
 1 AS `specialist_name`,
 1 AS `specialist_patronymic`,
 1 AS `specialist_date`,
 1 AS `specialist_login`,
 1 AS `specialist_password`,
 1 AS `specialty_name`,
 1 AS `salary`,
 1 AS `premium`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `list_specialist_ver_2`
--

DROP TABLE IF EXISTS `list_specialist_ver_2`;
/*!50001 DROP VIEW IF EXISTS `list_specialist_ver_2`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `list_specialist_ver_2` AS SELECT 
 1 AS `specialist_surname`,
 1 AS `specialist_name`,
 1 AS `specialist_patronymic`,
 1 AS `specialist_date`,
 1 AS `specialist_login`,
 1 AS `specialist_password`,
 1 AS `specialty_name`,
 1 AS `salary`,
 1 AS `premium`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `list_specialist_ver_3`
--

DROP TABLE IF EXISTS `list_specialist_ver_3`;
/*!50001 DROP VIEW IF EXISTS `list_specialist_ver_3`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `list_specialist_ver_3` AS SELECT 
 1 AS `specialist_surname`,
 1 AS `specialist_name`,
 1 AS `specialist_patronymic`,
 1 AS `specialist_date`,
 1 AS `specialist_login`,
 1 AS `specialist_password`,
 1 AS `specialty_name`,
 1 AS `salary`,
 1 AS `premium`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `list_specialists`
--

DROP TABLE IF EXISTS `list_specialists`;
/*!50001 DROP VIEW IF EXISTS `list_specialists`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `list_specialists` AS SELECT 
 1 AS `specialist_num`,
 1 AS `specialist_surname`,
 1 AS `specialist_name`,
 1 AS `specialist_patronymic`,
 1 AS `specialist_date`,
 1 AS `specialist_login`,
 1 AS `specialist_password`,
 1 AS `specialty_name`,
 1 AS `salary`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient` (
  `patient_num` int NOT NULL AUTO_INCREMENT,
  `patient_date` date DEFAULT NULL,
  `patient_mail` varchar(45) DEFAULT NULL,
  `patient_phone` varchar(15) DEFAULT NULL,
  `patient_name` varchar(45) DEFAULT NULL,
  `patient_surname` varchar(45) DEFAULT NULL,
  `patient_patronymic` varchar(45) DEFAULT NULL,
  `patient_login` varchar(45) DEFAULT NULL,
  `patient_password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`patient_num`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient`
--

LOCK TABLES `patient` WRITE;
/*!40000 ALTER TABLE `patient` DISABLE KEYS */;
INSERT INTO `patient` VALUES (1,'2000-03-01','example@mail.ru','7999999999','Акакий','Пешков','Акакиевич','IP7jqPNy','HkV0JPcV'),(2,'1990-03-04','example2@mail.ru','7999222999','Тимофей','Ладанин','Сергеевич','1','1'),(3,'1996-06-03','example3@mail.ru','79992229996','Илон','Маск','Петрович','2','1'),(4,'1993-06-03','example4@mail.ru','79992229997','Максим','Рино','Петрович','hF9RD0','l8fkob'),(5,'1963-06-03','example5@mail.ru','79992228888','Петр','Петров','Петрович','zQiZYaV','i85hnSW'),(6,'1983-06-29','example6@mail.ru','79992227777','Егор','Петров','Алексеевич','nVbhJj2','nBoKOxZ'),(7,'1988-06-24','example7@mail.ru','79992226666','Алексей','Козаков','Алексеевич','NyJ11hj','rEtM895'),(8,'1998-06-24','example8@mail.ru','79992225555','Илья','Козаков','Тимофеевич','JYd8ag2o','S2dJCvtN'),(9,'1997-06-24','example9@mail.ru','79992223333','Павел','Денисов','Тимофеевич','EWlVnp','LU0QLl'),(10,'1987-08-24','example10@mail.ru','79992222222','Лена','Денисова','Тимофеевна','Aec9NVQ','eoJqYZF'),(11,'1990-08-24','example11@mail.ru','79998888888','Елизавета','Сергеева','Сергеевна','gNCs1fNZ','F1lUC3Gq'),(12,'1992-08-24','example12@mail.ru','79998888888','Дарья','Волкова','Даниловна','aY8PPRG2','bM7esc7T'),(13,'1996-08-24','example13@mail.ru','79998888881','Петр','Волков','Данилович','H7cArV','o8eGUu'),(14,'1997-08-24','example14@mail.ru','79998888887','Петр','Войтов','Данилович','hPXiXQ9','zeLYv7b'),(15,'2001-08-23','example15@mail.ru','79998888822','Павел','Лешко','Павлович','oFe8Ca','xmJVHo'),(16,'2002-08-23','example16@mail.ru','79998888833','Павел','Лешко','Егорович','yw2eCY','tLHWNi'),(17,'2003-08-23','example17@mail.ru','79998888844','Иван','Шелко','Иванович','kVVzW2z','gIkL1lq'),(18,'2006-08-22','example18@mail.ru','79998888855','Роман','Петкович','Иванович','JhxwGWy','WjswH4T'),(19,'2001-08-23','example19@mail.ru','79998888800','Ева','Ковачич','Евангелия','INfW0cwK','AOAMNxPU'),(20,'1999-08-03','example20@mail.ru','79998888811','Егор','Модрич','Егорович','Jk7TSR','FrMgkK'),(21,'2001-08-03','example21@mail.ru','79998888333','Данил','Бензема','Бенземович','AEvQRa','ZdyDRe'),(22,'1990-08-03','example22@mail.ru','79998888222','Винни','Винисиус','Павлович','D0Ic62Fn','1OXOyxBX'),(23,'1993-08-20','example23@mail.ru','79998888666','Александра','Зинченко','Петровна','Qpl5ut','ZiILhM'),(24,'2003-08-22','example24@mail.ru','79998888555','Владимир','Володев','Владимирович','d1gnQc','3er6A8'),(25,'1998-08-01','example25@mail.ru','79998888332','Сергей','Зайцев','Сергеевич','qOS8NIa','bdHnf0m'),(26,'2000-03-03','example26@mail.ru','79999999999','Иван','Иванов','Иванович','X1RFQA','SBBSjd');
/*!40000 ALTER TABLE `patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reception`
--

DROP TABLE IF EXISTS `reception`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reception` (
  `reception_num` int NOT NULL AUTO_INCREMENT,
  `reception_datetime` datetime DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `patient_patient_num` int NOT NULL,
  `specialist_specialist_num` int NOT NULL,
  PRIMARY KEY (`reception_num`),
  KEY `fk_ reception_patient_idx` (`patient_patient_num`),
  KEY `fk_ reception_specialist1_idx` (`specialist_specialist_num`),
  CONSTRAINT `fk_ reception_patient` FOREIGN KEY (`patient_patient_num`) REFERENCES `patient` (`patient_num`),
  CONSTRAINT `fk_ reception_specialist1` FOREIGN KEY (`specialist_specialist_num`) REFERENCES `specialist` (`specialist_num`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reception`
--

LOCK TABLES `reception` WRITE;
/*!40000 ALTER TABLE `reception` DISABLE KEYS */;
INSERT INTO `reception` VALUES (4,'2021-06-18 17:00:00','Повторная запись',22,2),(5,'2021-06-04 11:00:00','Расскажу на приеме',22,6),(22,'2021-06-04 12:00:00','Привет',2,3),(23,'2021-06-04 15:00:00','Привет ещё раз',2,3),(24,'2021-06-04 17:00:00','2',2,3),(25,'2021-06-05 11:00:00','ПРивет',4,1),(26,'2021-06-05 12:00:00','123213',4,1),(27,'2021-06-05 14:00:00','Привет',4,2),(28,'2021-06-05 12:00:00','Привет',25,2),(29,'2021-06-05 14:00:00','1',25,2),(32,'2021-06-05 16:18:31','',3,1);
/*!40000 ALTER TABLE `reception` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reception_result`
--

DROP TABLE IF EXISTS `reception_result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reception_result` (
  `reception_result_num` int NOT NULL AUTO_INCREMENT,
  `reception_result_date` datetime DEFAULT NULL,
  `reception_result_info` varchar(220) DEFAULT NULL,
  `specialist_specialist_num` int NOT NULL,
  `patient_patient_num` int NOT NULL,
  `diagnosis_diagnosis_num` int NOT NULL,
  PRIMARY KEY (`reception_result_num`),
  KEY `fk_reception_result_specialist1_idx` (`specialist_specialist_num`),
  KEY `fk_reception_result_patient1_idx` (`patient_patient_num`),
  KEY `fk_reception_result_diagnosis1_idx` (`diagnosis_diagnosis_num`),
  CONSTRAINT `fk_reception_result_diagnosis1` FOREIGN KEY (`diagnosis_diagnosis_num`) REFERENCES `diagnosis` (`diagnosis_num`),
  CONSTRAINT `fk_reception_result_patient1` FOREIGN KEY (`patient_patient_num`) REFERENCES `patient` (`patient_num`),
  CONSTRAINT `fk_reception_result_specialist1` FOREIGN KEY (`specialist_specialist_num`) REFERENCES `specialist` (`specialist_num`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reception_result`
--

LOCK TABLES `reception_result` WRITE;
/*!40000 ALTER TABLE `reception_result` DISABLE KEYS */;
INSERT INTO `reception_result` VALUES (1,'2021-06-04 00:00:00','Отказ от курения, выполнение элиминационных мероприятий в отношении причиннозначимых аллергенов, а также снижение массы тела при ожирении.',1,6,1),(2,'2021-06-04 00:00:00','Ходите на носках и на пятках, на внутренних и внешних сторонах стоп.\nХодите с поджатыми пальцами ног и с поднятыми пальцами.',1,3,17),(3,'2021-06-03 11:00:00','Меньше пейте и будете здоровы',2,22,4),(4,'2021-06-01 18:00:00','Лечитесь',3,25,18),(5,'2021-06-02 08:00:00','Приходите на доп. обследование',3,25,18),(6,'2021-05-31 18:00:00','Принимайте таблетки по инструкции',5,25,22),(7,'2021-06-03 16:40:00','Химиотерапия',12,25,23),(8,'2021-05-13 10:00:00','Повторное обследование',10,24,28),(9,'2021-05-28 11:00:00','Повторное обследование',10,24,29),(10,'2021-06-02 11:00:00','Регулярно чистить зубы',10,24,29),(11,'2021-05-20 09:00:00','Принимать таблетки',17,23,7),(12,'2021-06-01 11:00:00','Принимать таблетки',17,21,27),(13,'2021-06-03 15:00:00','Принимать таблетки(2 недели)',17,21,27),(14,'2021-06-03 10:00:00','Полноценный сон',17,23,7),(15,'2021-05-31 11:00:00','Борьба с инфекцией',12,25,30),(16,'2021-05-20 10:00:00','-',16,23,31),(17,'2021-06-01 10:00:00','химиотерапия',9,21,18),(18,'2021-06-05 15:52:23','1',1,3,1);
/*!40000 ALTER TABLE `reception_result` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `insert_rr` AFTER INSERT ON `reception_result` FOR EACH ROW BEGIN    
	DELETE FROM reception WHERE reception_datetime = New.reception_result_date;
 END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `insert_d` AFTER INSERT ON `reception_result` FOR EACH ROW BEGIN    
	UPDATE diagnosis
		set diagnosis_count = diagnosis_count + 1 where diagnosis_num = new.diagnosis_diagnosis_num;
 END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `salary`
--

DROP TABLE IF EXISTS `salary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salary` (
  `salary_num` int NOT NULL AUTO_INCREMENT,
  `salary` varchar(45) DEFAULT NULL,
  `premium` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`salary_num`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salary`
--

LOCK TABLES `salary` WRITE;
/*!40000 ALTER TABLE `salary` DISABLE KEYS */;
INSERT INTO `salary` VALUES (1,'25000','0'),(2,'12000','0'),(3,'30000','0'),(4,'30000','0'),(5,'34000','0'),(6,'43000','0'),(7,'34000','0'),(8,'35888','3588.8'),(9,'13000','0'),(10,'100000','0'),(11,'16592','0'),(12,'34900','0'),(13,'45000','0'),(14,'90000','0'),(15,'89000','0'),(16,'25000','0'),(17,'50000','0');
/*!40000 ALTER TABLE `salary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `show_diagnosis`
--

DROP TABLE IF EXISTS `show_diagnosis`;
/*!50001 DROP VIEW IF EXISTS `show_diagnosis`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `show_diagnosis` AS SELECT 
 1 AS `patient_patient_num`,
 1 AS `Пациент`,
 1 AS `diagnosis_name`,
 1 AS `Специалист`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `specialist`
--

DROP TABLE IF EXISTS `specialist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `specialist` (
  `specialist_num` int NOT NULL AUTO_INCREMENT,
  `specialist_name` varchar(45) DEFAULT NULL,
  `specialist_surname` varchar(45) DEFAULT NULL,
  `specialist_patronymic` varchar(45) DEFAULT NULL,
  `specialist_date` date DEFAULT NULL,
  `specialist_login` varchar(70) DEFAULT NULL,
  `specialist_password` varchar(45) DEFAULT NULL,
  `salary_salary_num` int NOT NULL,
  PRIMARY KEY (`specialist_num`,`salary_salary_num`),
  KEY `fk_specialist_salary1_idx` (`salary_salary_num`),
  CONSTRAINT `fk_specialist_salary1` FOREIGN KEY (`salary_salary_num`) REFERENCES `salary` (`salary_num`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `specialist`
--

LOCK TABLES `specialist` WRITE;
/*!40000 ALTER TABLE `specialist` DISABLE KEYS */;
INSERT INTO `specialist` VALUES (1,'Егор','Томилин','Сергеевич','1900-01-01','qwerty','12345',1),(2,'Станислав','Попов','Сергеевич','1965-05-04','qwerty1','12345',2),(3,'Анастасия','Волкова','Денисовна','1990-11-04','wasd','1234',3),(4,'Лена','Романова','Ивановна','1999-03-25','wasd1','12345',4),(5,'Вильнюс','Вилесов','Алексеевич','2001-03-02','cool','228',5),(6,'Иван','Каптель','Иванович','1990-10-04','captelmarvel','43000',6),(7,'Илья','Чемезов','Станиславович','1999-03-02','bestginekolog','12345',7),(8,'Виктория','Ананасова','Викторовна','2000-09-09','helloworld','123456789',8),(9,'Петр','Петров','Петрович','1990-09-09','Petr','229',9),(10,'Данил','Гений','Генадьевич','2000-09-08','qwertyu','228229',10),(11,'Екатерина','Томилова','Сергеевна','2001-09-09','asdfgh','9659',11),(12,'Геннадий','Булкин','Вячеславович','2002-03-02','user','45245',12),(13,'Вячеслав','Лосев','Иванович','1999-03-05','plko','852369',13),(14,'Джон','Уик','Джоквич','1993-03-05','terrar','666',14),(15,'Константин','Фильм','Петрович','1997-03-05','kycok','909090',15),(16,'Иван','Иванов','Иванович','1990-05-06','ggwpbratki','965785',16),(17,'Луиза','Димитреску','Дмитриевна','2000-09-09','cookie','1234567890',17);
/*!40000 ALTER TABLE `specialist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `specialists_patients`
--

DROP TABLE IF EXISTS `specialists_patients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `specialists_patients` (
  `specialist_specialist_num` int NOT NULL,
  `patient_patient_num` int NOT NULL,
  PRIMARY KEY (`specialist_specialist_num`,`patient_patient_num`),
  KEY `fk_specialist_has_patient_patient1_idx` (`patient_patient_num`),
  KEY `fk_specialist_has_patient_specialist1_idx` (`specialist_specialist_num`),
  CONSTRAINT `fk_specialist_has_patient_patient1` FOREIGN KEY (`patient_patient_num`) REFERENCES `patient` (`patient_num`),
  CONSTRAINT `fk_specialist_has_patient_specialist1` FOREIGN KEY (`specialist_specialist_num`) REFERENCES `specialist` (`specialist_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `specialists_patients`
--

LOCK TABLES `specialists_patients` WRITE;
/*!40000 ALTER TABLE `specialists_patients` DISABLE KEYS */;
INSERT INTO `specialists_patients` VALUES (3,2),(1,3),(1,4),(2,4),(1,6),(9,21),(17,21),(2,22),(6,22),(16,23),(17,23),(10,24),(2,25),(3,25),(5,25),(12,25);
/*!40000 ALTER TABLE `specialists_patients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `specialists_specialties`
--

DROP TABLE IF EXISTS `specialists_specialties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `specialists_specialties` (
  `specialty_specialty_num` int NOT NULL,
  `specialist_specialist_num` int NOT NULL,
  PRIMARY KEY (`specialty_specialty_num`,`specialist_specialist_num`),
  KEY `fk_specialty_has_specialist_specialist1_idx` (`specialist_specialist_num`),
  KEY `fk_specialty_has_specialist_specialty1_idx` (`specialty_specialty_num`),
  CONSTRAINT `fk_specialty_has_specialist_specialist1` FOREIGN KEY (`specialist_specialist_num`) REFERENCES `specialist` (`specialist_num`),
  CONSTRAINT `fk_specialty_has_specialist_specialty1` FOREIGN KEY (`specialty_specialty_num`) REFERENCES `specialty` (`specialty_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `specialists_specialties`
--

LOCK TABLES `specialists_specialties` WRITE;
/*!40000 ALTER TABLE `specialists_specialties` DISABLE KEYS */;
INSERT INTO `specialists_specialties` VALUES (3,1),(7,2),(8,3),(6,4),(3,5),(3,6),(9,7),(9,8),(10,9),(4,10),(4,11),(16,12),(5,13),(5,14),(15,15),(12,16),(13,17);
/*!40000 ALTER TABLE `specialists_specialties` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `insert_sp` AFTER INSERT ON `specialists_specialties` FOR EACH ROW BEGIN    
	UPDATE specialty
		set specialty_count = specialty_count + 1 where specialty_num = New.specialty_specialty_num;
 END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `specialty`
--

DROP TABLE IF EXISTS `specialty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `specialty` (
  `specialty_num` int NOT NULL AUTO_INCREMENT,
  `specialty_name` varchar(45) DEFAULT NULL,
  `specialty_count` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`specialty_num`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `specialty`
--

LOCK TABLES `specialty` WRITE;
/*!40000 ALTER TABLE `specialty` DISABLE KEYS */;
INSERT INTO `specialty` VALUES (1,'Косметолог','1'),(2,'Психиатр','0'),(3,'Терапевт','3'),(4,'Стоматолог','2'),(5,'Нарколог','2'),(6,'Фармацевт','1'),(7,'Хирург','1'),(8,'Акушер','1'),(9,'Гинеколог','2'),(10,'Онколог','1'),(11,'Дерматолог','0'),(12,'Рентгенолог','1'),(13,'Невролог','1'),(14,'Нарколог','0'),(15,'Окулист','1'),(16,'Маммолог','1');
/*!40000 ALTER TABLE `specialty` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `user_num` int NOT NULL AUTO_INCREMENT,
  `user_login` varchar(45) DEFAULT NULL,
  `user_password` varchar(25) DEFAULT NULL,
  `type` tinyint DEFAULT NULL,
  PRIMARY KEY (`user_num`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Admin','',0),(2,'qwerty','',1),(3,'qwerty1','12345',1),(4,'wasd','1234',1),(5,'wasd1','12345',1),(6,'cool','228',1),(7,'captelmarvel','43000',1),(8,'bestginekolog','12345',1),(9,'helloworld','123456789',1),(10,'Petr','229',1),(11,'qwertyu','228229',1),(12,'asdfgh','9659',1),(13,'user','45245',1),(14,'plko','852369',1),(15,'terrar','666',1),(16,'kycok','909090',1),(17,'ggwpbratki','965785',1),(18,'cookie','1234567890',1),(19,'IP7jqPNy','HkV0JPcV',2),(20,'BWUuN8','QV7eLc',2),(21,'Pz9WlUl','nssD8Bl',2),(22,'hF9RD0','l8fkob',2),(23,'zQiZYaV','i85hnSW',2),(24,'nVbhJj2','nBoKOxZ',2),(25,'NyJ11hj','rEtM895',2),(26,'JYd8ag2o','S2dJCvtN',2),(27,'EWlVnp','LU0QLl',2),(28,'Aec9NVQ','eoJqYZF',2),(29,'gNCs1fNZ','F1lUC3Gq',2),(30,'aY8PPRG2','bM7esc7T',2),(31,'H7cArV','o8eGUu',2),(32,'hPXiXQ9','zeLYv7b',2),(33,'oFe8Ca','xmJVHo',2),(34,'yw2eCY','tLHWNi',2),(35,'kVVzW2z','gIkL1lq',2),(36,'JhxwGWy','WjswH4T',2),(37,'INfW0cwK','AOAMNxPU',2),(38,'Jk7TSR','FrMgkK',2),(39,'AEvQRa','ZdyDRe',2),(40,'D0Ic62Fn','1OXOyxBX',2),(41,'Qpl5ut','ZiILhM',2),(42,'d1gnQc','3er6A8',2),(43,'qOS8NIa','bdHnf0m',2),(44,'X1RFQA','SBBSjd',2);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'hospital'
--

--
-- Dumping routines for database 'hospital'
--
/*!50003 DROP PROCEDURE IF EXISTS `get_patients` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_patients`(num varchar(32))
BEGIN
	select patient_surname, patient_name, patient_patronymic, Concat(CONVERT(ls.specialist_surname, CHAR), " ", CONVERT(ls.specialist_name, CHAR), " ", CONVERT(ls.specialist_patronymic, CHAR), 
"\n", CONVERT(ls.specialty_name, CHAR)) as Специалист, patient_date, patient_mail, patient_phone from patient p, list_specialists ls, specialists_patients sp where sp.patient_patient_num = p.patient_num and sp.specialist_specialist_num = num and ls.specialist_num = num;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_specialist` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_specialist`(num varchar(32))
BEGIN
select ls.specialist_surname, ls.specialist_name, ls.specialist_patronymic, ls.specialty_name, ls.specialist_date
from list_specialists ls join specialists_patients sp where ls.specialist_num = sp.specialist_specialist_num and sp.patient_patient_num = num;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_sp` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_sp`(num varchar(12), count varchar(10))
BEGIN
    INSERT INTO specialists_specialties (specialty_specialty_num, specialist_specialist_num) values (num, count);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `list_of_records_1` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `list_of_records_1`(num varchar(10))
BEGIN
	sELECT patient_surname, patient_name, patient_patronymic, reception_datetime, description
	FROM reception r JOIN patient p ON r.patient_patient_num=p.patient_num and r.specialist_specialist_num = num ORDER BY 4;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `list_of_records_2` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `list_of_records_2`(num varchar(10))
BEGIN
	sELECT patient_surname, patient_name, patient_patronymic, reception_datetime, description
	FROM reception r JOIN patient p ON r.patient_patient_num=p.patient_num and r.specialist_specialist_num = num ORDER BY 1, 4 ;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `list_of_records_3` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `list_of_records_3`(num varchar(10))
BEGIN
	sELECT patient_surname, patient_name, patient_patronymic, reception_datetime, description
	FROM reception r JOIN patient p ON r.patient_patient_num=p.patient_num and r.specialist_specialist_num = num ORDER BY 1 DESC, 4;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `patient_id` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `patient_id`(name varchar(50), surname varchar(50), patronymic varchar(50))
BEGIN
select s.patient_num from patient s 
where (s.patient_name = name and s.patient_surname = surname and s.patient_patronymic = patronymic);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `premium_value` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `premium_value`(percent INT, id varchar(12))
BEGIN
DECLARE per INT;
  IF percent > 0 AND percent < 100 THEN             
		UPDATE salary
           SET premium = salary * (percent / 100)
             WHERE salary_num = id;
     END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `records_patient` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `records_patient`(id_patient varchar(10), id_specialist varchar(10))
BEGIN
select reception_datetime, description from reception r where r.patient_patient_num = id_patient and reception_datetime > Now() and id_specialist = r.specialist_specialist_num;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `r_patient` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `r_patient`(patient_surn varchar(32), patient_n varchar(32), patient_patr varchar(32))
BEGIN
	select patient_num, patient_date, patient_phone, patient_mail from patient where patient_name = patient_n and patient_surname = patient_surn and patient_patr = patient_patronymic;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `show_patients` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `show_patients`(num varchar(50))
BEGIN
select patient_surname, patient_name, patient_patronymic from patient p join specialists_patients sp on sp.patient_patient_num = p.patient_num and specialist_specialist_num = num;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `show_patients_ver_2` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `show_patients_ver_2`(num varchar(50))
BEGIN
select patient_num, patient_surname, patient_name, patient_patronymic from patient p join specialists_patients sp on sp.patient_patient_num = p.patient_num and specialist_specialist_num = num;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `show_records_between_datetime` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `show_records_between_datetime`(datetime_1 DATETIME, datetime_2 DATETIME, num varchar(10))
BEGIN
	SELECT patient_surname, patient_name, patient_patronymic, reception_datetime, description
    FROM (sELECT patient_surname, patient_name, patient_patronymic, reception_datetime, description
	FROM reception r JOIN patient p ON r.patient_patient_num=p.patient_num and r.specialist_specialist_num = num ORDER BY 4) as t
    WHERE t.reception_datetime BETWEEN datetime_1 AND datetime_2;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `show_specialists` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `show_specialists`(specialty_ varchar(50))
BEGIN
SELECT specialist_surname, specialist_name, specialist_patronymic, specialty_name
    FROM list_specialist ls where ls.specialty_name = specialty_;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `specialistid` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `specialistid`(name varchar(50), surname varchar(50), patronymic varchar(50))
BEGIN
select s.specialist_num from specialist s 
where (s.specialist_name = name and s.specialist_surname = surname and s.specialist_patronymic = patronymic);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `table_filter_specialty` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `table_filter_specialty`(spec varchar(32))
BEGIN
	select * from list_specialist where specialty_name = spec;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Final view structure for view `completer_specialist`
--

/*!50001 DROP VIEW IF EXISTS `completer_specialist`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `completer_specialist` AS select `specialist`.`specialist_surname` AS `specialist_surname`,`specialist`.`specialist_name` AS `specialist_name`,`specialist`.`specialist_patronymic` AS `specialist_patronymic` from `specialist` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `completer_specialty`
--

/*!50001 DROP VIEW IF EXISTS `completer_specialty`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `completer_specialty` AS select `specialty`.`specialty_name` AS `specialty_name` from `specialty` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `list_specialist`
--

/*!50001 DROP VIEW IF EXISTS `list_specialist`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `list_specialist` AS select `s`.`specialist_surname` AS `specialist_surname`,`s`.`specialist_name` AS `specialist_name`,`s`.`specialist_patronymic` AS `specialist_patronymic`,`s`.`specialist_date` AS `specialist_date`,`s`.`specialist_login` AS `specialist_login`,`s`.`specialist_password` AS `specialist_password`,`sp`.`specialty_name` AS `specialty_name`,`sa`.`salary` AS `salary`,`sa`.`premium` AS `premium` from (((`specialist` `s` join `salary` `sa` on((`s`.`salary_salary_num` = `sa`.`salary_num`))) join `specialists_specialties` `ssp` on((`ssp`.`specialist_specialist_num` = `s`.`specialist_num`))) join `specialty` `sp` on((`sp`.`specialty_num` = `ssp`.`specialty_specialty_num`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `list_specialist_ver_2`
--

/*!50001 DROP VIEW IF EXISTS `list_specialist_ver_2`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `list_specialist_ver_2` AS select `list_specialist`.`specialist_surname` AS `specialist_surname`,`list_specialist`.`specialist_name` AS `specialist_name`,`list_specialist`.`specialist_patronymic` AS `specialist_patronymic`,`list_specialist`.`specialist_date` AS `specialist_date`,`list_specialist`.`specialist_login` AS `specialist_login`,`list_specialist`.`specialist_password` AS `specialist_password`,`list_specialist`.`specialty_name` AS `specialty_name`,`list_specialist`.`salary` AS `salary`,`list_specialist`.`premium` AS `premium` from `list_specialist` order by `list_specialist`.`specialist_surname` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `list_specialist_ver_3`
--

/*!50001 DROP VIEW IF EXISTS `list_specialist_ver_3`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `list_specialist_ver_3` AS select `list_specialist`.`specialist_surname` AS `specialist_surname`,`list_specialist`.`specialist_name` AS `specialist_name`,`list_specialist`.`specialist_patronymic` AS `specialist_patronymic`,`list_specialist`.`specialist_date` AS `specialist_date`,`list_specialist`.`specialist_login` AS `specialist_login`,`list_specialist`.`specialist_password` AS `specialist_password`,`list_specialist`.`specialty_name` AS `specialty_name`,`list_specialist`.`salary` AS `salary`,`list_specialist`.`premium` AS `premium` from `list_specialist` order by `list_specialist`.`specialist_surname` desc */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `list_specialists`
--

/*!50001 DROP VIEW IF EXISTS `list_specialists`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `list_specialists` AS select `s`.`specialist_num` AS `specialist_num`,`s`.`specialist_surname` AS `specialist_surname`,`s`.`specialist_name` AS `specialist_name`,`s`.`specialist_patronymic` AS `specialist_patronymic`,`s`.`specialist_date` AS `specialist_date`,`s`.`specialist_login` AS `specialist_login`,`s`.`specialist_password` AS `specialist_password`,`sp`.`specialty_name` AS `specialty_name`,`sa`.`salary` AS `salary` from (((`specialist` `s` join `salary` `sa` on((`s`.`salary_salary_num` = `sa`.`salary_num`))) join `specialists_specialties` `ssp` on((`ssp`.`specialist_specialist_num` = `s`.`specialist_num`))) join `specialty` `sp` on((`sp`.`specialty_num` = `ssp`.`specialty_specialty_num`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `show_diagnosis`
--

/*!50001 DROP VIEW IF EXISTS `show_diagnosis`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `show_diagnosis` AS select `rr`.`patient_patient_num` AS `patient_patient_num`,concat(cast(`p`.`patient_name` as char charset utf8mb4),' ',cast(`p`.`patient_surname` as char charset utf8mb4),' ',cast(`p`.`patient_patronymic` as char charset utf8mb4)) AS `Пациент`,`d`.`diagnosis_name` AS `diagnosis_name`,concat(cast(`ls`.`specialist_surname` as char charset utf8mb4),' ',cast(`ls`.`specialist_name` as char charset utf8mb4),' ',cast(`ls`.`specialist_patronymic` as char charset utf8mb4),'\n',cast(`ls`.`specialty_name` as char charset utf8mb4)) AS `Специалист` from (((`reception_result` `rr` join `patient` `p`) join `list_specialists` `ls`) join `diagnosis` `d`) where ((`rr`.`patient_patient_num` = `p`.`patient_num`) and (`rr`.`specialist_specialist_num` = `ls`.`specialist_num`) and (`rr`.`diagnosis_diagnosis_num` = `d`.`diagnosis_num`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-05 16:43:51
