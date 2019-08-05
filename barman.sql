-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 05. Aug 2019 um 09:47
-- Server-Version: 10.1.38-MariaDB
-- PHP-Version: 7.3.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `barman`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `d_device`
--

CREATE TABLE `d_device` (
  `k_key` decimal(15,0) NOT NULL,
  `k_name` int(11) DEFAULT NULL,
  `k_theme` varchar(6) DEFAULT NULL,
  `k_u_currentUser` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Daten für Tabelle `d_device`
--

INSERT INTO `d_device` (`k_key`, `k_name`, `k_theme`, `k_u_currentUser`) VALUES
('193101163196977', NULL, 'Dark', 1);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `p_pump`
--

CREATE TABLE `p_pump` (
  `p_id` int(11) NOT NULL,
  `p_pump` int(11) DEFAULT NULL,
  `p_name` varchar(56) DEFAULT NULL,
  `p_device` decimal(15,0) DEFAULT NULL,
  `p_amount` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `r_recipe`
--

CREATE TABLE `r_recipe` (
  `r_id` int(11) NOT NULL,
  `r_u_id` int(11) DEFAULT NULL,
  `r_name` varchar(25) DEFAULT NULL,
  `r_preset` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `u_user`
--

CREATE TABLE `u_user` (
  `u_id` int(11) NOT NULL,
  `u_name` varchar(20) DEFAULT NULL,
  `u_pwd` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Daten für Tabelle `u_user`
--

INSERT INTO `u_user` (`u_id`, `u_name`, `u_pwd`) VALUES
(1, 'Franz', NULL);

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `d_device`
--
ALTER TABLE `d_device`
  ADD PRIMARY KEY (`k_key`),
  ADD UNIQUE KEY `k_key_k_key_uindex` (`k_key`),
  ADD KEY `d_device_u_user_u_id_fk` (`k_u_currentUser`);

--
-- Indizes für die Tabelle `p_pump`
--
ALTER TABLE `p_pump`
  ADD PRIMARY KEY (`p_id`),
  ADD KEY `p_pump_d_device_k_key_fk` (`p_device`);

--
-- Indizes für die Tabelle `r_recipe`
--
ALTER TABLE `r_recipe`
  ADD PRIMARY KEY (`r_id`),
  ADD KEY `r_recipe_u_user_u_id_fk` (`r_u_id`);

--
-- Indizes für die Tabelle `u_user`
--
ALTER TABLE `u_user`
  ADD PRIMARY KEY (`u_id`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `p_pump`
--
ALTER TABLE `p_pump`
  MODIFY `p_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `r_recipe`
--
ALTER TABLE `r_recipe`
  MODIFY `r_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `u_user`
--
ALTER TABLE `u_user`
  MODIFY `u_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints der exportierten Tabellen
--

--
-- Constraints der Tabelle `d_device`
--
ALTER TABLE `d_device`
  ADD CONSTRAINT `d_device_u_user_u_id_fk` FOREIGN KEY (`k_u_currentUser`) REFERENCES `u_user` (`u_id`);

--
-- Constraints der Tabelle `p_pump`
--
ALTER TABLE `p_pump`
  ADD CONSTRAINT `p_pump_d_device_k_key_fk` FOREIGN KEY (`p_device`) REFERENCES `d_device` (`k_key`);

--
-- Constraints der Tabelle `r_recipe`
--
ALTER TABLE `r_recipe`
  ADD CONSTRAINT `r_recipe_u_user_u_id_fk` FOREIGN KEY (`r_u_id`) REFERENCES `u_user` (`u_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
