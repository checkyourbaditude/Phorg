-- phpMyAdmin SQL Dump
-- version 4.4.15.9
-- https://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 10, 2019 at 12:41 AM
-- Server version: 5.6.35
-- PHP Version: 5.5.38

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `PhotoData`
--

-- --------------------------------------------------------

--
-- Table structure for table `cameraData`
--

CREATE TABLE IF NOT EXISTS `cameraData` (
  `cameraIndex` int(11) NOT NULL,
  `cameraMake` varchar(10) NOT NULL,
  `cameraModel` varchar(10) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cameraData`
--

INSERT INTO `cameraData` (`cameraIndex`, `cameraMake`, `cameraModel`) VALUES
(1, 'SONY', 'ILCE-6000');

-- --------------------------------------------------------

--
-- Table structure for table `lensData`
--

CREATE TABLE IF NOT EXISTS `lensData` (
  `lensIndex` int(11) NOT NULL,
  `lensMake` varchar(11) NOT NULL,
  `fullLensName` varchar(50) NOT NULL,
  `lensMinFocal` int(3) NOT NULL,
  `lensMaxFocal` int(3) NOT NULL,
  `lensMinFStop` varchar(3) NOT NULL,
  `lensMaxFStop` varchar(2) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `lensData`
--

INSERT INTO `lensData` (`lensIndex`, `lensMake`, `fullLensName`, `lensMinFocal`, `lensMaxFocal`, `lensMinFStop`, `lensMaxFStop`) VALUES
(1, 'SONY', 'E PZ 16-50mm f/3.5-5.6 OSS Lens', 16, 50, '3.5', '36'),
(2, 'SIGMA', '30mm F1.4 DC DN | Contemporary 016', 30, 30, '1.4', '16'),
(3, 'ROKINON', '12mm f/2.0 NCS CS', 12, 12, '2', '22'),
(4, 'SONY', 'FE 85mm f/1.8', 85, 85, '1.8', '22'),
(5, 'SONY', 'FE 70-200mm f/4 G OSS', 70, 200, '4', '22');

-- --------------------------------------------------------

--
-- Table structure for table `photoHighlights`
--

CREATE TABLE IF NOT EXISTS `photoHighlights` (
  `photoIndex` int(11) NOT NULL,
  `Highlight` tinyint(1) DEFAULT NULL,
  `Gallery` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `photoMetaData`
--

CREATE TABLE IF NOT EXISTS `photoMetaData` (
  `photoIndex` int(11) unsigned NOT NULL,
  `photoName` varchar(10) NOT NULL,
  `photoDate` date NOT NULL,
  `focalLength` int(11) unsigned NOT NULL DEFAULT '0',
  `aperture` float NOT NULL,
  `shutterSpeed` char(6) NOT NULL,
  `ISO` smallint(6) DEFAULT NULL,
  `BrightnessValue` float NOT NULL,
  `cameraIndex` tinyint(4) NOT NULL,
  `lensIndex` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cameraData`
--
ALTER TABLE `cameraData`
  ADD PRIMARY KEY (`cameraIndex`);

--
-- Indexes for table `lensData`
--
ALTER TABLE `lensData`
  ADD PRIMARY KEY (`lensIndex`);

--
-- Indexes for table `photoHighlights`
--
ALTER TABLE `photoHighlights`
  ADD UNIQUE KEY `photoHighlightIndex` (`photoIndex`);

--
-- Indexes for table `photoMetaData`
--
ALTER TABLE `photoMetaData`
  ADD PRIMARY KEY (`photoIndex`),
  ADD UNIQUE KEY `photoName` (`photoName`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cameraData`
--
ALTER TABLE `cameraData`
  MODIFY `cameraIndex` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `lensData`
--
ALTER TABLE `lensData`
  MODIFY `lensIndex` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `photoMetaData`
--
ALTER TABLE `photoMetaData`
  MODIFY `photoIndex` int(11) unsigned NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
