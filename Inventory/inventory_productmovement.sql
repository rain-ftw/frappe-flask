-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: localhost    Database: inventory
-- ------------------------------------------------------
-- Server version	8.0.18

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
-- Table structure for table `productmovement`
--

DROP TABLE IF EXISTS `productmovement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productmovement` (
  `movement_id` int(11) NOT NULL,
  `timestamp` timestamp NOT NULL,
  `from_location` varchar(45) DEFAULT NULL,
  `to_location` varchar(45) DEFAULT NULL,
  `product_id` int(11) NOT NULL,
  `qty` int(11) DEFAULT NULL,
  PRIMARY KEY (`movement_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productmovement`
--

LOCK TABLES `productmovement` WRITE;
/*!40000 ALTER TABLE `productmovement` DISABLE KEYS */;
INSERT INTO `productmovement` VALUES (1,'2019-12-21 16:32:59','1','2',1,43),(2,'2019-12-22 06:18:28','','3',2,10),(3,'2019-12-22 06:19:14','1','',2,4),(4,'2019-12-22 06:19:40','2','1',5,32),(5,'2019-12-22 06:20:23','2','',5,2),(6,'2019-12-22 06:20:55','','1',5,3),(7,'2019-12-22 06:21:55','1','2',4,6),(8,'2019-12-22 06:22:10','1','',4,8),(9,'2019-12-22 06:22:23','1','',4,5),(10,'2019-12-22 06:22:57','5','1',3,12),(11,'2019-12-22 06:23:25','4','1',3,3),(12,'2019-12-22 06:23:51','2','5',2,10),(13,'2019-12-22 06:24:57','3','',2,1),(15,'2019-12-22 06:25:40','2','4',1,11),(16,'2019-12-22 06:25:55','2','5',1,1),(17,'2019-12-22 06:26:05','4','',4,5),(18,'2019-12-22 06:26:26','3','5',1,33),(19,'2019-12-22 06:26:58','5','',5,17),(20,'2019-12-22 06:27:38','3','1',3,7);
/*!40000 ALTER TABLE `productmovement` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-22  6:34:42
