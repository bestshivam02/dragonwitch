-- MariaDB dump 10.19  Distrib 10.6.7-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: Denwear
-- ------------------------------------------------------
-- Server version	10.6.7-MariaDB-3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Products_productimages`
--

DROP TABLE IF EXISTS `Products_productimages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Products_productimages` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) DEFAULT NULL,
  `product_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Products_productimages_product_id_74e30105_fk_tbl_product_id` (`product_id`),
  CONSTRAINT `Products_productimages_product_id_74e30105_fk_tbl_product_id` FOREIGN KEY (`product_id`) REFERENCES `tbl_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Products_productimages`
--

LOCK TABLES `Products_productimages` WRITE;
/*!40000 ALTER TABLE `Products_productimages` DISABLE KEYS */;
INSERT INTO `Products_productimages` VALUES (1,'product_img/1_z0OGmAj.png',2),(2,'product_img/Image_8Py5mV3.png',3),(3,'product_img/joggers_oZyJN3B.png',4),(4,'product_img/1_OSq6DVq.png',5),(5,'product_img/1_Df5CPpX.png',1);
/*!40000 ALTER TABLE `Products_productimages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
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
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=189 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add site',6,'add_site'),(22,'Can change site',6,'change_site'),(23,'Can delete site',6,'delete_site'),(24,'Can view site',6,'view_site'),(25,'Can add flat page',7,'add_flatpage'),(26,'Can change flat page',7,'change_flatpage'),(27,'Can delete flat page',7,'delete_flatpage'),(28,'Can view flat page',7,'view_flatpage'),(29,'Can add Token',8,'add_token'),(30,'Can change Token',8,'change_token'),(31,'Can delete Token',8,'delete_token'),(32,'Can view Token',8,'view_token'),(33,'Can add token',9,'add_tokenproxy'),(34,'Can change token',9,'change_tokenproxy'),(35,'Can delete token',9,'delete_tokenproxy'),(36,'Can view token',9,'view_tokenproxy'),(37,'Can add user',10,'add_user'),(38,'Can change user',10,'change_user'),(39,'Can delete user',10,'delete_user'),(40,'Can view user',10,'view_user'),(41,'Can add transaction',11,'add_transaction'),(42,'Can change transaction',11,'change_transaction'),(43,'Can delete transaction',11,'delete_transaction'),(44,'Can view transaction',11,'view_transaction'),(45,'Can add device',12,'add_device'),(46,'Can change device',12,'change_device'),(47,'Can delete device',12,'delete_device'),(48,'Can view device',12,'view_device'),(49,'Can add user address',13,'add_useraddress'),(50,'Can change user address',13,'change_useraddress'),(51,'Can delete user address',13,'delete_useraddress'),(52,'Can view user address',13,'view_useraddress'),(53,'Can add category',14,'add_category'),(54,'Can change category',14,'change_category'),(55,'Can delete category',14,'delete_category'),(56,'Can view category',14,'view_category'),(57,'Can add product',15,'add_product'),(58,'Can change product',15,'change_product'),(59,'Can delete product',15,'delete_product'),(60,'Can view product',15,'view_product'),(61,'Can add product rating',16,'add_productrating'),(62,'Can change product rating',16,'change_productrating'),(63,'Can delete product rating',16,'delete_productrating'),(64,'Can view product rating',16,'view_productrating'),(65,'Can add user wish list',17,'add_userwishlist'),(66,'Can change user wish list',17,'change_userwishlist'),(67,'Can delete user wish list',17,'delete_userwishlist'),(68,'Can view user wish list',17,'view_userwishlist'),(69,'Can add user order history',18,'add_userorderhistory'),(70,'Can change user order history',18,'change_userorderhistory'),(71,'Can delete user order history',18,'delete_userorderhistory'),(72,'Can view user order history',18,'view_userorderhistory'),(73,'Can add user cart',19,'add_usercart'),(74,'Can change user cart',19,'change_usercart'),(75,'Can delete user cart',19,'delete_usercart'),(76,'Can view user cart',19,'view_usercart'),(77,'Can add product review',20,'add_productreview'),(78,'Can change product review',20,'change_productreview'),(79,'Can delete product review',20,'delete_productreview'),(80,'Can view product review',20,'view_productreview'),(81,'Can add product category',21,'add_productcategory'),(82,'Can change product category',21,'change_productcategory'),(83,'Can delete product category',21,'delete_productcategory'),(84,'Can view product category',21,'view_productcategory'),(85,'Can add color',22,'add_color'),(86,'Can change color',22,'change_color'),(87,'Can delete color',22,'delete_color'),(88,'Can view color',22,'view_color'),(89,'Can add design',23,'add_design'),(90,'Can change design',23,'change_design'),(91,'Can delete design',23,'delete_design'),(92,'Can view design',23,'view_design'),(93,'Can add material',24,'add_material'),(94,'Can change material',24,'change_material'),(95,'Can delete material',24,'delete_material'),(96,'Can view material',24,'view_material'),(97,'Can add product images',25,'add_productimages'),(98,'Can change product images',25,'change_productimages'),(99,'Can delete product images',25,'delete_productimages'),(100,'Can view product images',25,'view_productimages'),(101,'Can add size',26,'add_size'),(102,'Can change size',26,'change_size'),(103,'Can delete size',26,'delete_size'),(104,'Can view size',26,'view_size'),(105,'Can add product size',27,'add_productsize'),(106,'Can change product size',27,'change_productsize'),(107,'Can delete product size',27,'delete_productsize'),(108,'Can view product size',27,'view_productsize'),(109,'Can add product material',28,'add_productmaterial'),(110,'Can change product material',28,'change_productmaterial'),(111,'Can delete product material',28,'delete_productmaterial'),(112,'Can view product material',28,'view_productmaterial'),(113,'Can add product design',29,'add_productdesign'),(114,'Can change product design',29,'change_productdesign'),(115,'Can delete product design',29,'delete_productdesign'),(116,'Can view product design',29,'view_productdesign'),(117,'Can add product color',30,'add_productcolor'),(118,'Can change product color',30,'change_productcolor'),(119,'Can delete product color',30,'delete_productcolor'),(120,'Can view product color',30,'view_productcolor'),(121,'Can add user order',31,'add_userorder'),(122,'Can change user order',31,'change_userorder'),(123,'Can delete user order',31,'delete_userorder'),(124,'Can view user order',31,'view_userorder'),(125,'Can add user custom design',32,'add_usercustomdesign'),(126,'Can change user custom design',32,'change_usercustomdesign'),(127,'Can delete user custom design',32,'delete_usercustomdesign'),(128,'Can view user custom design',32,'view_usercustomdesign'),(129,'Can add user custom product order',33,'add_usercustomproductorder'),(130,'Can change user custom product order',33,'change_usercustomproductorder'),(131,'Can delete user custom product order',33,'delete_usercustomproductorder'),(132,'Can view user custom product order',33,'view_usercustomproductorder'),(133,'Can add promo code',34,'add_promocode'),(134,'Can change promo code',34,'change_promocode'),(135,'Can delete promo code',34,'delete_promocode'),(136,'Can view promo code',34,'view_promocode'),(137,'Can add user promo code',35,'add_userpromocode'),(138,'Can change user promo code',35,'change_userpromocode'),(139,'Can delete user promo code',35,'delete_userpromocode'),(140,'Can view user promo code',35,'view_userpromocode'),(141,'Can add category banner',36,'add_categorybanner'),(142,'Can change category banner',36,'change_categorybanner'),(143,'Can delete category banner',36,'delete_categorybanner'),(144,'Can view category banner',36,'view_categorybanner'),(145,'Can add main carousel',37,'add_maincarousel'),(146,'Can change main carousel',37,'change_maincarousel'),(147,'Can delete main carousel',37,'delete_maincarousel'),(148,'Can view main carousel',37,'view_maincarousel'),(149,'Can add sale banner',38,'add_salebanner'),(150,'Can change sale banner',38,'change_salebanner'),(151,'Can delete sale banner',38,'delete_salebanner'),(152,'Can view sale banner',38,'view_salebanner'),(153,'Can add countdown banner',39,'add_countdownbanner'),(154,'Can change countdown banner',39,'change_countdownbanner'),(155,'Can delete countdown banner',39,'delete_countdownbanner'),(156,'Can view countdown banner',39,'view_countdownbanner'),(157,'Can add custome shirt banner',40,'add_customeshirtbanner'),(158,'Can change custome shirt banner',40,'change_customeshirtbanner'),(159,'Can delete custome shirt banner',40,'delete_customeshirtbanner'),(160,'Can view custome shirt banner',40,'view_customeshirtbanner'),(161,'Can add testimonials',41,'add_testimonials'),(162,'Can change testimonials',41,'change_testimonials'),(163,'Can delete testimonials',41,'delete_testimonials'),(164,'Can view testimonials',41,'view_testimonials'),(165,'Can add contact us',42,'add_contactus'),(166,'Can change contact us',42,'change_contactus'),(167,'Can delete contact us',42,'delete_contactus'),(168,'Can view contact us',42,'view_contactus'),(169,'Can add contact info',43,'add_contactinfo'),(170,'Can change contact info',43,'change_contactinfo'),(171,'Can delete contact info',43,'delete_contactinfo'),(172,'Can view contact info',43,'view_contactinfo'),(173,'Can add home faq',44,'add_homefaq'),(174,'Can change home faq',44,'change_homefaq'),(175,'Can delete home faq',44,'delete_homefaq'),(176,'Can view home faq',44,'view_homefaq'),(177,'Can add user dashboard module',45,'add_userdashboardmodule'),(178,'Can change user dashboard module',45,'change_userdashboardmodule'),(179,'Can delete user dashboard module',45,'delete_userdashboardmodule'),(180,'Can view user dashboard module',45,'view_userdashboardmodule'),(181,'Can add bookmark',46,'add_bookmark'),(182,'Can change bookmark',46,'change_bookmark'),(183,'Can delete bookmark',46,'delete_bookmark'),(184,'Can view bookmark',46,'view_bookmark'),(185,'Can add pinned application',47,'add_pinnedapplication'),(186,'Can change pinned application',47,'change_pinnedapplication'),(187,'Can delete pinned application',47,'delete_pinnedapplication'),(188,'Can view pinned application',47,'view_pinnedapplication');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_tbl_user_id` FOREIGN KEY (`user_id`) REFERENCES `tbl_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authtoken_token`
--

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
INSERT INTO `authtoken_token` VALUES ('48ee8817f977eefafd39e0e2630fe2a188644e79','2022-05-09 05:10:58.202404',1),('4d0e9c52e54cf7a0de810dcc5c7bf5ba0739fe3b','2022-05-09 05:10:45.960914',2),('820910c5e84c64f3f487853c50091a175fa8ed60','2022-05-12 07:29:46.340157',3);
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dashboard_userdashboardmodule`
--

DROP TABLE IF EXISTS `dashboard_userdashboardmodule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dashboard_userdashboardmodule` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `module` varchar(255) NOT NULL,
  `app_label` varchar(255) DEFAULT NULL,
  `user` int(10) unsigned NOT NULL CHECK (`user` >= 0),
  `column` int(10) unsigned NOT NULL CHECK (`column` >= 0),
  `order` int(11) NOT NULL,
  `settings` longtext NOT NULL,
  `children` longtext NOT NULL,
  `collapsed` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dashboard_userdashboardmodule`
