-- phpMyAdmin SQL Dump
-- version 2.10.1
-- http://www.phpmyadmin.net
-- 
-- Host: localhost
-- Generation Time: Jan 01, 2002 at 12:09 AM
-- Server version: 5.0.41
-- PHP Version: 5.2.2

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

-- 
-- Database: `kamus`
-- 
CREATE DATABASE `kamus` DEFAULT CHARACTER SET latin1 COLLATE latin1_general_ci;
USE `kamus`;

-- --------------------------------------------------------

-- 
-- Table structure for table `balasan`
-- 

CREATE TABLE `balasan` (
  `balas` varchar(1000) collate latin1_general_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- 
-- Dumping data for table `balasan`
-- 

INSERT INTO `balasan` VALUES ('oy kenpa jon?');
INSERT INTO `balasan` VALUES ('dih aneh :/');
INSERT INTO `balasan` VALUES ('dih aneh :?');

-- --------------------------------------------------------

-- 
-- Table structure for table `kata`
-- 

CREATE TABLE `kata` (
  `inggris` varchar(1000) collate latin1_general_ci NOT NULL,
  `indonesia` varchar(1000) collate latin1_general_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- 
-- Dumping data for table `kata`
-- 

INSERT INTO `kata` VALUES ('you', 'kamu');
INSERT INTO `kata` VALUES ('am', 'saya');
INSERT INTO `kata` VALUES ('city', 'kota');

-- --------------------------------------------------------

-- 
-- Table structure for table `kms_indo`
-- 

CREATE TABLE `kms_indo` (
  `id` varchar(1000) collate latin1_general_ci NOT NULL,
  `kosakata_ind` varchar(1000) collate latin1_general_ci NOT NULL,
  `pengertian_ind` varchar(1000) collate latin1_general_ci NOT NULL,
  `sample_ind` varchar(1000) collate latin1_general_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- 
-- Dumping data for table `kms_indo`
-- 

INSERT INTO `kms_indo` VALUES ('textCtrl1', 'sinonim', 'Persamaan Kata', 'Sayang sinonim nya adalah ======== kasih');
INSERT INTO `kms_indo` VALUES ('', 'antonim', 'Lawan Kata', 'Jelek Antonimnya adalah Ganteng Kaya gua B)');

-- --------------------------------------------------------

-- 
-- Table structure for table `kms_ingg`
-- 

CREATE TABLE `kms_ingg` (
  `id` varchar(1000) collate latin1_general_ci NOT NULL,
  `kosakata_ingg` varchar(1000) collate latin1_general_ci NOT NULL,
  `pengertian_ingg` varchar(1000) collate latin1_general_ci NOT NULL,
  `sample_ingg` varchar(1000) collate latin1_general_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- 
-- Dumping data for table `kms_ingg`
-- 

INSERT INTO `kms_ingg` VALUES ('', 'thankyou', 'dalam bahasa indonesia berati ber Terima kasih', 'contoh\n----thankyou very much as be help\ndalam indonesia\n----terimakasih banyak atas bantuannya\n');
INSERT INTO `kms_ingg` VALUES ('', 'help', 'dalam bahasa indonesia adalah minta tolong\natau biasa digunakan ketika memerlukan bantauan', 'contoh\n----please help me \ndalam bahasa indo\n----tolong bantu saya');

-- --------------------------------------------------------

-- 
-- Table structure for table `kms_python`
-- 

CREATE TABLE `kms_python` (
  `id` varchar(1000) collate latin1_general_ci NOT NULL,
  `kosakata` varchar(1000) collate latin1_general_ci NOT NULL,
  `pengertian` varchar(1000) collate latin1_general_ci NOT NULL,
  `sample` varchar(1000) collate latin1_general_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- 
-- Dumping data for table `kms_python`
-- 

INSERT INTO `kms_python` VALUES ('', 'variabel', 'penyimpanan sementara', 'a = 1\nb = 2\nprint "a + b"\nhasil nya adalah 3');
INSERT INTO `kms_python` VALUES ('', 'string', 'text', 'string = johanesdesmonkapoyos\nint = 89048098092840r84208');
INSERT INTO `kms_python` VALUES ('', 'module', 'alat yang digunakan untuk membangun program python', 'contoh module:\n-wx\n-tkinter\n-socket\n-os\n-lib\n-dll');
INSERT INTO `kms_python` VALUES ('', 'sacasc', 'ascasc', 'sacascasc');
INSERT INTO `kms_python` VALUES ('', 'johanes', 'MANDI LU,BAU', 'ORANG JELEK');

-- --------------------------------------------------------

-- 
-- Table structure for table `pertanyaan`
-- 

CREATE TABLE `pertanyaan` (
  `tanya` varchar(1000) collate latin1_general_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- 
-- Dumping data for table `pertanyaan`
-- 

INSERT INTO `pertanyaan` VALUES ('min ?\n\n\n\n\n\n#johanes');
INSERT INTO `pertanyaan` VALUES ('gk \n\n#johanes');
INSERT INTO `pertanyaan` VALUES ('admin !\n#??');
INSERT INTO `pertanyaan` VALUES ('MIN PENGEN TANYA\n#KERNEX');

-- --------------------------------------------------------

-- 
-- Table structure for table `tentangprogram`
-- 

CREATE TABLE `tentangprogram` (
  `nama` varchar(100) collate latin1_general_ci NOT NULL,
  `kritikdansaran` varchar(1000) collate latin1_general_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- 
-- Dumping data for table `tentangprogram`
-- 

INSERT INTO `tentangprogram` VALUES ('johanesdesmonkapoyos', 'Desaign nya lebih dikreatifin lagi, Terimakasih :)');
INSERT INTO `tentangprogram` VALUES ('Nama..', 'Kritik dan Saran..');
INSERT INTO `tentangprogram` VALUES ('johanesdesmon', 'apa yaa..? :/');
INSERT INTO `tentangprogram` VALUES ('andika', 'apaya');
INSERT INTO `tentangprogram` VALUES ('KERNEX', 'Proramnya BAGUS');

-- --------------------------------------------------------

-- 
-- Table structure for table `translate`
-- 

CREATE TABLE `translate` (
  `indonesia` varchar(1000) collate latin1_general_ci NOT NULL,
  `jepang` varchar(1000) collate latin1_general_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- 
-- Dumping data for table `translate`
-- 

INSERT INTO `translate` VALUES ('makasi', 'arigatou');
INSERT INTO `translate` VALUES ('maju', 'ikeh');
INSERT INTO `translate` VALUES ('ayo', 'ikoh');
