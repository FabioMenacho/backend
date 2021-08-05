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

-- Volcando estructura para tabla db_practicasistemapos.tipo_doc_ide
CREATE TABLE IF NOT EXISTS `tipo_doc_ide` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci COMMENT='tipos de documentos de identidad';

-- Volcando datos para la tabla db_practicasistemapos.tipo_doc_ide: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `tipo_doc_ide` DISABLE KEYS */;
INSERT INTO `tipo_doc_ide` (`id`, `nombre`) VALUES
	(1, 'DNI'),
	(2, 'RUC'),
	(3, 'CARNET DE EXTRANJERIA');
/*!40000 ALTER TABLE `tipo_doc_ide` ENABLE KEYS */;


-- Volcando estructura para tabla db_practicasistemapos.cat_producto
CREATE TABLE IF NOT EXISTS `cat_producto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci COMMENT='categoria de producto';

-- Volcando datos para la tabla db_practicasistemapos.cat_producto: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `cat_producto` DISABLE KEYS */;
INSERT INTO `cat_producto` (`id`, `nombre`) VALUES
	(1, 'PC'),
	(2, 'LAPTOP');
/*!40000 ALTER TABLE `cat_producto` ENABLE KEYS */;

-- Volcando estructura para tabla db_practicasistemapos.clientes
CREATE TABLE IF NOT EXISTS `clientes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_doc_ide_id` int(11) NOT NULL DEFAULT '0' COMMENT 'referencia a tabla tipo_doc_ide',
  `nro_doc` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `nombre` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `telefono` varchar(20) COLLATE utf8_spanish_ci DEFAULT NULL,
  `email` varchar(20) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `u_documento_identidad` (`tipo_doc_ide_id`,`nro_doc`),
  CONSTRAINT `fk_clientes_tipo_doc_ide` FOREIGN KEY (`tipo_doc_ide_id`) REFERENCES `tipo_doc_ide` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci COMMENT='registra los clientes del sistema';

-- Volcando datos para la tabla db_practicasistemapos.clientes: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` (`id`, `tipo_doc_ide_id`, `nro_doc`, `nombre`, `telefono`, `email`) VALUES
	(1, 1, '441458784', 'Fernando', '997064940', 'fmenacho@ni.pe'),
	(2, 2, '20507836372', 'safiro srl', '014557085', 'info@safirosrl.pe'),
	(3, 1, '41458784', 'fabio M', NULL, NULL);
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;

-- Volcando estructura para tabla db_practicasistemapos.producto
CREATE TABLE IF NOT EXISTS `producto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cat_producto_id` int(11) NOT NULL,
  `nombre` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `marca` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `modelo` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `nro_serie` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `mem_ram` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `procesador` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `disco_duro` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `precio` decimal(10,2) NOT NULL DEFAULT '0.00',
  `stock` bigint(20) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `fk_producto_cat_producto_id` (`cat_producto_id`),
  CONSTRAINT `fk_producto_cat_producto_id` FOREIGN KEY (`cat_producto_id`) REFERENCES `cat_producto` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci COMMENT='producto';

-- Volcando datos para la tabla db_practicasistemapos.producto: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` (`id`, `cat_producto_id`, `nombre`, `marca`, `modelo`, `nro_serie`, `mem_ram`, `procesador`, `disco_duro`, `precio`, `stock`) VALUES
	(1, 1, 'PC CORE I5 ESTUDIANTES', 'LENOVO', 'E5100', 'DDS56576', '8 GB', 'CORE I5 10G', '1 TB', 3500.00, 10),
	(2, 2, 'DELL INSPIRON 5000', 'DELL', 'INSPIRON', 'SDGFHG76543', '16 GB', 'CORE I7 11G', '1 TB', 4700.00, 5),
	(3, 1, 'PC GAMER', 'ASUS', 'COMMIT', 'FD6545', '32 GB', 'INTEL CORE I9', '4 TB', 9750.00, 3);
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;


/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
