/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : packdefinfo

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2020-03-07 17:21:04
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `daily_count`
-- ----------------------------
DROP TABLE IF EXISTS `daily_count`;
CREATE TABLE `daily_count` (
  `date` date NOT NULL,
  `pack_count_` int(11) NOT NULL,
  `input_count` int(11) NOT NULL,
  `def_count` int(11) NOT NULL,
  PRIMARY KEY (`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of daily_count
-- ----------------------------

-- ----------------------------
-- Table structure for `daily_target`
-- ----------------------------
DROP TABLE IF EXISTS `daily_target`;
CREATE TABLE `daily_target` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dep` varchar(10) NOT NULL,
  `date` date NOT NULL,
  `target` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of daily_target
-- ----------------------------

-- ----------------------------
-- Table structure for `history_input`
-- ----------------------------
DROP TABLE IF EXISTS `history_input`;
CREATE TABLE `history_input` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` datetime NOT NULL,
  `line` varchar(10) NOT NULL,
  `type` varchar(10) NOT NULL,
  `defType` varchar(50) DEFAULT '',
  `qcInfo` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of history_input
-- ----------------------------

-- ----------------------------
-- Table structure for `realtime_input`
-- ----------------------------
DROP TABLE IF EXISTS `realtime_input`;
CREATE TABLE `realtime_input` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` datetime NOT NULL,
  `line` varchar(10) NOT NULL,
  `type` varchar(10) NOT NULL,
  `defType` varchar(50) DEFAULT NULL,
  `qcInfo` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of realtime_input
-- ----------------------------
