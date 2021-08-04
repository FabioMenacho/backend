-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         5.7.33 - MySQL Community Server (GPL)
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para db_sistemapos
-- CREATE DATABASE IF NOT EXISTS `db_sistemapos` /*!40100 DEFAULT CHARACTER SET latin1 COLLATE latin1_spanish_ci */;
USE `bk_dia5`;

-- Volcando estructura para tabla db_sistemapos.cat_producto
CREATE TABLE IF NOT EXISTS `cat_producto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE latin1_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci COMMENT='categoria de producto';

-- Volcando datos para la tabla db_sistemapos.cat_producto: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `cat_producto` DISABLE KEYS */;
INSERT INTO `cat_producto` (`id`, `nombre`) VALUES
	(1, 'PC'),
	(2, 'LAPTOP');
/*!40000 ALTER TABLE `cat_producto` ENABLE KEYS */;

-- Volcando estructura para tabla db_sistemapos.clientes
CREATE TABLE IF NOT EXISTS `clientes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_doc_id` int(11) NOT NULL DEFAULT '0' COMMENT 'referencia a tabla tipo_doc',
  `nro_doc` varchar(20) CHARACTER SET latin1 COLLATE latin1_spanish_ci NOT NULL DEFAULT '',
  `nombre` varchar(255) CHARACTER SET latin1 COLLATE latin1_spanish_ci NOT NULL DEFAULT '',
  `telefono` varchar(20) CHARACTER SET latin1 COLLATE latin1_spanish_ci DEFAULT '',
  `email` varchar(20) CHARACTER SET latin1 COLLATE latin1_spanish_ci DEFAULT '',
  PRIMARY KEY (`id`),
  UNIQUE KEY `u_documento` (`tipo_doc_id`,`nro_doc`) USING BTREE,
  CONSTRAINT `fk_clientes_tipo_doc` FOREIGN KEY (`tipo_doc_id`) REFERENCES `tipo_doc` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci COMMENT='Registro los clientes del sistema';

-- Volcando datos para la tabla db_sistemapos.clientes: ~1 rows (aproximadamente)
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` (`id`, `tipo_doc_id`, `nro_doc`, `nombre`, `telefono`, `email`) VALUES
	(1, 1, '41458784', 'fabio', '997064940', 'fmenacho@uni.pe'),
	(2, 2, '20457368', 'safiro srl', '014556633', 'info@safiro.com');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;

-- Volcando estructura para tabla db_sistemapos.producto
CREATE TABLE IF NOT EXISTS `producto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cat_producto_id` int(11) NOT NULL DEFAULT '0',
  `nombre` varchar(255) COLLATE latin1_spanish_ci NOT NULL DEFAULT '0',
  `marca` varchar(255) COLLATE latin1_spanish_ci DEFAULT '0',
  `modelo` varchar(255) COLLATE latin1_spanish_ci DEFAULT '0',
  `nro_serie` varchar(255) COLLATE latin1_spanish_ci DEFAULT '0',
  `mem_ram` varchar(255) COLLATE latin1_spanish_ci NOT NULL DEFAULT '0',
  `procesador` varchar(255) COLLATE latin1_spanish_ci NOT NULL DEFAULT '0',
  `disco_duro` varchar(255) COLLATE latin1_spanish_ci NOT NULL DEFAULT '0',
  `precio` decimal(10,2) NOT NULL DEFAULT '0.00',
  `stock` bigint(20) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `fk_producto_cat_producto_id` (`cat_producto_id`),
  CONSTRAINT `fk_producto_cat_producto_id` FOREIGN KEY (`cat_producto_id`) REFERENCES `cat_producto` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci COMMENT='producto';

-- Volcando datos para la tabla db_sistemapos.producto: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` (`id`, `cat_producto_id`, `nombre`, `marca`, `modelo`, `nro_serie`, `mem_ram`, `procesador`, `disco_duro`, `precio`, `stock`) VALUES
	(1, 1, 'PC CORE I5 ESTUDIANTES', 'LENOVO', 'E5100', 'ER534242', '8 GB', 'CORE I5 10', '1 TB', 3500.00, 10),
	(2, 2, 'DELL INSPIRON 5000', 'DELL', 'INSPIRON', 'GH765432', '16 GB', 'CORE I7 11', '1 TB', 4700.00, 5),
	(3, 2, 'LAPTOR GAMER DOTA 2', 'ACER', '234', 'GFDGD65432', '64 GB', 'AMD RAYZER 9', '4 TB', 15600.00, 1);
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;

-- Volcando estructura para tabla db_sistemapos.tipo_doc
CREATE TABLE IF NOT EXISTS `tipo_doc` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) COLLATE latin1_spanish_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci COMMENT='tipo de documento de identidad';

-- Volcando datos para la tabla db_sistemapos.tipo_doc: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `tipo_doc` DISABLE KEYS */;
INSERT INTO `tipo_doc` (`id`, `nombre`) VALUES
	(1, 'DNI'),
	(2, 'RUC'),
	(3, 'CARNET EXTRANJERIA');
/*!40000 ALTER TABLE `tipo_doc` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