--

LOCK TABLES `dashboard_userdashboardmodule` WRITE;
/*!40000 ALTER TABLE `dashboard_userdashboardmodule` DISABLE KEYS */;
/*!40000 ALTER TABLE `dashboard_userdashboardmodule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_tbl_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_tbl_user_id` FOREIGN KEY (`user_id`) REFERENCES `tbl_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2022-05-09 05:14:14.670698','1','admin',2,'[{\"changed\": {\"fields\": [\"Role id\"]}}]',10,1),(2,'2022-05-09 05:22:44.660550','1','MainCarousel object (1)',1,'[{\"added\": {}}]',37,1),(3,'2022-05-09 05:23:31.285186','2','MainCarousel object (2)',1,'[{\"added\": {}}]',37,1),(4,'2022-05-09 05:23:45.803534','3','MainCarousel object (3)',1,'[{\"added\": {}}]',37,1),(5,'2022-05-09 05:26:00.419344','1','SaleBanner object (1)',1,'[{\"added\": {}}]',38,1),(6,'2022-05-09 05:27:06.391113','2','SaleBanner object (2)',1,'[{\"added\": {}}]',38,1),(7,'2022-05-09 05:27:31.599935','3','SaleBanner object (3)',1,'[{\"added\": {}}]',38,1),(8,'2022-05-09 05:27:50.460937','2','SaleBanner object (2)',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',38,1),(9,'2022-05-09 05:32:47.865501','1','Category object (1)',1,'[{\"added\": {}}]',14,1),(10,'2022-05-09 05:33:58.475708','1','shirt',1,'[{\"added\": {}}]',15,1),(11,'2022-05-09 05:34:49.088941','1','CountdownBanner object (1)',1,'[{\"added\": {}}]',39,1),(12,'2022-05-09 05:37:06.631083','1','CustomeShirtBanner object (1)',1,'[{\"added\": {}}]',40,1),(13,'2022-05-09 05:41:14.515965','2','CustomeShirtBanner object (2)',1,'[{\"added\": {}}]',40,1),(14,'2022-05-09 05:41:35.539419','2','CustomeShirtBanner object (2)',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',40,1),(15,'2022-05-09 05:44:02.725205','2','CustomeShirtBanner object (2)',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',40,1),(16,'2022-05-09 05:44:30.129214','1','CategoryBanner object (1)',1,'[{\"added\": {}}]',36,1),(17,'2022-05-09 05:44:51.986351','2','CustomeShirtBanner object (2)',3,'',40,1),(18,'2022-05-09 05:45:43.885586','1','CustomeShirtBanner object (1)',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',40,1),(19,'2022-05-09 05:46:42.239919','2','CategoryBanner object (2)',1,'[{\"added\": {}}]',36,1),(20,'2022-05-09 05:46:53.705917','3','CategoryBanner object (3)',1,'[{\"added\": {}}]',36,1),(21,'2022-05-09 05:47:06.461700','4','CategoryBanner object (4)',1,'[{\"added\": {}}]',36,1),(22,'2022-05-09 05:47:17.110107','5','CategoryBanner object (5)',1,'[{\"added\": {}}]',36,1),(23,'2022-05-09 05:48:56.011221','2','Category object (2)',1,'[{\"added\": {}}]',14,1),(24,'2022-05-09 05:49:34.894416','3','Category object (3)',1,'[{\"added\": {}}]',14,1),(25,'2022-05-09 05:49:58.072079','4','Category object (4)',1,'[{\"added\": {}}]',14,1),(26,'2022-05-09 05:55:23.597865','9','Design object (9)',3,'',23,1),(27,'2022-05-09 05:55:23.604540','8','Design object (8)',3,'',23,1),(28,'2022-05-09 05:55:23.606034','7','Design object (7)',3,'',23,1),(29,'2022-05-09 05:55:23.606988','6','Design object (6)',3,'',23,1),(30,'2022-05-09 05:55:23.607681','5','Design object (5)',3,'',23,1),(31,'2022-05-09 06:50:24.705401','1','PromoCode object (1)',1,'[{\"added\": {}}]',34,1),(32,'2022-05-09 06:54:23.841079','1','admin',2,'[{\"changed\": {\"fields\": [\"Full name\", \"First name\"]}}]',10,1),(33,'2022-05-09 12:27:14.999808','1','ProductRating object (1)',2,'[{\"changed\": {\"fields\": [\"Rating star\"]}}]',16,1),(34,'2022-05-09 12:27:30.680379','1','ProductReview object (1)',2,'[{\"changed\": {\"fields\": [\"Rating\", \"Rating star\"]}}]',20,1),(35,'2022-05-09 12:27:37.051274','1','ProductRating object (1)',2,'[]',16,1),(36,'2022-05-09 12:28:00.684032','2','ProductRating object (2)',2,'[{\"changed\": {\"fields\": [\"Rating star\"]}}]',16,1),(37,'2022-05-09 12:28:14.775315','2','ProductReview object (2)',2,'[{\"changed\": {\"fields\": [\"Rating\", \"Rating star\"]}}]',20,1),(38,'2022-05-12 07:25:37.834585','2','ProductRating object (2)',2,'[{\"changed\": {\"fields\": [\"Rating star\"]}}]',16,1),(39,'2022-05-12 07:25:45.909460','3','ProductReview object (3)',3,'',20,1),(40,'2022-05-12 07:27:47.698951','4','ProductReview object (4)',3,'',20,1),(41,'2022-05-12 07:27:52.428840','2','ProductRating object (2)',3,'',16,1),(42,'2022-05-12 07:28:08.115431','6','ProductRating object (6)',3,'',16,1),(43,'2022-05-12 07:28:14.685575','5','ProductRating object (5)',3,'',16,1),(44,'2022-05-12 07:31:32.193000','7','ProductRating object (7)',3,'',16,1),(45,'2022-05-12 07:31:44.593254','6','ProductReview object (6)',3,'',20,1),(46,'2022-05-12 07:31:54.306113','5','ProductReview object (5)',2,'[{\"changed\": {\"fields\": [\"Rating star\"]}}]',20,1),(47,'2022-05-12 07:32:01.345744','8','ProductRating object (8)',2,'[{\"changed\": {\"fields\": [\"Rating star\"]}}]',16,1),(48,'2022-05-12 07:32:22.147412','5','ProductReview object (5)',2,'[{\"changed\": {\"fields\": [\"User\"]}}]',20,1),(49,'2022-05-12 07:40:22.000478','8','ProductRating object (8)',2,'[{\"changed\": {\"fields\": [\"Rating star\"]}}]',16,1),(50,'2022-05-12 07:40:29.123467','7','ProductReview object (7)',3,'',20,1),(51,'2022-05-12 09:33:04.918862','1','shirt',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',15,1),(52,'2022-05-12 09:33:42.502046','5','ProductImages object (5)',1,'[{\"added\": {}}]',25,1),(53,'2022-05-12 09:50:31.299660','5','ProductImages object (5)',2,'[{\"changed\": {\"fields\": [\"Product_image\"]}}]',25,1),(54,'2022-05-12 09:50:59.814837','1','ProductImages object (1)',2,'[{\"changed\": {\"fields\": [\"Product_image\"]}}]',25,1),(55,'2022-05-12 09:51:24.882443','2','product2',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',15,1);
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
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (12,'accounts','device'),(11,'accounts','transaction'),(10,'accounts','user'),(13,'accounts','useraddress'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(8,'authtoken','token'),(9,'authtoken','tokenproxy'),(4,'contenttypes','contenttype'),(45,'dashboard','userdashboardmodule'),(7,'flatpages','flatpage'),(36,'frontend','categorybanner'),(43,'frontend','contactinfo'),(42,'frontend','contactus'),(39,'frontend','countdownbanner'),(40,'frontend','customeshirtbanner'),(44,'frontend','homefaq'),(37,'frontend','maincarousel'),(38,'frontend','salebanner'),(41,'frontend','testimonials'),(46,'jet','bookmark'),(47,'jet','pinnedapplication'),(14,'Products','category'),(22,'Products','color'),(23,'Products','design'),(24,'Products','material'),(15,'Products','product'),(21,'Products','productcategory'),(30,'Products','productcolor'),(29,'Products','productdesign'),(25,'Products','productimages'),(28,'Products','productmaterial'),(16,'Products','productrating'),(20,'Products','productreview'),(27,'Products','productsize'),(34,'Products','promocode'),(26,'Products','size'),(19,'Products','usercart'),(32,'Products','usercustomdesign'),(33,'Products','usercustomproductorder'),(31,'Products','userorder'),(18,'Products','userorderhistory'),(35,'Products','userpromocode'),(17,'Products','userwishlist'),(5,'sessions','session'),(6,'sites','site');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_flatpage`
--

DROP TABLE IF EXISTS `django_flatpage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_flatpage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(100) NOT NULL,
  `title` varchar(200) NOT NULL,
  `content` longtext NOT NULL,
  `enable_comments` tinyint(1) NOT NULL,
  `template_name` varchar(70) NOT NULL,
  `registration_required` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_flatpage_url_41612362` (`url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_flatpage`
--

LOCK TABLES `django_flatpage` WRITE;
/*!40000 ALTER TABLE `django_flatpage` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_flatpage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_flatpage_sites`
--

DROP TABLE IF EXISTS `django_flatpage_sites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_flatpage_sites` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `flatpage_id` int(11) NOT NULL,
  `site_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_flatpage_sites_flatpage_id_site_id_0d29d9d1_uniq` (`flatpage_id`,`site_id`),
  KEY `django_flatpage_sites_site_id_bfd8ea84_fk_django_site_id` (`site_id`),
  CONSTRAINT `django_flatpage_sites_flatpage_id_078bbc8b_fk_django_flatpage_id` FOREIGN KEY (`flatpage_id`) REFERENCES `django_flatpage` (`id`),
  CONSTRAINT `django_flatpage_sites_site_id_bfd8ea84_fk_django_site_id` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_flatpage_sites`
--

LOCK TABLES `django_flatpage_sites` WRITE;
/*!40000 ALTER TABLE `django_flatpage_sites` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_flatpage_sites` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=88 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-05-09 04:26:41.360421'),(2,'contenttypes','0002_remove_content_type_name','2022-05-09 04:26:41.378447'),(3,'auth','0001_initial','2022-05-09 04:26:41.439656'),(4,'auth','0002_alter_permission_name_max_length','2022-05-09 04:26:41.452418'),(5,'auth','0003_alter_user_email_max_length','2022-05-09 04:26:41.456350'),(6,'auth','0004_alter_user_username_opts','2022-05-09 04:26:41.461295'),(7,'auth','0005_alter_user_last_login_null','2022-05-09 04:26:41.464067'),(8,'auth','0006_require_contenttypes_0002','2022-05-09 04:26:41.464970'),(9,'auth','0007_alter_validators_add_error_messages','2022-05-09 04:26:41.467623'),(10,'auth','0008_alter_user_username_max_length','2022-05-09 04:26:41.470410'),(11,'auth','0009_alter_user_last_name_max_length','2022-05-09 04:26:41.473101'),(12,'auth','0010_alter_group_name_max_length','2022-05-09 04:26:41.479939'),(13,'auth','0011_update_proxy_permissions','2022-05-09 04:26:41.483116'),(14,'auth','0012_alter_user_first_name_max_length','2022-05-09 04:26:41.485784'),(15,'accounts','0001_initial','2022-05-09 04:26:41.630538'),(16,'accounts','0002_auto_20220404_0431','2022-05-09 04:26:41.671125'),(17,'accounts','0003_auto_20220406_0720','2022-05-09 04:26:41.750906'),(18,'accounts','0004_alter_user_profile_pic','2022-05-09 04:26:41.761193'),(19,'accounts','0005_auto_20220428_0547','2022-05-09 04:26:41.841017'),(20,'accounts','0006_alter_transaction_status','2022-05-09 04:26:41.871897'),(21,'Products','0001_initial','2022-05-09 04:26:42.085287'),(22,'Products','0002_remove_productrating_user','2022-05-09 04:26:42.109578'),(23,'Products','0003_auto_20220405_0449','2022-05-09 04:26:42.157860'),(24,'Products','0004_product_create_on','2022-05-09 04:26:42.173125'),(25,'Products','0005_product_quantity','2022-05-09 04:26:42.187764'),(26,'Products','0006_rename_staus_productcategory_status','2022-05-09 04:26:42.199984'),(27,'Products','0007_productimages','2022-05-09 04:26:42.228396'),(28,'Products','0008_auto_20220418_0736','2022-05-09 04:26:42.331868'),(29,'Products','0009_auto_20220418_0834','2022-05-09 04:26:42.442064'),(30,'Products','0010_productcolor_productdesign_productmaterial_productsize','2022-05-09 04:26:42.603899'),(31,'Products','0011_userorderhistory_slug','2022-05-09 04:26:42.629096'),(32,'Products','0012_usercart_qty','2022-05-09 04:26:42.651356'),(33,'Products','0013_alter_productreview_rating','2022-05-09 04:26:42.699057'),(34,'Products','0014_auto_20220422_1211','2022-05-09 04:26:42.732643'),(35,'Products','0015_auto_20220422_1224','2022-05-09 04:26:42.767252'),(36,'Products','0016_usercart_price','2022-05-09 04:26:42.785329'),(37,'Products','0017_auto_20220428_0547','2022-05-09 04:26:42.835140'),(38,'Products','0018_auto_20220428_0625','2022-05-09 04:26:42.973091'),(39,'Products','0019_auto_20220428_0823','2022-05-09 04:26:43.077239'),(40,'Products','0020_category_image','2022-05-09 04:26:43.088990'),(41,'Products','0021_product_additional_information','2022-05-09 04:26:43.099387'),(42,'Products','0022_usercustomorder','2022-05-09 04:26:43.131389'),(43,'Products','0023_auto_20220504_0849','2022-05-09 04:26:43.214786'),(44,'Products','0024_auto_20220504_0858','2022-05-09 04:26:43.279927'),(45,'Products','0025_auto_20220504_0955','2022-05-09 04:26:43.367447'),(46,'Products','0026_auto_20220504_0955','2022-05-09 04:26:43.443135'),(47,'Products','0027_rename_create_by_usercustomdesign_created_by','2022-05-09 04:26:43.478384'),(48,'Products','0028_auto_20220504_1005','2022-05-09 04:26:43.536829'),(49,'Products','0029_auto_20220504_1034','2022-05-09 04:26:43.582888'),(50,'Products','0030_usercustomdesign_is_active','2022-05-09 04:26:43.603995'),(51,'Products','0031_userorderhistory_has_delivered','2022-05-09 04:26:43.625117'),(52,'Products','0032_promocode_userpromocode','2022-05-09 04:26:43.702432'),(53,'Products','0033_promocode_is_active','2022-05-09 04:26:43.714265'),(54,'Products','0034_promocode_percentage','2022-05-09 04:26:43.726652'),(55,'Products','0035_remove_userpromocode_slug','2022-05-09 04:26:43.744904'),(56,'admin','0001_initial','2022-05-09 04:26:43.844830'),(57,'admin','0002_logentry_remove_auto_add','2022-05-09 04:26:43.854195'),(58,'admin','0003_logentry_add_action_flag_choices','2022-05-09 04:26:43.862418'),(59,'authtoken','0001_initial','2022-05-09 04:26:43.889636'),(60,'authtoken','0002_auto_20160226_1747','2022-05-09 04:26:43.922953'),(61,'authtoken','0003_tokenproxy','2022-05-09 04:26:43.925151'),(62,'sites','0001_initial','2022-05-09 04:26:43.932553'),(63,'flatpages','0001_initial','2022-05-09 04:26:43.978229'),(64,'frontend','0001_initial','2022-05-09 04:26:44.024590'),(65,'frontend','0002_auto_20220405_0619','2022-05-09 04:26:44.051621'),(66,'frontend','0003_customeshirtbanner','2022-05-09 04:26:44.059526'),(67,'frontend','0004_testimonials','2022-05-09 04:26:44.087190'),(68,'frontend','0005_auto_20220425_0701','2022-05-09 04:26:44.135338'),(69,'frontend','0006_auto_20220425_1055','2022-05-09 04:26:44.176949'),(70,'frontend','0007_contactus','2022-05-09 04:26:44.207251'),(71,'frontend','0008_alter_contactus_email','2022-05-09 04:26:44.223785'),(72,'frontend','0009_contactinfo','2022-05-09 04:26:44.233297'),(73,'frontend','0010_contactinfo_image','2022-05-09 04:26:44.241419'),(74,'frontend','0011_contactinfo_is_active','2022-05-09 04:26:44.252020'),(75,'frontend','0012_alter_contactinfo_mobile_no','2022-05-09 04:26:44.260892'),(76,'frontend','0013_alter_contactinfo_email','2022-05-09 04:26:44.270457'),(77,'frontend','0014_homefaq','2022-05-09 04:26:44.278967'),(78,'sessions','0001_initial','2022-05-09 04:26:44.290431'),(79,'sites','0002_alter_domain_unique','2022-05-09 04:26:44.299745'),(80,'dashboard','0001_initial','2022-05-09 05:12:14.831375'),(81,'dashboard','0002_alter_userdashboardmodule_id','2022-05-09 05:12:14.843896'),(82,'jet','0001_initial','2022-05-09 05:12:14.865605'),(83,'jet','0002_delete_userdashboardmodule','2022-05-09 05:12:14.869798'),(84,'jet','0003_auto_20220425_0944','2022-05-09 05:12:14.890013'),(85,'Products','0036_productreview_rating_star','2022-05-09 12:18:03.232814'),(86,'accounts','0007_alter_user_role_id','2022-05-09 12:18:03.244627'),(87,'accounts','0008_useraddress_country','2022-05-12 10:54:02.470033');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
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
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('lsdc7k09gcduuxo5cyfwm7m54zmk8cbj','.eJxVizsOAiEQQO9CbTYOfyxN7LwDGYdBiMomy1IZ764mW2j7Pk8Rcawljs5LrEkcBIjdL7sg3bh9BRLNo6192tB0emC9n-drbcct-jsL9vLZWFqAnA1LY3O2oAKRdhC0dOhJ6j0Ag7EuBWITkLO3WqNSXgOFzEm83iCUNPE:1nnxJQ:WccBeITei5sVo0ofpVEtL_ZlnJgiC3SkcN3bOEv6hkU','2022-05-23 06:56:08.729947');
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
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_site_domain_a2e37b91_uniq` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
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
-- Table structure for table `jet_bookmark`
--

DROP TABLE IF EXISTS `jet_bookmark`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jet_bookmark` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `url` varchar(200) NOT NULL,
  `title` varchar(255) NOT NULL,
  `user` int(10) unsigned NOT NULL CHECK (`user` >= 0),
  `date_add` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jet_bookmark`
--

LOCK TABLES `jet_bookmark` WRITE;
/*!40000 ALTER TABLE `jet_bookmark` DISABLE KEYS */;
/*!40000 ALTER TABLE `jet_bookmark` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jet_pinnedapplication`
--

DROP TABLE IF EXISTS `jet_pinnedapplication`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jet_pinnedapplication` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(255) NOT NULL,
  `user` int(10) unsigned NOT NULL CHECK (`user` >= 0),
  `date_add` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jet_pinnedapplication`
--

LOCK TABLES `jet_pinnedapplication` WRITE;
/*!40000 ALTER TABLE `jet_pinnedapplication` DISABLE KEYS */;
/*!40000 ALTER TABLE `jet_pinnedapplication` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_category`
--

DROP TABLE IF EXISTS `tbl_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_category` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(75) NOT NULL,
  `slug` varchar(75) NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_category`
--

LOCK TABLES `tbl_category` WRITE;
/*!40000 ALTER TABLE `tbl_category` DISABLE KEYS */;
INSERT INTO `tbl_category` VALUES (1,'Upper wear','upper_wear2','category_img/banner_img.png'),(2,'lower wear','lower_wear','category_img/1.png'),(3,'jackets','','category_img/account-jkt.png'),(4,'t shirt','t_shirt','category_default.png'),(5,'shirt','shirt','category_default.png');
/*!40000 ALTER TABLE `tbl_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_category_banner`
--

DROP TABLE IF EXISTS `tbl_category_banner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_category_banner` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) DEFAULT NULL,
  `description` varchar(250) DEFAULT NULL,
  `redirect_link` varchar(250) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_category_banner`
--

LOCK TABLES `tbl_category_banner` WRITE;
/*!40000 ALTER TABLE `tbl_category_banner` DISABLE KEYS */;
INSERT INTO `tbl_category_banner` VALUES (1,'countdown_banner/Image-winter_xv2XKp9.png','category banner',NULL,1),(2,'countdown_banner/joggers_NxEQbID.png','category banner',NULL,1),(3,'countdown_banner/joggers_r0L7qRS.png','category banner 3',NULL,1),(4,'countdown_banner/Image_LMnAXId.png','category banner 4',NULL,1),(5,'countdown_banner/Image-winter_B0NVKCv.png','category banner 5',NULL,1);
/*!40000 ALTER TABLE `tbl_category_banner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_color`
--

DROP TABLE IF EXISTS `tbl_color`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_color` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(75) NOT NULL,
  `slug` varchar(75) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_color`
--

LOCK TABLES `tbl_color` WRITE;
/*!40000 ALTER TABLE `tbl_color` DISABLE KEYS */;
INSERT INTO `tbl_color` VALUES (1,'black','black'),(2,'red','red'),(3,'white','white');
/*!40000 ALTER TABLE `tbl_color` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_contact_us`
--

DROP TABLE IF EXISTS `tbl_contact_us`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_contact_us` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(300) DEFAULT NULL,
  `subject` varchar(300) DEFAULT NULL,
  `message` longtext NOT NULL,
  `email` varchar(254) DEFAULT NULL,
  `created_on` datetime(6) NOT NULL,
  `created_by_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tbl_contact_us_created_by_id_6655c34a_fk_tbl_user_id` (`created_by_id`),
  CONSTRAINT `tbl_contact_us_created_by_id_6655c34a_fk_tbl_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `tbl_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_contact_us`
--

LOCK TABLES `tbl_contact_us` WRITE;
/*!40000 ALTER TABLE `tbl_contact_us` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_contact_us` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_countdown_banner`
--

DROP TABLE IF EXISTS `tbl_countdown_banner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_countdown_banner` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) DEFAULT NULL,
  `description` varchar(250) DEFAULT NULL,
  `redirect_link` varchar(250) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `product_detail_id` bigint(20) NOT NULL,
  `sale_end_date` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tbl_countdown_banner_product_detail_id_87348839_fk_tbl_produ` (`product_detail_id`),
  CONSTRAINT `tbl_countdown_banner_product_detail_id_87348839_fk_tbl_produ` FOREIGN KEY (`product_detail_id`) REFERENCES `tbl_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_countdown_banner`
--

LOCK TABLES `tbl_countdown_banner` WRITE;
/*!40000 ALTER TABLE `tbl_countdown_banner` DISABLE KEYS */;
INSERT INTO `tbl_countdown_banner` VALUES (1,'countdown_banner/1.png','countdown poer',NULL,1,1,'2022-05-19 00:00:00.000000');
/*!40000 ALTER TABLE `tbl_countdown_banner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_custom_shirt_banner`
--

DROP TABLE IF EXISTS `tbl_custom_shirt_banner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_custom_shirt_banner` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) DEFAULT NULL,
  `description` varchar(250) DEFAULT NULL,
  `redirect_link` varchar(250) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_custom_shirt_banner`
--

LOCK TABLES `tbl_custom_shirt_banner` WRITE;
/*!40000 ALTER TABLE `tbl_custom_shirt_banner` DISABLE KEYS */;
INSERT INTO `tbl_custom_shirt_banner` VALUES (1,'countdown_banner/spcl_offr.png','custom shirt banner',NULL,1);
/*!40000 ALTER TABLE `tbl_custom_shirt_banner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_desgin`
--

DROP TABLE IF EXISTS `tbl_desgin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_desgin` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(75) NOT NULL,
  `slug` varchar(75) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_desgin`
--

LOCK TABLES `tbl_desgin` WRITE;
/*!40000 ALTER TABLE `tbl_desgin` DISABLE KEYS */;
INSERT INTO `tbl_desgin` VALUES (1,'printed','printed'),(2,'polo','polo'),(3,'cool','cool'),(4,'formal','formal');
/*!40000 ALTER TABLE `tbl_desgin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_device`
--

DROP TABLE IF EXISTS `tbl_device`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_device` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `device_type` int(10) unsigned DEFAULT NULL CHECK (`device_type` >= 0),
  `device_name` varchar(50) DEFAULT NULL,
  `device_token` varchar(500) DEFAULT NULL,
  `created_by_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `created_by_id` (`created_by_id`),
  CONSTRAINT `tbl_device_created_by_id_c3de8e14_fk_tbl_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `tbl_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_device`
--

LOCK TABLES `tbl_device` WRITE;
/*!40000 ALTER TABLE `tbl_device` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_device` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_home_faq`
--

DROP TABLE IF EXISTS `tbl_home_faq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_home_faq` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `question` varchar(300) DEFAULT NULL,
  `answer` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_home_faq`
--

LOCK TABLES `tbl_home_faq` WRITE;
/*!40000 ALTER TABLE `tbl_home_faq` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_home_faq` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_main_carousel`
--

DROP TABLE IF EXISTS `tbl_main_carousel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_main_carousel` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) DEFAULT NULL,
  `description` varchar(650) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `redirect_link` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_main_carousel`
--

LOCK TABLES `tbl_main_carousel` WRITE;
/*!40000 ALTER TABLE `tbl_main_carousel` DISABLE KEYS */;
INSERT INTO `tbl_main_carousel` VALUES (1,'main_carousel/Image_Banner_N8bn41U.png','main banner 1',1,NULL),(2,'main_carousel/Image_Banner_rT5w70r.png','main banner 2',1,NULL),(3,'main_carousel/Image_Banner_0bADwIa.png','main banner 3',1,NULL);
/*!40000 ALTER TABLE `tbl_main_carousel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_material`
--

DROP TABLE IF EXISTS `tbl_material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_material` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(75) NOT NULL,
  `slug` varchar(75) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_material`
--

LOCK TABLES `tbl_material` WRITE;
/*!40000 ALTER TABLE `tbl_material` DISABLE KEYS */;
INSERT INTO `tbl_material` VALUES (1,'cotton','cotton'),(2,'wool','wool'),(3,'silk','silk');
/*!40000 ALTER TABLE `tbl_material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_our_contact_info`
--

DROP TABLE IF EXISTS `tbl_our_contact_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_our_contact_info` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(300) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `mobile_no` varchar(16) DEFAULT NULL,
  `created_on` datetime(6) NOT NULL,
  `updated_on` datetime(6) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_our_contact_info`
--

LOCK TABLES `tbl_our_contact_info` WRITE;
/*!40000 ALTER TABLE `tbl_our_contact_info` DISABLE KEYS */;
INSERT INTO `tbl_our_contact_info` VALUES (1,'Denwear','dummy@gmail.com','999999999','2022-05-09 05:15:19.924964','2022-05-09 05:15:19.924981','our_contact_info_img/den-logo-12-change_c853WyW.png',1);
/*!40000 ALTER TABLE `tbl_our_contact_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_product`
--

DROP TABLE IF EXISTS `tbl_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_product` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `price` bigint(20) unsigned NOT NULL CHECK (`price` >= 0),
  `discount_price` bigint(20) unsigned DEFAULT NULL CHECK (`discount_price` >= 0),
  `description` longtext DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  `slug` varchar(150) NOT NULL,
  `size` int(10) unsigned NOT NULL CHECK (`size` >= 0),
  `create_on` datetime(6) NOT NULL,
  `quantity` int(10) unsigned NOT NULL CHECK (`quantity` >= 0),
  `additional_information` longtext DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_product`
--

LOCK TABLES `tbl_product` WRITE;
/*!40000 ALTER TABLE `tbl_product` DISABLE KEYS */;
INSERT INTO `tbl_product` VALUES (1,'shirt',54,54,'good shirt','product_img/1_fWIZ6FU.png','shirt_1',2,'2022-05-09 05:33:58.474236',10,'very good shirt'),(2,'product2',55,55,'productproductproductproductproductproductproductproductproductproductproductproduct','product_img/1_HJIIh3u.png','product2',2,'2022-05-09 06:04:25.619097',20,''),(3,'potato',55,54,'productproductproductproduct','product_img/Image.png','potato',2,'2022-05-09 06:23:42.801962',56,NULL),(4,'blue shirt',21,12,'productproductproductproductproduct','product_img/joggers_5GeEP3C.png','blue shirt',2,'2022-05-09 06:24:39.123024',11,NULL),(5,'sonu ',33,33,'productproductproductproductproduct','product_img/1_xfkXUig.png','sonu ',2,'2022-05-09 06:27:40.194839',21,NULL);
/*!40000 ALTER TABLE `tbl_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_product_category`
--

DROP TABLE IF EXISTS `tbl_product_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_product_category` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `status` tinyint(1) NOT NULL,
  `category_id` bigint(20) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  `quantity` int(10) unsigned NOT NULL CHECK (`quantity` >= 0),
  PRIMARY KEY (`id`),
  KEY `tbl_product_category_category_id_8cd3a31b_fk_tbl_category_id` (`category_id`),
  KEY `tbl_product_category_product_id_92a11cf1_fk_tbl_product_id` (`product_id`),
  CONSTRAINT `tbl_product_category_category_id_8cd3a31b_fk_tbl_category_id` FOREIGN KEY (`category_id`) REFERENCES `tbl_category` (`id`),
  CONSTRAINT `tbl_product_category_product_id_92a11cf1_fk_tbl_product_id` FOREIGN KEY (`product_id`) REFERENCES `tbl_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_product_category`
--

LOCK TABLES `tbl_product_category` WRITE;
/*!40000 ALTER TABLE `tbl_product_category` DISABLE KEYS */;
INSERT INTO `tbl_product_category` VALUES (1,1,1,2,20),(2,1,3,3,56),(3,1,4,4,11),(4,1,1,5,21);
/*!40000 ALTER TABLE `tbl_product_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_product_color`
--

DROP TABLE IF EXISTS `tbl_product_color`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_product_color` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `status` tinyint(1) NOT NULL,
  `color_id` bigint(20) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  `quantity` int(10) unsigned NOT NULL CHECK (`quantity` >= 0),
  PRIMARY KEY (`id`),
  KEY `tbl_product_color_color_id_4b00361e_fk_tbl_color_id` (`color_id`),
  KEY `tbl_product_color_product_id_5d4d1f85_fk_tbl_product_id` (`product_id`),
  CONSTRAINT `tbl_product_color_color_id_4b00361e_fk_tbl_color_id` FOREIGN KEY (`color_id`) REFERENCES `tbl_color` (`id`),
  CONSTRAINT `tbl_product_color_product_id_5d4d1f85_fk_tbl_product_id` FOREIGN KEY (`product_id`) REFERENCES `tbl_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_product_color`
--

LOCK TABLES `tbl_product_color` WRITE;
/*!40000 ALTER TABLE `tbl_product_color` DISABLE KEYS */;
INSERT INTO `tbl_product_color` VALUES (1,1,2,3,56),(2,1,1,4,11),(3,1,3,4,11),(4,1,2,5,21);
/*!40000 ALTER TABLE `tbl_product_color` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_product_design`
--

DROP TABLE IF EXISTS `tbl_product_design`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_product_design` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `status` tinyint(1) NOT NULL,
  `design_id` bigint(20) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  `quantity` int(10) unsigned NOT NULL CHECK (`quantity` >= 0),
  PRIMARY KEY (`id`),
  KEY `tbl_product_design_design_id_9d18b4a0_fk_tbl_desgin_id` (`design_id`),
  KEY `tbl_product_design_product_id_d002eb50_fk_tbl_product_id` (`product_id`),
  CONSTRAINT `tbl_product_design_design_id_9d18b4a0_fk_tbl_desgin_id` FOREIGN KEY (`design_id`) REFERENCES `tbl_desgin` (`id`),
  CONSTRAINT `tbl_product_design_product_id_d002eb50_fk_tbl_product_id` FOREIGN KEY (`product_id`) REFERENCES `tbl_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_product_design`
--

LOCK TABLES `tbl_product_design` WRITE;
/*!40000 ALTER TABLE `tbl_product_design` DISABLE KEYS */;
INSERT INTO `tbl_product_design` VALUES (1,1,1,2,20),(2,1,1,3,56),(3,1,3,3,56),(4,1,1,4,11),(5,1,3,4,11),(6,1,1,5,21),(7,1,2,5,22);
/*!40000 ALTER TABLE `tbl_product_design` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_product_material`
--

DROP TABLE IF EXISTS `tbl_product_material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_product_material` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `status` tinyint(1) NOT NULL,
  `material_id` bigint(20) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  `quantity` int(10) unsigned NOT NULL CHECK (`quantity` >= 0),
  PRIMARY KEY (`id`),
  KEY `tbl_product_material_material_id_6586f7ef_fk_tbl_material_id` (`material_id`),
  KEY `tbl_product_material_product_id_97305372_fk_tbl_product_id` (`product_id`),
  CONSTRAINT `tbl_product_material_material_id_6586f7ef_fk_tbl_material_id` FOREIGN KEY (`material_id`) REFERENCES `tbl_material` (`id`),
  CONSTRAINT `tbl_product_material_product_id_97305372_fk_tbl_product_id` FOREIGN KEY (`product_id`) REFERENCES `tbl_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_product_material`
--

LOCK TABLES `tbl_product_material` WRITE;
/*!40000 ALTER TABLE `tbl_product_material` DISABLE KEYS */;
INSERT INTO `tbl_product_material` VALUES (1,1,1,2,20),(2,1,1,3,56),(3,1,3,3,56),(4,1,1,4,11),(5,1,3,4,11),(6,1,2,5,21);
/*!40000 ALTER TABLE `tbl_product_material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_product_rating`
--

DROP TABLE IF EXISTS `tbl_product_rating`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_product_rating` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `rating_star` double DEFAULT NULL,
  `product_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tbl_product_rating_product_id_c25cd196_fk_tbl_product_id` (`product_id`),
  CONSTRAINT `tbl_product_rating_product_id_c25cd196_fk_tbl_product_id` FOREIGN KEY (`product_id`) REFERENCES `tbl_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_product_rating`
--

LOCK TABLES `tbl_product_rating` WRITE;
/*!40000 ALTER TABLE `tbl_product_rating` DISABLE KEYS */;
INSERT INTO `tbl_product_rating` VALUES (1,3.2,2),(3,0,4),(4,0,5),(8,4,3);
/*!40000 ALTER TABLE `tbl_product_rating` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_product_review`
--

DROP TABLE IF EXISTS `tbl_product_review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_product_review` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `review` longtext DEFAULT NULL,
  `product_id` bigint(20) NOT NULL,
  `rating_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  `title` varchar(100) DEFAULT NULL,
  `created_on` datetime(6) NOT NULL,
  `updated_on` datetime(6) NOT NULL,
  `rating_star` double DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tbl_product_review_product_id_7afad6cc_fk_tbl_product_id` (`product_id`),
  KEY `tbl_product_review_user_id_a38b5b8c_fk_tbl_user_id` (`user_id`),
  KEY `tbl_product_review_rating_id_0df0fc1b_fk_tbl_product_rating_id` (`rating_id`),
  CONSTRAINT `tbl_product_review_product_id_7afad6cc_fk_tbl_product_id` FOREIGN KEY (`product_id`) REFERENCES `tbl_product` (`id`),
  CONSTRAINT `tbl_product_review_rating_id_0df0fc1b_fk_tbl_product_rating_id` FOREIGN KEY (`rating_id`) REFERENCES `tbl_product_rating` (`id`),
  CONSTRAINT `tbl_product_review_user_id_a38b5b8c_fk_tbl_user_id` FOREIGN KEY (`user_id`) REFERENCES `tbl_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_product_review`
--

LOCK TABLES `tbl_product_review` WRITE;
/*!40000 ALTER TABLE `tbl_product_review` DISABLE KEYS */;
INSERT INTO `tbl_product_review` VALUES (1,'dhfhdhhfhdkfhsfhdskfkasl',2,1,1,'bahut badiya','2022-05-09 07:23:44.325131','2022-05-09 07:23:44.325210',3),(5,'wwwwwwwwwwwwwwwwwwwwwwwwwe',3,NULL,3,'wwwwwwwwwwwwwwwwwwwwwwwwwww','2022-05-12 07:28:47.900770','2022-05-12 07:28:47.900864',2),(8,'SSSSSSSSSSSSS',3,NULL,1,'SSSSSSSSS','2022-05-12 07:40:44.406718','2022-05-12 07:40:44.406863',5);
/*!40000 ALTER TABLE `tbl_product_review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_product_size`
--

DROP TABLE IF EXISTS `tbl_product_size`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_product_size` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `status` tinyint(1) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  `size_id` bigint(20) NOT NULL,
  `quantity` int(10) unsigned NOT NULL CHECK (`quantity` >= 0),
  PRIMARY KEY (`id`),
  KEY `tbl_product_size_product_id_e53ac2c3_fk_tbl_product_id` (`product_id`),
  KEY `tbl_product_size_size_id_9efb0a84_fk_tbl_size_id` (`size_id`),
  CONSTRAINT `tbl_product_size_product_id_e53ac2c3_fk_tbl_product_id` FOREIGN KEY (`product_id`) REFERENCES `tbl_product` (`id`),
  CONSTRAINT `tbl_product_size_size_id_9efb0a84_fk_tbl_size_id` FOREIGN KEY (`size_id`) REFERENCES `tbl_size` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_product_size`
--

LOCK TABLES `tbl_product_size` WRITE;
/*!40000 ALTER TABLE `tbl_product_size` DISABLE KEYS */;
INSERT INTO `tbl_product_size` VALUES (1,1,3,1,56),(2,1,3,2,56),(3,1,4,2,11),(4,1,4,3,11),(5,1,5,1,21),(6,1,5,3,22);
/*!40000 ALTER TABLE `tbl_product_size` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_promo_code`
--

DROP TABLE IF EXISTS `tbl_promo_code`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_promo_code` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(75) NOT NULL,
  `slug` varchar(75) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `percentage` bigint(20) unsigned NOT NULL CHECK (`percentage` >= 0),
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_promo_code`
--

LOCK TABLES `tbl_promo_code` WRITE;
/*!40000 ALTER TABLE `tbl_promo_code` DISABLE KEYS */;
INSERT INTO `tbl_promo_code` VALUES (1,'fiftyshifty','fifty_shifty',1,50);
/*!40000 ALTER TABLE `tbl_promo_code` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_sale_banner`
--

DROP TABLE IF EXISTS `tbl_sale_banner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_sale_banner` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) DEFAULT NULL,
  `description` varchar(250) DEFAULT NULL,
  `discounts` varchar(250) DEFAULT NULL,
  `redirect_link` varchar(250) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_sale_banner`
--

LOCK TABLES `tbl_sale_banner` WRITE;
/*!40000 ALTER TABLE `tbl_sale_banner` DISABLE KEYS */;
INSERT INTO `tbl_sale_banner` VALUES (1,'sale_banner/banner_img.png','sale banner 1','50%',NULL,1),(2,'sale_banner/Image-winter_dZKMiBN.png','sale banner type 2','60%',NULL,1),(3,'sale_banner/Image-winter.png','sale banner type 3','40%',NULL,1);
/*!40000 ALTER TABLE `tbl_sale_banner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_size`
--

DROP TABLE IF EXISTS `tbl_size`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_size` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(75) NOT NULL,
  `slug` varchar(75) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_size`
--

LOCK TABLES `tbl_size` WRITE;
/*!40000 ALTER TABLE `tbl_size` DISABLE KEYS */;
INSERT INTO `tbl_size` VALUES (1,'s','s'),(2,'m','m'),(3,'l','l'),(4,'xl','xl');
/*!40000 ALTER TABLE `tbl_size` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_testimonials`
--

DROP TABLE IF EXISTS `tbl_testimonials`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_testimonials` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(300) DEFAULT NULL,
  `review` longtext NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `created_on` datetime(6) NOT NULL,
  `created_by_id` bigint(20) NOT NULL,
  `rating_star` double DEFAULT NULL,
  `update_by_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tbl_testimonials_created_by_id_178dee13_fk_tbl_user_id` (`created_by_id`),
  KEY `tbl_testimonials_update_by_id_b9985324_fk_tbl_user_id` (`update_by_id`),
  CONSTRAINT `tbl_testimonials_created_by_id_178dee13_fk_tbl_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `tbl_user` (`id`),
  CONSTRAINT `tbl_testimonials_update_by_id_b9985324_fk_tbl_user_id` FOREIGN KEY (`update_by_id`) REFERENCES `tbl_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_testimonials`
--

LOCK TABLES `tbl_testimonials` WRITE;
/*!40000 ALTER TABLE `tbl_testimonials` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_testimonials` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_transaction`
--

DROP TABLE IF EXISTS `tbl_transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_transaction` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `amount` varchar(255) DEFAULT NULL,
  `transactio_id` varchar(255) DEFAULT NULL,
  `receipt` varchar(255) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`data`)),
  `created_on` datetime(6) NOT NULL,
  `created_by_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tbl_transaction_created_by_id_478b67fe_fk_tbl_user_id` (`created_by_id`),
  CONSTRAINT `tbl_transaction_created_by_id_478b67fe_fk_tbl_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `tbl_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_transaction`
--

LOCK TABLES `tbl_transaction` WRITE;
/*!40000 ALTER TABLE `tbl_transaction` DISABLE KEYS */;
INSERT INTO `tbl_transaction` VALUES (1,'516.0','pi_3KxQR6SAfluecUvn1IYgNV2R','',0,'{\"id\": \"cs_test_b1yssIoPB0fvQqKQtsTgJl5tk38pj40lcULwRwWbDZQqSnX3aBr5Ie4ySo\", \"object\": \"checkout.session\", \"after_expiration\": null, \"allow_promotion_codes\": null, \"amount_subtotal\": 51600, \"amount_total\": 51600, \"automatic_tax\": {\"enabled\": false, \"status\": null}, \"billing_address_collection\": null, \"cancel_url\": \"http://localhost:8000/cancelled/\", \"client_reference_id\": \"1\", \"consent\": null, \"consent_collection\": null, \"currency\": \"inr\", \"customer\": null, \"customer_creation\": \"always\", \"customer_details\": null, \"customer_email\": null, \"expires_at\": 1652165476, \"livemode\": false, \"locale\": null, \"metadata\": {}, \"mode\": \"payment\", \"payment_intent\": \"pi_3KxQR6SAfluecUvn1IYgNV2R\", \"payment_link\": null, \"payment_method_options\": {}, \"payment_method_types\": [\"card\"], \"payment_status\": \"unpaid\", \"phone_number_collection\": {\"enabled\": false}, \"recovered_from\": null, \"setup_intent\": null, \"shipping\": null, \"shipping_address_collection\": null, \"shipping_options\": [], \"shipping_rate\": null, \"status\": \"open\", \"submit_type\": null, \"subscription\": null, \"success_url\": \"http://localhost:8000/order_placed?session_id={CHECKOUT_SESSION_ID}\", \"total_details\": {\"amount_discount\": 0, \"amount_shipping\": 0, \"amount_tax\": 0}, \"url\": \"https://checkout.stripe.com/pay/cs_test_b1yssIoPB0fvQqKQtsTgJl5tk38pj40lcULwRwWbDZQqSnX3aBr5Ie4ySo#fidkdWxOYHwnPyd1blpxYHZxWjA0TnRzPU9WRGNpcGBmUHNraGtpT1xScHQxN1ZscjxJZ0E0M0FGNlJ2fWpnYHZPQVIxMTZGMjZoXHJvV213PVxoQmxMYERATD1wVkNhUEp0U2liXDU3TE1KNTVMZmI8fWdidScpJ2N3amhWYHdzYHcnP3F3cGApJ2lkfGpwcVF8dWAnPydocGlxbFpscWBoJyknYGtkZ2lgVWlkZmBtamlhYHd2Jz9xd3BgeCUl\"}','2022-05-09 06:51:17.133022',1),(2,'516.0','pi_3KxQUwSAfluecUvn0Fq7GRQG','',0,'{\"id\": \"cs_test_b1FV8oudPKF0xt2Xvk5nKXq0mnSPtbfG2pMJs3Y0lMYNDaKook95mU7Tdo\", \"object\": \"checkout.session\", \"after_expiration\": null, \"allow_promotion_codes\": null, \"amount_subtotal\": 51600, \"amount_total\": 51600, \"automatic_tax\": {\"enabled\": false, \"status\": null}, \"billing_address_collection\": null, \"cancel_url\": \"http://localhost:8000/cancelled/\", \"client_reference_id\": \"1\", \"consent\": null, \"consent_collection\": null, \"currency\": \"inr\", \"customer\": null, \"customer_creation\": \"always\", \"customer_details\": null, \"customer_email\": null, \"expires_at\": 1652165714, \"livemode\": false, \"locale\": null, \"metadata\": {}, \"mode\": \"payment\", \"payment_intent\": \"pi_3KxQUwSAfluecUvn0Fq7GRQG\", \"payment_link\": null, \"payment_method_options\": {}, \"payment_method_types\": [\"card\"], \"payment_status\": \"unpaid\", \"phone_number_collection\": {\"enabled\": false}, \"recovered_from\": null, \"setup_intent\": null, \"shipping\": null, \"shipping_address_collection\": null, \"shipping_options\": [], \"shipping_rate\": null, \"status\": \"open\", \"submit_type\": null, \"subscription\": null, \"success_url\": \"http://localhost:8000/order_placed?session_id={CHECKOUT_SESSION_ID}\", \"total_details\": {\"amount_discount\": 0, \"amount_shipping\": 0, \"amount_tax\": 0}, \"url\": \"https://checkout.stripe.com/pay/cs_test_b1FV8oudPKF0xt2Xvk5nKXq0mnSPtbfG2pMJs3Y0lMYNDaKook95mU7Tdo#fidkdWxOYHwnPyd1blpxYHZxWjA0TnRzPU9WRGNpcGBmUHNraGtpT1xScHQxN1ZscjxJZ0E0M0FGNlJ2fWpnYHZPQVIxMTZGMjZoXHJvV213PVxoQmxMYERATD1wVkNhUEp0U2liXDU3TE1KNTVMZmI8fWdidScpJ2N3amhWYHdzYHcnP3F3cGApJ2lkfGpwcVF8dWAnPydocGlxbFpscWBoJyknYGtkZ2lgVWlkZmBtamlhYHd2Jz9xd3BgeCUl\"}','2022-05-09 06:55:14.708021',1),(3,'28.0','pi_3KxQYuSAfluecUvn1HgaBDzr','',1,'{\"id\": \"cs_test_b14NXauiLB37UuIKPbWj5RJtBOVasDsJyqeUabOyoR5Ps7t6BTaKebudOI\", \"object\": \"checkout.session\", \"after_expiration\": null, \"allow_promotion_codes\": null, \"amount_subtotal\": 2800, \"amount_total\": 2800, \"automatic_tax\": {\"enabled\": false, \"status\": null}, \"billing_address_collection\": null, \"cancel_url\": \"http://localhost:8000/cancelled/\", \"client_reference_id\": \"1\", \"consent\": null, \"consent_collection\": null, \"currency\": \"inr\", \"customer\": null, \"customer_creation\": \"always\", \"customer_details\": null, \"customer_email\": null, \"expires_at\": 1652165960, \"livemode\": false, \"locale\": null, \"metadata\": {}, \"mode\": \"payment\", \"payment_intent\": \"pi_3KxQYuSAfluecUvn1HgaBDzr\", \"payment_link\": null, \"payment_method_options\": {}, \"payment_method_types\": [\"card\"], \"payment_status\": \"unpaid\", \"phone_number_collection\": {\"enabled\": false}, \"recovered_from\": null, \"setup_intent\": null, \"shipping\": null, \"shipping_address_collection\": null, \"shipping_options\": [], \"shipping_rate\": null, \"status\": \"open\", \"submit_type\": null, \"subscription\": null, \"success_url\": \"http://localhost:8000/order_placed?session_id={CHECKOUT_SESSION_ID}\", \"total_details\": {\"amount_discount\": 0, \"amount_shipping\": 0, \"amount_tax\": 0}, \"url\": \"https://checkout.stripe.com/pay/cs_test_b14NXauiLB37UuIKPbWj5RJtBOVasDsJyqeUabOyoR5Ps7t6BTaKebudOI#fidkdWxOYHwnPyd1blpxYHZxWjA0TnRzPU9WRGNpcGBmUHNraGtpT1xScHQxN1ZscjxJZ0E0M0FGNlJ2fWpnYHZPQVIxMTZGMjZoXHJvV213PVxoQmxMYERATD1wVkNhUEp0U2liXDU3TE1KNTVMZmI8fWdidScpJ2N3amhWYHdzYHcnP3F3cGApJ2lkfGpwcVF8dWAnPydocGlxbFpscWBoJyknYGtkZ2lgVWlkZmBtamlhYHd2Jz9xd3BgeCUl\"}','2022-05-09 06:59:21.080839',1);
/*!40000 ALTER TABLE `tbl_transaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user`
--

DROP TABLE IF EXISTS `tbl_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `password` varchar(150) DEFAULT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `username` varchar(150) DEFAULT NULL,
  `full_name` varchar(150) DEFAULT NULL,
  `first_name` varchar(150) DEFAULT NULL,
  `last_name` varchar(150) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `mobile_no` varchar(16) DEFAULT NULL,
  `profile_pic` varchar(100) DEFAULT NULL,
  `role_id` int(10) unsigned NOT NULL CHECK (`role_id` >= 0),
  `created_on` datetime(6) NOT NULL,
  `updated_on` datetime(6) NOT NULL,
  `dob` varchar(150) DEFAULT NULL,
  `verification_code` varchar(25) DEFAULT NULL,
  `secondary_mobile_no` varchar(16) DEFAULT NULL,
  `otp_verifY` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `mobile_no` (`mobile_no`),
  UNIQUE KEY `secondary_mobile_no` (`secondary_mobile_no`),
  UNIQUE KEY `tbl_user_password_42650e25_uniq` (`password`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user`
--

LOCK TABLES `tbl_user` WRITE;
/*!40000 ALTER TABLE `tbl_user` DISABLE KEYS */;
INSERT INTO `tbl_user` VALUES (1,'pbkdf2_sha256$260000$MhVG3VvAi9Vb05EZnV2qeC$mysOdvZLDivoLQQna41IKNxBJYNjJ4IBzWKqvTfZPww=','2022-05-12 07:30:35.432436',1,1,1,'2022-05-09 05:10:11.000000','admin','Nitish','Nitish',NULL,'admin@gmail.com','22222222','default.png',1,'2022-05-09 05:10:11.442263','2022-05-09 05:10:11.442274',NULL,NULL,NULL,0),(2,'pbkdf2_sha256$260000$z2KRZsoxryfIAcH0UFUARj$1QZu7DNTk1HyJl8UICHrvvAZSgHZ5lI3ZGD7C8C6dq8=','2022-05-09 05:10:45.951169',0,0,1,'2022-05-09 05:10:36.889316','nitish@gmail.com','Nitish',NULL,NULL,'nitish@gmail.com','8989898989','default.png',3,'2022-05-09 05:10:36.889586','2022-05-09 05:10:36.889595',NULL,NULL,NULL,0),(3,'pbkdf2_sha256$260000$iS33yFQF1cQg91HLfGCZNO$WZ37uHyqFmn8oQHDHww0FTeQ4uog7F2/Z64jM5RaF4U=','2022-05-12 07:29:46.319436',0,0,1,'2022-05-12 07:29:40.760044','2@gmail.com','222222222222222',NULL,NULL,'2@gmail.com','07087376726','default.png',3,'2022-05-12 07:29:40.760421','2022-05-12 07:29:40.760431',NULL,NULL,NULL,0);
/*!40000 ALTER TABLE `tbl_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_address`
--

DROP TABLE IF EXISTS `tbl_user_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_user_address` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `address` varchar(150) DEFAULT NULL,
  `city` varchar(150) DEFAULT NULL,
  `state` varchar(150) DEFAULT NULL,
  `zipcode` varchar(150) DEFAULT NULL,
  `created_on` datetime(6) NOT NULL,
  `updated_on` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `country` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tbl_user_address_user_id_a159aeb0_fk_tbl_user_id` (`user_id`),
  CONSTRAINT `tbl_user_address_user_id_a159aeb0_fk_tbl_user_id` FOREIGN KEY (`user_id`) REFERENCES `tbl_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_address`
--

LOCK TABLES `tbl_user_address` WRITE;
/*!40000 ALTER TABLE `tbl_user_address` DISABLE KEYS */;
INSERT INTO `tbl_user_address` VALUES (3,'George H. Washington','Mohali','Punjab','152122','2022-05-12 10:54:27.504056','2022-05-12 10:54:27.504114',1,'india');
/*!40000 ALTER TABLE `tbl_user_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_cart`
--

DROP TABLE IF EXISTS `tbl_user_cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_user_cart` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `product_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `qty` int(11) NOT NULL,
  `price` bigint(20) unsigned NOT NULL CHECK (`price` >= 0),
  `size_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tbl_user_cart_product_id_9a28f47d_fk_tbl_product_id` (`product_id`),
  KEY `tbl_user_cart_user_id_9b5e4851_fk_tbl_user_id` (`user_id`),
  KEY `tbl_user_cart_size_id_7195ed77_fk_tbl_size_id` (`size_id`),
  CONSTRAINT `tbl_user_cart_product_id_9a28f47d_fk_tbl_product_id` FOREIGN KEY (`product_id`) REFERENCES `tbl_product` (`id`),
  CONSTRAINT `tbl_user_cart_size_id_7195ed77_fk_tbl_size_id` FOREIGN KEY (`size_id`) REFERENCES `tbl_size` (`id`),
  CONSTRAINT `tbl_user_cart_user_id_9b5e4851_fk_tbl_user_id` FOREIGN KEY (`user_id`) REFERENCES `tbl_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_cart`
--

LOCK TABLES `tbl_user_cart` WRITE;
/*!40000 ALTER TABLE `tbl_user_cart` DISABLE KEYS */;
INSERT INTO `tbl_user_cart` VALUES (2,3,1,2,110,1);
/*!40000 ALTER TABLE `tbl_user_cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_custom_design`
--

DROP TABLE IF EXISTS `tbl_user_custom_design`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_user_custom_design` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `product_image` longtext DEFAULT NULL,
  `front_desing` longtext DEFAULT NULL,
  `back_desing` longtext DEFAULT NULL,
  `created_on` datetime(6) NOT NULL,
  `slug` varchar(75) NOT NULL,
  `created_by_id` bigint(20) NOT NULL,
  `amount` int(11) NOT NULL,
  `name` varchar(75) DEFAULT NULL,
  `qty` int(11) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `tbl_user_custom_design_created_by_id_a7469804_fk_tbl_user_id` (`created_by_id`),
  CONSTRAINT `tbl_user_custom_design_created_by_id_a7469804_fk_tbl_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `tbl_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_custom_design`
--

LOCK TABLES `tbl_user_custom_design` WRITE;
/*!40000 ALTER TABLE `tbl_user_custom_design` DISABLE KEYS */;
INSERT INTO `tbl_user_custom_design` VALUES (1,'/static/images/custome_image/img/mens_longsleeve_front.png','data:image/png;base64,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','data:image/png;base64,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','2022-05-09 06:57:43.976058','custom_productadmin005200',1,12,NULL,1,0);
/*!40000 ALTER TABLE `tbl_user_custom_design` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_custom_product_order`
--

DROP TABLE IF EXISTS `tbl_user_custom_product_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_user_custom_product_order` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `qty` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  `stripe_payment_intent` varchar(200) NOT NULL,
  `created_on` datetime(6) NOT NULL,
  `slug` varchar(75) NOT NULL,
  `order_history_id` bigint(20) NOT NULL,
  `tranastion_id_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `user_design_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `tbl_user_custom_orud_order_history_id_0729333a_fk_tbl_user_` (`order_history_id`),
  KEY `tbl_user_custom_orud_tranastion_id_id_70934ade_fk_tbl_trans` (`tranastion_id_id`),
  KEY `tbl_user_custom_orudct_order_user_id_fea9ee60_fk_tbl_user_id` (`user_id`),
  KEY `tbl_user_custom_orud_user_design_id_7ead833d_fk_tbl_user_` (`user_design_id`),
  CONSTRAINT `tbl_user_custom_orud_order_history_id_0729333a_fk_tbl_user_` FOREIGN KEY (`order_history_id`) REFERENCES `tbl_user_order_history` (`id`),
  CONSTRAINT `tbl_user_custom_orud_tranastion_id_id_70934ade_fk_tbl_trans` FOREIGN KEY (`tranastion_id_id`) REFERENCES `tbl_transaction` (`id`),
  CONSTRAINT `tbl_user_custom_orud_user_design_id_7ead833d_fk_tbl_user_` FOREIGN KEY (`user_design_id`) REFERENCES `tbl_user_custom_design` (`id`),
  CONSTRAINT `tbl_user_custom_orudct_order_user_id_fea9ee60_fk_tbl_user_id` FOREIGN KEY (`user_id`) REFERENCES `tbl_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_custom_product_order`
--

LOCK TABLES `tbl_user_custom_product_order` WRITE;
/*!40000 ALTER TABLE `tbl_user_custom_product_order` DISABLE KEYS */;
INSERT INTO `tbl_user_custom_product_order` VALUES (1,1,12,'pi_3KxQYuSAfluecUvn1HgaBDzr','2022-05-09 06:59:21.092701','user_orderNitishpi_3KxQYuSAfluecUvn1HgaBDzr',2,3,1,1);
/*!40000 ALTER TABLE `tbl_user_custom_product_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_groups`
--

DROP TABLE IF EXISTS `tbl_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tbl_user_groups_user_id_group_id_96fc015e_uniq` (`user_id`,`group_id`),
  KEY `tbl_user_groups_group_id_d81345eb_fk_auth_group_id` (`group_id`),
  CONSTRAINT `tbl_user_groups_group_id_d81345eb_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `tbl_user_groups_user_id_6dda685a_fk_tbl_user_id` FOREIGN KEY (`user_id`) REFERENCES `tbl_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_groups`
--

LOCK TABLES `tbl_user_groups` WRITE;
/*!40000 ALTER TABLE `tbl_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_order`
--

DROP TABLE IF EXISTS `tbl_user_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_user_order` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `qty` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  `stripe_payment_intent` varchar(200) NOT NULL,
  `created_on` datetime(6) NOT NULL,
  `slug` varchar(75) NOT NULL,
  `order_history_id` bigint(20) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  `tranastion_id_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `tbl_user_order_order_history_id_05cc1584_fk_tbl_user_` (`order_history_id`),
  KEY `tbl_user_order_product_id_0d121e01_fk_tbl_product_id` (`product_id`),
  KEY `tbl_user_order_tranastion_id_id_1d943ea7_fk_tbl_transaction_id` (`tranastion_id_id`),
  KEY `tbl_user_order_user_id_0e5925b1_fk_tbl_user_id` (`user_id`),
  CONSTRAINT `tbl_user_order_order_history_id_05cc1584_fk_tbl_user_` FOREIGN KEY (`order_history_id`) REFERENCES `tbl_user_order_history` (`id`),
  CONSTRAINT `tbl_user_order_product_id_0d121e01_fk_tbl_product_id` FOREIGN KEY (`product_id`) REFERENCES `tbl_product` (`id`),
  CONSTRAINT `tbl_user_order_tranastion_id_id_1d943ea7_fk_tbl_transaction_id` FOREIGN KEY (`tranastion_id_id`) REFERENCES `tbl_transaction` (`id`),
  CONSTRAINT `tbl_user_order_user_id_0e5925b1_fk_tbl_user_id` FOREIGN KEY (`user_id`) REFERENCES `tbl_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_order`
--

LOCK TABLES `tbl_user_order` WRITE;
/*!40000 ALTER TABLE `tbl_user_order` DISABLE KEYS */;
INSERT INTO `tbl_user_order` VALUES (1,1,16,'pi_3KxQUwSAfluecUvn0Fq7GRQG','2022-05-09 06:55:14.718456','user_orderNitishpi_3KxQUwSAfluecUvn0Fq7GRQGsonu ',1,5,2,1),(2,1,16,'pi_3KxQYuSAfluecUvn1HgaBDzr','2022-05-09 06:59:21.090623','user_orderNitishpi_3KxQYuSAfluecUvn1HgaBDzrsonu ',2,5,3,1);
/*!40000 ALTER TABLE `tbl_user_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_order_history`
--

DROP TABLE IF EXISTS `tbl_user_order_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_user_order_history` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_on` datetime(6) NOT NULL,
  `tranastion_id_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `slug` varchar(75) NOT NULL,
  `amount` int(11) NOT NULL,
  `has_paid` tinyint(1) NOT NULL,
  `stripe_payment_intent` varchar(200) NOT NULL,
  `has_delivered` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `tbl_user_order_histo_tranastion_id_id_3b9988ab_fk_tbl_trans` (`tranastion_id_id`),
  KEY `tbl_user_order_history_user_id_c04b7dca_fk_tbl_user_id` (`user_id`),
  CONSTRAINT `tbl_user_order_histo_tranastion_id_id_3b9988ab_fk_tbl_trans` FOREIGN KEY (`tranastion_id_id`) REFERENCES `tbl_transaction` (`id`),
  CONSTRAINT `tbl_user_order_history_user_id_c04b7dca_fk_tbl_user_id` FOREIGN KEY (`user_id`) REFERENCES `tbl_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_order_history`
--

LOCK TABLES `tbl_user_order_history` WRITE;
/*!40000 ALTER TABLE `tbl_user_order_history` DISABLE KEYS */;
INSERT INTO `tbl_user_order_history` VALUES (1,'2022-05-09 06:55:14.716290',2,1,'user_order_historyNitishpi_3KxQUwSAfluecUvn0Fq7GRQG',500,0,'pi_3KxQUwSAfluecUvn0Fq7GRQG',0),(2,'2022-05-09 06:59:21.088519',3,1,'user_order_historyNitishpi_3KxQYuSAfluecUvn1HgaBDzr',12,1,'pi_3KxQYuSAfluecUvn1HgaBDzr',0);
/*!40000 ALTER TABLE `tbl_user_order_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_promo_code`
--

DROP TABLE IF EXISTS `tbl_user_promo_code`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_user_promo_code` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `promocode_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tbl_user_promo_code_promocode_id_921a60c3_fk_tbl_promo_code_id` (`promocode_id`),
  KEY `tbl_user_promo_code_user_id_db9435c9_fk_tbl_user_id` (`user_id`),
  CONSTRAINT `tbl_user_promo_code_promocode_id_921a60c3_fk_tbl_promo_code_id` FOREIGN KEY (`promocode_id`) REFERENCES `tbl_promo_code` (`id`),
  CONSTRAINT `tbl_user_promo_code_user_id_db9435c9_fk_tbl_user_id` FOREIGN KEY (`user_id`) REFERENCES `tbl_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_promo_code`
--

LOCK TABLES `tbl_user_promo_code` WRITE;
/*!40000 ALTER TABLE `tbl_user_promo_code` DISABLE KEYS */;
INSERT INTO `tbl_user_promo_code` VALUES (1,1,1);
/*!40000 ALTER TABLE `tbl_user_promo_code` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_user_permissions`
--

DROP TABLE IF EXISTS `tbl_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tbl_user_user_permissions_user_id_permission_id_98f65383_uniq` (`user_id`,`permission_id`),
  KEY `tbl_user_user_permis_permission_id_f2f92266_fk_auth_perm` (`permission_id`),
  CONSTRAINT `tbl_user_user_permis_permission_id_f2f92266_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `tbl_user_user_permissions_user_id_205d273c_fk_tbl_user_id` FOREIGN KEY (`user_id`) REFERENCES `tbl_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_user_permissions`
--

LOCK TABLES `tbl_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `tbl_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_wishlist`
--

DROP TABLE IF EXISTS `tbl_user_wishlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_user_wishlist` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `product_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tbl_user_wishlist_product_id_bcd1d004_fk_tbl_product_id` (`product_id`),
  KEY `tbl_user_wishlist_user_id_5f5392ca_fk_tbl_user_id` (`user_id`),
  CONSTRAINT `tbl_user_wishlist_product_id_bcd1d004_fk_tbl_product_id` FOREIGN KEY (`product_id`) REFERENCES `tbl_product` (`id`),
  CONSTRAINT `tbl_user_wishlist_user_id_5f5392ca_fk_tbl_user_id` FOREIGN KEY (`user_id`) REFERENCES `tbl_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_wishlist`
--

LOCK TABLES `tbl_user_wishlist` WRITE;
/*!40000 ALTER TABLE `tbl_user_wishlist` DISABLE KEYS */;
INSERT INTO `tbl_user_wishlist` VALUES (1,1,1),(2,2,1);
/*!40000 ALTER TABLE `tbl_user_wishlist` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-12 17:05:11
