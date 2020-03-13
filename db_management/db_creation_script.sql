DROP SCHEMA IF EXISTS `main_db_food_suggestor` ;


CREATE SCHEMA IF NOT EXISTS `main_db_food_suggestor` DEFAULT CHARACTER SET utf8mb4;
USE `main_db_food_suggestor` ;


CREATE TABLE IF NOT EXISTS `main_db_food_suggestor`.`categorie` (
  `ID` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE INDEX `related_category_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


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
DEFAULT CHARACTER SET = utf8mb4;


CREATE TABLE IF NOT EXISTS `main_db_food_suggestor`.`substitut` (
  `ID` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `id_initial_product` INT(10) UNSIGNED NOT NULL UNIQUE,
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
DEFAULT CHARACTER SET = utf8mb4;