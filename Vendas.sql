CREATE SCHEMA `database` ;
CREATE TABLE `database`.`vendas` (
  `idVendas` INT NOT NULL AUTO_INCREMENT,
  `nome_produto` VARCHAR(45) NULL,
  `valor` INT NULL,
  PRIMARY KEY (`idVendas`));
SELECT * FROM `database`.`vendas`;