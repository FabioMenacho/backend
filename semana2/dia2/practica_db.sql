-- MySQL Script generated by MySQL Workbench
-- Fri Jul 30 16:26:07 2021
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema db_practica
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema db_practica
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `db_practica` DEFAULT CHARACTER SET latin1 ;
-- -----------------------------------------------------
-- Schema db_pos
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema db_pos
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `db_pos` DEFAULT CHARACTER SET latin1 ;
USE `db_practica` ;

-- -----------------------------------------------------
-- Table `db_practica`.`rol`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_practica`.`rol` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `db_practica`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_practica`.`usuario` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(50) NOT NULL,
  `clave` VARCHAR(100) NOT NULL,
  `rol_id` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `usuario_ibfk_1`
    FOREIGN KEY (`rol_id`)
    REFERENCES `db_practica`.`rol` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `db_practica`.`categorias`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_practica`.`categorias` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_practica`.`productos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_practica`.`productos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `precio` DECIMAL NOT NULL,
  `stock` INT(11) NOT NULL DEFAULT 0 COMMENT 'stock del producto',
  `categorias_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_productos_categorias1`
    FOREIGN KEY (`categorias_id`)
    REFERENCES `db_practica`.`categorias` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `db_pos` ;

-- -----------------------------------------------------
-- Table `db_pos`.`categorias`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_pos`.`categorias` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `db_pos`.`productos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_pos`.`productos` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `precio` DECIMAL NOT NULL,
  `categorias_id` INT(11) NOT NULL,
  `nombre` VARCHAR(100) NOT NULL,
  `stock` INT(11) NOT NULL DEFAULT 0 COMMENT 'stock del producto',
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_productos_categorias`
    FOREIGN KEY (`categorias_id`)
    REFERENCES `db_pos`.`categorias` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `db_pos`.`rol`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_pos`.`rol` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `db_pos`.`usuario`
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


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
