-- MySQL dump 10.11
--
-- Host: localhost    Database: hcwiley_dj
-- ------------------------------------------------------
-- Server version	5.0.77

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL auto_increment,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_425ae3c4` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_message`
--

DROP TABLE IF EXISTS `auth_message`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `auth_message` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `auth_message_403f60f` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `auth_message`
--

LOCK TABLES `auth_message` WRITE;
/*!40000 ALTER TABLE `auth_message` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_1bb8f392` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add message',4,'add_message'),(11,'Can change message',4,'change_message'),(12,'Can delete message',4,'delete_message'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add site',7,'add_site'),(20,'Can change site',7,'change_site'),(21,'Can delete site',7,'delete_site'),(22,'Can add log entry',8,'add_logentry'),(23,'Can change log entry',8,'change_logentry'),(24,'Can delete log entry',8,'delete_logentry'),(36,'Can delete images',12,'delete_images'),(35,'Can change images',12,'change_images'),(34,'Can add images',12,'add_images'),(28,'Can add piece',10,'add_piece'),(29,'Can change piece',10,'change_piece'),(30,'Can delete piece',10,'delete_piece'),(31,'Can add dimensions',11,'add_dimensions'),(32,'Can change dimensions',11,'change_dimensions'),(33,'Can delete dimensions',11,'delete_dimensions'),(37,'Can add dimensions',13,'add_dimensions'),(38,'Can change dimensions',13,'change_dimensions'),(39,'Can delete dimensions',13,'delete_dimensions'),(40,'Can add image',9,'add_image'),(41,'Can change image',9,'change_image'),(42,'Can delete image',9,'delete_image'),(43,'Can add dimensions',10,'add_dimensions'),(44,'Can change dimensions',10,'change_dimensions'),(45,'Can delete dimensions',10,'delete_dimensions'),(46,'Can add piece',11,'add_piece'),(47,'Can change piece',11,'change_piece'),(48,'Can delete piece',11,'delete_piece');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL auto_increment,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'hcwiley','','','hcwiley@gmail.com','sha1$0ad75$43544e2fc628f86cb7a6e8e2d995aba8939d3a14',1,1,1,'2011-04-11 22:45:20','2011-03-02 09:53:55');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_403f60f` (`user_id`),
  KEY `auth_user_groups_425ae3c4` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_403f60f` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL auto_increment,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) default NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `django_admin_log_403f60f` (`user_id`),
  KEY `django_admin_log_1bb8f392` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=145 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2011-03-23 01:25:09',1,9,'2','/media/gallery/docslogo_1.png',1,''),(2,'2011-03-23 01:25:26',1,9,'3','/media/gallery/still-video-1.png',1,''),(3,'2011-03-23 01:25:32',1,10,'1','2\' x 3\'',1,''),(4,'2011-03-23 01:25:39',1,11,'1','piece one',1,''),(5,'2011-03-23 01:25:46',1,11,'1','piece one',2,'Changed default_image.'),(6,'2011-03-23 02:47:24',1,11,'2','asd',1,''),(7,'2011-03-23 02:52:00',1,9,'4','/media/gallery/still-video-1_1.png',1,''),(8,'2011-03-23 02:52:08',1,11,'3','dfasdasf',1,''),(9,'2011-03-23 02:53:07',1,9,'5','/media/gallery/still-video-3.png',1,''),(10,'2011-03-23 02:53:43',1,9,'6','/media/gallery/still-video-3_1.png',1,''),(11,'2011-03-23 02:57:13',1,9,'1','/media/gallery/docslogo_2.png',1,''),(12,'2011-03-23 02:57:18',1,11,'1','asdsa',1,''),(13,'2011-03-23 02:57:29',1,9,'2','/media/gallery/still-video-1_2.png',1,''),(14,'2011-03-23 02:57:36',1,11,'2','3214324',1,''),(15,'2011-03-23 02:57:48',1,9,'3','/media/gallery/still-video-2.png',1,''),(16,'2011-03-23 02:57:52',1,11,'3','324reqewr',1,''),(17,'2011-03-23 02:58:06',1,9,'4','/media/gallery/indeep_logo.png',1,''),(18,'2011-03-23 02:58:13',1,11,'4','2rdfdfqwefr',1,''),(19,'2011-03-23 02:58:25',1,9,'5','/media/gallery/still-video-3_2.png',1,''),(20,'2011-03-23 02:58:29',1,11,'5','fgklaj',1,''),(21,'2011-03-23 04:01:13',1,9,'1','/media/gallery/finally.png',1,''),(22,'2011-03-23 04:01:56',1,9,'2','/media/gallery/back_night.png',1,''),(23,'2011-03-23 04:02:02',1,9,'3','/media/gallery/back_right_night.png',1,''),(24,'2011-03-23 04:02:10',1,9,'4','/media/gallery/front_night.png',1,''),(25,'2011-03-23 04:02:18',1,9,'5','/media/gallery/front_right.png',1,''),(26,'2011-03-23 04:02:50',1,10,'1','4\' x 9\' x 5\'',1,''),(27,'2011-03-23 04:02:53',1,11,'1','finally',1,''),(28,'2011-03-23 04:03:41',1,9,'6','/media/gallery/img_1325.png',1,''),(29,'2011-03-23 04:03:53',1,9,'7','/media/gallery/img_1336.png',1,''),(30,'2011-03-23 04:04:22',1,9,'8','/media/gallery/img_1338.png',1,''),(31,'2011-03-23 04:04:31',1,9,'9','/media/gallery/img_1337.png',1,''),(32,'2011-03-23 04:04:55',1,10,'2','2\' x 3\' x 2\'',1,''),(33,'2011-03-23 04:04:57',1,11,'2','cav-nivorous',1,''),(34,'2011-03-23 04:05:21',1,9,'10','/media/gallery/frontal_small_1.png',1,''),(35,'2011-03-23 04:05:44',1,9,'11','/media/gallery/frontal.png',1,''),(36,'2011-03-23 04:06:11',1,9,'12','/media/gallery/left_profile.png',1,''),(37,'2011-03-23 04:06:26',1,10,'3','2\' x 3\' x 1\'',1,''),(38,'2011-03-23 04:06:27',1,11,'3','follow me in',1,''),(39,'2011-03-23 07:03:50',1,9,'13','/media/gallery/devolution2.png',1,''),(40,'2011-03-23 07:04:20',1,9,'14','/media/gallery/devolution2_1.png',1,''),(41,'2011-03-23 07:04:28',1,9,'15','/media/gallery/devolution1.png',1,''),(42,'2011-03-23 07:05:01',1,10,'4','2\' x 3\' x 2\'',1,''),(43,'2011-03-23 07:05:04',1,11,'4','devolution',1,''),(44,'2011-03-23 07:05:22',1,9,'16','/media/gallery/stop_light1.png',1,''),(45,'2011-03-23 07:05:49',1,9,'17','/media/gallery/stop_light2.png',1,''),(46,'2011-03-23 07:06:00',1,9,'18','/media/gallery/stop_light1_1.png',1,''),(47,'2011-03-23 07:06:02',1,11,'5','mayhem at astop light',1,''),(48,'2011-03-23 08:04:52',1,9,'19','/media/gallery/lunar1.png',1,''),(49,'2011-03-23 08:05:02',1,9,'20','/media/gallery/lunar2.png',1,''),(50,'2011-03-23 08:07:27',1,10,'5','3\' x 5\' x 3\'',1,''),(51,'2011-03-23 08:07:39',1,11,'6','lunar landar',1,''),(52,'2011-03-23 08:08:45',1,11,'4','de-evolution',2,'Changed title, description, date, price and images.'),(53,'2011-03-23 08:15:23',1,11,'2','cav-nivorous',2,'Changed description, date and price.'),(54,'2011-03-23 08:26:39',1,9,'21','/media/gallery/dual-panorama.png',1,''),(55,'2011-03-23 08:28:13',1,9,'22','/media/gallery/finally2.png',1,''),(56,'2011-03-23 08:28:24',1,9,'23','/media/gallery/finally3.png',1,''),(57,'2011-03-23 08:33:41',1,10,'6','7\' x 9\' x 6\'',1,''),(58,'2011-03-23 08:33:45',1,11,'1','finally',2,'Changed description, default_image, date, images and dimensions.'),(59,'2011-03-23 08:35:16',1,11,'1','finally',2,'Changed description.'),(60,'2011-03-23 08:45:18',1,9,'24','/media/gallery/mountains1.png',1,''),(61,'2011-03-23 08:46:09',1,9,'25','/media/gallery/mountains2.png',1,''),(62,'2011-03-23 08:46:28',1,10,'7','2\' x 2\' x 2\'',1,''),(63,'2011-03-23 08:46:35',1,11,'7','mountains',1,''),(64,'2011-03-23 08:47:14',1,9,'26','/media/gallery/satan1.png',1,''),(65,'2011-03-23 08:48:15',1,9,'27','/media/gallery/satan2.png',1,''),(66,'2011-03-23 08:49:09',1,10,'8','2\' x 2\' x 3\'',1,''),(67,'2011-03-23 08:49:23',1,11,'8','satan\'s arm',1,''),(68,'2011-03-23 08:51:04',1,9,'2','/media/gallery/back_night.png',3,''),(69,'2011-03-23 08:51:30',1,9,'3','/media/gallery/back_right_night.png',3,''),(70,'2011-03-23 08:51:30',1,9,'14','/media/gallery/devolution2_1.png',3,''),(71,'2011-03-23 08:51:30',1,9,'10','/media/gallery/frontal_small_1.png',3,''),(72,'2011-03-23 08:51:30',1,9,'4','/media/gallery/front_night.png',3,''),(73,'2011-03-23 08:51:30',1,9,'16','/media/gallery/stop_light1.png',3,''),(74,'2011-03-23 08:51:30',1,9,'18','/media/gallery/stop_light1_1.png',3,''),(75,'2011-03-23 08:51:30',1,9,'17','/media/gallery/stop_light2.png',3,''),(76,'2011-03-23 08:52:54',1,9,'28','/media/gallery/stop_light2.png',1,''),(77,'2011-03-23 08:53:10',1,9,'29','/media/gallery/stop_light1.png',1,''),(78,'2011-03-23 08:54:01',1,10,'9','1\' x 3\' x 2\'',1,''),(79,'2011-03-23 08:54:03',1,11,'9','mayhem at a stop light',1,''),(80,'2011-03-23 08:54:44',1,9,'30','/media/gallery/heart1.png',1,''),(81,'2011-03-23 08:54:52',1,9,'31','/media/gallery/heart2.png',1,''),(82,'2011-03-23 08:56:22',1,10,'10','2\' x 5\' x 2\'',1,''),(83,'2011-03-23 08:56:28',1,11,'10','a base',1,''),(84,'2011-03-23 08:57:33',1,9,'32','/media/gallery/grind_bowl1.png',1,''),(85,'2011-03-23 08:58:22',1,10,'11','1\' x 0\' x 1\'',1,''),(86,'2011-03-23 08:58:24',1,11,'11','bowl of the gods',1,''),(87,'2011-03-23 08:59:02',1,9,'33','/media/gallery/yorik2.png',1,''),(88,'2011-03-23 08:59:45',1,9,'34','/media/gallery/yorik1.png',1,''),(89,'2011-03-23 08:59:55',1,10,'12','0\' x 0\' x 0\'',1,''),(90,'2011-03-23 08:59:57',1,11,'12','yorik',1,''),(91,'2011-03-23 09:00:33',1,9,'35','/media/gallery/rings2.png',1,''),(92,'2011-03-23 09:01:26',1,9,'36','/media/gallery/rings1.png',1,''),(93,'2011-03-23 09:01:37',1,10,'13','0\' x 1\' x 0\'',1,''),(94,'2011-03-23 09:01:40',1,11,'13','to the mayans',1,''),(95,'2011-03-23 09:02:40',1,9,'37','/media/gallery/gmod.png',1,''),(96,'2011-03-23 09:04:20',1,10,'14','5\' x 4\'',1,''),(97,'2011-03-23 09:04:23',1,11,'14','j2c',1,''),(98,'2011-03-23 09:05:04',1,9,'38','/media/gallery/burn.png',1,''),(99,'2011-03-23 09:06:03',1,10,'15','4\' x 3\'',1,''),(100,'2011-03-23 09:06:08',1,11,'15','congestion',1,''),(101,'2011-03-23 09:07:12',1,9,'39','/media/gallery/beckman.png',1,''),(102,'2011-03-23 09:07:55',1,10,'16','1\' x 2\'',1,''),(103,'2011-03-23 09:07:58',1,11,'16','beckmann',1,''),(104,'2011-03-23 09:10:10',1,11,'14','j2c',2,'Changed materials.'),(105,'2011-03-23 09:12:20',1,11,'16','beckmann',2,'No fields changed.'),(106,'2011-03-23 09:14:49',1,9,'40','/media/gallery/atom1.png',1,''),(107,'2011-03-23 09:15:33',1,9,'41','/media/gallery/atom2.png',1,''),(108,'2011-03-23 09:15:37',1,11,'17','creation',1,''),(109,'2011-03-23 09:16:52',1,9,'42','/media/gallery/first.png',1,''),(110,'2011-03-23 09:17:31',1,10,'17','0\' x 2\' x 0\'',1,''),(111,'2011-03-23 09:17:33',1,11,'18','first',1,''),(112,'2011-03-23 09:17:54',1,10,'18','2\' x 2\' x 1\'',1,''),(113,'2011-03-23 09:17:56',1,11,'17','creation',2,'Changed dimensions.'),(114,'2011-03-23 09:20:33',1,9,'43','/media/gallery/frontal_1.png',1,''),(115,'2011-03-23 09:21:54',1,9,'44','/media/gallery/left_profile_1.png',1,''),(116,'2011-03-23 09:22:10',1,10,'19','2\' x 3\' x 1\'',1,''),(117,'2011-03-23 09:22:12',1,11,'19','follow me in',1,''),(118,'2011-03-23 09:30:11',1,9,'45','/media/gallery/owl.png',1,''),(119,'2011-03-23 09:33:09',1,11,'20','owl eyes',1,''),(120,'2011-03-23 09:35:44',1,11,'20','owl eyes',2,'Changed description.'),(121,'2011-03-23 09:45:58',1,9,'46','/media/gallery/nature2.png',1,''),(122,'2011-03-23 09:46:38',1,9,'47','/media/gallery/bikes.png',1,''),(123,'2011-03-23 09:46:52',1,9,'48','/media/gallery/nature5.png',1,''),(124,'2011-03-23 09:47:03',1,9,'49','/media/gallery/pier1.png',1,''),(125,'2011-03-23 09:47:17',1,9,'50','/media/gallery/pier2.png',1,''),(126,'2011-03-23 09:47:26',1,9,'51','/media/gallery/pier3.png',1,''),(127,'2011-03-23 09:48:11',1,9,'52','/media/gallery/water_leaf.png',1,''),(128,'2011-03-23 09:48:15',1,11,'21','slo series',1,''),(129,'2011-03-23 09:49:14',1,9,'53','/media/gallery/zack-1-full.png',1,''),(130,'2011-03-23 09:49:54',1,9,'54','/media/gallery/zack-2-full.png',1,''),(131,'2011-03-23 09:50:02',1,9,'55','/media/gallery/zack-3-full.png',1,''),(132,'2011-03-23 09:54:21',1,9,'56','/media/gallery/tent-full.png',1,''),(133,'2011-03-23 09:54:33',1,9,'57','/media/gallery/IMG_1152.png',1,''),(134,'2011-03-23 09:54:45',1,11,'22','black and white affair',1,''),(135,'2011-03-23 10:10:56',1,9,'58','/media/gallery/look_out.png',1,''),(136,'2011-03-23 10:11:17',1,9,'59','/media/gallery/chinese_and_beer.png',1,''),(137,'2011-03-23 10:11:23',1,9,'60','/media/gallery/stir.png',1,''),(138,'2011-03-23 10:11:56',1,9,'61','/media/gallery/team_effort.png',1,''),(139,'2011-03-23 10:12:03',1,9,'62','/media/gallery/metal_and_dust.png',1,''),(140,'2011-03-23 10:12:13',1,9,'63','/media/gallery/fire_men.png',1,''),(141,'2011-03-23 10:12:25',1,9,'64','/media/gallery/pile.png',1,''),(142,'2011-03-23 10:12:33',1,9,'65','/media/gallery/bubbly.png',1,''),(143,'2011-03-23 10:12:34',1,11,'23','afterburn',1,''),(144,'2011-03-23 10:24:37',1,11,'20','owl eyes',2,'Changed description.');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'message','auth','message'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'site','sites','site'),(8,'log entry','admin','logentry'),(9,'image','piece','image'),(10,'dimensions','piece','dimensions'),(11,'piece','piece','piece');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY  (`session_key`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('a61759f00923b1ee58399421c6785d04','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS5lYTY3ZWQ1NTQ1ODU5OTFiMmY1\nZWVkZDhjNzRmMzViNw==\n','2011-04-06 01:23:57'),('6bc81f16d44f8eae2476f06210bba5b4','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS5lYTY3ZWQ1NTQ1ODU5OTFiMmY1\nZWVkZDhjNzRmMzViNw==\n','2011-04-06 06:52:21'),('4511675ac88495add6634a0cb66faa28','MjliZTQ3YjkyZThkZTA0ZTY0ODFkZjk5YTU3NTQwYzg0MDNjNGJlNzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2011-04-25 22:45:20');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL auto_increment,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `piece_dimensions`
--

DROP TABLE IF EXISTS `piece_dimensions`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `piece_dimensions` (
  `id` int(11) NOT NULL auto_increment,
  `width` double default NULL,
  `height` double default NULL,
  `depth` double default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `piece_dimensions`
--

LOCK TABLES `piece_dimensions` WRITE;
/*!40000 ALTER TABLE `piece_dimensions` DISABLE KEYS */;
INSERT INTO `piece_dimensions` VALUES (1,4,9,5),(2,2.5,3,2.5),(3,2.5,3,1),(4,2,3,2),(5,3.5,5.5,3),(6,7,9,6),(7,2,2,2),(8,2.5,2,3),(9,1,3,2),(10,2.5,5,2),(11,1,0.5,1),(12,0.5,0.5,0.5),(13,0.5,1,0.5),(14,5,4,NULL),(15,4,3,NULL),(16,1.5,2,NULL),(17,0.5,2,0.5),(18,2,2.5,1),(19,2.5,3.5,1);
/*!40000 ALTER TABLE `piece_dimensions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `piece_image`
--

DROP TABLE IF EXISTS `piece_image`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `piece_image` (
  `id` int(11) NOT NULL auto_increment,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=66 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `piece_image`
--

LOCK TABLES `piece_image` WRITE;
/*!40000 ALTER TABLE `piece_image` DISABLE KEYS */;
INSERT INTO `piece_image` VALUES (1,'gallery/finally.png'),(35,'gallery/rings2.png'),(34,'gallery/yorik1.png'),(33,'gallery/yorik2.png'),(5,'gallery/front_right.png'),(6,'gallery/img_1325.png'),(7,'gallery/img_1336.png'),(8,'gallery/img_1338.png'),(9,'gallery/img_1337.png'),(32,'gallery/grind_bowl1.png'),(11,'gallery/frontal.png'),(12,'gallery/left_profile.png'),(13,'gallery/devolution2.png'),(31,'gallery/heart2.png'),(15,'gallery/devolution1.png'),(30,'gallery/heart1.png'),(29,'gallery/stop_light1.png'),(28,'gallery/stop_light2.png'),(19,'gallery/lunar1.png'),(20,'gallery/lunar2.png'),(21,'gallery/dual-panorama.png'),(22,'gallery/finally2.png'),(23,'gallery/finally3.png'),(24,'gallery/mountains1.png'),(25,'gallery/mountains2.png'),(26,'gallery/satan1.png'),(27,'gallery/satan2.png'),(36,'gallery/rings1.png'),(37,'gallery/gmod.png'),(38,'gallery/burn.png'),(39,'gallery/beckman.png'),(40,'gallery/atom1.png'),(41,'gallery/atom2.png'),(42,'gallery/first.png'),(43,'gallery/frontal_1.png'),(44,'gallery/left_profile_1.png'),(45,'gallery/owl.png'),(46,'gallery/nature2.png'),(47,'gallery/bikes.png'),(48,'gallery/nature5.png'),(49,'gallery/pier1.png'),(50,'gallery/pier2.png'),(51,'gallery/pier3.png'),(52,'gallery/water_leaf.png'),(53,'gallery/zack-1-full.png'),(54,'gallery/zack-2-full.png'),(55,'gallery/zack-3-full.png'),(56,'gallery/tent-full.png'),(57,'gallery/IMG_1152.png'),(58,'gallery/look_out.png'),(59,'gallery/chinese_and_beer.png'),(60,'gallery/stir.png'),(61,'gallery/team_effort.png'),(62,'gallery/metal_and_dust.png'),(63,'gallery/fire_men.png'),(64,'gallery/pile.png'),(65,'gallery/bubbly.png');
/*!40000 ALTER TABLE `piece_image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `piece_piece`
--

DROP TABLE IF EXISTS `piece_piece`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `piece_piece` (
  `id` int(11) NOT NULL auto_increment,
  `title` varchar(400) NOT NULL,
  `description` longtext,
  `default_image_id` int(11) default NULL,
  `date` date default NULL,
  `price` int(10) unsigned default NULL,
  `materials` longtext,
  `medium` varchar(100) NOT NULL,
  `slug` varchar(160) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `piece_piece_28c69cb4` (`default_image_id`),
  KEY `piece_piece_56ae2a2a` (`slug`)
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `piece_piece`
--

LOCK TABLES `piece_piece` WRITE;
/*!40000 ALTER TABLE `piece_piece` DISABLE KEYS */;
INSERT INTO `piece_piece` VALUES (1,'finally','finally is a self portrait.<br/>\r\nIn the physical depiction of one of the figures, I made the figure out of an abstracted series of rods exploding out from where the figure would be. The other figure represents the opposite, all the rods meet to geometrical shapes.',21,'2011-02-06',1200,'steel','sculpture','finally'),(2,'cav-nivorous','I sought to create the environment of cave by using various methods of creating rough edges and harsh textures.',6,'2010-10-05',1200,'steel','sculpture','cav-nivorous'),(4,'de-evolution','Exploration of wood, steel, and patina. I wanted to explore ways of combining wood and steel to show various levels of a form evolving and de-evolving.',13,'2006-11-20',NULL,'wood, steel','sculpture','de-evolution'),(9,'mayhem at a stop light','Exploration of bending, twisting, and intertwining steel; also using polychrome paint as a finish.',28,'2007-05-02',500,'steel, polychrome paint','sculpture','mayhem-at-a-stop-light'),(6,'lunar landar','Exploration of steel, patina, and scale. My main focus was exploring the effect of scale on a piece as a whole. It was the largest piece I had made at that time.',19,'2006-08-01',NULL,'steel, patina','sculpture','lunar-landar'),(7,'mountains','Exploration of steel, nails, paint, and gold leaf.',24,'2007-12-09',NULL,'steel, nails, patina, paint, gold leaf','sculpture','mountains'),(8,'satan\'s arm','Inspired by \"Inferno\" by Dante Alighieri. Exploring ways of using welding rod to build muscle and sheet metal of various levels of decay to represent flesh.',26,'2007-09-29',NULL,'steel','sculpture','satans-arm'),(10,'a base','Exploration of form, balance, and patina. First piece I made in steel. Started as just the top piece. All I needed to do was make a base, and so it began...',30,'2005-10-04',NULL,'steel, patina','sculpture','a-base'),(11,'bowl of the gods','Exploring ways of working with steel and using gold leaf and grinders/buffers to create a finish.',32,'2006-11-20',NULL,'steel, gold leaf','sculpture','bowl-of-the-gods'),(12,'yorik','Inspired by \"Hamlet\" by William Shakespeare. Exploring using various wood carving techniques and etching in brass. Hamlet\'s \"Too, too sullied flesh\" soliloquy is engraved in the brass.',33,'2007-09-28',NULL,'wood, brass','sculpture','yorik'),(13,'to the mayans','Exploration of using styrofoam and patina as a finish to deny base material. Piece heavily focused on weight, balance, and tension.',35,'2007-05-02',NULL,'styrofoam, patina','sculpture','to-the-mayans'),(14,'j2c','A mixture of High Renaissance subject and style meshed with video game content and rendering.',37,'2010-06-10',NULL,'acrylic, oil, and spray paint on wood panel. mounted as a triptych.','painting','j2c'),(15,'congestion','I wanted to investigate urban and suburban life. Through the build up of many layers I wanted to create the feel of congestion that I feel in both over developed suburbia and the urban jungle. Focused on creating a feeling through various textures and types of paint.',38,'2010-05-06',NULL,'acrylic and oil paint and patina on wood panel','painting','congestion'),(16,'beckmann','Based off of <a href=\'0.tqn.com/d/arthistory/1/0/4/T/gad_01.jpg\'>\"Self Portrait with Champagne Glass\" by Max Beckmann</a>',39,'2009-10-15',NULL,'acrylic on canvas','painting','beckmann'),(17,'creation','Inspired by \"A brief history of time\" by Stephen Hawking. Exploration into translating ideas in text into physical form. I wanted to represent the idea of man studying nature through the constructs created by man.',40,'2006-10-10',NULL,'steel, text book','sculpture','creation'),(18,'first','My first piece. Exploration of everything.',42,'2005-09-10',NULL,'wood, brass, copper','sculpture','first'),(19,'follow me in','This piece explores ways of entangling wood and metal into a unified whole. I sought to combine the two materials in such a way that they were physically separate but intertwined. Working in tandem, the materials seek to create an environment in which the viewer can fully enter and embrace. This environment reflects my own during the time of creation.',43,'2010-11-23',NULL,'wood, steel','sculpture','follow-me-in'),(20,'owl eyes','The concept for “Owl Eyes” focused on the relationship between the viewer of art and the piece of art itself, the goal being to blur the lines of this relationship. By using emerging open source technology a system was created to track people. A basic webcam, rotor, and laptop were used to run the system. The rotor and webcam were mounted inside of the owl’s head and connected to the laptop. The webcam captured live video of the installation space and was then processed through a detection and motion tracking system. The code was written in <a href=\'http://python.org/\'>Python</a>, and utilized <a href=\'http://opencv.willowgarage.com/wiki/\'>Open Computer Vision (OpenCV)</a> library.<br/>\r\nAdditional videos can be found <a href=\'http://www.youtube.com/user/hcwiley?feature=mhum#p/f\'>here</a>',45,'2010-03-30',NULL,'fake owl, web cam, rotor, laptop, projector, wood','installation','owl-eyes'),(21,'slo series','Photos I took in San Luis Obispo. ',46,'2010-01-01',NULL,'','photography','slo-series'),(22,'black and white affair','Black and White New Year\'s party',53,'2011-01-01',NULL,'','photography','black-and-white-affair'),(23,'afterburn','Series of photos from the day after new years.',58,'2011-01-01',NULL,'','photography','afterburn');
/*!40000 ALTER TABLE `piece_piece` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `piece_piece_dimensions`
--

DROP TABLE IF EXISTS `piece_piece_dimensions`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `piece_piece_dimensions` (
  `id` int(11) NOT NULL auto_increment,
  `piece_id` int(11) NOT NULL,
  `dimensions_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `piece_id` (`piece_id`,`dimensions_id`),
  KEY `dimensions_id_refs_id_5cfe24e8` (`dimensions_id`)
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `piece_piece_dimensions`
--

LOCK TABLES `piece_piece_dimensions` WRITE;
/*!40000 ALTER TABLE `piece_piece_dimensions` DISABLE KEYS */;
INSERT INTO `piece_piece_dimensions` VALUES (9,1,6),(7,2,2),(12,9,9),(6,4,4),(5,6,5),(10,7,7),(11,8,8),(13,10,10),(14,11,11),(15,12,12),(16,13,13),(20,14,14),(18,15,15),(21,16,16),(22,18,17),(23,17,18),(24,19,19);
/*!40000 ALTER TABLE `piece_piece_dimensions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `piece_piece_images`
--

DROP TABLE IF EXISTS `piece_piece_images`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `piece_piece_images` (
  `id` int(11) NOT NULL auto_increment,
  `piece_id` int(11) NOT NULL,
  `image_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `piece_id` (`piece_id`,`image_id`),
  KEY `image_id_refs_id_1ca4b242` (`image_id`)
) ENGINE=MyISAM AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `piece_piece_images`
--

LOCK TABLES `piece_piece_images` WRITE;
/*!40000 ALTER TABLE `piece_piece_images` DISABLE KEYS */;
INSERT INTO `piece_piece_images` VALUES (24,8,27),(23,7,25),(21,1,22),(22,1,23),(18,2,7),(17,2,9),(16,2,8),(28,13,36),(27,12,34),(30,17,41),(15,4,15),(26,10,31),(25,9,29),(14,6,20),(31,19,44),(32,21,47),(33,21,48),(34,21,49),(35,21,50),(36,21,51),(37,21,52),(38,22,56),(39,22,57),(40,22,54),(41,22,55),(42,23,64),(43,23,65),(44,23,59),(45,23,60),(46,23,61),(47,23,62),(48,23,63);
/*!40000 ALTER TABLE `piece_piece_images` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2011-04-14 19:09:13
