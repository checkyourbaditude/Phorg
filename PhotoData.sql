-- phpMyAdmin SQL Dump
-- version 4.4.15.9
-- https://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 25, 2019 at 07:05 PM
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
-- Table structure for table `dateData`
--

CREATE TABLE IF NOT EXISTS `dateData` (
  `Date` date NOT NULL COMMENT 'This is the information for a specific date',
  `numPhotos` smallint(5) unsigned NOT NULL COMMENT 'Number of Photos taken on the specifc date'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `photoData`
--

CREATE TABLE IF NOT EXISTS `photoData` (
  `photoIndex` int(10) unsigned NOT NULL,
  `photoDate` date NOT NULL,
  `photoName` tinytext CHARACTER SET utf16 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='This table stores all the data from the photos metadata, plus the users selections for the highlights folder and eventually edits';

-- --------------------------------------------------------

--
-- Table structure for table `photoGallery`
--

CREATE TABLE IF NOT EXISTS `photoGallery` (
  `photoIndex` int(10) unsigned NOT NULL DEFAULT '0',
  `Gallery` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `photoHighlights`
--

CREATE TABLE IF NOT EXISTS `photoHighlights` (
  `photoIndex` int(10) unsigned NOT NULL DEFAULT '0',
  `Hightlight` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `photoMetaData`
--

CREATE TABLE IF NOT EXISTS `photoMetaData` (
  `photoIndex` int(11) unsigned NOT NULL DEFAULT '0',
  `focalLength` int(11) unsigned NOT NULL DEFAULT '0',
  `aperture` tinyint(4) NOT NULL,
  `shutterSpeed` char(6) NOT NULL,
  `ISO` smallint(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dateData`
--
ALTER TABLE `dateData`
  ADD PRIMARY KEY (`Date`),
  ADD UNIQUE KEY `Date` (`Date`),
  ADD KEY `Date_2` (`Date`);

--
-- Indexes for table `photoData`
--
ALTER TABLE `photoData`
  ADD PRIMARY KEY (`photoIndex`),
  ADD KEY `photoDate` (`photoDate`);

--
-- Indexes for table `photoGallery`
--
ALTER TABLE `photoGallery`
  ADD PRIMARY KEY (`photoIndex`);

--
-- Indexes for table `photoHighlights`
--
ALTER TABLE `photoHighlights`
  ADD PRIMARY KEY (`photoIndex`);

--
-- Indexes for table `photoMetaData`
--
ALTER TABLE `photoMetaData`
  ADD PRIMARY KEY (`photoIndex`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `photoData`
--
ALTER TABLE `photoData`
  MODIFY `photoIndex` int(10) unsigned NOT NULL AUTO_INCREMENT;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `photoData`
--
ALTER TABLE `photoData`
  ADD CONSTRAINT `photodata_ibfk_1` FOREIGN KEY (`photoDate`) REFERENCES `dateData` (`Date`);

--
-- Constraints for table `photoGallery`
--
ALTER TABLE `photoGallery`
  ADD CONSTRAINT `photogallery_ibfk_1` FOREIGN KEY (`photoIndex`) REFERENCES `photoData` (`photoIndex`);

--
-- Constraints for table `photoHighlights`
--
ALTER TABLE `photoHighlights`
  ADD CONSTRAINT `photohighlights_ibfk_1` FOREIGN KEY (`photoIndex`) REFERENCES `photoData` (`photoIndex`) ON UPDATE CASCADE;

--
-- Constraints for table `photoMetaData`
--
ALTER TABLE `photoMetaData`
  ADD CONSTRAINT `photometadata_ibfk_1` FOREIGN KEY (`photoIndex`) REFERENCES `photoData` (`photoIndex`) ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
