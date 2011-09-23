-- MySQL dump 10.13  Distrib 5.1.53, for apple-darwin10.3.0 (i386)
--
-- Host: localhost    Database: digital825p_site
-- ------------------------------------------------------
-- Server version	5.1.53

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
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_425ae3c4` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `auth_message_403f60f` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_1bb8f392` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add message',4,'add_message'),(11,'Can change message',4,'change_message'),(12,'Can delete message',4,'delete_message'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add site',7,'add_site'),(20,'Can change site',7,'change_site'),(21,'Can delete site',7,'delete_site'),(22,'Can add log entry',8,'add_logentry'),(23,'Can change log entry',8,'change_logentry'),(24,'Can delete log entry',8,'delete_logentry'),(25,'Can add image',9,'add_image'),(26,'Can change image',9,'change_image'),(27,'Can delete image',9,'delete_image'),(28,'Can add series',10,'add_series'),(29,'Can change series',10,'change_series'),(30,'Can delete series',10,'delete_series'),(31,'Can add piece',11,'add_piece'),(32,'Can change piece',11,'change_piece'),(33,'Can delete piece',11,'delete_piece');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
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
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'digital825p','','','digital825p@yahoo.com','sha1$f32bf$e356a439498cef5c956112941e8d1c27dc828d33',1,1,1,'2011-06-11 12:07:39','2011-04-28 17:44:07');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_403f60f` (`user_id`),
  KEY `auth_user_groups_425ae3c4` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_403f60f` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_403f60f` (`user_id`),
  KEY `django_admin_log_1bb8f392` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2011-06-11 13:28:51',1,10,'16','',3,''),(2,'2011-06-11 13:45:47',1,11,'159','sdfdsafsdf',3,''),(3,'2011-06-11 13:45:47',1,11,'158','sdfdsaf',3,''),(4,'2011-06-11 13:45:47',1,11,'157','asdfdsfsdsd',3,''),(5,'2011-06-11 13:45:47',1,11,'156','dasfsf',3,''),(6,'2011-06-11 13:45:47',1,11,'155','sdafsd',3,''),(7,'2011-06-11 13:45:47',1,11,'154','foo',3,''),(8,'2011-06-11 17:10:05',1,11,'163','asdffsdf',3,''),(9,'2011-06-11 17:10:05',1,11,'162','dsaf',3,''),(10,'2011-06-11 17:10:05',1,11,'161','first',3,''),(11,'2011-06-11 17:10:05',1,11,'160','asdfsf',3,''),(12,'2011-06-11 17:23:32',1,11,'172','foo',3,''),(13,'2011-06-11 17:23:32',1,11,'171','dsafsdf',3,''),(14,'2011-06-11 17:23:32',1,11,'170','yes',3,''),(15,'2011-06-11 17:23:32',1,11,'169','new',3,''),(16,'2011-06-11 17:23:32',1,11,'168','dsfdsaf',3,''),(17,'2011-06-11 17:23:32',1,11,'167','dsafdsafasd',3,''),(18,'2011-06-11 17:23:32',1,11,'166','dasfdsfsda',3,''),(19,'2011-06-11 17:23:32',1,11,'165','dsfsdf',3,''),(20,'2011-06-11 17:23:32',1,11,'164','dsafasd',3,''),(21,'2011-06-11 17:23:43',1,10,'22','bar',3,''),(22,'2011-06-11 17:23:43',1,10,'21','new',3,''),(23,'2011-06-11 17:23:43',1,10,'20','arrg',3,''),(24,'2011-06-11 17:23:43',1,10,'19','yep',3,''),(25,'2011-06-11 17:23:43',1,10,'18','test',3,''),(26,'2011-06-11 17:23:43',1,10,'17','new-series',3,'');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'message','auth','message'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'site','sites','site'),(8,'log entry','admin','logentry'),(9,'image','piece','image'),(10,'series','piece','series'),(11,'piece','piece','piece');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_3da3d3d8` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('8c10d115c85ac5929422f44c72b076c1','gAJ9cQFVCnRlc3Rjb29raWVxAlUGd29ya2VkcQNzLjhiNzUzN2RiNDI5MTU4NTMzNjU1M2U3MDNi\nM2E0MDAy\n','2011-05-17 12:45:45'),('cc5f3c7658a380ed0ac9aefa2b68a28c','MjliZTQ3YjkyZThkZTA0ZTY0ODFkZjk5YTU3NTQwYzg0MDNjNGJlNzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2011-05-12 17:44:22'),('19137aa6fdf34f2ead0b481815b8c29a','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS5lYTY3ZWQ1NTQ1ODU5OTFiMmY1\nZWVkZDhjNzRmMzViNw==\n','2011-05-12 18:05:42'),('5175c1e24fb093d768956ec73fa356d1','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS5lYTY3ZWQ1NTQ1ODU5OTFiMmY1\nZWVkZDhjNzRmMzViNw==\n','2011-05-12 21:11:43'),('2890ed4227d2d007bd8990a12bdc2606','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS5lYTY3ZWQ1NTQ1ODU5OTFiMmY1\nZWVkZDhjNzRmMzViNw==\n','2011-05-12 21:16:30'),('99d6c1a78b0e7a5bafd0b3285bb807a5','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS5lYTY3ZWQ1NTQ1ODU5OTFiMmY1\nZWVkZDhjNzRmMzViNw==\n','2011-05-12 22:06:06'),('f3a5abb910ce42231dd5a2a23f3a23fb','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS5lYTY3ZWQ1NTQ1ODU5OTFiMmY1\nZWVkZDhjNzRmMzViNw==\n','2011-05-13 13:30:23'),('f8c407eaf9ace2f8d425782b061ebb6c','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS5lYTY3ZWQ1NTQ1ODU5OTFiMmY1\nZWVkZDhjNzRmMzViNw==\n','2011-05-13 15:13:06'),('e0abbbbc29f9de52331ab8a734e734b7','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS5lYTY3ZWQ1NTQ1ODU5OTFiMmY1\nZWVkZDhjNzRmMzViNw==\n','2011-05-14 14:12:53'),('c0cd028666542f722fb4c880af01d764','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS5lYTY3ZWQ1NTQ1ODU5OTFiMmY1\nZWVkZDhjNzRmMzViNw==\n','2011-05-14 16:00:21'),('5dce70f0b90136779038c13e471e4781','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS5lYTY3ZWQ1NTQ1ODU5OTFiMmY1\nZWVkZDhjNzRmMzViNw==\n','2011-06-16 16:21:54'),('ef3b8c22f859de5218cf4ce269f1fbc0','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS5lYTY3ZWQ1NTQ1ODU5OTFiMmY1\nZWVkZDhjNzRmMzViNw==\n','2011-05-17 14:38:22'),('54303967bf3f1df96cfc80b682c2b9d7','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS5lYTY3ZWQ1NTQ1ODU5OTFiMmY1\nZWVkZDhjNzRmMzViNw==\n','2011-05-24 20:16:33'),('e018bfffb7c9d521459ebcfcbe58546e','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS5lYTY3ZWQ1NTQ1ODU5OTFiMmY1\nZWVkZDhjNzRmMzViNw==\n','2011-05-24 23:10:01'),('f525fa386c9ba72ec8504de5513fb422','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS5lYTY3ZWQ1NTQ1ODU5OTFiMmY1\nZWVkZDhjNzRmMzViNw==\n','2011-05-25 23:03:50'),('ce5d7d747eb38b0419d03b3f9f4413c3','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS5lYTY3ZWQ1NTQ1ODU5OTFiMmY1\nZWVkZDhjNzRmMzViNw==\n','2011-05-26 22:52:25'),('4a0c9d266937386677c928f3efcadc42','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS5lYTY3ZWQ1NTQ1ODU5OTFiMmY1\nZWVkZDhjNzRmMzViNw==\n','2011-05-27 23:48:36'),('b6208e68c982b2fe4c09ee2796437c70','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS5lYTY3ZWQ1NTQ1ODU5OTFiMmY1\nZWVkZDhjNzRmMzViNw==\n','2011-06-07 13:29:03'),('7ef9fb83ad7538c65911462e8e679f6a','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS5lYTY3ZWQ1NTQ1ODU5OTFiMmY1\nZWVkZDhjNzRmMzViNw==\n','2011-06-10 22:52:13'),('238d16b9cd891a6b157763f892e1e901','gAJ9cQFVCnRlc3Rjb29raWVxAlUGd29ya2VkcQNzLjhiNzUzN2RiNDI5MTU4NTMzNjU1M2U3MDNi\nM2E0MDAy\n','2011-06-19 04:15:03'),('6e5f0f8ee4380390fe081f7d949621bd','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS5lYTY3ZWQ1NTQ1ODU5OTFiMmY1\nZWVkZDhjNzRmMzViNw==\n','2011-06-24 10:30:55'),('45dc223d1f5aa9e430e6ef09cc7a6ae0','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS5lYTY3ZWQ1NTQ1ODU5OTFiMmY1\nZWVkZDhjNzRmMzViNw==\n','2011-06-25 12:07:39');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `piece_image`
