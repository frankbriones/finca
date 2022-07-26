CREATE DATABASE  IF NOT EXISTS `finca_bnn` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_spanish_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `finca_bnn`;
-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: finca_bnn
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'ADMINISTRADOR'),(2,'bodeguero_ECUADOR'),(3,'produccion_ECUADOR');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (12,1,25),(11,1,26),(10,1,27),(6,1,32),(4,1,33),(5,1,34),(8,1,39),(9,1,40),(7,1,41),(25,1,46),(26,1,47),(27,1,48),(1,1,53),(3,1,54),(2,1,55),(15,1,80),(14,1,81),(13,1,82),(17,1,87),(18,1,88),(16,1,89),(20,1,94),(19,1,95),(21,1,96),(24,1,101),(22,1,102),(23,1,103),(28,1,172),(29,1,173),(32,1,207),(33,1,208),(30,2,172),(31,2,173),(34,3,207),(35,3,208);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=215 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add personal finca',6,'add_personalfinca'),(22,'Can change personal finca',6,'change_personalfinca'),(23,'Can delete personal finca',6,'delete_personalfinca'),(24,'Can view personal finca',6,'view_personalfinca'),(25,'Actualizar Personal',6,'actualizar_personal'),(26,'Editar Personal',6,'editar_personal'),(27,'Crear Personal',6,'crear_personal'),(28,'Can add categoria personal',7,'add_categoriapersonal'),(29,'Can change categoria personal',7,'change_categoriapersonal'),(30,'Can delete categoria personal',7,'delete_categoriapersonal'),(31,'Can view categoria personal',7,'view_categoriapersonal'),(32,'Actualizar Categoria Personal',7,'actualizar_categoria_personal'),(33,'Crear Categoria Personal',7,'crear_categoria_personal'),(34,'Editar Categoria Personal',7,'editar_categoria_personal'),(35,'Can add tipo personal',8,'add_tipopersonal'),(36,'Can change tipo personal',8,'change_tipopersonal'),(37,'Can delete tipo personal',8,'delete_tipopersonal'),(38,'Can view tipo personal',8,'view_tipopersonal'),(39,'Editar Tipo Personal',8,'editar_tipo_personal'),(40,'Actualizar Tipo Personal',8,'actualizar_tipo_personal'),(41,'Crear Tipo Personal',8,'crear_tipo_personal'),(42,'Can add usuarios',9,'add_usuarios'),(43,'Can change usuarios',9,'change_usuarios'),(44,'Can delete usuarios',9,'delete_usuarios'),(45,'Can view usuarios',9,'view_usuarios'),(46,'Crear Usuarios',9,'crear_usuarios'),(47,'Editar Usuarios',9,'editar_usuarios'),(48,'Actualizar Usuarios',9,'actualizar_usuarios'),(49,'Can add roles',10,'add_roles'),(50,'Can change roles',10,'change_roles'),(51,'Can delete roles',10,'delete_roles'),(52,'Can view roles',10,'view_roles'),(53,'Crear Rol',10,'crear_rol'),(54,'Actualizar Rol',10,'actualizar_rol'),(55,'Editar Rol',10,'editar_rol'),(56,'Can add grupos permisos',11,'add_grupospermisos'),(57,'Can change grupos permisos',11,'change_grupospermisos'),(58,'Can delete grupos permisos',11,'delete_grupospermisos'),(59,'Can view grupos permisos',11,'view_grupospermisos'),(60,'Can add usuarios grupos',12,'add_usuariosgrupos'),(61,'Can change usuarios grupos',12,'change_usuariosgrupos'),(62,'Can delete usuarios grupos',12,'delete_usuariosgrupos'),(63,'Can view usuarios grupos',12,'view_usuariosgrupos'),(64,'Can add tipo usuario',13,'add_tipousuario'),(65,'Can change tipo usuario',13,'change_tipousuario'),(66,'Can delete tipo usuario',13,'delete_tipousuario'),(67,'Can view tipo usuario',13,'view_tipousuario'),(68,'Can add estados',14,'add_estados'),(69,'Can change estados',14,'change_estados'),(70,'Can delete estados',14,'delete_estados'),(71,'Can view estados',14,'view_estados'),(72,'Can add configuracion sistema',15,'add_configuracionsistema'),(73,'Can change configuracion sistema',15,'change_configuracionsistema'),(74,'Can delete configuracion sistema',15,'delete_configuracionsistema'),(75,'Can view configuracion sistema',15,'view_configuracionsistema'),(76,'Can add pais',16,'add_pais'),(77,'Can change pais',16,'change_pais'),(78,'Can delete pais',16,'delete_pais'),(79,'Can view pais',16,'view_pais'),(80,'Actualizar Pais',16,'actualizar_pais'),(81,'Editar Pais',16,'editar_pais'),(82,'Crear Pais',16,'crear_pais'),(83,'Can add ciudades',17,'add_ciudades'),(84,'Can change ciudades',17,'change_ciudades'),(85,'Can delete ciudades',17,'delete_ciudades'),(86,'Can view ciudades',17,'view_ciudades'),(87,'Editar Ciudad',17,'editar_ciudades'),(88,'Actualizar Ciudad',17,'actualizar_ciudades'),(89,'Crear Ciudad',17,'crear_ciudades'),(90,'Can add sectores',18,'add_sectores'),(91,'Can change sectores',18,'change_sectores'),(92,'Can delete sectores',18,'delete_sectores'),(93,'Can view sectores',18,'view_sectores'),(94,'Editar Sectores',18,'editar_sectores'),(95,'Crear Sectores',18,'crear_sectores'),(96,'Actualizar Sectores',18,'actualizar_sectores'),(97,'Can add lotes',19,'add_lotes'),(98,'Can change lotes',19,'change_lotes'),(99,'Can delete lotes',19,'delete_lotes'),(100,'Can view lotes',19,'view_lotes'),(101,'Actualizar Lotes',19,'actualizar_lotes'),(102,'Crear Lotes',19,'crear_lotes'),(103,'Editar Lotes',19,'editar_lotes'),(104,'Can add bodegas',20,'add_bodegas'),(105,'Can change bodegas',20,'change_bodegas'),(106,'Can delete bodegas',20,'delete_bodegas'),(107,'Can view bodegas',20,'view_bodegas'),(108,'Crear Bodega',20,'crear_bodega'),(109,'Actualizar Bodega',20,'actualizar_bodega'),(110,'Editar Bodega',20,'editar_bodega'),(111,'Can add secciones',21,'add_secciones'),(112,'Can change secciones',21,'change_secciones'),(113,'Can delete secciones',21,'delete_secciones'),(114,'Can view secciones',21,'view_secciones'),(115,'Crear Bodega',21,'crear_bodega'),(116,'Actualizar Bodega',21,'actualizar_bodega'),(117,'Editar Bodega',21,'editar_bodega'),(118,'Can add notificacion',22,'add_notificacion'),(119,'Can change notificacion',22,'change_notificacion'),(120,'Can delete notificacion',22,'delete_notificacion'),(121,'Can view notificacion',22,'view_notificacion'),(122,'Can add categoria producto',23,'add_categoriaproducto'),(123,'Can change categoria producto',23,'change_categoriaproducto'),(124,'Can delete categoria producto',23,'delete_categoriaproducto'),(125,'Can view categoria producto',23,'view_categoriaproducto'),(126,'Crear Categoria Producto',23,'crear_categoria_prd'),(127,'Actualizar Categoria Prducto',23,'actualizar_categoria_prd'),(128,'Editar Categoria Prducto',23,'editar_categoria_prd'),(129,'Can add unidad medida',24,'add_unidadmedida'),(130,'Can change unidad medida',24,'change_unidadmedida'),(131,'Can delete unidad medida',24,'delete_unidadmedida'),(132,'Can view unidad medida',24,'view_unidadmedida'),(133,'Crear Unidad Medida',24,'crear_unidad_meidida'),(134,'Actualizar Unidad Medida',24,'actualizar_unidad_meidida'),(135,'Editar Unidad Medida',24,'editar_unidad_meidida'),(136,'Can add productos',25,'add_productos'),(137,'Can change productos',25,'change_productos'),(138,'Can delete productos',25,'delete_productos'),(139,'Can view productos',25,'view_productos'),(140,'Actualizar Prducto',25,'actualizar_producto'),(141,'Crear Producto',25,'crear_producto'),(142,'Editar Prducto',25,'editar_producto'),(143,'Can add proveedores',26,'add_proveedores'),(144,'Can change proveedores',26,'change_proveedores'),(145,'Can delete proveedores',26,'delete_proveedores'),(146,'Can view proveedores',26,'view_proveedores'),(147,'Editar Proveedor',26,'editar_proveedor'),(148,'Crear Proveedor',26,'crear_proveedor'),(149,'Actualizar Proveedor',26,'actualizar_proveedor'),(150,'Can add categoria proveedor',27,'add_categoriaproveedor'),(151,'Can change categoria proveedor',27,'change_categoriaproveedor'),(152,'Can delete categoria proveedor',27,'delete_categoriaproveedor'),(153,'Can view categoria proveedor',27,'view_categoriaproveedor'),(154,'Can add solicitud pedido',28,'add_solicitudpedido'),(155,'Can change solicitud pedido',28,'change_solicitudpedido'),(156,'Can delete solicitud pedido',28,'delete_solicitudpedido'),(157,'Can view solicitud pedido',28,'view_solicitudpedido'),(158,'Can add productos solicitud',29,'add_productossolicitud'),(159,'Can change productos solicitud',29,'change_productossolicitud'),(160,'Can delete productos solicitud',29,'delete_productossolicitud'),(161,'Can view productos solicitud',29,'view_productossolicitud'),(162,'Editar Producto a Pedido',29,'editar_producto_pedido'),(163,'Agregar Producto a Pedido',29,'crear_producto_pedido'),(164,'Can add tipo orden bodega',30,'add_tipoordenbodega'),(165,'Can change tipo orden bodega',30,'change_tipoordenbodega'),(166,'Can delete tipo orden bodega',30,'delete_tipoordenbodega'),(167,'Can view tipo orden bodega',30,'view_tipoordenbodega'),(168,'Can add orden bodega',31,'add_ordenbodega'),(169,'Can change orden bodega',31,'change_ordenbodega'),(170,'Can delete orden bodega',31,'delete_ordenbodega'),(171,'Can view orden bodega',31,'view_ordenbodega'),(172,'Ver Orden de Ingreso',31,'ver_orden_ingreso'),(173,'Actualizar Orden de Ingreso',31,'actualizar_orden_ingreso'),(174,'Agregar Orden de Ingreso',31,'crear_orden_ingreso'),(175,'Can add detalle orden bodega',32,'add_detalleordenbodega'),(176,'Can change detalle orden bodega',32,'change_detalleordenbodega'),(177,'Can delete detalle orden bodega',32,'delete_detalleordenbodega'),(178,'Can view detalle orden bodega',32,'view_detalleordenbodega'),(179,'Can add crontab',33,'add_crontabschedule'),(180,'Can change crontab',33,'change_crontabschedule'),(181,'Can delete crontab',33,'delete_crontabschedule'),(182,'Can view crontab',33,'view_crontabschedule'),(183,'Can add interval',34,'add_intervalschedule'),(184,'Can change interval',34,'change_intervalschedule'),(185,'Can delete interval',34,'delete_intervalschedule'),(186,'Can view interval',34,'view_intervalschedule'),(187,'Can add periodic task',35,'add_periodictask'),(188,'Can change periodic task',35,'change_periodictask'),(189,'Can delete periodic task',35,'delete_periodictask'),(190,'Can view periodic task',35,'view_periodictask'),(191,'Can add periodic tasks',36,'add_periodictasks'),(192,'Can change periodic tasks',36,'change_periodictasks'),(193,'Can delete periodic tasks',36,'delete_periodictasks'),(194,'Can view periodic tasks',36,'view_periodictasks'),(195,'Can add solar event',37,'add_solarschedule'),(196,'Can change solar event',37,'change_solarschedule'),(197,'Can delete solar event',37,'delete_solarschedule'),(198,'Can view solar event',37,'view_solarschedule'),(199,'Can add clocked',38,'add_clockedschedule'),(200,'Can change clocked',38,'change_clockedschedule'),(201,'Can delete clocked',38,'delete_clockedschedule'),(202,'Can view clocked',38,'view_clockedschedule'),(203,'Can add orden produccion',39,'add_ordenproduccion'),(204,'Can change orden produccion',39,'change_ordenproduccion'),(205,'Can delete orden produccion',39,'delete_ordenproduccion'),(206,'Can view orden produccion',39,'view_ordenproduccion'),(207,'Agregar Orden Produccion',39,'crear_orden_produccion'),(208,'Editar Orden Produccion',39,'editar_orden_produccion'),(209,'Can add detalle orden',40,'add_detalleorden'),(210,'Can change detalle orden',40,'change_detalleorden'),(211,'Can delete detalle orden',40,'delete_detalleorden'),(212,'Can view detalle orden',40,'view_detalleorden'),(213,'Agregar Producto a Orden',40,'crear_producto_orden'),(214,'Editar Producto a Orden',40,'editar_producto_orden');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bases_configuracionsistema`
--

