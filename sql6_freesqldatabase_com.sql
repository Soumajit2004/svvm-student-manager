-- phpMyAdmin SQL Dump
-- version 4.7.1
-- https://www.phpmyadmin.net/
--
-- Host: sql6.freesqldatabase.com
-- Generation Time: Nov 06, 2022 at 04:03 PM
-- Server version: 5.5.62-0ubuntu0.14.04.1
-- PHP Version: 7.0.33-0ubuntu0.16.04.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sms`
--
CREATE DATABASE IF NOT EXISTS `sms` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `sms`;

-- --------------------------------------------------------

--
-- Table structure for table `marks`
--

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

CREATE TABLE `marks` (
  `id_fk` bigint(20) NOT NULL,
  `sub_code` varchar(10) NOT NULL,
  `mt_1` int(11) DEFAULT NULL,
  `mt_2` int(11) DEFAULT NULL,
  `mt_3` int(11) DEFAULT NULL,
  `mt_4` int(11) DEFAULT NULL,
  `mt_5` int(11) DEFAULT NULL,
  `mt_6` int(11) DEFAULT NULL,
  `mt_7` int(11) DEFAULT NULL,
  `mt_8` int(11) DEFAULT NULL,
  `mt_9` int(11) DEFAULT NULL,
  `mt_10` int(11) DEFAULT NULL,
  `mt_11` int(11) DEFAULT NULL,
  `mt_12` int(11) DEFAULT NULL,
  `ut_1` int(11) DEFAULT NULL,
  `ut_2` int(11) DEFAULT NULL,
  `mid_term` int(11) DEFAULT NULL,
  `final_term` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `class` int(11) DEFAULT NULL,
  `father_name` varchar(100) DEFAULT NULL,
  `mother_name` varchar(100) DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL,
  `father_no` bigint(20) DEFAULT NULL,
  `mother_no` bigint(20) DEFAULT NULL,
  `roll_no` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `marks`
--
ALTER TABLE `marks`
  ADD KEY `id_fk` (`id_fk`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `students_id_uindex` (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51910;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `marks`
--
ALTER TABLE `marks`
  ADD CONSTRAINT `id_fk` FOREIGN KEY (`id_fk`) REFERENCES `students` (`id`);
COMMIT;
