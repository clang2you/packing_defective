/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 100411
 Source Host           : localhost:3306
 Source Schema         : packdefinfo

 Target Server Type    : MySQL
 Target Server Version : 100411
 File Encoding         : 65001

 Date: 09/03/2020 17:34:36
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for com_input
-- ----------------------------
DROP TABLE IF EXISTS `com_input`;
CREATE TABLE `com_input`  (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `btn_pos` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `line` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 35 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of com_input
-- ----------------------------
INSERT INTO `com_input` VALUES (24, '01', 'AL');
INSERT INTO `com_input` VALUES (25, '02', 'AL');
INSERT INTO `com_input` VALUES (26, '01', 'AL');
INSERT INTO `com_input` VALUES (27, '01', 'AL');
INSERT INTO `com_input` VALUES (28, '03', 'AL');
INSERT INTO `com_input` VALUES (29, '03', 'AL');
INSERT INTO `com_input` VALUES (30, '07', 'AL');
INSERT INTO `com_input` VALUES (31, '08', 'AL');
INSERT INTO `com_input` VALUES (32, '01', 'Al');
INSERT INTO `com_input` VALUES (33, '02', 'AL');
INSERT INTO `com_input` VALUES (34, '01', 'AL');

-- ----------------------------
-- Table structure for config
-- ----------------------------
DROP TABLE IF EXISTS `config`;
CREATE TABLE `config`  (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `type` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `def_type_no` int(5) NULL DEFAULT NULL,
  `btn_pos` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `qcPos` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of config
-- ----------------------------
INSERT INTO `config` VALUES (1, '投料', NULL, '01', NULL);
INSERT INTO `config` VALUES (2, '包装', NULL, '02', NULL);
INSERT INTO `config` VALUES (3, '高胶', 1, '03', '1');
INSERT INTO `config` VALUES (4, '脱胶', 2, '04', '1');
INSERT INTO `config` VALUES (5, '不对称', 3, '05', '1');
INSERT INTO `config` VALUES (6, '清洁度', 4, '06', '1');
INSERT INTO `config` VALUES (7, '针车不良', 5, '07', '1');
INSERT INTO `config` VALUES (8, '研磨线', 6, '08', '1');
INSERT INTO `config` VALUES (9, '其他', 7, '09', '1');

-- ----------------------------
-- Table structure for daily_count
-- ----------------------------
DROP TABLE IF EXISTS `daily_count`;
CREATE TABLE `daily_count`  (
  `date` date NOT NULL,
  `pack_count_` int(11) NULL DEFAULT NULL,
  `input_count` int(11) NULL DEFAULT NULL,
  `def_count` int(11) NULL DEFAULT NULL,
  `def_type1_count` int(10) NULL DEFAULT NULL,
  `def_type2_count` int(10) NULL DEFAULT NULL,
  `def_type3_count` int(10) NULL DEFAULT NULL,
  `def_type4_count` int(10) NULL DEFAULT NULL,
  `def_type5_count` int(10) NULL DEFAULT NULL,
  `def_type6_count` int(10) NULL DEFAULT NULL,
  `def_type7_count` int(10) NULL DEFAULT NULL,
  PRIMARY KEY (`date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for daily_target
-- ----------------------------
DROP TABLE IF EXISTS `daily_target`;
CREATE TABLE `daily_target`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dep` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `date` date NOT NULL,
  `target` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for history_input
-- ----------------------------
DROP TABLE IF EXISTS `history_input`;
CREATE TABLE `history_input`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` datetime(0) NULL,
  `line` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `type` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `defType` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '',
  `qcInfo` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for manual_fixed_log
-- ----------------------------
DROP TABLE IF EXISTS `manual_fixed_log`;
CREATE TABLE `manual_fixed_log`  (
  `time` datetime(0) NULL,
  `type` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `pack_count` int(11) NULL DEFAULT NULL,
  `input_count` int(11) NULL DEFAULT NULL,
  `pack_diff` int(11) NULL DEFAULT NULL,
  `input_diff` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`time`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for realtime_input
-- ----------------------------
DROP TABLE IF EXISTS `realtime_input`;
CREATE TABLE `realtime_input`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` datetime(0) NULL,
  `line` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `type` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `defType` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `qcPos` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '',
  `btn_pos` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `qty` int(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 44 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of realtime_input
-- ----------------------------
INSERT INTO `realtime_input` VALUES (33, '2020-03-09 15:06:18', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (34, '2020-03-09 15:06:25', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (35, '2020-03-09 15:06:30', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (36, '2020-03-09 15:06:36', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (37, '2020-03-09 15:06:41', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (38, '2020-03-09 15:06:46', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (39, '2020-03-09 15:47:54', 'AL', '针车不良', '5', '1', '07', 1);
INSERT INTO `realtime_input` VALUES (40, '2020-03-09 15:47:58', 'AL', '研磨线', '6', '1', '08', 1);
INSERT INTO `realtime_input` VALUES (41, '2020-03-09 15:48:03', 'Al', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (42, '2020-03-09 15:48:08', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (43, '2020-03-09 15:48:13', 'AL', '投料', NULL, NULL, '01', 1);

-- ----------------------------
-- Triggers structure for table com_input
-- ----------------------------
DROP TRIGGER IF EXISTS `insert_to_realtime`;
delimiter ;;
CREATE TRIGGER `insert_to_realtime` AFTER INSERT ON `com_input` FOR EACH ROW insert into realtime_input(time, type, defType, qcPos, line, btn_pos, qty)
select now(), s.type, s.def_type_no, s.qcPos,c.line, NEW.btn_pos, 1
from config s, com_input c
where s.btn_pos = NEW.btn_pos and c.id = NEW.id
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