DROP TABLE IF EXISTS `bases_configuracionsistema`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bases_configuracionsistema` (
  `id` int NOT NULL AUTO_INCREMENT,
  `clave` varchar(200) NOT NULL,
  `valor` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bases_configuracionsistema`
--

LOCK TABLES `bases_configuracionsistema` WRITE;
/*!40000 ALTER TABLE `bases_configuracionsistema` DISABLE KEYS */;
INSERT INTO `bases_configuracionsistema` VALUES (1,'key-clima','42db7bd825ea65bca5c805bad53ca658'),(2,'codigo_ciudad','3657509');
/*!40000 ALTER TABLE `bases_configuracionsistema` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bases_estados`
--

DROP TABLE IF EXISTS `bases_estados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bases_estados` (
  `id_estado` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(100) NOT NULL,
  PRIMARY KEY (`id_estado`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bases_estados`
--

LOCK TABLES `bases_estados` WRITE;
/*!40000 ALTER TABLE `bases_estados` DISABLE KEYS */;
INSERT INTO `bases_estados` VALUES (1,'ACTIVO'),(2,'INACTIVO'),(3,'GENERADA'),(4,'EN PROCESO'),(5,'ALMACENADO'),(6,'PEDIDO CREADO'),(7,'PEDIDO EN PROCESO'),(8,'PEDIDO ENVIADO'),(9,'PEDIDO RECIBIDO'),(10,'DISPONIBLE'),(11,'NO DISPONIBLE'),(12,'SOLICITADO'),(13,'ORDEN SOLICITADA'),(14,'ORD PROD. PROCESADA');
/*!40000 ALTER TABLE `bases_estados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_usr_usuarios_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_usr_usuarios_id` FOREIGN KEY (`user_id`) REFERENCES `usr_usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2022-03-06 07:29:07.206116','1','ADMINISTRADOR',2,'[]',10,3),(2,'2022-03-06 07:30:06.781061','1','GUAYAQUIL',1,'[{\"added\": {}}]',17,3),(3,'2022-03-06 07:30:29.079551','1','MARGARITA',1,'[{\"added\": {}}]',20,3),(4,'2022-03-06 18:40:26.894831','1','FERTILIZANTES',1,'[{\"added\": {}}]',27,3),(5,'2022-03-06 18:40:38.684147','2','AGROQUIMICOS',1,'[{\"added\": {}}]',27,3),(6,'2022-03-06 18:41:17.587831','3','SEMILLAS Y MATERIALES DE SIEEMBRA',1,'[{\"added\": {}}]',27,3),(7,'2022-03-06 18:42:53.357381','4','MAQUINARIAS',1,'[{\"added\": {}}]',27,3),(8,'2022-03-06 18:48:21.435092','3','SEMILLAS',2,'[{\"changed\": {\"fields\": [\"descripcion\"]}}]',27,3),(9,'2022-03-06 18:48:35.871144','5','MATERIALES DE SIEMBRA',1,'[{\"added\": {}}]',27,3),(10,'2022-03-06 18:49:52.491193','1','AGROQUIMICOS',1,'[{\"added\": {}}]',23,3),(11,'2022-03-06 18:50:01.878281','2','FERTILIZANTES',1,'[{\"added\": {}}]',23,3),(12,'2022-03-06 18:50:08.702006','3','SEMILLAS',1,'[{\"added\": {}}]',23,3),(13,'2022-03-06 18:50:19.425786','4','MAQUINARIAS',1,'[{\"added\": {}}]',23,3),(14,'2022-03-06 18:50:34.774824','5','MATERIALES DE SIEMBRA',1,'[{\"added\": {}}]',23,3),(15,'2022-03-06 18:52:45.769654','1','GRAMOS',1,'[{\"added\": {}}]',24,3),(16,'2022-03-06 18:52:53.329357','2','MILIGRAMOS',1,'[{\"added\": {}}]',24,3),(17,'2022-03-06 18:53:05.108210','3','LITROS',1,'[{\"added\": {}}]',24,3),(18,'2022-03-06 18:53:14.489421','4','GALONES',1,'[{\"added\": {}}]',24,3),(19,'2022-03-06 18:53:26.464893','5','KINTALES',1,'[{\"added\": {}}]',24,3),(20,'2022-03-06 18:53:39.353662','6','CANECA',1,'[{\"added\": {}}]',24,3),(21,'2022-03-06 18:53:49.709751','7','KILOGRAMOS',1,'[{\"added\": {}}]',24,3),(22,'2022-03-06 18:53:57.915208','8','UNIDAD',1,'[{\"added\": {}}]',24,3),(23,'2022-03-06 18:55:17.575502','1','ENTRADA',1,'[{\"added\": {}}]',30,3),(24,'2022-03-06 18:55:24.045232','2','SALIDA',1,'[{\"added\": {}}]',30,3),(25,'2022-03-06 19:00:07.196444','1','ERICK VILLA CAICEDO',1,'[{\"added\": {}}]',26,3);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_beat_clockedschedule`
--

DROP TABLE IF EXISTS `django_celery_beat_clockedschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_celery_beat_clockedschedule` (
  `id` int NOT NULL AUTO_INCREMENT,
  `clocked_time` datetime(6) NOT NULL,
  `enabled` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_beat_clockedschedule`
--

LOCK TABLES `django_celery_beat_clockedschedule` WRITE;
/*!40000 ALTER TABLE `django_celery_beat_clockedschedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_celery_beat_clockedschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_beat_crontabschedule`
--

DROP TABLE IF EXISTS `django_celery_beat_crontabschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_celery_beat_crontabschedule` (
  `id` int NOT NULL AUTO_INCREMENT,
  `minute` varchar(240) NOT NULL,
  `hour` varchar(96) NOT NULL,
  `day_of_week` varchar(64) NOT NULL,
  `day_of_month` varchar(124) NOT NULL,
  `month_of_year` varchar(64) NOT NULL,
  `timezone` varchar(63) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_beat_crontabschedule`
--

LOCK TABLES `django_celery_beat_crontabschedule` WRITE;
/*!40000 ALTER TABLE `django_celery_beat_crontabschedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_celery_beat_crontabschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_beat_intervalschedule`
--

DROP TABLE IF EXISTS `django_celery_beat_intervalschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_celery_beat_intervalschedule` (
  `id` int NOT NULL AUTO_INCREMENT,
  `every` int NOT NULL,
  `period` varchar(24) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_beat_intervalschedule`
--

LOCK TABLES `django_celery_beat_intervalschedule` WRITE;
/*!40000 ALTER TABLE `django_celery_beat_intervalschedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_celery_beat_intervalschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_beat_periodictask`
--

DROP TABLE IF EXISTS `django_celery_beat_periodictask`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_celery_beat_periodictask` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `task` varchar(200) NOT NULL,
  `args` longtext NOT NULL,
  `kwargs` longtext NOT NULL,
  `queue` varchar(200) DEFAULT NULL,
  `exchange` varchar(200) DEFAULT NULL,
  `routing_key` varchar(200) DEFAULT NULL,
  `expires` datetime(6) DEFAULT NULL,
  `enabled` tinyint(1) NOT NULL,
  `last_run_at` datetime(6) DEFAULT NULL,
  `total_run_count` int unsigned NOT NULL,
  `date_changed` datetime(6) NOT NULL,
  `description` longtext NOT NULL,
  `crontab_id` int DEFAULT NULL,
  `interval_id` int DEFAULT NULL,
  `solar_id` int DEFAULT NULL,
  `one_off` tinyint(1) NOT NULL,
  `start_time` datetime(6) DEFAULT NULL,
  `priority` int unsigned DEFAULT NULL,
  `headers` longtext NOT NULL,
  `clocked_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `django_celery_beat_p_crontab_id_d3cba168_fk_django_ce` (`crontab_id`),
  KEY `django_celery_beat_p_interval_id_a8ca27da_fk_django_ce` (`interval_id`),
  KEY `django_celery_beat_p_solar_id_a87ce72c_fk_django_ce` (`solar_id`),
  KEY `django_celery_beat_p_clocked_id_47a69f82_fk_django_ce` (`clocked_id`),
  CONSTRAINT `django_celery_beat_p_clocked_id_47a69f82_fk_django_ce` FOREIGN KEY (`clocked_id`) REFERENCES `django_celery_beat_clockedschedule` (`id`),
  CONSTRAINT `django_celery_beat_p_crontab_id_d3cba168_fk_django_ce` FOREIGN KEY (`crontab_id`) REFERENCES `django_celery_beat_crontabschedule` (`id`),
  CONSTRAINT `django_celery_beat_p_interval_id_a8ca27da_fk_django_ce` FOREIGN KEY (`interval_id`) REFERENCES `django_celery_beat_intervalschedule` (`id`),
  CONSTRAINT `django_celery_beat_p_solar_id_a87ce72c_fk_django_ce` FOREIGN KEY (`solar_id`) REFERENCES `django_celery_beat_solarschedule` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_beat_periodictask`
--

LOCK TABLES `django_celery_beat_periodictask` WRITE;
/*!40000 ALTER TABLE `django_celery_beat_periodictask` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_celery_beat_periodictask` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_beat_periodictasks`
--

DROP TABLE IF EXISTS `django_celery_beat_periodictasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_celery_beat_periodictasks` (
  `ident` smallint NOT NULL,
  `last_update` datetime(6) NOT NULL,
  PRIMARY KEY (`ident`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_beat_periodictasks`
--

LOCK TABLES `django_celery_beat_periodictasks` WRITE;
/*!40000 ALTER TABLE `django_celery_beat_periodictasks` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_celery_beat_periodictasks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_beat_solarschedule`
--

DROP TABLE IF EXISTS `django_celery_beat_solarschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_celery_beat_solarschedule` (
  `id` int NOT NULL AUTO_INCREMENT,
  `event` varchar(24) NOT NULL,
  `latitude` decimal(9,6) NOT NULL,
  `longitude` decimal(9,6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_celery_beat_solar_event_latitude_longitude_ba64999a_uniq` (`event`,`latitude`,`longitude`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_beat_solarschedule`
--

LOCK TABLES `django_celery_beat_solarschedule` WRITE;
/*!40000 ALTER TABLE `django_celery_beat_solarschedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_celery_beat_solarschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(15,'bases','configuracionsistema'),(14,'bases','estados'),(4,'contenttypes','contenttype'),(38,'django_celery_beat','clockedschedule'),(33,'django_celery_beat','crontabschedule'),(34,'django_celery_beat','intervalschedule'),(35,'django_celery_beat','periodictask'),(36,'django_celery_beat','periodictasks'),(37,'django_celery_beat','solarschedule'),(22,'ntf','notificacion'),(7,'personal','categoriapersonal'),(6,'personal','personalfinca'),(8,'personal','tipopersonal'),(23,'prd','categoriaproducto'),(25,'prd','productos'),(24,'prd','unidadmedida'),(27,'prv','categoriaproveedor'),(26,'prv','proveedores'),(5,'sessions','session'),(40,'trn','detalleorden'),(32,'trn','detalleordenbodega'),(31,'trn','ordenbodega'),(39,'trn','ordenproduccion'),(29,'trn','productossolicitud'),(28,'trn','solicitudpedido'),(30,'trn','tipoordenbodega'),(20,'ubc','bodegas'),(17,'ubc','ciudades'),(19,'ubc','lotes'),(16,'ubc','pais'),(21,'ubc','secciones'),(18,'ubc','sectores'),(11,'usr','grupospermisos'),(10,'usr','roles'),(13,'usr','tipousuario'),(9,'usr','usuarios'),(12,'usr','usuariosgrupos');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=84 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'ubc','0001_initial','2022-03-06 04:17:13.214838'),(2,'bases','0001_initial','2022-03-06 04:17:13.261703'),(3,'contenttypes','0001_initial','2022-03-06 04:17:13.308567'),(4,'contenttypes','0002_remove_content_type_name','2022-03-06 04:17:13.433538'),(5,'auth','0001_initial','2022-03-06 04:17:13.542888'),(6,'auth','0002_alter_permission_name_max_length','2022-03-06 04:17:13.917805'),(7,'auth','0003_alter_user_email_max_length','2022-03-06 04:17:13.933537'),(8,'auth','0004_alter_user_username_opts','2022-03-06 04:17:13.949042'),(9,'auth','0005_alter_user_last_login_null','2022-03-06 04:17:13.949042'),(10,'auth','0006_require_contenttypes_0002','2022-03-06 04:17:13.964664'),(11,'auth','0007_alter_validators_add_error_messages','2022-03-06 04:17:13.964664'),(12,'auth','0008_alter_user_username_max_length','2022-03-06 04:17:13.980289'),(13,'auth','0009_alter_user_last_name_max_length','2022-03-06 04:17:13.980289'),(14,'usr','0001_initial','2022-03-06 04:17:14.199009'),(15,'admin','0001_initial','2022-03-06 04:17:15.198749'),(16,'admin','0002_logentry_remove_auto_add','2022-03-06 04:17:15.354994'),(17,'admin','0003_logentry_add_action_flag_choices','2022-03-06 04:17:15.354994'),(18,'auth','0010_alter_group_name_max_length','2022-03-06 04:17:15.386249'),(19,'auth','0011_update_proxy_permissions','2022-03-06 04:17:15.401862'),(20,'bases','0002_configuracionsistema','2022-03-06 04:17:15.433093'),(21,'django_celery_beat','0001_initial','2022-03-06 04:17:15.683010'),(22,'django_celery_beat','0002_auto_20161118_0346','2022-03-06 04:17:16.073733'),(23,'django_celery_beat','0003_auto_20161209_0049','2022-03-06 04:17:16.215555'),(24,'django_celery_beat','0004_auto_20170221_0000','2022-03-06 04:17:16.215555'),(25,'django_celery_beat','0005_add_solarschedule_events_choices','2022-03-06 04:17:16.231176'),(26,'django_celery_beat','0006_auto_20180322_0932','2022-03-06 04:17:16.340684'),(27,'django_celery_beat','0007_auto_20180521_0826','2022-03-06 04:17:16.418760'),(28,'django_celery_beat','0008_auto_20180914_1922','2022-03-06 04:17:16.449875'),(29,'django_celery_beat','0006_auto_20180210_1226','2022-03-06 04:17:16.465532'),(30,'django_celery_beat','0006_periodictask_priority','2022-03-06 04:17:16.527982'),(31,'django_celery_beat','0009_periodictask_headers','2022-03-06 04:17:16.606089'),(32,'django_celery_beat','0010_auto_20190429_0326','2022-03-06 04:17:17.262184'),(33,'django_celery_beat','0011_auto_20190508_0153','2022-03-06 04:17:17.324670'),(34,'ubc','0002_auto_20220124_1648','2022-03-06 04:17:17.527772'),(35,'ubc','0003_auto_20220124_1649','2022-03-06 04:17:18.168223'),(36,'ubc','0004_lotes_sectores','2022-03-06 04:17:18.261978'),(37,'ubc','0005_auto_20220204_1114','2022-03-06 04:17:19.183609'),(38,'ubc','0006_auto_20220207_1250','2022-03-06 04:17:19.214889'),(39,'ubc','0007_pais_prefijo_cel','2022-03-06 04:17:19.261843'),(40,'ubc','0008_ciudades_codigo_api_ciudad','2022-03-06 04:17:19.308581'),(41,'prv','0001_initial','2022-03-06 04:17:19.371065'),(42,'prv','0002_auto_20220214_0354','2022-03-06 04:17:19.636725'),(43,'ubc','0009_bodegas_secciones','2022-03-06 04:17:19.730449'),(44,'ubc','0010_auto_20220220_1452','2022-03-06 04:17:19.949055'),(45,'prd','0001_initial','2022-03-06 04:17:20.402074'),(46,'prd','0002_auto_20220216_1209','2022-03-06 04:17:20.917605'),(47,'prd','0003_productos_seccion','2022-03-06 04:17:20.964443'),(48,'trn','0001_initial','2022-03-06 04:17:21.323733'),(49,'trn','0002_auto_20220223_0143','2022-03-06 04:17:22.002578'),(50,'trn','0003_auto_20220223_0233','2022-03-06 04:17:22.106912'),(51,'trn','0004_solicitudpedido_secuencia','2022-03-06 04:17:22.142640'),(52,'trn','0005_solicitudpedido_estado','2022-03-06 04:17:22.222136'),(53,'trn','0006_detalleordenbodega_ordenbodega_tipoordenbodega','2022-03-06 04:17:22.450106'),(54,'trn','0007_ordenbodega_estado','2022-03-06 04:17:22.901854'),(55,'trn','0008_solicitudpedido_total_envio','2022-03-06 04:17:23.207217'),(56,'trn','0009_auto_20220228_2151','2022-03-06 04:17:23.232478'),(57,'ntf','0001_initial','2022-03-06 04:17:23.283515'),(58,'personal','0001_initial','2022-03-06 04:17:23.532173'),(59,'personal','0002_auto_20220124_2201','2022-03-06 04:17:23.890641'),(60,'personal','0003_auto_20220207_1250','2022-03-06 04:17:24.551237'),(61,'personal','0004_auto_20220211_1843','2022-03-06 04:17:24.644934'),(62,'personal','0005_auto_20220214_0353','2022-03-06 04:17:25.228060'),(63,'prv','0003_auto_20220225_2055','2022-03-06 04:17:25.321788'),(64,'prd','0004_auto_20220226_1943','2022-03-06 04:17:25.786539'),(65,'prd','0005_auto_20220226_1955','2022-03-06 04:17:26.177728'),(66,'prd','0006_auto_20220226_2108','2022-03-06 04:17:26.847771'),(67,'prd','0007_productos_proveedor','2022-03-06 04:17:26.917031'),(68,'prd','0008_auto_20220226_2122','2022-03-06 04:17:27.495539'),(69,'sessions','0001_initial','2022-03-06 04:17:27.529982'),(70,'usr','0002_auto_20220206_1246','2022-03-06 04:17:27.628733'),(71,'usr','0003_auto_20220207_1250','2022-03-06 04:17:27.653211'),(72,'usr','0004_usuarios_img_perfil','2022-03-06 04:17:27.729003'),(73,'usr','0005_usuarios_telefono','2022-03-06 04:17:27.783955'),(74,'usr','0006_usuarios_usuario_telegram','2022-03-06 04:17:27.838943'),(75,'usr','0007_usuariosgrupos','2022-03-06 04:17:27.847542'),(76,'usr','0008_tipousuario','2022-03-06 04:17:27.887272'),(77,'usr','0009_usuarios_tipo_usuario','2022-03-06 04:17:27.957459'),(78,'usr','0010_roles_tipo_usuario','2022-03-06 04:17:28.134752'),(79,'trn','0010_detalleorden_ordenproduccion','2022-03-07 04:02:50.046100'),(80,'ntf','0002_notificacion_orden_prd','2022-03-08 10:18:32.046587'),(81,'ntf','0003_auto_20220308_0520','2022-03-08 10:20:11.244492'),(82,'trn','0011_ordenbodega_orden_produccion','2022-03-08 15:01:40.114320'),(83,'trn','0012_auto_20220308_1013','2022-03-08 15:13:14.268216');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('4cfifwf2guw4zcwyy0zlxai2w7419p8d','M2ZiMWMyNjQ1MTEzN2RjNDFlZjEyM2IxNzFlNzJhZWRlZmE4NmI5Zjp7Il9hdXRoX3VzZXJfaWQiOiI1IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2NGU1YzIzZGQwOWRiYmM5MzdlZGMzNjYzYWQ5YzZjYTY0NzUyNmU5In0=','2022-03-22 16:55:40.280517'),('7xji568l57rjr2at2ztkpc35opnt3gv1','MWM1N2E0MDRiOWI2NjVmY2NjOGIzZWNjODY5YTU1ZWNkZmRlMDEzZDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2NGU1YzIzZGQwOWRiYmM5MzdlZGMzNjYzYWQ5YzZjYTY0NzUyNmU5In0=','2022-03-22 16:30:33.748842'),('88gng227psm4ederx69mhmjxkk6p20fi','MWM1N2E0MDRiOWI2NjVmY2NjOGIzZWNjODY5YTU1ZWNkZmRlMDEzZDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2NGU1YzIzZGQwOWRiYmM5MzdlZGMzNjYzYWQ5YzZjYTY0NzUyNmU5In0=','2022-03-20 21:41:27.150750'),('ewnuqvklk41evqpf65itqvmh8alc4y42','MWM1N2E0MDRiOWI2NjVmY2NjOGIzZWNjODY5YTU1ZWNkZmRlMDEzZDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2NGU1YzIzZGQwOWRiYmM5MzdlZGMzNjYzYWQ5YzZjYTY0NzUyNmU5In0=','2022-03-22 16:18:36.608530'),('je7v2jcm5ckac716m4yt2ouvm4wdgs9r','OTVhNzQ3OWZhYTViNmM1NTY4ZjJlYWYyNGFhMGU1MTlmMDA0NTY2NDp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2NGU1YzIzZGQwOWRiYmM5MzdlZGMzNjYzYWQ5YzZjYTY0NzUyNmU5In0=','2022-03-21 03:04:31.646907'),('ltsrcay8j6a5wap33y0ncgt58j29wc0i','OTVhNzQ3OWZhYTViNmM1NTY4ZjJlYWYyNGFhMGU1MTlmMDA0NTY2NDp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2NGU1YzIzZGQwOWRiYmM5MzdlZGMzNjYzYWQ5YzZjYTY0NzUyNmU5In0=','2022-03-21 17:47:17.028865'),('regp7dvt36664yq24xz5lxqv8llz8xmj','OTVhNzQ3OWZhYTViNmM1NTY4ZjJlYWYyNGFhMGU1MTlmMDA0NTY2NDp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2NGU1YzIzZGQwOWRiYmM5MzdlZGMzNjYzYWQ5YzZjYTY0NzUyNmU5In0=','2022-03-20 21:24:30.615407'),('se47yft7v3e8eqlek4h2su1wul0w289g','OTVhNzQ3OWZhYTViNmM1NTY4ZjJlYWYyNGFhMGU1MTlmMDA0NTY2NDp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2NGU1YzIzZGQwOWRiYmM5MzdlZGMzNjYzYWQ5YzZjYTY0NzUyNmU5In0=','2022-03-20 20:12:22.734602'),('smanmqw1dzyi7mokehlrub2hedhoajkm','M2ZiMWMyNjQ1MTEzN2RjNDFlZjEyM2IxNzFlNzJhZWRlZmE4NmI5Zjp7Il9hdXRoX3VzZXJfaWQiOiI1IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2NGU1YzIzZGQwOWRiYmM5MzdlZGMzNjYzYWQ5YzZjYTY0NzUyNmU5In0=','2022-03-21 06:39:14.758882'),('ufhowtfjxx49r73gjuucktn922pix6ep','M2ZiMWMyNjQ1MTEzN2RjNDFlZjEyM2IxNzFlNzJhZWRlZmE4NmI5Zjp7Il9hdXRoX3VzZXJfaWQiOiI1IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2NGU1YzIzZGQwOWRiYmM5MzdlZGMzNjYzYWQ5YzZjYTY0NzUyNmU5In0=','2022-03-21 04:09:23.392436'),('velghfi6t1w7euqzwvrl0066hzbkg5xo','OTVhNzQ3OWZhYTViNmM1NTY4ZjJlYWYyNGFhMGU1MTlmMDA0NTY2NDp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2NGU1YzIzZGQwOWRiYmM5MzdlZGMzNjYzYWQ5YzZjYTY0NzUyNmU5In0=','2022-03-20 22:43:20.218116'),('xf5x7frrtiy480b3ww2tow352g6586nw','MWM1N2E0MDRiOWI2NjVmY2NjOGIzZWNjODY5YTU1ZWNkZmRlMDEzZDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2NGU1YzIzZGQwOWRiYmM5MzdlZGMzNjYzYWQ5YzZjYTY0NzUyNmU5In0=','2022-03-22 11:37:34.068975'),('zkjt8krtzc6azmefxjvuxi60ftoeg4zk','M2ZiMWMyNjQ1MTEzN2RjNDFlZjEyM2IxNzFlNzJhZWRlZmE4NmI5Zjp7Il9hdXRoX3VzZXJfaWQiOiI1IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2NGU1YzIzZGQwOWRiYmM5MzdlZGMzNjYzYWQ5YzZjYTY0NzUyNmU5In0=','2022-03-22 16:31:41.020458');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ntf_notificacion`
--

DROP TABLE IF EXISTS `ntf_notificacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ntf_notificacion` (
  `id_notificacion` int NOT NULL AUTO_INCREMENT,
  `vista` tinyint(1) NOT NULL,
  `fecha_creacion` datetime(6) NOT NULL,
  `usuario_crea` int DEFAULT NULL,
  `encargado_id` int NOT NULL,
  `estado_id_id` int NOT NULL,
  `orden_id` int DEFAULT NULL,
  `orden_prd` int DEFAULT NULL,
  PRIMARY KEY (`id_notificacion`),
  KEY `ntf_notificacion_encargado_id_cec26bff_fk_usr_usuarios_id` (`encargado_id`),
  KEY `ntf_notificacion_estado_id_id_2f8ca5d8_fk_bases_est` (`estado_id_id`),
  KEY `ntf_notificacion_orden_id_865b9ee6_fk_trn_ordenbodega_id_orden` (`orden_id`),
  CONSTRAINT `ntf_notificacion_encargado_id_cec26bff_fk_usr_usuarios_id` FOREIGN KEY (`encargado_id`) REFERENCES `usr_usuarios` (`id`),
  CONSTRAINT `ntf_notificacion_estado_id_id_2f8ca5d8_fk_bases_est` FOREIGN KEY (`estado_id_id`) REFERENCES `bases_estados` (`id_estado`),
  CONSTRAINT `ntf_notificacion_orden_id_865b9ee6_fk_trn_ordenbodega_id_orden` FOREIGN KEY (`orden_id`) REFERENCES `trn_ordenbodega` (`id_orden`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ntf_notificacion`
--

LOCK TABLES `ntf_notificacion` WRITE;
/*!40000 ALTER TABLE `ntf_notificacion` DISABLE KEYS */;
INSERT INTO `ntf_notificacion` VALUES (19,1,'2022-03-08 15:57:51.585075',3,4,3,14,NULL),(20,1,'2022-03-08 16:02:30.097273',5,3,13,NULL,24),(21,1,'2022-03-08 16:04:35.550644',5,3,13,NULL,25),(22,1,'2022-03-08 16:10:27.176343',5,3,13,NULL,26),(23,1,'2022-03-08 16:18:25.070920',3,4,3,16,NULL),(24,1,'2022-03-08 16:26:41.739009',3,4,3,18,NULL),(25,1,'2022-03-08 16:29:08.615939',5,3,13,NULL,27),(26,1,'2022-03-08 16:33:03.427474',5,3,13,NULL,28),(27,1,'2022-03-08 16:34:21.447155',3,4,3,20,NULL),(28,1,'2022-03-08 18:05:07.739553',5,3,13,NULL,29),(29,0,'2022-03-08 18:05:07.745050',3,4,4,22,NULL),(30,1,'2022-03-08 18:07:16.907920',5,3,13,NULL,30);
/*!40000 ALTER TABLE `ntf_notificacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personal_categoriapersonal`
--

DROP TABLE IF EXISTS `personal_categoriapersonal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personal_categoriapersonal` (
  `fecha_creacion` datetime(6) NOT NULL,
  `usuario_crea` int NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `usuario_modifica` int NOT NULL,
  `id_categoria` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(350) NOT NULL,
  `estado_id` int NOT NULL,
  PRIMARY KEY (`id_categoria`),
  KEY `personal_categoriape_estado_id_c6938bed_fk_bases_est` (`estado_id`),
  CONSTRAINT `personal_categoriape_estado_id_c6938bed_fk_bases_est` FOREIGN KEY (`estado_id`) REFERENCES `bases_estados` (`id_estado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personal_categoriapersonal`
--

LOCK TABLES `personal_categoriapersonal` WRITE;
/*!40000 ALTER TABLE `personal_categoriapersonal` DISABLE KEYS */;
/*!40000 ALTER TABLE `personal_categoriapersonal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personal_personalfinca`
--

DROP TABLE IF EXISTS `personal_personalfinca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personal_personalfinca` (
  `id_personal` int NOT NULL AUTO_INCREMENT,
  `primer_nombre` varchar(350) NOT NULL,
  `segundo_nombre` varchar(350) NOT NULL,
  `primer_apellido` varchar(350) NOT NULL,
  `segundo_apellido` varchar(350) NOT NULL,
  `direccion` varchar(400) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `fecha_creacion` datetime(6) NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `usuario_crea` int NOT NULL,
  `usuario_modifica` int NOT NULL,
  `categoria_id` int DEFAULT NULL,
  `tipo_id` int DEFAULT NULL,
  PRIMARY KEY (`id_personal`),
  KEY `personal_personalfin_categoria_id_55bbd822_fk_personal_` (`categoria_id`),
  KEY `personal_personalfin_tipo_id_ea1fd8ff_fk_personal_` (`tipo_id`),
  CONSTRAINT `personal_personalfin_categoria_id_55bbd822_fk_personal_` FOREIGN KEY (`categoria_id`) REFERENCES `personal_categoriapersonal` (`id_categoria`),
  CONSTRAINT `personal_personalfin_tipo_id_ea1fd8ff_fk_personal_` FOREIGN KEY (`tipo_id`) REFERENCES `personal_tipopersonal` (`id_tipo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personal_personalfinca`
--

LOCK TABLES `personal_personalfinca` WRITE;
/*!40000 ALTER TABLE `personal_personalfinca` DISABLE KEYS */;
/*!40000 ALTER TABLE `personal_personalfinca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personal_tipopersonal`
--

DROP TABLE IF EXISTS `personal_tipopersonal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personal_tipopersonal` (
  `fecha_creacion` datetime(6) NOT NULL,
  `usuario_crea` int NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `usuario_modifica` int NOT NULL,
  `id_tipo` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(350) NOT NULL,
  `estado_id` int NOT NULL,
  PRIMARY KEY (`id_tipo`),
  KEY `personal_tipopersona_estado_id_83b3b93a_fk_bases_est` (`estado_id`),
  CONSTRAINT `personal_tipopersona_estado_id_83b3b93a_fk_bases_est` FOREIGN KEY (`estado_id`) REFERENCES `bases_estados` (`id_estado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personal_tipopersonal`
--

LOCK TABLES `personal_tipopersonal` WRITE;
/*!40000 ALTER TABLE `personal_tipopersonal` DISABLE KEYS */;
/*!40000 ALTER TABLE `personal_tipopersonal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prd_categoriaproducto`
--

DROP TABLE IF EXISTS `prd_categoriaproducto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prd_categoriaproducto` (
  `fecha_creacion` datetime(6) NOT NULL,
  `usuario_crea` int NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `usuario_modifica` int NOT NULL,
  `id_categoria` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(200) NOT NULL,
  `estado_id` int NOT NULL,
  PRIMARY KEY (`id_categoria`),
  KEY `prd_categoriaproduct_estado_id_c3ed85ce_fk_bases_est` (`estado_id`),
  CONSTRAINT `prd_categoriaproduct_estado_id_c3ed85ce_fk_bases_est` FOREIGN KEY (`estado_id`) REFERENCES `bases_estados` (`id_estado`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prd_categoriaproducto`
--

LOCK TABLES `prd_categoriaproducto` WRITE;
/*!40000 ALTER TABLE `prd_categoriaproducto` DISABLE KEYS */;
INSERT INTO `prd_categoriaproducto` VALUES ('2022-03-06 18:49:52.489197',1,'2022-03-06 18:49:52.490232',1,1,'AGROQUIMICOS',1),('2022-03-06 18:50:01.877283',1,'2022-03-06 18:50:01.877283',1,2,'FERTILIZANTES',1),('2022-03-06 18:50:08.701035',1,'2022-03-06 18:50:08.701035',1,3,'SEMILLAS',1),('2022-03-06 18:50:19.424718',1,'2022-03-06 18:50:19.424718',1,4,'MAQUINARIAS',1),('2022-03-06 18:50:34.772365',1,'2022-03-06 18:50:34.772365',1,5,'MATERIALES DE SIEMBRA',1);
/*!40000 ALTER TABLE `prd_categoriaproducto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prd_productos`
--

DROP TABLE IF EXISTS `prd_productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prd_productos` (
  `fecha_creacion` datetime(6) NOT NULL,
  `usuario_crea` int NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `usuario_modifica` int NOT NULL,
  `id_producto` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(200) NOT NULL,
  `categoria_id` int NOT NULL,
  `estado_id` int NOT NULL,
  `unidad_medida_id` int NOT NULL,
  `cantidad_existente` int DEFAULT NULL,
  `cantidad_minima` int DEFAULT NULL,
  `seccion_id` int NOT NULL,
  `bodega_id` int NOT NULL,
  `proveedor_id` int NOT NULL,
  PRIMARY KEY (`id_producto`),
  KEY `prd_productos_categoria_id_f9d2075e_fk_prd_categ` (`categoria_id`),
  KEY `prd_productos_estado_id_2ee38eda_fk_bases_estados_id_estado` (`estado_id`),
  KEY `prd_productos_unidad_medida_id_6d51b5e8_fk_prd_unida` (`unidad_medida_id`),
  KEY `prd_productos_bodega_id_17b8d9c9_fk_ubc_bodegas_id_bodega` (`bodega_id`),
  KEY `prd_productos_seccion_id_2e993c97_fk_ubc_secciones_id_seccion` (`seccion_id`),
  KEY `prd_productos_proveedor_id_5a5ebaa6_fk_prv_prove` (`proveedor_id`),
  CONSTRAINT `prd_productos_bodega_id_17b8d9c9_fk_ubc_bodegas_id_bodega` FOREIGN KEY (`bodega_id`) REFERENCES `ubc_bodegas` (`id_bodega`),
  CONSTRAINT `prd_productos_categoria_id_f9d2075e_fk_prd_categ` FOREIGN KEY (`categoria_id`) REFERENCES `prd_categoriaproducto` (`id_categoria`),
  CONSTRAINT `prd_productos_estado_id_2ee38eda_fk_bases_estados_id_estado` FOREIGN KEY (`estado_id`) REFERENCES `bases_estados` (`id_estado`),
  CONSTRAINT `prd_productos_proveedor_id_5a5ebaa6_fk_prv_prove` FOREIGN KEY (`proveedor_id`) REFERENCES `prv_proveedores` (`id_proveedor`),
  CONSTRAINT `prd_productos_seccion_id_2e993c97_fk_ubc_secciones_id_seccion` FOREIGN KEY (`seccion_id`) REFERENCES `ubc_secciones` (`id_seccion`),
  CONSTRAINT `prd_productos_unidad_medida_id_6d51b5e8_fk_prd_unida` FOREIGN KEY (`unidad_medida_id`) REFERENCES `prd_unidadmedida` (`id_categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prd_productos`
--

LOCK TABLES `prd_productos` WRITE;
/*!40000 ALTER TABLE `prd_productos` DISABLE KEYS */;
INSERT INTO `prd_productos` VALUES ('2022-03-06 21:54:46.610677',3,'2022-03-08 16:36:59.469380',3,2,'TRACTOR',4,10,8,10,25,4,1,1),('2022-03-06 22:01:38.866348',3,'2022-03-08 16:19:41.390333',3,3,'RASTRILLOS',4,10,8,5,25,4,1,1),('2022-03-06 22:03:18.266574',3,'2022-03-06 22:03:18.266574',3,4,'TOPOGRAFO',4,11,8,0,25,4,1,1),('2022-03-06 22:05:10.587611',3,'2022-03-08 15:40:27.718972',3,5,'CORMO',3,11,8,0,100,3,1,1),('2022-03-06 22:07:37.323498',3,'2022-03-07 18:07:38.400458',3,6,'CABEZA DE TORO',3,11,8,0,50,3,1,1),('2022-03-06 22:08:51.194702',3,'2022-03-06 22:08:51.194702',3,7,'PUYON',3,11,8,0,50,3,1,1),('2022-03-06 22:23:06.628093',3,'2022-03-06 22:23:06.628093',3,8,'MALEXONE',1,11,3,0,19,1,1,1),('2022-03-06 22:23:47.638525',3,'2022-03-08 18:07:56.242476',3,9,'APRISCO',1,10,3,2,60,1,1,1),('2022-03-06 22:24:46.599148',3,'2022-03-06 22:24:46.599148',3,10,'JASPE',1,11,7,0,100,1,1,1),('2022-03-06 22:28:27.180496',3,'2022-03-08 16:32:22.807524',3,11,'AGRO K',2,10,7,50,10,2,1,1),('2022-03-06 22:29:43.766915',3,'2022-03-06 22:29:43.766915',3,12,'COSMO R 14-8-19',2,11,7,0,25,2,1,1),('2022-03-06 22:32:10.162127',3,'2022-03-06 22:32:10.162127',3,13,'RADIFLEX',2,11,3,0,100,2,1,1),('2022-03-06 22:41:18.300825',3,'2022-03-08 16:16:57.855746',3,14,'FUNDAS',5,11,8,0,100,5,1,1),('2022-03-06 22:41:55.704428',3,'2022-03-08 15:26:05.030965',3,15,'CINTAS',5,11,8,0,100,5,1,1),('2022-03-06 22:43:20.108734',3,'2022-03-06 22:43:20.108734',3,16,'GUANTES',5,11,8,0,200,5,1,1);
/*!40000 ALTER TABLE `prd_productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prd_unidadmedida`
--

DROP TABLE IF EXISTS `prd_unidadmedida`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prd_unidadmedida` (
  `fecha_creacion` datetime(6) NOT NULL,
  `usuario_crea` int NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `usuario_modifica` int NOT NULL,
  `id_categoria` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(200) NOT NULL,
  `estado_id` int NOT NULL,
  PRIMARY KEY (`id_categoria`),
  KEY `prd_unidadmedida_estado_id_8f0af289_fk_bases_estados_id_estado` (`estado_id`),
  CONSTRAINT `prd_unidadmedida_estado_id_8f0af289_fk_bases_estados_id_estado` FOREIGN KEY (`estado_id`) REFERENCES `bases_estados` (`id_estado`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prd_unidadmedida`
--

LOCK TABLES `prd_unidadmedida` WRITE;
/*!40000 ALTER TABLE `prd_unidadmedida` DISABLE KEYS */;
INSERT INTO `prd_unidadmedida` VALUES ('2022-03-06 18:52:45.768659',1,'2022-03-06 18:52:45.768659',1,1,'GRAMOS',1),('2022-03-06 18:52:53.327319',1,'2022-03-06 18:52:53.327319',1,2,'MILIGRAMOS',1),('2022-03-06 18:53:05.107212',1,'2022-03-06 18:53:05.107212',1,3,'LITROS',1),('2022-03-06 18:53:14.488460',1,'2022-03-06 18:53:14.488460',1,4,'GALONES',1),('2022-03-06 18:53:26.463043',1,'2022-03-06 18:53:26.464041',1,5,'KINTALES',1),('2022-03-06 18:53:39.352520',1,'2022-03-06 18:53:39.352520',1,6,'CANECA',1),('2022-03-06 18:53:49.708787',1,'2022-03-06 18:53:49.708787',1,7,'KILOGRAMOS',1),('2022-03-06 18:53:57.914243',1,'2022-03-06 18:53:57.914243',1,8,'UNIDAD',1);
/*!40000 ALTER TABLE `prd_unidadmedida` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prv_categoriaproveedor`
--

DROP TABLE IF EXISTS `prv_categoriaproveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prv_categoriaproveedor` (
  `fecha_creacion` datetime(6) NOT NULL,
  `usuario_crea` int NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `usuario_modifica` int NOT NULL,
  `id_categoria` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(300) NOT NULL,
  `estado_id` int NOT NULL,
  PRIMARY KEY (`id_categoria`),
  KEY `prv_categoriaproveed_estado_id_4431dc29_fk_bases_est` (`estado_id`),
  CONSTRAINT `prv_categoriaproveed_estado_id_4431dc29_fk_bases_est` FOREIGN KEY (`estado_id`) REFERENCES `bases_estados` (`id_estado`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prv_categoriaproveedor`
--

LOCK TABLES `prv_categoriaproveedor` WRITE;
/*!40000 ALTER TABLE `prv_categoriaproveedor` DISABLE KEYS */;
INSERT INTO `prv_categoriaproveedor` VALUES ('2022-03-06 18:40:26.891840',1,'2022-03-06 18:40:26.891840',1,1,'FERTILIZANTES',1),('2022-03-06 18:40:38.682150',1,'2022-03-06 18:40:38.682150',1,2,'AGROQUIMICOS',1),('2022-03-06 18:41:17.586677',1,'2022-03-06 18:48:21.433097',1,3,'SEMILLAS',1),('2022-03-06 18:42:53.354144',1,'2022-03-06 18:42:53.354144',1,4,'MAQUINARIAS',1),('2022-03-06 18:48:35.869263',1,'2022-03-06 18:48:35.869263',1,5,'MATERIALES DE SIEMBRA',1);
/*!40000 ALTER TABLE `prv_categoriaproveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prv_proveedores`
--

DROP TABLE IF EXISTS `prv_proveedores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prv_proveedores` (
  `fecha_creacion` datetime(6) NOT NULL,
  `usuario_crea` int NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `usuario_modifica` int NOT NULL,
  `id_proveedor` int NOT NULL AUTO_INCREMENT,
  `identificacion` varchar(30) NOT NULL,
  `nombres` varchar(200) NOT NULL,
  `apellidos` varchar(200) NOT NULL,
  `direccion` varchar(500) NOT NULL,
  `telefono` varchar(50) DEFAULT NULL,
  `correo` varchar(254) DEFAULT NULL,
  `ciudad_id` int NOT NULL,
  `estado_id` int NOT NULL,
  `pais_id` int NOT NULL,
  `categoria_id` int DEFAULT NULL,
  PRIMARY KEY (`id_proveedor`),
  UNIQUE KEY `correo` (`correo`),
  KEY `prv_proveedores_ciudad_id_fca12e52_fk_ubc_ciudades_id_ciudad` (`ciudad_id`),
  KEY `prv_proveedores_estado_id_ec064d07_fk_bases_estados_id_estado` (`estado_id`),
  KEY `prv_proveedores_pais_id_67414f1a_fk_ubc_pais_id_pais` (`pais_id`),
  KEY `prv_proveedores_categoria_id_da26907e_fk_prv_categ` (`categoria_id`),
  CONSTRAINT `prv_proveedores_categoria_id_da26907e_fk_prv_categ` FOREIGN KEY (`categoria_id`) REFERENCES `prv_categoriaproveedor` (`id_categoria`),
  CONSTRAINT `prv_proveedores_ciudad_id_fca12e52_fk_ubc_ciudades_id_ciudad` FOREIGN KEY (`ciudad_id`) REFERENCES `ubc_ciudades` (`id_ciudad`),
  CONSTRAINT `prv_proveedores_estado_id_ec064d07_fk_bases_estados_id_estado` FOREIGN KEY (`estado_id`) REFERENCES `bases_estados` (`id_estado`),
  CONSTRAINT `prv_proveedores_pais_id_67414f1a_fk_ubc_pais_id_pais` FOREIGN KEY (`pais_id`) REFERENCES `ubc_pais` (`id_pais`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prv_proveedores`
--

LOCK TABLES `prv_proveedores` WRITE;
/*!40000 ALTER TABLE `prv_proveedores` DISABLE KEYS */;
INSERT INTO `prv_proveedores` VALUES ('2022-03-06 19:00:07.194230',1,'2022-03-06 23:03:22.011849',1,1,'0923439855','ERICK','VILLA CAICEDO','SUR DE LA CIUDAD','8887765555','erickmanuelvlogs@gmail.com',1,1,1,3),('2022-03-08 17:46:44.248447',3,'2022-03-08 17:46:44.248447',3,2,'092343786555555555555555555555','','','','','',1,1,1,NULL);
/*!40000 ALTER TABLE `prv_proveedores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trn_detalleorden`
--

DROP TABLE IF EXISTS `trn_detalleorden`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trn_detalleorden` (
  `fecha_creacion` datetime(6) NOT NULL,
  `usuario_crea` int NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `usuario_modifica` int NOT NULL,
  `id_detalle` int NOT NULL AUTO_INCREMENT,
  `cantidad` decimal(10,2) DEFAULT NULL,
  `orden_id` int NOT NULL,
  `producto_id` int NOT NULL,
  PRIMARY KEY (`id_detalle`),
  KEY `trn_detalleorden_orden_id_adf682ff_fk_trn_orden` (`orden_id`),
  KEY `trn_detalleorden_producto_id_f279f220_fk_prd_produ` (`producto_id`),
  CONSTRAINT `trn_detalleorden_orden_id_adf682ff_fk_trn_orden` FOREIGN KEY (`orden_id`) REFERENCES `trn_ordenproduccion` (`id_solicitud`),
  CONSTRAINT `trn_detalleorden_producto_id_f279f220_fk_prd_produ` FOREIGN KEY (`producto_id`) REFERENCES `prd_productos` (`id_producto`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trn_detalleorden`
--

LOCK TABLES `trn_detalleorden` WRITE;
/*!40000 ALTER TABLE `trn_detalleorden` DISABLE KEYS */;
INSERT INTO `trn_detalleorden` VALUES ('2022-03-08 16:02:02.880637',5,'2022-03-08 16:02:30.040788',5,24,300.00,24,14),('2022-03-08 16:04:24.908125',5,'2022-03-08 16:04:35.524506',5,25,200.00,25,14),('2022-03-08 16:10:18.812403',5,'2022-03-08 16:10:27.065526',5,26,10.00,26,3),('2022-03-08 16:28:49.010872',5,'2022-03-08 16:29:08.553359',5,27,50.00,27,11),('2022-03-08 16:32:54.347969',5,'2022-03-08 16:33:03.378567',5,28,5.00,28,2),('2022-03-08 18:03:32.300557',5,'2022-03-08 18:04:16.962947',5,29,5.00,29,5),('2022-03-08 18:07:08.181972',5,'2022-03-08 18:07:16.855994',5,30,5.00,30,9);
/*!40000 ALTER TABLE `trn_detalleorden` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trn_detalleordenbodega`
--

DROP TABLE IF EXISTS `trn_detalleordenbodega`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trn_detalleordenbodega` (
  `fecha_creacion` datetime(6) NOT NULL,
  `usuario_crea` int NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `usuario_modifica` int NOT NULL,
  `id_detalle` int NOT NULL AUTO_INCREMENT,
  `cantidad` decimal(10,2) DEFAULT NULL,
  `orden_id` int NOT NULL,
  `producto_id` int NOT NULL,
  PRIMARY KEY (`id_detalle`),
  KEY `trn_detalleordenbode_orden_id_3cdc7549_fk_trn_orden` (`orden_id`),
  KEY `trn_detalleordenbode_producto_id_3e504c42_fk_prd_produ` (`producto_id`),
  CONSTRAINT `trn_detalleordenbode_orden_id_3cdc7549_fk_trn_orden` FOREIGN KEY (`orden_id`) REFERENCES `trn_ordenbodega` (`id_orden`),
  CONSTRAINT `trn_detalleordenbode_producto_id_3e504c42_fk_prd_produ` FOREIGN KEY (`producto_id`) REFERENCES `prd_productos` (`id_producto`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trn_detalleordenbodega`
--

LOCK TABLES `trn_detalleordenbodega` WRITE;
/*!40000 ALTER TABLE `trn_detalleordenbodega` DISABLE KEYS */;
INSERT INTO `trn_detalleordenbodega` VALUES ('2022-03-08 15:57:51.568137',3,'2022-03-08 15:57:51.568137',3,14,200.00,14,14),('2022-03-08 16:04:57.658730',3,'2022-03-08 16:04:57.658730',3,15,200.00,15,14),('2022-03-08 16:18:25.052969',3,'2022-03-08 16:18:25.052969',3,16,15.00,16,3),('2022-03-08 16:19:25.865082',3,'2022-03-08 16:19:25.865082',3,17,10.00,17,3),('2022-03-08 16:26:41.723423',3,'2022-03-08 16:26:41.723423',3,18,100.00,18,11),('2022-03-08 16:29:40.060463',3,'2022-03-08 16:29:40.060463',3,19,50.00,19,11),('2022-03-08 16:34:21.424217',3,'2022-03-08 16:34:21.424217',3,20,15.00,20,2),('2022-03-08 16:36:49.333245',3,'2022-03-08 16:36:49.334241',3,21,5.00,21,2),('2022-03-08 17:54:30.944402',3,'2022-03-08 17:54:30.945401',3,22,7.00,22,9),('2022-03-08 18:07:32.422156',3,'2022-03-08 18:07:32.422156',3,23,5.00,23,9);
/*!40000 ALTER TABLE `trn_detalleordenbodega` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trn_ordenbodega`
--

DROP TABLE IF EXISTS `trn_ordenbodega`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trn_ordenbodega` (
  `fecha_creacion` datetime(6) NOT NULL,
  `usuario_crea` int NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `usuario_modifica` int NOT NULL,
  `id_orden` int NOT NULL AUTO_INCREMENT,
  `encargado_id` int DEFAULT NULL,
  `pedido_id` int DEFAULT NULL,
  `tipo_id` int NOT NULL,
  `estado_id` int DEFAULT NULL,
  `orden_produccion` int DEFAULT NULL,
  PRIMARY KEY (`id_orden`),
  KEY `trn_ordenbodega_encargado_id_19d3047c_fk_usr_usuarios_id` (`encargado_id`),
  KEY `trn_ordenbodega_pedido_id_6371fe73_fk_trn_solic` (`pedido_id`),
  KEY `trn_ordenbodega_tipo_id_5aafc1b3_fk_trn_tipoordenbodega_id_tipo` (`tipo_id`),
  KEY `trn_ordenbodega_estado_id_fe0d9dbf_fk_bases_estados_id_estado` (`estado_id`),
  CONSTRAINT `trn_ordenbodega_encargado_id_19d3047c_fk_usr_usuarios_id` FOREIGN KEY (`encargado_id`) REFERENCES `usr_usuarios` (`id`),
  CONSTRAINT `trn_ordenbodega_estado_id_fe0d9dbf_fk_bases_estados_id_estado` FOREIGN KEY (`estado_id`) REFERENCES `bases_estados` (`id_estado`),
  CONSTRAINT `trn_ordenbodega_pedido_id_6371fe73_fk_trn_solic` FOREIGN KEY (`pedido_id`) REFERENCES `trn_solicitudpedido` (`id_solicitud`),
  CONSTRAINT `trn_ordenbodega_tipo_id_5aafc1b3_fk_trn_tipoordenbodega_id_tipo` FOREIGN KEY (`tipo_id`) REFERENCES `trn_tipoordenbodega` (`id_tipo`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trn_ordenbodega`
--

LOCK TABLES `trn_ordenbodega` WRITE;
/*!40000 ALTER TABLE `trn_ordenbodega` DISABLE KEYS */;
INSERT INTO `trn_ordenbodega` VALUES ('2022-03-08 15:57:51.550964',3,'2022-03-08 16:01:15.819895',3,14,4,16,1,4,NULL),('2022-03-08 16:04:57.634802',3,'2022-03-08 16:16:57.865155',3,15,4,NULL,2,14,25),('2022-03-08 16:18:25.031295',3,'2022-03-08 16:18:46.562083',3,16,4,17,1,4,NULL),('2022-03-08 16:19:25.844105',3,'2022-03-08 16:19:41.400011',3,17,4,NULL,2,14,26),('2022-03-08 16:26:41.692195',3,'2022-03-08 16:27:43.132793',3,18,4,18,1,4,NULL),('2022-03-08 16:29:40.029115',3,'2022-03-08 16:32:22.814405',3,19,4,NULL,2,14,27),('2022-03-08 16:34:21.398210',3,'2022-03-08 16:34:55.681738',3,20,4,19,1,4,NULL),('2022-03-08 16:36:49.294500',3,'2022-03-08 16:36:59.469380',3,21,4,NULL,2,14,28),('2022-03-08 17:54:30.898780',3,'2022-03-08 17:56:15.744982',3,22,4,20,1,4,NULL),('2022-03-08 18:07:32.365297',3,'2022-03-08 18:07:56.263312',3,23,4,NULL,2,14,30);
/*!40000 ALTER TABLE `trn_ordenbodega` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trn_ordenproduccion`
--

DROP TABLE IF EXISTS `trn_ordenproduccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trn_ordenproduccion` (
  `fecha_creacion` datetime(6) NOT NULL,
  `usuario_crea` int NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `usuario_modifica` int NOT NULL,
  `id_solicitud` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(500) NOT NULL,
  `secuencia` varchar(20) DEFAULT NULL,
  `fecha_almacenado` datetime(6) DEFAULT NULL,
  `total_orden` decimal(10,2) DEFAULT NULL,
  `estado_id` int DEFAULT NULL,
  PRIMARY KEY (`id_solicitud`),
  KEY `trn_ordenproduccion_estado_id_b3fef644_fk_bases_est` (`estado_id`),
  CONSTRAINT `trn_ordenproduccion_estado_id_b3fef644_fk_bases_est` FOREIGN KEY (`estado_id`) REFERENCES `bases_estados` (`id_estado`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trn_ordenproduccion`
--

LOCK TABLES `trn_ordenproduccion` WRITE;
/*!40000 ALTER TABLE `trn_ordenproduccion` DISABLE KEYS */;
INSERT INTO `trn_ordenproduccion` VALUES ('2022-03-08 16:02:02.871045',5,'2022-03-08 16:02:30.046471',5,24,'MENSAJE DE PRUEBAS DE ORDEN DE PRODUCCION','ORD-001',NULL,300.00,13),('2022-03-08 16:04:24.898404',5,'2022-03-08 16:04:57.623540',5,25,'MENSAJE 2','ORD-0025',NULL,200.00,14),('2022-03-08 16:10:18.802682',5,'2022-03-08 16:19:25.829617',5,26,'EJEMPLOS','ORD-0026',NULL,10.00,14),('2022-03-08 16:28:48.995254',5,'2022-03-08 16:29:40.013533',5,27,'PRUEBA PROD','ORD-0027',NULL,50.00,14),('2022-03-08 16:32:54.337025',5,'2022-03-08 16:36:49.278915',5,28,'PRUEBA 4','ORD-0028',NULL,5.00,14),('2022-03-08 18:03:32.283288',5,'2022-03-08 18:04:16.971232',5,29,'','ORD-0029',NULL,5.00,13),('2022-03-08 18:07:08.167411',5,'2022-03-08 18:07:32.336354',5,30,'JJJJ','ORD-0030',NULL,5.00,14);
/*!40000 ALTER TABLE `trn_ordenproduccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trn_productossolicitud`
--

DROP TABLE IF EXISTS `trn_productossolicitud`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trn_productossolicitud` (
  `fecha_creacion` datetime(6) NOT NULL,
  `usuario_crea` int NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `usuario_modifica` int NOT NULL,
  `id_detalle` int NOT NULL AUTO_INCREMENT,
  `cantidad` decimal(10,2) DEFAULT NULL,
  `producto_id` int NOT NULL,
  `solicitud_id` int NOT NULL,
  PRIMARY KEY (`id_detalle`),
  KEY `trn_productossolicit_producto_id_8027f64b_fk_prd_produ` (`producto_id`),
  KEY `trn_productossolicit_solicitud_id_401a8326_fk_trn_solic` (`solicitud_id`),
  CONSTRAINT `trn_productossolicit_producto_id_8027f64b_fk_prd_produ` FOREIGN KEY (`producto_id`) REFERENCES `prd_productos` (`id_producto`),
  CONSTRAINT `trn_productossolicit_solicitud_id_401a8326_fk_trn_solic` FOREIGN KEY (`solicitud_id`) REFERENCES `trn_solicitudpedido` (`id_solicitud`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trn_productossolicitud`
--

LOCK TABLES `trn_productossolicitud` WRITE;
/*!40000 ALTER TABLE `trn_productossolicitud` DISABLE KEYS */;
INSERT INTO `trn_productossolicitud` VALUES ('2022-03-08 15:57:10.186498',3,'2022-03-08 15:57:27.530382',3,16,200.00,14,16),('2022-03-08 16:18:13.304738',3,'2022-03-08 16:18:19.926754',3,17,15.00,3,17),('2022-03-08 16:24:38.664467',3,'2022-03-08 16:25:56.246830',3,18,100.00,11,18),('2022-03-08 16:34:03.562486',3,'2022-03-08 16:34:15.028527',3,19,15.00,2,19),('2022-03-08 17:47:34.141471',3,'2022-03-08 17:52:51.808971',3,20,7.00,9,20),('2022-03-08 17:48:49.515364',3,'2022-03-08 17:48:49.515364',3,21,NULL,9,21),('2022-03-08 17:53:06.178270',3,'2022-03-08 17:53:06.178270',3,22,NULL,6,22),('2022-03-08 17:59:08.508036',3,'2022-03-08 17:59:08.508036',3,23,NULL,15,23);
/*!40000 ALTER TABLE `trn_productossolicitud` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trn_solicitudpedido`
--

DROP TABLE IF EXISTS `trn_solicitudpedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trn_solicitudpedido` (
  `fecha_creacion` datetime(6) NOT NULL,
  `usuario_crea` int NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `usuario_modifica` int NOT NULL,
  `id_solicitud` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(500) NOT NULL,
  `proveedor_id` int DEFAULT NULL,
  `fecha_envio` datetime(6) DEFAULT NULL,
  `fecha_recibida` datetime(6) DEFAULT NULL,
  `secuencia` varchar(20) DEFAULT NULL,
  `estado_id` int DEFAULT NULL,
  `total_envio` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id_solicitud`),
  KEY `trn_solicitudpedido_proveedor_id_ce739574_fk_prv_prove` (`proveedor_id`),
  KEY `trn_solicitudpedido_estado_id_4a4d7fd2_fk_bases_est` (`estado_id`),
  CONSTRAINT `trn_solicitudpedido_estado_id_4a4d7fd2_fk_bases_est` FOREIGN KEY (`estado_id`) REFERENCES `bases_estados` (`id_estado`),
  CONSTRAINT `trn_solicitudpedido_proveedor_id_ce739574_fk_prv_prove` FOREIGN KEY (`proveedor_id`) REFERENCES `prv_proveedores` (`id_proveedor`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trn_solicitudpedido`
--

LOCK TABLES `trn_solicitudpedido` WRITE;
/*!40000 ALTER TABLE `trn_solicitudpedido` DISABLE KEYS */;
INSERT INTO `trn_solicitudpedido` VALUES ('2022-03-08 15:57:10.177634',3,'2022-03-08 15:57:51.536540',3,16,'SOLICITA FUNDAS DE ENVOLTURA',1,'2022-03-08 10:57:27.549329','2022-03-08 10:57:51.536540',NULL,9,200.00),('2022-03-08 16:18:13.292231',3,'2022-03-08 16:18:25.018694',3,17,'SDASD',1,'2022-03-08 11:18:19.940716','2022-03-08 11:18:25.018694',NULL,9,15.00),('2022-03-08 16:24:38.633248',3,'2022-03-08 16:26:41.660978',3,18,'PRUEBAS 3',1,'2022-03-08 11:25:56.262282','2022-03-08 11:26:41.660978',NULL,9,100.00),('2022-03-08 16:34:03.553214',3,'2022-03-08 16:34:21.376890',3,19,'PRUEBAS PEDIDO',1,'2022-03-08 11:34:15.047437','2022-03-08 11:34:21.376890',NULL,9,15.00),('2022-03-08 17:47:34.127579',3,'2022-03-08 17:54:30.866607',3,20,'SEMILLAS',1,'2022-03-08 12:52:51.836914','2022-03-08 12:54:30.865568',NULL,9,7.00),('2022-03-08 17:48:49.499137',3,'2022-03-08 17:48:49.499661',3,21,'',NULL,NULL,NULL,NULL,6,0.00),('2022-03-08 17:53:06.164033',3,'2022-03-08 17:53:06.164161',3,22,'',NULL,NULL,NULL,NULL,6,0.00),('2022-03-08 17:59:08.491176',3,'2022-03-08 17:59:08.491176',3,23,'',NULL,NULL,NULL,NULL,6,0.00);
/*!40000 ALTER TABLE `trn_solicitudpedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trn_tipoordenbodega`
--

DROP TABLE IF EXISTS `trn_tipoordenbodega`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trn_tipoordenbodega` (
  `fecha_creacion` datetime(6) NOT NULL,
  `usuario_crea` int NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `usuario_modifica` int NOT NULL,
  `id_tipo` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(100) NOT NULL,
  PRIMARY KEY (`id_tipo`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trn_tipoordenbodega`
--

LOCK TABLES `trn_tipoordenbodega` WRITE;
/*!40000 ALTER TABLE `trn_tipoordenbodega` DISABLE KEYS */;
INSERT INTO `trn_tipoordenbodega` VALUES ('2022-03-06 18:55:17.574530',1,'2022-03-06 18:55:17.574530',1,1,'ENTRADA'),('2022-03-06 18:55:24.044286',1,'2022-03-06 18:55:24.044286',1,2,'SALIDA');
/*!40000 ALTER TABLE `trn_tipoordenbodega` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ubc_bodegas`
--

DROP TABLE IF EXISTS `ubc_bodegas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ubc_bodegas` (
  `id_bodega` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(150) NOT NULL,
  `direccion1` varchar(150) NOT NULL,
  `ciudad_id` int NOT NULL,
  `estado_id` int NOT NULL,
  PRIMARY KEY (`id_bodega`),
  KEY `ubc_bodegas_ciudad_id_5e6cf9a0_fk_ubc_ciudades_id_ciudad` (`ciudad_id`),
  KEY `ubc_bodegas_estado_id_cfb3912a_fk_bases_estados_id_estado` (`estado_id`),
  CONSTRAINT `ubc_bodegas_ciudad_id_5e6cf9a0_fk_ubc_ciudades_id_ciudad` FOREIGN KEY (`ciudad_id`) REFERENCES `ubc_ciudades` (`id_ciudad`),
  CONSTRAINT `ubc_bodegas_estado_id_cfb3912a_fk_bases_estados_id_estado` FOREIGN KEY (`estado_id`) REFERENCES `bases_estados` (`id_estado`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ubc_bodegas`
--

LOCK TABLES `ubc_bodegas` WRITE;
/*!40000 ALTER TABLE `ubc_bodegas` DISABLE KEYS */;
INSERT INTO `ubc_bodegas` VALUES (1,'MARGARITA','KM 24',1,1);
/*!40000 ALTER TABLE `ubc_bodegas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ubc_ciudades`
--

DROP TABLE IF EXISTS `ubc_ciudades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ubc_ciudades` (
  `id_ciudad` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(150) NOT NULL,
  `estado_id` int NOT NULL,
  `pais_id` int NOT NULL,
  `codigo_api_ciudad` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id_ciudad`),
  KEY `ubc_ciudades_pais_id_a3de4d64_fk_ubc_pais_id_pais` (`pais_id`),
  KEY `ubc_ciudades_estado_id_6ff4bfc9_fk_bases_estados_id_estado` (`estado_id`),
  CONSTRAINT `ubc_ciudades_estado_id_6ff4bfc9_fk_bases_estados_id_estado` FOREIGN KEY (`estado_id`) REFERENCES `bases_estados` (`id_estado`),
  CONSTRAINT `ubc_ciudades_pais_id_a3de4d64_fk_ubc_pais_id_pais` FOREIGN KEY (`pais_id`) REFERENCES `ubc_pais` (`id_pais`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ubc_ciudades`
--

LOCK TABLES `ubc_ciudades` WRITE;
/*!40000 ALTER TABLE `ubc_ciudades` DISABLE KEYS */;
INSERT INTO `ubc_ciudades` VALUES (1,'GUAYAQUIL',1,1,'1222222');
/*!40000 ALTER TABLE `ubc_ciudades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ubc_lotes`
--

DROP TABLE IF EXISTS `ubc_lotes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ubc_lotes` (
  `id_lote` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(150) NOT NULL,
  `estado_id` int NOT NULL,
  `sector_id` int NOT NULL,
  `fecha_creacion` datetime(6) NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `usuario_crea` int NOT NULL,
  `usuario_modifica` int NOT NULL,
  PRIMARY KEY (`id_lote`),
  KEY `ubc_lotes_estado_id_0e104aea_fk_bases_estados_id_estado` (`estado_id`),
  KEY `ubc_lotes_sector_id_0d41bd80_fk_ubc_sectores_id_sector` (`sector_id`),
  CONSTRAINT `ubc_lotes_estado_id_0e104aea_fk_bases_estados_id_estado` FOREIGN KEY (`estado_id`) REFERENCES `bases_estados` (`id_estado`),
  CONSTRAINT `ubc_lotes_sector_id_0d41bd80_fk_ubc_sectores_id_sector` FOREIGN KEY (`sector_id`) REFERENCES `ubc_sectores` (`id_sector`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ubc_lotes`
--

LOCK TABLES `ubc_lotes` WRITE;
/*!40000 ALTER TABLE `ubc_lotes` DISABLE KEYS */;
/*!40000 ALTER TABLE `ubc_lotes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ubc_pais`
--

DROP TABLE IF EXISTS `ubc_pais`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ubc_pais` (
  `id_pais` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(150) NOT NULL,
  `estado_id` int NOT NULL,
  `prefijo_cel` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id_pais`),
  KEY `ubc_pais_estado_id_ffdb4d82_fk_bases_estados_id_estado` (`estado_id`),
  CONSTRAINT `ubc_pais_estado_id_ffdb4d82_fk_bases_estados_id_estado` FOREIGN KEY (`estado_id`) REFERENCES `bases_estados` (`id_estado`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ubc_pais`
--

LOCK TABLES `ubc_pais` WRITE;
/*!40000 ALTER TABLE `ubc_pais` DISABLE KEYS */;
INSERT INTO `ubc_pais` VALUES (1,'ECUADOR',1,'+593');
/*!40000 ALTER TABLE `ubc_pais` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ubc_secciones`
--

DROP TABLE IF EXISTS `ubc_secciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ubc_secciones` (
  `id_seccion` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(150) NOT NULL,
  `bodega_id` int NOT NULL,
  `estado_id` int NOT NULL,
  PRIMARY KEY (`id_seccion`),
  KEY `ubc_secciones_bodega_id_35e0e9af_fk_ubc_bodegas_id_bodega` (`bodega_id`),
  KEY `ubc_secciones_estado_id_f3be4a2f_fk_bases_estados_id_estado` (`estado_id`),
  CONSTRAINT `ubc_secciones_bodega_id_35e0e9af_fk_ubc_bodegas_id_bodega` FOREIGN KEY (`bodega_id`) REFERENCES `ubc_bodegas` (`id_bodega`),
  CONSTRAINT `ubc_secciones_estado_id_f3be4a2f_fk_bases_estados_id_estado` FOREIGN KEY (`estado_id`) REFERENCES `bases_estados` (`id_estado`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ubc_secciones`
--

LOCK TABLES `ubc_secciones` WRITE;
/*!40000 ALTER TABLE `ubc_secciones` DISABLE KEYS */;
INSERT INTO `ubc_secciones` VALUES (1,'AGROQUIMICOS',1,1),(2,'FERTILIZANTES',1,1),(3,'SEMILLAS',1,1),(4,'MAQUINARIAS',1,1),(5,'MATERIALES DE SIEMBRA',1,1);
/*!40000 ALTER TABLE `ubc_secciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ubc_sectores`
--

DROP TABLE IF EXISTS `ubc_sectores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ubc_sectores` (
  `id_sector` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(150) NOT NULL,
  `ciudad_id` int NOT NULL,
  `estado_id` int NOT NULL,
  `fecha_creacion` datetime(6) NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `usuario_crea` int NOT NULL,
  `usuario_modifica` int NOT NULL,
  PRIMARY KEY (`id_sector`),
  KEY `ubc_sectores_ciudad_id_55007b92_fk_ubc_ciudades_id_ciudad` (`ciudad_id`),
  KEY `ubc_sectores_estado_id_903dfb0c_fk_bases_estados_id_estado` (`estado_id`),
  CONSTRAINT `ubc_sectores_ciudad_id_55007b92_fk_ubc_ciudades_id_ciudad` FOREIGN KEY (`ciudad_id`) REFERENCES `ubc_ciudades` (`id_ciudad`),
  CONSTRAINT `ubc_sectores_estado_id_903dfb0c_fk_bases_estados_id_estado` FOREIGN KEY (`estado_id`) REFERENCES `bases_estados` (`id_estado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ubc_sectores`
--

LOCK TABLES `ubc_sectores` WRITE;
/*!40000 ALTER TABLE `ubc_sectores` DISABLE KEYS */;
/*!40000 ALTER TABLE `ubc_sectores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usr_roles`
--

DROP TABLE IF EXISTS `usr_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usr_roles` (
  `fecha_creacion` datetime(6) NOT NULL,
  `usuario_crea` int NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `usuario_modifica` int NOT NULL,
  `id_rol` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(100) NOT NULL,
  `estado_id` int NOT NULL,
  `grupo_id` int NOT NULL,
  `tipo_usuario_id` int DEFAULT NULL,
  PRIMARY KEY (`id_rol`),
  KEY `usr_roles_estado_id_47a1c842_fk_bases_estados_id_estado` (`estado_id`),
  KEY `usr_roles_grupo_id_48393073_fk_auth_group_id` (`grupo_id`),
  KEY `usr_roles_tipo_usuario_id_0133f6c2_fk_usr_tipousuario_id_tipo` (`tipo_usuario_id`),
  CONSTRAINT `usr_roles_estado_id_47a1c842_fk_bases_estados_id_estado` FOREIGN KEY (`estado_id`) REFERENCES `bases_estados` (`id_estado`),
  CONSTRAINT `usr_roles_grupo_id_48393073_fk_auth_group_id` FOREIGN KEY (`grupo_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `usr_roles_tipo_usuario_id_0133f6c2_fk_usr_tipousuario_id_tipo` FOREIGN KEY (`tipo_usuario_id`) REFERENCES `usr_tipousuario` (`id_tipo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usr_roles`
--

LOCK TABLES `usr_roles` WRITE;
/*!40000 ALTER TABLE `usr_roles` DISABLE KEYS */;
INSERT INTO `usr_roles` VALUES ('2022-03-06 00:00:00.000000',1,'2022-03-06 07:29:07.205052',1,1,'ADMINISTRADOR',1,1,2),('2022-03-06 18:58:24.810912',3,'2022-03-06 18:58:24.810912',3,2,'BODEGUERO',1,2,2),('2022-03-07 04:06:06.305046',3,'2022-03-07 04:06:06.305046',3,3,'PRODUCCION',1,3,2);
/*!40000 ALTER TABLE `usr_roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usr_tipousuario`
--

DROP TABLE IF EXISTS `usr_tipousuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usr_tipousuario` (
  `fecha_creacion` datetime(6) NOT NULL,
  `usuario_crea` int NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `usuario_modifica` int NOT NULL,
  `id_tipo` int NOT NULL AUTO_INCREMENT,
  `tipo_usuario` varchar(100) DEFAULT NULL,
  `descripcion` varchar(100) NOT NULL,
  PRIMARY KEY (`id_tipo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usr_tipousuario`
--

LOCK TABLES `usr_tipousuario` WRITE;
/*!40000 ALTER TABLE `usr_tipousuario` DISABLE KEYS */;
INSERT INTO `usr_tipousuario` VALUES ('2022-03-06 06:02:14.292532',1,'2022-03-06 06:02:14.292532',1,1,'ADMINISTRADOR','ADMINISTRADOR'),('2022-03-06 06:02:14.292532',1,'2022-03-06 06:02:14.292532',1,2,'INSUMOS','USUARIO INSUMOS'),('2022-03-06 06:02:14.292532',1,'2022-03-06 06:02:14.292532',1,3,'PRODUCCION','USUARIO PRODUCCION');
/*!40000 ALTER TABLE `usr_tipousuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usr_usuarios`
--

DROP TABLE IF EXISTS `usr_usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usr_usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `estado_id` int NOT NULL,
  `pais_id` int NOT NULL,
  `rol_id` int NOT NULL,
  `img_perfil` varchar(100) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `usuario_telegram` varchar(50) DEFAULT NULL,
  `tipo_usuario_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `usr_usuarios_estado_id_02496124_fk_bases_estados_id_estado` (`estado_id`),
  KEY `usr_usuarios_pais_id_41489a88_fk_ubc_pais_id_pais` (`pais_id`),
  KEY `usr_usuarios_rol_id_c665b34a_fk_usr_roles_id_rol` (`rol_id`),
  KEY `usr_usuarios_tipo_usuario_id_a241ad73_fk_usr_tipousuario_id_tipo` (`tipo_usuario_id`),
  CONSTRAINT `usr_usuarios_estado_id_02496124_fk_bases_estados_id_estado` FOREIGN KEY (`estado_id`) REFERENCES `bases_estados` (`id_estado`),
  CONSTRAINT `usr_usuarios_pais_id_41489a88_fk_ubc_pais_id_pais` FOREIGN KEY (`pais_id`) REFERENCES `ubc_pais` (`id_pais`),
  CONSTRAINT `usr_usuarios_rol_id_c665b34a_fk_usr_roles_id_rol` FOREIGN KEY (`rol_id`) REFERENCES `usr_roles` (`id_rol`),
  CONSTRAINT `usr_usuarios_tipo_usuario_id_a241ad73_fk_usr_tipousuario_id_tipo` FOREIGN KEY (`tipo_usuario_id`) REFERENCES `usr_tipousuario` (`id_tipo`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usr_usuarios`
--

LOCK TABLES `usr_usuarios` WRITE;
/*!40000 ALTER TABLE `usr_usuarios` DISABLE KEYS */;
INSERT INTO `usr_usuarios` VALUES (3,'pbkdf2_sha256$150000$t8Ebi3YFkdBa$Gjx3CAt6zRDbbrm9zBgXZzaFbdKueAm7/oN1lzNL+w0=','2022-03-07 17:47:17.022882',1,'fbriones','Franklin','Briones','javier1992frank@gmail.com',1,1,'2022-03-06 06:01:41.506576',1,1,1,'','0989273646',NULL,2),(4,'pbkdf2_sha256$150000$t8Ebi3YFkdBa$Gjx3CAt6zRDbbrm9zBgXZzaFbdKueAm7/oN1lzNL+w0=','2022-03-08 16:30:33.733254',0,'josep','Jose','Jose','jose@mail.com',1,1,'2022-03-06 06:02:14.292532',1,1,2,NULL,'0999999999',NULL,2),(5,'pbkdf2_sha256$150000$t8Ebi3YFkdBa$Gjx3CAt6zRDbbrm9zBgXZzaFbdKueAm7/oN1lzNL+w0=','2022-03-08 16:55:40.275289',0,'produccion','Produccion','.','franko@mail.com',0,1,'2022-03-07 04:08:40.415204',1,1,3,'','1233453212','das',3);
/*!40000 ALTER TABLE `usr_usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usr_usuarios_groups`
--

DROP TABLE IF EXISTS `usr_usuarios_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usr_usuarios_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuarios_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usr_usuarios_groups_usuarios_id_group_id_2461287a_uniq` (`usuarios_id`,`group_id`),
  KEY `usr_usuarios_groups_group_id_89202b4d_fk_auth_group_id` (`group_id`),
  CONSTRAINT `usr_usuarios_groups_group_id_89202b4d_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `usr_usuarios_groups_usuarios_id_b523eff4_fk_usr_usuarios_id` FOREIGN KEY (`usuarios_id`) REFERENCES `usr_usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usr_usuarios_groups`
--

LOCK TABLES `usr_usuarios_groups` WRITE;
/*!40000 ALTER TABLE `usr_usuarios_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `usr_usuarios_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usr_usuarios_user_permissions`
--

DROP TABLE IF EXISTS `usr_usuarios_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usr_usuarios_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuarios_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usr_usuarios_user_permis_usuarios_id_permission_i_353ebfd2_uniq` (`usuarios_id`,`permission_id`),
  KEY `usr_usuarios_user_pe_permission_id_a9552108_fk_auth_perm` (`permission_id`),
  CONSTRAINT `usr_usuarios_user_pe_permission_id_a9552108_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `usr_usuarios_user_pe_usuarios_id_a0503182_fk_usr_usuar` FOREIGN KEY (`usuarios_id`) REFERENCES `usr_usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usr_usuarios_user_permissions`
--

LOCK TABLES `usr_usuarios_user_permissions` WRITE;
/*!40000 ALTER TABLE `usr_usuarios_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `usr_usuarios_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'finca_bnn'
--

--
-- Dumping routines for database 'finca_bnn'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-04 17:00:17
