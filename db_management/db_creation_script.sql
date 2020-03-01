-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema main_db_food_suggestor
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `main_db_food_suggestor` ;

-- -----------------------------------------------------
-- Schema main_db_food_suggestor
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `main_db_food_suggestor` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `main_db_food_suggestor` ;

-- -----------------------------------------------------
-- Table `main_db_food_suggestor`.`categorie`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `main_db_food_suggestor`.`categorie` (
  `ID` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE INDEX `related_category_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB
-- AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `main_db_food_suggestor`.`db_aliments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `main_db_food_suggestor`.`db_aliments` (
  `ID` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `categorie_id` INT(10) UNSIGNED NOT NULL,
  `alim_name` VARCHAR(255) NOT NULL,
  `store` VARCHAR(255) NOT NULL,
  `website_link` VARCHAR(255) NOT NULL,
  `nutriscore` TINYTEXT NOT NULL,
  PRIMARY KEY (`ID`),
  INDEX `fk_db_aliments_categorie_idx` (`categorie_id` ASC) VISIBLE,
  CONSTRAINT `fk_db_aliments_categorie`
    FOREIGN KEY (`categorie_id`)
    REFERENCES `main_db_food_suggestor`.`categorie` (`ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `main_db_food_suggestor`.`substitut`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `main_db_food_suggestor`.`substitut` (
  `ID` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `id_initial_product` INT(10) UNSIGNED NOT NULL,
  `id_substitute_product` INT(10) UNSIGNED NOT NULL,
  PRIMARY KEY (`ID`),
  INDEX `fk_substitut_db_aliments1_idx` (`id_initial_product` ASC) VISIBLE,
  INDEX `fk_substitut_db_aliments2_idx` (`id_substitute_product` ASC) VISIBLE,
  CONSTRAINT `fk_substitut_db_aliments1`
    FOREIGN KEY (`id_initial_product`)
    REFERENCES `main_db_food_suggestor`.`db_aliments` (`ID`),
  CONSTRAINT `fk_substitut_db_aliments2`
    FOREIGN KEY (`id_substitute_product`)
    REFERENCES `main_db_food_suggestor`.`db_aliments` (`ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
