-- -----------------------------------------------------
-- Schema FITAIRLINES
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `FITAIRLINES`;

CREATE SCHEMA IF NOT EXISTS `FITAIRLINES` DEFAULT CHARACTER SET utf8mb4;
USE `FITAIRLINES`;

-- -----------------------------------------------------
-- Tabela: aeroporto
-- -----------------------------------------------------
DROP TABLE IF EXISTS `aeroporto`;
CREATE TABLE `aeroporto` (
  `ID_AEROPORTO` INT NOT NULL AUTO_INCREMENT,
  `NOME` VARCHAR(100) DEFAULT NULL,
  `CIDADE` VARCHAR(50) DEFAULT NULL,
  `ESTADO` VARCHAR(50) DEFAULT NULL,
  `PAIS` VARCHAR(50) DEFAULT NULL,
  `CAPACIDADE` INT DEFAULT NULL,
  `CODIGO` VARCHAR(10) DEFAULT NULL,
  `LATITUDE` DECIMAL(9,6) NOT NULL,
  `LONGITUDE` DECIMAL(9,6) NOT NULL,
  PRIMARY KEY (`ID_AEROPORTO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- -----------------------------------------------------
-- Tabela: tipo_aeronave
-- -----------------------------------------------------
DROP TABLE IF EXISTS `tipo_aeronave`;
CREATE TABLE `tipo_aeronave` (
  `ID_TIPO_AERONAVE` INT NOT NULL AUTO_INCREMENT,
  `NOME` VARCHAR(100) DEFAULT NULL,
  `FABRICANTE` VARCHAR(100) DEFAULT NULL,
  `CAPACIDADE_PASSAGEIROS` INT DEFAULT NULL,
  `DESCRICAO` VARCHAR(255) DEFAULT NULL,
  PRIMARY KEY (`ID_TIPO_AERONAVE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- -----------------------------------------------------
-- Tabela: voo
-- -----------------------------------------------------
DROP TABLE IF EXISTS `voo`;
CREATE TABLE `voo` (
  `ID_VOO` INT NOT NULL AUTO_INCREMENT,
  `ID_TIPO_AERONAVE` INT NOT NULL,
  `ID_AEROPORTO_PARTIDA` INT NOT NULL,
  `ID_AEROPORTO_CHEGADA` INT NOT NULL,
  `CODIGO` VARCHAR(15) DEFAULT NULL,
  `PARTIDA` DATETIME NOT NULL,
  `CHEGADA` DATETIME NOT NULL,
  `DURACAO` TIME DEFAULT NULL,
  `ASSENTOS_TOTAIS` INT NOT NULL,
  `ASSENTOS_DISPONIVEIS` INT DEFAULT NULL,
  `STATUS` ENUM("programado", "cancelado", "finalizado", "em andamento") NOT NULL,
  PRIMARY KEY (`ID_VOO`),
  FOREIGN KEY (`ID_AEROPORTO_PARTIDA`) REFERENCES `aeroporto` (`ID_AEROPORTO`),
  FOREIGN KEY (`ID_AEROPORTO_CHEGADA`) REFERENCES `aeroporto` (`ID_AEROPORTO`),
  FOREIGN KEY (`ID_TIPO_AERONAVE`) REFERENCES `tipo_aeronave` (`ID_TIPO_AERONAVE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- -----------------------------------------------------
-- Tabela: classe
-- -----------------------------------------------------
DROP TABLE IF EXISTS `classe`;
CREATE TABLE `classe` (
  `ID_CLASSE` INT NOT NULL AUTO_INCREMENT,
  `TIPO` VARCHAR(45) DEFAULT NULL,
  `PRIORIDADE` INT DEFAULT NULL,
  `DESCRICAO` VARCHAR(255) DEFAULT NULL,
  `NOME` VARCHAR(50) DEFAULT NULL,
  `PRECO_ADICIONAL` DECIMAL(10,2) DEFAULT NULL,
  PRIMARY KEY (`ID_CLASSE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- -----------------------------------------------------
-- Tabela: assento
-- -----------------------------------------------------
DROP TABLE IF EXISTS `assento`;
CREATE TABLE `assento` (
  `ID_ASSENTO` INT NOT NULL AUTO_INCREMENT,
  `ID_CLASSE` INT NOT NULL,
  `ID_VOO` INT NOT NULL,
  `NUMERO` VARCHAR(5) DEFAULT NULL,
  `LOCALIZACAO` VARCHAR(10) DEFAULT NULL,
  `DESCRICAO` VARCHAR(255) DEFAULT NULL,
  `OCUPADO` TINYINT(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`ID_ASSENTO`),
  FOREIGN KEY (`ID_CLASSE`) REFERENCES `classe` (`ID_CLASSE`),
  FOREIGN KEY (`ID_VOO`) REFERENCES `voo` (`ID_VOO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- -----------------------------------------------------
-- Tabela: itinerario
-- -----------------------------------------------------
DROP TABLE IF EXISTS `itinerario`;
CREATE TABLE `itinerario` (
  `ID_ITINERARIO` INT NOT NULL AUTO_INCREMENT,
  `PARADAS` VARCHAR(255) DEFAULT NULL,
  `DISTANCIA_KM` FLOAT DEFAULT NULL,
  `DURACAO` TIME DEFAULT NULL,
  `DESCRICAO` VARCHAR(255) DEFAULT NULL,
  PRIMARY KEY (`ID_ITINERARIO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- -----------------------------------------------------
-- Tabela: passageiro
-- -----------------------------------------------------
DROP TABLE IF EXISTS `passageiro`;
CREATE TABLE `passageiro` (
  `ID_PASSAGEIRO` INT NOT NULL AUTO_INCREMENT,
  `NOME` VARCHAR(200) DEFAULT NULL,
  `ENDERECO` VARCHAR(500) DEFAULT NULL,
  `TELEFONE` VARCHAR(20) DEFAULT NULL,
  `IDADE` INT DEFAULT NULL,
  `CPF` VARCHAR(11) DEFAULT NULL,
  `NACIONALIDADE` VARCHAR(45) DEFAULT NULL,
  `EMAIL` VARCHAR(100) DEFAULT NULL,
  PRIMARY KEY (`ID_PASSAGEIRO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- -----------------------------------------------------
-- Tabela: reserva
-- -----------------------------------------------------
DROP TABLE IF EXISTS `reserva`;
CREATE TABLE `reserva` (
  `ID_RESERVA` INT NOT NULL AUTO_INCREMENT,
  `ID_ASSENTO` INT NOT NULL,
  `ID_PASSAGEIRO` INT NOT NULL,
  `DATA` DATETIME NOT NULL,
  `STATUS` INT NOT NULL,
  `PRECO` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`ID_RESERVA`),
  FOREIGN KEY (`ID_ASSENTO`) REFERENCES `assento` (`ID_ASSENTO`),
  FOREIGN KEY (`ID_PASSAGEIRO`) REFERENCES `passageiro` (`ID_PASSAGEIRO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- -----------------------------------------------------
-- Tabela: tipo_pagamento
-- -----------------------------------------------------
DROP TABLE IF EXISTS `tipo_pagamento`;
CREATE TABLE `tipo_pagamento` (
  `ID_TIPO_PAGAMENTO` INT NOT NULL AUTO_INCREMENT,
  `TIPO` VARCHAR(50) DEFAULT NULL,
  `DESCRICAO` VARCHAR(255) DEFAULT NULL,
  PRIMARY KEY (`ID_TIPO_PAGAMENTO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- -----------------------------------------------------
-- Tabela: pagamento
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pagamento`;
CREATE TABLE `pagamento` (
  `ID_PAGAMENTO` INT NOT NULL AUTO_INCREMENT,
  `ID_RESERVA` INT NOT NULL,
  `ID_TIPO_PAGAMENTO` INT NOT NULL,
  `DATA_PAGAMENTO` DATETIME NOT NULL,
  `VALOR` DECIMAL(10,2) NOT NULL,
  `STATUS` INT NOT NULL,
  PRIMARY KEY (`ID_PAGAMENTO`),
  FOREIGN KEY (`ID_RESERVA`) REFERENCES `reserva` (`ID_RESERVA`),
  FOREIGN KEY (`ID_TIPO_PAGAMENTO`) REFERENCES `tipo_pagamento` (`ID_TIPO_PAGAMENTO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- -----------------------------------------------------
-- Tabela: ticket
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ticket`;
CREATE TABLE `ticket` (
  `ID_TICKET` INT NOT NULL AUTO_INCREMENT,
  `ID_RESERVA` INT NOT NULL,
  `DATA_EMISSAO` DATETIME NOT NULL,
  `PRECO_FINAL` DECIMAL(10,2) NOT NULL,
  `STATUS` INT NOT NULL,
  PRIMARY KEY (`ID_TICKET`),
  FOREIGN KEY (`ID_RESERVA`) REFERENCES `reserva` (`ID_RESERVA`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- -----------------------------------------------------
-- Tabela: voo_itinerario
-- -----------------------------------------------------
DROP TABLE IF EXISTS voo_itinerario;
CREATE TABLE voo_itinerario (
  ID_VOO_ITINERARIO int(11) NOT NULL AUTO_INCREMENT,
  ID_VOO int(11) NOT NULL,
  ID_ITINERARIO int(11) NOT NULL,
  PRIMARY KEY (ID_VOO_ITINERARIO),
  KEY fk_VOO_ITINERARIO_VOO_idx (ID_VOO),
  KEY fk_VOO_ITINERARIO_ITINERARIO_idx (ID_ITINERARIO),
  CONSTRAINT fk_VOO_ITINERARIO_ITINERARIO FOREIGN KEY (ID_ITINERARIO) REFERENCES itinerario (ID_ITINERARIO) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT fk_VOO_ITINERARIO_VOO FOREIGN KEY (ID_VOO) REFERENCES voo (ID_VOO) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_general_ci;
