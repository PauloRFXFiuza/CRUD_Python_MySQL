CREATE DATABASE MeuBanco;
USE MeuBanco;

CREATE TABLE Usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL
);

INSERT INTO Usuarios (nome, email, senha)
VALUES ('João Silva', 'joao@email.com', '123456');