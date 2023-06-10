-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 09-Jun-2023 às 03:50
-- Versão do servidor: 10.4.27-MariaDB
-- versão do PHP: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `senai`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `biticoin`
--

CREATE TABLE `biticoin` (
  `id` int(11) NOT NULL,
  `valor_biticoin` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Extraindo dados da tabela `biticoin`
--

INSERT INTO `biticoin` (`id`, `valor_biticoin`) VALUES
(1, '130.358,96');

-- --------------------------------------------------------

--
-- Estrutura da tabela `clima`
--

CREATE TABLE `clima` (
  `id` int(11) NOT NULL,
  `temperatura_atual` varchar(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Extraindo dados da tabela `clima`
--

INSERT INTO `clima` (`id`, `temperatura_atual`) VALUES
(1, '22');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `biticoin`
--
ALTER TABLE `biticoin`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `clima`
--
ALTER TABLE `clima`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `biticoin`
--
ALTER TABLE `biticoin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `clima`
--
ALTER TABLE `clima`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
