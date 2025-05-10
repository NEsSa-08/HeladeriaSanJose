-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema HeladeriaSanJose
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `HeladeriaSanJose` ;

-- -----------------------------------------------------
-- Schema HeladeriaSanJose
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `HeladeriaSanJose` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `HeladeriaSanJose` ;

-- -----------------------------------------------------
-- Table `HeladeriaSanJose`.`clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `HeladeriaSanJose`.`clientes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(25) NOT NULL,
  `telefono` INT(13) NULL DEFAULT NULL,
  `email` VARCHAR(25) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `HeladeriaSanJose`.`pedidos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `HeladeriaSanJose`.`pedidos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `cliente_id` INT NULL,
  `fecha` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `total` FLOAT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `cliente_id` (`cliente_id` ASC) VISIBLE,
  CONSTRAINT `pedidos_ibfk_1`
    FOREIGN KEY (`cliente_id`)
    REFERENCES `HeladeriaSanJose`.`clientes` (`id`)
    ON DELETE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `HeladeriaSanJose`.`productos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `HeladeriaSanJose`.`productos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(30) NOT NULL,
  `precio` DECIMAL(10,2) NOT NULL,
  `descripcion` VARCHAR(50) NULL DEFAULT NULL,
  `tipo` VARCHAR(40) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `HeladeriaSanJose`.`detalle_pedido`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `HeladeriaSanJose`.`detalle_pedido` (
  `id` INT UNSIGNED NOT NULL,
  `pedido_id` INT NULL DEFAULT NULL,
  `producto_id` INT NULL DEFAULT NULL,
  `cantidad` INT NOT NULL,
  `subtotal` FLOAT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `producto_id` (`producto_id` ASC) VISIBLE,
  INDEX `detalle_pedido_ibfk_1_idx` (`pedido_id` ASC) VISIBLE,
  CONSTRAINT `detalle_pedido_ibfk_1`
    FOREIGN KEY (`pedido_id`)
    REFERENCES `HeladeriaSanJose`.`pedidos` (`id`)
    ON DELETE CASCADE,
  CONSTRAINT `detalle_pedido_ibfk_2`
    FOREIGN KEY (`producto_id`)
    REFERENCES `HeladeriaSanJose`.`productos` (`id`)
    ON DELETE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