--

DROP TABLE IF EXISTS `piece_image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `piece_image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=180 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `piece_image`
--

LOCK TABLES `piece_image` WRITE;
/*!40000 ALTER TABLE `piece_image` DISABLE KEYS */;
INSERT INTO `piece_image` VALUES (20,'gallery/DSC_0283.png'),(19,'gallery/DSC_0230.png'),(18,'gallery/DSC_0141.png'),(17,'gallery/DSC_0120.png'),(16,'gallery/DSC_0041.png'),(15,'gallery/DSC_0029.png'),(14,'gallery/DSC_0021.png'),(13,'gallery/DSC_0017.png'),(12,'gallery/DSC_0005.png'),(21,'gallery/DSC_0290.png'),(22,'gallery/DSC_0304.png'),(23,'gallery/DSC_0309.png'),(24,'gallery/DSC_0962.png'),(25,'gallery/DSC_0964.png'),(26,'gallery/DSC_0977.png'),(27,'gallery/DSC_0984.png'),(28,'gallery/DSC_0992.png'),(29,'gallery/DSC_0996.png'),(30,'gallery/DSC_1000.png'),(31,'gallery/DSC_0036.png'),(32,'gallery/DSC_0733.png'),(33,'gallery/li.png'),(34,'gallery/lii.png'),(35,'gallery/fi.png'),(36,'gallery/fii.png'),(37,'gallery/fiii.png'),(38,'gallery/mi.png'),(39,'gallery/mii.png'),(40,'gallery/miii.png'),(41,'gallery/miv.png'),(42,'gallery/mv.png'),(43,'gallery/fli.png'),(44,'gallery/flii.png'),(45,'gallery/fliii.png'),(46,'gallery/fliv.png'),(47,'gallery/flv.png'),(48,'gallery/flvi.png'),(49,'gallery/qi.png'),(50,'gallery/qii.png'),(55,'gallery/robi.png'),(52,'gallery/qiv.png'),(53,'gallery/qv.png'),(54,'gallery/qvi.png'),(56,'gallery/robii.png'),(57,'gallery/robiii.png'),(58,'gallery/robai.png'),(59,'gallery/robaii.png'),(60,'gallery/robaiii.png'),(61,'gallery/robaiv.png'),(62,'gallery/robav.png'),(63,'gallery/robavi.png'),(64,'gallery/robavii.png'),(65,'gallery/robaviii.png'),(66,'gallery/robiv.png'),(67,'gallery/robix.png'),(68,'gallery/robl.png'),(69,'gallery/roblii.png'),(70,'gallery/robliii.png'),(71,'gallery/roblix.png'),(72,'gallery/robliv.png'),(73,'gallery/roblv.png'),(74,'gallery/roblvi.png'),(75,'gallery/roblvii.png'),(76,'gallery/roblviii.png'),(77,'gallery/roblxi.png'),(78,'gallery/roblxii.png'),(79,'gallery/roblxiii.png'),(80,'gallery/roblxiv.png'),(81,'gallery/roblxv.png'),(82,'gallery/roblxvi.png'),(83,'gallery/roblxvii.png'),(84,'gallery/roblxviii.png'),(85,'gallery/robv.png'),(86,'gallery/robvi.png'),(87,'gallery/robvii.png'),(88,'gallery/robviii.png'),(89,'gallery/robx.png'),(90,'gallery/robxi.png'),(91,'gallery/robxii.png'),(92,'gallery/robxiii.png'),(93,'gallery/robxiv.png'),(94,'gallery/robxix.png'),(95,'gallery/robxl.png'),(96,'gallery/robxli.png'),(97,'gallery/robxlii.png'),(98,'gallery/robxliii.png'),(99,'gallery/robxliv.png'),(100,'gallery/robxlv.png'),(101,'gallery/robxlvi.png'),(102,'gallery/robxlvii.png'),(103,'gallery/robxlviii.png'),(104,'gallery/robxlvix.png'),(105,'gallery/robxv.png'),(106,'gallery/robxv_1.png'),(107,'gallery/robxvi.png'),(108,'gallery/robxvii.png'),(109,'gallery/robxviii.png'),(110,'gallery/robxx.png'),(111,'gallery/robxxi.png'),(112,'gallery/robxxii.png'),(113,'gallery/robxxiii.png'),(114,'gallery/robxxiv.png'),(115,'gallery/robxxix.png'),(116,'gallery/robxxv.png'),(117,'gallery/robxxvi.png'),(118,'gallery/robxxvii.png'),(119,'gallery/robxxviii.png'),(120,'gallery/robxxx.png'),(121,'gallery/robxxxi.png'),(122,'gallery/robxxxii.png'),(123,'gallery/robxxxiii.png'),(124,'gallery/robxxxiv.png'),(125,'gallery/robxxxix.png'),(126,'gallery/robxxxv.png'),(127,'gallery/robxxxvi.png'),(128,'gallery/robxxxvii.png'),(129,'gallery/robxxxviii.png'),(130,'gallery/chefai.png'),(131,'gallery/chefaii.png'),(132,'gallery/chefaiii.png'),(133,'gallery/chefaiv.png'),(134,'gallery/chefav.png'),(135,'gallery/chefavi.png'),(136,'gallery/chefavii.png'),(137,'gallery/chefaviii.png'),(138,'gallery/magai.png'),(139,'gallery/magaii.png'),(140,'gallery/magaiii.png'),(141,'gallery/magaiv.png'),(142,'gallery/magav.png'),(143,'gallery/magavi.png'),(144,'gallery/magavii.png'),(145,'gallery/magaviii.png'),(146,'gallery/propler_head1.png'),(147,'gallery/propler_head2.png'),(148,'gallery/propler_head1_1.png'),(149,'gallery/propler_head2_1.png'),(150,'gallery/propler_head1_2.png'),(151,'gallery/propler_head1_3.png'),(152,'gallery/propler_head2_2.png'),(153,'gallery/propler_head1_4.png'),(154,'gallery/propler_head2_3.png'),(155,'gallery/propler_head2_4.png'),(156,'gallery/propler_head1_5.png'),(157,'gallery/propler_head2_5.png'),(158,'gallery/propler_head1_6.png'),(159,'gallery/propler_head2_6.png'),(160,'gallery/propler_head1_7.png'),(161,'gallery/propler_head2_7.png'),(162,'gallery/img-7.png'),(163,'gallery/img-7_1.png'),(164,'gallery/img-13.png'),(165,'gallery/img-10.png'),(166,'gallery/img-10_1.png'),(167,'gallery/img-7_2.png'),(168,'gallery/img-7_3.png'),(169,'gallery/img-15.png'),(170,'gallery/img-8.png'),(171,'gallery/img-9.png'),(172,'gallery/img-9_1.png'),(173,'gallery/img-19.png'),(174,'gallery/img-7_4.png'),(175,'gallery/img-5.png'),(176,'gallery/img-7_5.png'),(177,'gallery/img-26.png'),(178,'gallery/img-9_2.png'),(179,'gallery/img-2.png');
/*!40000 ALTER TABLE `piece_image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `piece_piece`
--

DROP TABLE IF EXISTS `piece_piece`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `piece_piece` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(400) NOT NULL,
  `default_image_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `price` int(10) unsigned DEFAULT NULL,
  `slug` varchar(160) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `piece_piece_28c69cb4` (`default_image_id`),
  KEY `piece_piece_56ae2a2a` (`slug`)
) ENGINE=MyISAM AUTO_INCREMENT=184 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `piece_piece`
--

LOCK TABLES `piece_piece` WRITE;
/*!40000 ALTER TABLE `piece_piece` DISABLE KEYS */;
INSERT INTO `piece_piece` VALUES (18,'vii',18,'2011-05-11',NULL,'vii'),(17,'vi',17,'2011-05-11',NULL,'vi'),(16,'v',16,'2011-05-11',NULL,'v'),(15,'iv',15,'2011-05-11',NULL,'iv'),(14,'iii',14,'2011-05-11',NULL,'iii'),(13,'ii',13,'2011-05-11',NULL,'ii'),(12,'i',12,NULL,NULL,'i'),(20,'viii',19,'2011-05-11',NULL,'viii'),(21,'ix',20,'2011-05-12',NULL,'ix'),(22,'x',21,'2011-05-12',NULL,'x'),(23,'xi',22,'2011-05-12',NULL,'xi'),(24,'xii',23,'2011-05-12',NULL,'xii'),(25,'xiii',24,'2011-05-12',NULL,'xiii'),(26,'xiv',25,'2011-05-12',NULL,'xiv'),(27,'xv',26,'2011-05-12',NULL,'xv'),(28,'xvi',27,'2011-05-12',NULL,'xvi'),(29,'xvii',28,'2011-05-12',NULL,'xvii'),(30,'xviii',29,'2011-05-12',NULL,'xviii'),(31,'xix',30,'2011-05-12',NULL,'xix'),(33,'xx',31,'2011-05-12',NULL,'xx'),(35,'a',32,'2011-05-12',NULL,'a'),(36,'b',33,'2011-05-12',NULL,'b'),(37,'c',34,'2011-05-12',NULL,'c'),(38,'fi',35,'2011-05-12',NULL,'fi'),(39,'fii',36,'2011-05-12',NULL,'fii'),(40,'fiii',37,'2011-05-12',NULL,'fiii'),(41,'mi',38,'2011-05-12',NULL,'mi'),(42,'mii',39,'2011-05-12',NULL,'mii'),(43,'miii',40,'2011-05-12',NULL,'miii'),(44,'miv',41,'2011-05-12',NULL,'miv'),(45,'mv',42,'2011-05-12',NULL,'mv'),(46,'fli',43,'2011-05-12',NULL,'fli'),(47,'flii',44,'2011-05-12',NULL,'flii'),(48,'fliii',45,'2011-05-12',NULL,'fliii'),(49,'fliv',46,'2011-05-12',NULL,'fliv'),(50,'flv',47,'2011-05-12',NULL,'flv'),(51,'flvi',48,'2011-05-12',NULL,'flvi'),(52,'qi',49,'2011-05-13',NULL,'qi'),(53,'qii',50,'2011-05-13',NULL,'qii'),(67,'robaiv',63,'2011-05-28',20,'robaiv'),(55,'qiv',52,'2011-05-13',NULL,'qiv'),(56,'qv',53,'2011-05-13',NULL,'qv'),(57,'qvi',54,'2011-05-14',NULL,'qvi'),(66,'robaiii',60,'2011-05-28',20,'robaiii'),(65,'robaii',59,'2011-05-28',20,'robaii'),(64,'robai',58,'2011-05-28',20,'robai'),(68,'robav',62,'2011-05-28',20,'robav'),(69,'robavi',63,'2011-05-28',20,'robavi'),(70,'robavii',64,'2011-05-28',20,'robavii'),(71,'robaviii',65,'2011-05-28',20,'robaviii'),(72,'robi',55,'2011-05-28',20,'robi'),(73,'robii',56,'2011-05-28',20,'robii'),(74,'robiii',57,'2011-05-28',20,'robiii'),(75,'robiv',66,'2011-05-28',20,'robiv'),(76,'robix',67,'2011-05-28',20,'robix'),(77,'robl',68,'2011-05-28',20,'robl'),(78,'roblii',69,'2011-05-28',20,'roblii'),(79,'robliii',70,'2011-05-28',20,'robliii'),(80,'robliv',72,'2011-05-28',20,'robliv'),(81,'roblix',71,'2011-05-28',20,'roblix'),(82,'roblv',73,'2011-05-28',20,'roblv'),(83,'roblvi',74,'2011-05-28',20,'roblvi'),(84,'roblvii',75,'2011-05-28',20,'roblvii'),(85,'roblviii',76,'2011-05-28',20,'roblviii'),(86,'roblxi',77,'2011-05-28',20,'roblxi'),(87,'roblxii',78,'2011-05-28',20,'roblxii'),(88,'roblxiii',79,'2011-05-28',20,'roblxiii'),(89,'roblxiv',80,'2011-05-28',20,'roblxiv'),(90,'roblxv',81,'2011-05-28',20,'roblxv'),(91,'roblxvi',82,'2011-05-28',20,'roblxvi'),(92,'roblxvii',83,'2011-05-28',20,'roblxvii'),(93,'roblxviii',84,'2011-05-28',20,'roblxviii'),(94,'robv',85,'2011-05-28',20,'robv'),(95,'robvi',86,'2011-05-28',20,'robvi'),(96,'robvii',87,'2011-05-28',20,'robvii'),(97,'robviii',88,'2011-05-28',20,'robviii'),(98,'robxi',90,'2011-05-28',20,'robxi'),(99,'robxii',91,'2011-05-29',20,'robxii'),(100,'robxiii',92,'2011-05-29',20,'robxiii'),(101,'robxiv',93,'2011-05-29',20,'robxiv'),(102,'robxix',94,'2011-05-29',20,'robxix'),(103,'robxl',95,'2011-05-29',20,'robxl'),(104,'robxli',96,'2011-05-29',20,'robxli'),(105,'robxlii',97,'2011-05-29',20,'robxlii'),(106,'robxliii',98,'2011-05-29',20,'robxliii'),(107,'robxliv',99,'2011-05-29',20,'robxliv'),(108,'roblxvi',100,'2011-05-29',20,'roblxvi'),(109,'robxlvii',102,'2011-05-29',20,'robxlvii'),(110,'robxlviii',103,'2011-05-29',20,'robxlviii'),(111,'robxlvix',104,'2011-05-29',20,'robxlvix'),(112,'robxv',105,'2011-05-29',20,'robxv'),(113,'robxvi',107,'2011-05-29',20,'robxvi'),(114,'robxvii',108,'2011-05-29',20,'robxvii'),(115,'robxviii',109,'2011-05-29',20,'robxviii'),(117,'robxx',110,'2011-05-29',20,'robxx'),(118,'robxxi',111,'2011-05-29',20,'robxxi'),(119,'robxxii',112,'2011-05-29',20,'robxxii'),(120,'robxxiii',113,'2011-05-29',20,'robxxiii'),(121,'robxxiv',114,'2011-05-29',20,'robxxiv'),(122,'robxxix',115,'2011-05-29',20,'robxxix'),(123,'robxxv',116,'2011-05-29',20,'robxxv'),(124,'robxxvi',117,'2011-05-29',20,'robxxvi'),(125,'robxxvii',118,'2011-05-29',20,'robxxvii'),(126,'robxxviii',119,'2011-05-29',20,'robxxviii'),(127,'robxxx',120,'2011-05-29',20,'robxxx'),(128,'robxxxi',121,'2011-05-29',20,'robxxxi'),(129,'robxxxii',122,'2011-05-29',20,'robxxxii'),(130,'robxxxiii',123,'2011-05-29',20,'robxxxiii'),(131,'robxxxiv',124,'2011-05-29',20,'robxxxiv'),(132,'robxxxix',125,'2011-05-29',20,'robxxxix'),(133,'robxxxv',126,'2011-05-29',20,'robxxxv'),(134,'robxxxvi',127,'2011-05-29',20,'robxxxvi'),(135,'robxxxvii',128,'2011-05-29',20,'robxxxvii'),(136,'robxxxviii',129,'2011-05-29',20,'robxxxviii'),(137,'chefai',130,'2011-06-02',NULL,'chefai'),(138,'chefaii',131,'2011-06-02',NULL,'chefaii'),(139,'chefaiii',132,'2011-06-02',NULL,'chefaiii'),(140,'chefaiv',133,'2011-06-02',NULL,'chefaiv'),(141,'chefav',134,'2011-06-02',NULL,'chefav'),(142,'chefavi',135,'2011-06-02',NULL,'chefavi'),(143,'chefavii',136,'2011-06-02',NULL,'chefavii'),(144,'chefaviii',137,'2011-06-02',NULL,'chefaviii'),(145,'magai',138,'2011-06-02',NULL,'magai'),(146,'magaii',139,'2011-06-02',NULL,'magaii'),(147,'magaiii',140,'2011-06-02',NULL,'magaiii'),(148,'magaiv',141,'2011-06-02',NULL,'magaiv'),(149,'magav',142,'2011-06-02',NULL,'magav'),(150,'magavi',143,'2011-06-02',NULL,'magavi'),(151,'magavii',144,'2011-06-02',NULL,'magavii'),(152,'magaviii',145,'2011-06-02',NULL,'magaviii'),(153,'robx',89,'2011-06-10',20,'robx'),(178,'yes',174,NULL,NULL,'yes'),(179,'now',175,NULL,NULL,'now'),(180,'sdfsdafdfsda',176,NULL,NULL,'sdfsdafdfsda'),(181,'dasfdfadsfsdf',177,NULL,NULL,'dasfdfadsfsdf'),(177,'bbbbb',172,NULL,NULL,'bbbbb'),(176,'dsafdssdf',170,NULL,NULL,'dsafdssdf'),(175,'asdfd',169,NULL,NULL,'asdfd'),(174,'new',168,NULL,NULL,'new'),(173,'foo',173,NULL,NULL,'foo'),(182,'dsfdsafsd',178,NULL,NULL,'dsfdsafsd'),(183,'finally',179,NULL,NULL,'finally');
/*!40000 ALTER TABLE `piece_piece` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `piece_piece_series`
--

DROP TABLE IF EXISTS `piece_piece_series`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `piece_piece_series` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `piece_id` int(11) NOT NULL,
  `series_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `piece_id` (`piece_id`,`series_id`),
  KEY `piece_piece_series_2419b34d` (`piece_id`),
  KEY `piece_piece_series_b18a98d` (`series_id`)
) ENGINE=MyISAM AUTO_INCREMENT=196 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `piece_piece_series`
--

LOCK TABLES `piece_piece_series` WRITE;
/*!40000 ALTER TABLE `piece_piece_series` DISABLE KEYS */;
INSERT INTO `piece_piece_series` VALUES (28,20,3),(26,18,3),(25,17,3),(24,16,3),(23,15,3),(22,14,3),(21,13,3),(29,21,3),(20,12,3),(30,22,3),(31,23,3),(32,24,3),(33,25,3),(34,26,3),(35,27,3),(36,28,3),(37,29,3),(38,30,3),(39,31,3),(41,33,3),(43,35,7),(44,36,7),(45,37,7),(46,38,9),(47,39,9),(48,40,9),(49,41,10),(50,42,10),(51,43,10),(52,44,10),(53,45,10),(54,46,11),(55,47,11),(56,48,11),(57,49,11),(58,50,11),(59,51,11),(60,52,12),(61,53,12),(77,68,13),(63,55,12),(64,56,12),(65,57,12),(76,67,13),(75,66,13),(74,65,13),(73,64,13),(78,69,13),(79,70,13),(80,71,13),(81,72,13),(82,73,13),(83,74,13),(84,75,13),(85,76,13),(86,77,13),(87,78,13),(88,79,13),(89,80,13),(90,81,13),(91,82,13),(92,83,13),(93,84,13),(94,85,13),(95,86,13),(96,87,13),(97,88,13),(98,89,13),(99,90,13),(100,91,13),(101,92,13),(102,93,13),(103,94,13),(104,95,13),(105,96,13),(106,97,13),(107,98,13),(108,99,13),(109,100,13),(110,101,13),(111,102,13),(112,103,13),(113,104,13),(114,106,13),(115,107,13),(116,108,13),(117,109,13),(118,110,13),(119,111,13),(120,112,13),(121,113,13),(122,114,13),(123,115,13),(125,117,13),(126,118,13),(127,119,13),(128,120,13),(129,121,13),(130,122,13),(131,123,13),(132,124,13),(133,125,13),(134,126,13),(135,127,13),(136,128,13),(137,129,13),(138,130,13),(139,131,13),(140,132,13),(141,133,13),(142,134,13),(143,135,13),(144,136,13),(145,137,14),(146,138,14),(147,139,14),(148,140,14),(149,141,14),(150,142,14),(151,143,14),(152,144,14),(153,145,15),(154,146,15),(155,147,15),(156,148,15),(157,149,15),(158,150,15),(159,151,15),(160,152,15),(161,153,13),(186,176,26),(188,177,27),(193,181,23),(192,180,23),(191,179,23),(190,178,23),(185,175,25),(184,174,24),(189,173,23),(194,182,23),(195,183,28);
/*!40000 ALTER TABLE `piece_piece_series` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `piece_series`
--

DROP TABLE IF EXISTS `piece_series`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `piece_series` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(400) NOT NULL,
  `description` longtext,
  `slug` varchar(160) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `piece_series_56ae2a2a` (`slug`)
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `piece_series`
--

LOCK TABLES `piece_series` WRITE;
/*!40000 ALTER TABLE `piece_series` DISABLE KEYS */;
INSERT INTO `piece_series` VALUES (3,'synchronization','','synchronization'),(7,'left','','left'),(9,'fantasy','','fantasy'),(10,'eclipse','','eclipse'),(11,'flash','','flash'),(12,'queen','','queen'),(13,'robing','','robing'),(14,'chef','raekwon showed up and ripped the stage. \'nuff said.','chef'),(15,'magic','some nights are just full of good times','magic'),(28,'yeppp','','yeppp'),(27,'fun',NULL,'fun'),(26,'aaaaaa',NULL,'aaaaaa'),(25,'yes',NULL,'yes'),(24,'foo',NULL,'foo'),(23,'bar',NULL,'bar');
/*!40000 ALTER TABLE `piece_series` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2011-06-27 17:48:09
