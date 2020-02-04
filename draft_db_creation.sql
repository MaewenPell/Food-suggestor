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

-- -----------------------------------------------------
-- Schema main_db_food_suggestor
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `main_db_food_suggestor` DEFAULT CHARACTER SET utf8mb4 ;
USE `main_db_food_suggestor` ;

-- -----------------------------------------------------
-- Table `main_db_food_suggestor`.`categorie`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `main_db_food_suggestor`.`categorie` ;

CREATE TABLE IF NOT EXISTS `main_db_food_suggestor`.`categorie` (
  `ID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `related_category` VARCHAR(45) NOT NULL,
  `id_off` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE INDEX `related_category_UNIQUE` (`related_category` ASC) VISIBLE,
  UNIQUE INDEX `id_off_UNIQUE` (`id_off` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `main_db_food_suggestor`.`db_aliments`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `main_db_food_suggestor`.`db_aliments` ;

CREATE TABLE IF NOT EXISTS `main_db_food_suggestor`.`db_aliments` (
  `ID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `categorie_ID` INT UNSIGNED NOT NULL,
  `nom_aliment` VARCHAR(50) NOT NULL,
  `magasin` VARCHAR(30) NOT NULL,
  `lien` VARCHAR(255) NOT NULL,
  `nutriscore` TINYTEXT NOT NULL,
  PRIMARY KEY (`ID`),
  INDEX `fk_db_aliments_categorie_idx` (`categorie_ID` ASC) VISIBLE,
  CONSTRAINT `fk_db_aliments_categorie`
    FOREIGN KEY (`categorie_ID`)
    REFERENCES `main_db_food_suggestor`.`categorie` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `main_db_food_suggestor`.`substitut`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `main_db_food_suggestor`.`substitut` ;

CREATE TABLE IF NOT EXISTS `main_db_food_suggestor`.`substitut` (
  `ID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `ID_produit_initial` INT UNSIGNED NOT NULL,
  `ID_produit_subsitut` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`ID`),
  INDEX `fk_substitut_db_aliments1_idx` (`ID_produit_initial` ASC) VISIBLE,
  INDEX `fk_substitut_db_aliments2_idx` (`ID_produit_subsitut` ASC) VISIBLE,
  CONSTRAINT `fk_substitut_db_aliments1`
    FOREIGN KEY (`ID_produit_initial`)
    REFERENCES `main_db_food_suggestor`.`db_aliments` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_substitut_db_aliments2`
    FOREIGN KEY (`ID_produit_subsitut`)
    REFERENCES `main_db_food_suggestor`.`db_aliments` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
