-- MySQL Script generated by MySQL Workbench
-- Tue Jul 27 22:15:58 2021
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema db_sistema
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema db_sistema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `db_pos` DEFAULT CHARACTER SET latin1 ;
USE `db_pos` ;

-- -----------------------------------------------------
-- Table `db_sistema`.`rol`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_pos`.`rol` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `db_sistema`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_pos`.`usuario` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(50) NOT NULL,
  `clave` VARCHAR(100) NOT NULL,
  `rol_id` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `usuario_ibfk_1`
    FOREIGN KEY (`rol_id`)
    REFERENCES `db_pos`.`rol` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `db_sistema`.`categorias`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_pos`.`categorias` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_sistema`.`productos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_pos`.`productos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `precio` DECIMAL NOT NULL,
  `stock` INT(11) NOT NULL DEFAULT 0 COMMENT 'stock del producto',
  `categorias_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_productos_categorias1`
    FOREIGN KEY (`categorias_id`)
    REFERENCES `db_pos`.`categorias` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
