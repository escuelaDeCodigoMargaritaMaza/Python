CREATE DATABASE baseusuarios;
USE baseusuarios;
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(255) NOT NULL,
    contraseña VARCHAR(255) NOT NULL
);