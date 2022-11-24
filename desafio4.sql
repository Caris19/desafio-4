CREATE DATABASE IF NOT EXISTS `desafio4`;
USE `desafio4`;

CREATE TABLE IF NOT EXISTS `contatos` (
  `id` int(4) NOT NULL AUTO_INCREMENT,
  `email` varchar(30) DEFAULT NULL,
  `assunto` varchar(100) DEFAULT NULL,
  `descricao` varchar(100) DEFAULT null,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4;