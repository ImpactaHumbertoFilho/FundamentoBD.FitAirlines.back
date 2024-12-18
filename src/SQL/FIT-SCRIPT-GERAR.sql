-- MySQL Script generated by MySQL Workbench
-- Wed Nov 20 16:22:11 2024
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema FITAIRLINES
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `FITAIRLINES` ;

-- -----------------------------------------------------
-- Schema FITAIRLINES
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `FITAIRLINES` DEFAULT CHARACTER SET utf16 ;
USE `FITAIRLINES` ;

-- -----------------------------------------------------
-- Table `FITAIRLINES`.`CLASSE`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `FITAIRLINES`.`CLASSE` ;

CREATE TABLE IF NOT EXISTS `FITAIRLINES`.`CLASSE` (
  `ID_CLASSE` INT NOT NULL AUTO_INCREMENT,
  `TIPO` VARCHAR(45) NULL,
  `PRIORIDADE` INT NULL,
  `DESCRICAO` VARCHAR(255) NULL,
  `NOME` VARCHAR(50) NULL,
  `PRECO_ADICIONAL` DECIMAL NULL,
  PRIMARY KEY (`ID_CLASSE`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FITAIRLINES`.`TIPO_AERONAVE`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `FITAIRLINES`.`TIPO_AERONAVE` ;

CREATE TABLE IF NOT EXISTS `FITAIRLINES`.`TIPO_AERONAVE` (
  `ID_TIPO_AERONAVE` INT NOT NULL AUTO_INCREMENT,
  `NOME` VARCHAR(100) NULL,
  `FABRICANTE` VARCHAR(100) NULL,
  `CAPACIDADE_PASSAGEIROS` INT NULL,
  `DESCRICAO` VARCHAR(255) NULL,
  PRIMARY KEY (`ID_TIPO_AERONAVE`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FITAIRLINES`.`Aeronave`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `FITAIRLINES`.`Aeronave` ;

CREATE TABLE IF NOT EXISTS `FITAIRLINES`.`Aeronave` (
  `ID_AERONAVE` INT NOT NULL AUTO_INCREMENT,
  `ID_TIPO_AERONAVE` INT NOT NULL,
  `CODIGO` VARCHAR(20) NULL,
  `MODELO` VARCHAR(100) NULL,
  `ANO_FABRICACAO` YEAR NULL,
  `HORAS_VOADAS` DECIMAL(10,2) NULL DEFAULT 0,
  `STATUS` ENUM('ATIVA', 'MANUTENCAO', 'INATIVA') NULL DEFAULT 'ATIVA',
  PRIMARY KEY (`ID_AERONAVE`, `ID_TIPO_AERONAVE`),
  INDEX `fk_Aeronave_TIPO_AERONAVE1_idx` (`ID_TIPO_AERONAVE` ASC) VISIBLE,
  CONSTRAINT `fk_Aeronave_TIPO_AERONAVE1`
    FOREIGN KEY (`ID_TIPO_AERONAVE`)
    REFERENCES `FITAIRLINES`.`TIPO_AERONAVE` (`ID_TIPO_AERONAVE`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FITAIRLINES`.`ASSENTO`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `FITAIRLINES`.`ASSENTO` ;

CREATE TABLE IF NOT EXISTS `FITAIRLINES`.`ASSENTO` (
  `ID_ASSENTO` INT NOT NULL AUTO_INCREMENT,
  `ID_CLASSE` INT NOT NULL,
  `ID_AERONAVE` INT NOT NULL,
  `NUMERO` VARCHAR(5) NULL,
  `LOCALIZACAO` VARCHAR(10) NULL,
  `DESCRICAO` VARCHAR(255) NULL,
  PRIMARY KEY (`ID_ASSENTO`, `ID_CLASSE`, `ID_AERONAVE`),
  UNIQUE INDEX `idASSENTO_UNIQUE` (`ID_ASSENTO` ASC) VISIBLE,
  INDEX `fk_ASSENTO_CLASSE_idx` (`ID_CLASSE` ASC) VISIBLE,
  INDEX `fk_ASSENTO_Aeronave1_idx` (`ID_AERONAVE` ASC) VISIBLE,
  CONSTRAINT `fk_ASSENTO_CLASSE`
    FOREIGN KEY (`ID_CLASSE`)
    REFERENCES `FITAIRLINES`.`CLASSE` (`ID_CLASSE`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ASSENTO_Aeronave1`
    FOREIGN KEY (`ID_AERONAVE`)
    REFERENCES `FITAIRLINES`.`Aeronave` (`ID_AERONAVE`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FITAIRLINES`.`PASSAGEIRO`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `FITAIRLINES`.`PASSAGEIRO` ;

CREATE TABLE IF NOT EXISTS `FITAIRLINES`.`PASSAGEIRO` (
  `ID_PASSAGEIRO` INT NOT NULL AUTO_INCREMENT,
  `NOME` VARCHAR(200) NULL,
  `ENDERECO` VARCHAR(500) NULL,
  `TELEFONE` VARCHAR(20) NULL,
  `DATA_NASCIMENTO` DATETIME NULL,
  `CPF` VARCHAR(11) NULL,
  `NACIONALIDADE` VARCHAR(45) NULL,
  `EMAIL` VARCHAR(100) NULL,
  PRIMARY KEY (`ID_PASSAGEIRO`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FITAIRLINES`.`AEROPORTO`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `FITAIRLINES`.`AEROPORTO` ;

CREATE TABLE IF NOT EXISTS `FITAIRLINES`.`AEROPORTO` (
  `ID_AEROPORTO` INT NOT NULL AUTO_INCREMENT,
  `NOME` VARCHAR(100) NULL,
  `CIDADE` VARCHAR(50) NULL,
  `ESTADO` VARCHAR(50) NULL,
  `PAIS` VARCHAR(50) NULL,
  `CAPACIDADE` INT NULL,
  `CODIGO` VARCHAR(10) NULL,
  `LATITUDE` DECIMAL(9,6) NULL,
  `LONGITUDE` DECIMAL(9,6) NULL,
  PRIMARY KEY (`ID_AEROPORTO`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FITAIRLINES`.`VOO`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `FITAIRLINES`.`VOO` ;

CREATE TABLE IF NOT EXISTS `FITAIRLINES`.`VOO` (
  `ID_VOO` INT NOT NULL AUTO_INCREMENT,
  `ID_AERONAVE` INT NOT NULL,
  `ID_AEROPORTO_PARTIDA` INT NOT NULL,
  `ID_AEROPORTO_CHEGADA` INT NOT NULL,
  `CODIGO` VARCHAR(15) NULL,
  `PARTIDA` DATETIME NULL,
  `CHEGADA` DATETIME NULL,
  `DURACAO` TIME NULL,
  `ASSENTOS_DISPONIVEIS` INT NULL,
  `STATUS` ENUM("programado", "em andamento", "cancelado", "finalizado") NULL,
  `PRECO_BASE` DECIMAL(10,2) NULL,
  PRIMARY KEY (`ID_VOO`, `ID_AERONAVE`, `ID_AEROPORTO_PARTIDA`, `ID_AEROPORTO_CHEGADA`),
  INDEX `fk_VOO_AEROPORTO1_idx` (`ID_AEROPORTO_PARTIDA` ASC) VISIBLE,
  INDEX `fk_VOO_AEROPORTO2_idx` (`ID_AEROPORTO_CHEGADA` ASC) VISIBLE,
  INDEX `fk_VOO_Aeronave1_idx` (`ID_AERONAVE` ASC) VISIBLE,
  CONSTRAINT `fk_VOO_AEROPORTO1`
    FOREIGN KEY (`ID_AEROPORTO_PARTIDA`)
    REFERENCES `FITAIRLINES`.`AEROPORTO` (`ID_AEROPORTO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_VOO_AEROPORTO2`
    FOREIGN KEY (`ID_AEROPORTO_CHEGADA`)
    REFERENCES `FITAIRLINES`.`AEROPORTO` (`ID_AEROPORTO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_VOO_Aeronave1`
    FOREIGN KEY (`ID_AERONAVE`)
    REFERENCES `FITAIRLINES`.`Aeronave` (`ID_AERONAVE`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FITAIRLINES`.`ITINERARIO`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `FITAIRLINES`.`ITINERARIO` ;

CREATE TABLE IF NOT EXISTS `FITAIRLINES`.`ITINERARIO` (
  `ID_ITINERARIO` INT NOT NULL AUTO_INCREMENT,
  `PARADAS` VARCHAR(255) NULL,
  `DISTANCIA_KM` FLOAT NULL,
  `DURACAO` TIME NULL,
  `DESCRICAO` VARCHAR(255) NULL,
  PRIMARY KEY (`ID_ITINERARIO`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FITAIRLINES`.`RELATORIO`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `FITAIRLINES`.`RELATORIO` ;

CREATE TABLE IF NOT EXISTS `FITAIRLINES`.`RELATORIO` (
  `ID_RELATORIO` INT NOT NULL AUTO_INCREMENT,
  `ID_VOO` INT NOT NULL,
  `TEMPO` VARCHAR(15) NULL,
  `EMBARQUE` DATETIME NULL,
  `DESEMBARQUE` DATETIME NULL,
  `CLIMA` VARCHAR(20) NULL,
  `DESCRICAO` VARCHAR(750) NULL,
  `DATA` DATETIME NULL,
  PRIMARY KEY (`ID_RELATORIO`, `ID_VOO`),
  INDEX `fk_RELATORIO_VOO1_idx` (`ID_VOO` ASC) VISIBLE,
  CONSTRAINT `fk_RELATORIO_VOO1`
    FOREIGN KEY (`ID_VOO`)
    REFERENCES `FITAIRLINES`.`VOO` (`ID_VOO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FITAIRLINES`.`RESERVA_DE_ASSENTO_VOO`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `FITAIRLINES`.`RESERVA_DE_ASSENTO_VOO` ;

CREATE TABLE IF NOT EXISTS `FITAIRLINES`.`RESERVA_DE_ASSENTO_VOO` (
  `ID_RESERVA_DE_ASSENTO_VOO` INT NOT NULL AUTO_INCREMENT,
  `ID_VOO` INT NOT NULL,
  `ID_ASSENTO` INT NOT NULL,
  `ID_PASSAGEIRO` INT NOT NULL,
  `VALOR_TOTAL` DECIMAL(10,2) NULL,
  `DATA` DATE NULL,
  PRIMARY KEY (`ID_RESERVA_DE_ASSENTO_VOO`, `ID_VOO`, `ID_ASSENTO`, `ID_PASSAGEIRO`),
  INDEX `fk_ASSENTO_VOO_VOO1_idx` (`ID_VOO` ASC) VISIBLE,
  INDEX `fk_RESERVA_DE_ASSENTO_VOO_ASSENTO1_idx` (`ID_ASSENTO` ASC) VISIBLE,
  INDEX `fk_RESERVA_DE_ASSENTO_VOO_PASSAGEIRO1_idx` (`ID_PASSAGEIRO` ASC) VISIBLE,
  CONSTRAINT `fk_ASSENTO_VOO_VOO1`
    FOREIGN KEY (`ID_VOO`)
    REFERENCES `FITAIRLINES`.`VOO` (`ID_VOO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_RESERVA_DE_ASSENTO_VOO_ASSENTO1`
    FOREIGN KEY (`ID_ASSENTO`)
    REFERENCES `FITAIRLINES`.`ASSENTO` (`ID_ASSENTO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_RESERVA_DE_ASSENTO_VOO_PASSAGEIRO1`
    FOREIGN KEY (`ID_PASSAGEIRO`)
    REFERENCES `FITAIRLINES`.`PASSAGEIRO` (`ID_PASSAGEIRO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FITAIRLINES`.`TICKET`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `FITAIRLINES`.`TICKET` ;

CREATE TABLE IF NOT EXISTS `FITAIRLINES`.`TICKET` (
  `ID_TICKET` INT NOT NULL AUTO_INCREMENT,
  `ID_RESERVA_DE_ASSENTO_VOO` INT NOT NULL,
  `DATA_EMISSAO` DATETIME NULL,
  `PRECO_FINAL` DECIMAL NULL,
  `STATUS` INT NULL,
  PRIMARY KEY (`ID_TICKET`, `ID_RESERVA_DE_ASSENTO_VOO`),
  UNIQUE INDEX `ID_TICKET_UNIQUE` (`ID_TICKET` ASC) VISIBLE,
  INDEX `fk_TICKET_RESERVA_DE_ASSENTO_VOO1_idx` (`ID_RESERVA_DE_ASSENTO_VOO` ASC) VISIBLE,
  CONSTRAINT `fk_TICKET_RESERVA_DE_ASSENTO_VOO1`
    FOREIGN KEY (`ID_RESERVA_DE_ASSENTO_VOO`)
    REFERENCES `FITAIRLINES`.`RESERVA_DE_ASSENTO_VOO` (`ID_RESERVA_DE_ASSENTO_VOO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FITAIRLINES`.`VOO_ITINERARIO`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `FITAIRLINES`.`VOO_ITINERARIO` ;

CREATE TABLE IF NOT EXISTS `FITAIRLINES`.`VOO_ITINERARIO` (
  `ID_VOO_ITINERARIO` INT NOT NULL AUTO_INCREMENT,
  `ID_VOO` INT NOT NULL,
  `ID_ITINERARIO` INT NOT NULL,
  PRIMARY KEY (`ID_VOO_ITINERARIO`, `ID_VOO`, `ID_ITINERARIO`),
  INDEX `fk_VOO_ITINERARIO_VOO1_idx` (`ID_VOO` ASC) VISIBLE,
  INDEX `fk_VOO_ITINERARIO_ITINERARIO1_idx` (`ID_ITINERARIO` ASC) VISIBLE,
  CONSTRAINT `fk_VOO_ITINERARIO_VOO1`
    FOREIGN KEY (`ID_VOO`)
    REFERENCES `FITAIRLINES`.`VOO` (`ID_VOO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_VOO_ITINERARIO_ITINERARIO1`
    FOREIGN KEY (`ID_ITINERARIO`)
    REFERENCES `FITAIRLINES`.`ITINERARIO` (`ID_ITINERARIO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FITAIRLINES`.`TIPO_PAGAMENTO`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `FITAIRLINES`.`TIPO_PAGAMENTO` ;

CREATE TABLE IF NOT EXISTS `FITAIRLINES`.`TIPO_PAGAMENTO` (
  `ID_TIPO_PAGAMENTO` INT NOT NULL AUTO_INCREMENT,
  `TIPO` VARCHAR(50) NULL,
  `DESCRICAO` VARCHAR(255) NULL,
  PRIMARY KEY (`ID_TIPO_PAGAMENTO`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FITAIRLINES`.`PAGAMENTO`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `FITAIRLINES`.`PAGAMENTO` ;

CREATE TABLE IF NOT EXISTS `FITAIRLINES`.`PAGAMENTO` (
  `ID_PAGAMENTO` INT NOT NULL AUTO_INCREMENT,
  `ID_RESERVA_DE_ASSENTO_VOO` INT NOT NULL,
  `ID_TIPO_PAGAMENTO` INT NOT NULL,
  `DATA_PAGAMENTO` DATETIME NULL,
  `VALOR_TOTAL` DECIMAL(10,2) NULL,
  `STATUS` ENUM('PENDENTE', 'APROVADO', 'CANCELADO') NOT NULL DEFAULT 'PENDENTE',
  PRIMARY KEY (`ID_PAGAMENTO`, `ID_RESERVA_DE_ASSENTO_VOO`, `ID_TIPO_PAGAMENTO`),
  INDEX `fk_PAGAMENTO_TIPO_PAGAMENTO1_idx` (`ID_TIPO_PAGAMENTO` ASC) VISIBLE,
  INDEX `fk_PAGAMENTO_RESERVA_DE_ASSENTO_VOO1_idx` (`ID_RESERVA_DE_ASSENTO_VOO` ASC) VISIBLE,
  CONSTRAINT `fk_PAGAMENTO_TIPO_PAGAMENTO1`
    FOREIGN KEY (`ID_TIPO_PAGAMENTO`)
    REFERENCES `FITAIRLINES`.`TIPO_PAGAMENTO` (`ID_TIPO_PAGAMENTO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_PAGAMENTO_RESERVA_DE_ASSENTO_VOO1`
    FOREIGN KEY (`ID_RESERVA_DE_ASSENTO_VOO`)
    REFERENCES `FITAIRLINES`.`RESERVA_DE_ASSENTO_VOO` (`ID_RESERVA_DE_ASSENTO_VOO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FITAIRLINES`.`BAGAGEM`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `FITAIRLINES`.`BAGAGEM` ;

CREATE TABLE IF NOT EXISTS `FITAIRLINES`.`BAGAGEM` (
  `ID_BAGAGEM` INT NOT NULL AUTO_INCREMENT,
  `PESO_KG` DECIMAL(5,2) NULL,
  `DIMENSOES` VARCHAR(100) NULL,
  `TIPO_BAGAGEM` ENUM('DESPACHADA', 'DE_MAO') NOT NULL,
  `PRECO_ADICIONAL` DECIMAL(10,2) NULL,
  PRIMARY KEY (`ID_BAGAGEM`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FITAIRLINES`.`RESERVA_BAGAGEM`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `FITAIRLINES`.`RESERVA_BAGAGEM` ;

CREATE TABLE IF NOT EXISTS `FITAIRLINES`.`RESERVA_BAGAGEM` (
  `ID_RESERVA_BAGAGEM` INT NOT NULL AUTO_INCREMENT,
  `ID_BAGAGEM` INT NOT NULL,
  `ID_RESERVA_DE_ASSENTO_VOO` INT NOT NULL,
  PRIMARY KEY (`ID_RESERVA_BAGAGEM`),
  INDEX `fk_RESERVA_BAGAGEM_BAGAGEM1_idx` (`ID_BAGAGEM` ASC) VISIBLE,
  INDEX `fk_RESERVA_BAGAGEM_RESERVA_DE_ASSENTO_VOO1_idx` (`ID_RESERVA_DE_ASSENTO_VOO` ASC) VISIBLE,
  CONSTRAINT `fk_RESERVA_BAGAGEM_BAGAGEM1`
    FOREIGN KEY (`ID_BAGAGEM`)
    REFERENCES `FITAIRLINES`.`BAGAGEM` (`ID_BAGAGEM`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_RESERVA_BAGAGEM_RESERVA_DE_ASSENTO_VOO1`
    FOREIGN KEY (`ID_RESERVA_DE_ASSENTO_VOO`)
    REFERENCES `FITAIRLINES`.`RESERVA_DE_ASSENTO_VOO` (`ID_RESERVA_DE_ASSENTO_VOO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
