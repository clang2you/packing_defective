/*
 Navicat Premium Data Transfer

 Source Server         : 127.0.0.1
 Source Server Type    : MySQL
 Source Server Version : 100411
 Source Host           : localhost:3306
 Source Schema         : packdefinfo

 Target Server Type    : MySQL
 Target Server Version : 100411
 File Encoding         : 65001

 Date: 12/03/2020 00:27:03
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
) ENGINE = InnoDB AUTO_INCREMENT = 316 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

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
INSERT INTO `com_input` VALUES (35, '01', 'AL');
INSERT INTO `com_input` VALUES (36, '01', 'AL');
INSERT INTO `com_input` VALUES (37, '01', 'AL');
INSERT INTO `com_input` VALUES (38, '01', 'AL');
INSERT INTO `com_input` VALUES (39, '02', 'AL');
INSERT INTO `com_input` VALUES (40, '02', 'AL');
INSERT INTO `com_input` VALUES (41, '07', 'AL');
INSERT INTO `com_input` VALUES (42, '08', 'AL');
INSERT INTO `com_input` VALUES (43, '09', 'AL');
INSERT INTO `com_input` VALUES (44, '03', 'AL');
INSERT INTO `com_input` VALUES (45, '01', 'AL');
INSERT INTO `com_input` VALUES (46, '01', 'AL');
INSERT INTO `com_input` VALUES (47, '01', 'AL');
INSERT INTO `com_input` VALUES (48, '01', 'AL');
INSERT INTO `com_input` VALUES (49, '01', 'AL');
INSERT INTO `com_input` VALUES (50, '01', 'AL');
INSERT INTO `com_input` VALUES (51, '01', 'AL');
INSERT INTO `com_input` VALUES (52, '01', 'AL');
INSERT INTO `com_input` VALUES (53, '01', 'AL');
INSERT INTO `com_input` VALUES (54, '01', 'AL');
INSERT INTO `com_input` VALUES (55, '01', 'AL');
INSERT INTO `com_input` VALUES (56, '01', 'AL');
INSERT INTO `com_input` VALUES (57, '01', 'AL');
INSERT INTO `com_input` VALUES (58, '01', 'AL');
INSERT INTO `com_input` VALUES (59, '01', 'AL');
INSERT INTO `com_input` VALUES (60, '01', 'AL');
INSERT INTO `com_input` VALUES (61, '01', 'AL');
INSERT INTO `com_input` VALUES (62, '01', 'AL');
INSERT INTO `com_input` VALUES (63, '01', 'AL');
INSERT INTO `com_input` VALUES (64, '01', 'AL');
INSERT INTO `com_input` VALUES (65, '01', 'AL');
INSERT INTO `com_input` VALUES (66, '01', 'AL');
INSERT INTO `com_input` VALUES (67, '01', 'AL');
INSERT INTO `com_input` VALUES (68, '01', 'AL');
INSERT INTO `com_input` VALUES (69, '01', 'AL');
INSERT INTO `com_input` VALUES (70, '01', 'AL');
INSERT INTO `com_input` VALUES (71, '01', 'AL');
INSERT INTO `com_input` VALUES (72, '01', 'AL');
INSERT INTO `com_input` VALUES (73, '01', 'AL');
INSERT INTO `com_input` VALUES (74, '01', 'AL');
INSERT INTO `com_input` VALUES (75, '01', 'AL');
INSERT INTO `com_input` VALUES (76, '01', 'AL');
INSERT INTO `com_input` VALUES (77, '01', 'AL');
INSERT INTO `com_input` VALUES (78, '01', 'AL');
INSERT INTO `com_input` VALUES (79, '01', 'AL');
INSERT INTO `com_input` VALUES (80, '01', 'AL');
INSERT INTO `com_input` VALUES (81, '01', 'AL');
INSERT INTO `com_input` VALUES (82, '01', 'AL');
INSERT INTO `com_input` VALUES (83, '01', 'AL');
INSERT INTO `com_input` VALUES (84, '01', 'AL');
INSERT INTO `com_input` VALUES (85, '01', 'AL');
INSERT INTO `com_input` VALUES (86, '01', 'AL');
INSERT INTO `com_input` VALUES (87, '01', 'AL');
INSERT INTO `com_input` VALUES (88, '01', 'AL');
INSERT INTO `com_input` VALUES (89, '01', 'AL');
INSERT INTO `com_input` VALUES (90, '01', 'AL');
INSERT INTO `com_input` VALUES (91, '01', 'AL');
INSERT INTO `com_input` VALUES (92, '01', 'AL');
INSERT INTO `com_input` VALUES (93, '01', 'AL');
INSERT INTO `com_input` VALUES (94, '01', 'AL');
INSERT INTO `com_input` VALUES (95, '01', 'AL');
INSERT INTO `com_input` VALUES (96, '01', 'AL');
INSERT INTO `com_input` VALUES (97, '01', 'AL');
INSERT INTO `com_input` VALUES (98, '01', 'AL');
INSERT INTO `com_input` VALUES (99, '02', 'AL');
INSERT INTO `com_input` VALUES (100, '02', 'AL');
INSERT INTO `com_input` VALUES (101, '02', 'AL');
INSERT INTO `com_input` VALUES (102, '02', 'AL');
INSERT INTO `com_input` VALUES (103, '02', 'AL');
INSERT INTO `com_input` VALUES (104, '02', 'AL');
INSERT INTO `com_input` VALUES (105, '02', 'AL');
INSERT INTO `com_input` VALUES (106, '02', 'AL');
INSERT INTO `com_input` VALUES (107, '02', 'AL');
INSERT INTO `com_input` VALUES (108, '02', 'AL');
INSERT INTO `com_input` VALUES (109, '02', 'AL');
INSERT INTO `com_input` VALUES (110, '02', 'AL');
INSERT INTO `com_input` VALUES (111, '02', 'AL');
INSERT INTO `com_input` VALUES (112, '02', 'AL');
INSERT INTO `com_input` VALUES (113, '02', 'AL');
INSERT INTO `com_input` VALUES (114, '02', 'AL');
INSERT INTO `com_input` VALUES (115, '02', 'AL');
INSERT INTO `com_input` VALUES (116, '02', 'AL');
INSERT INTO `com_input` VALUES (117, '02', 'AL');
INSERT INTO `com_input` VALUES (118, '02', 'AL');
INSERT INTO `com_input` VALUES (119, '02', 'AL');
INSERT INTO `com_input` VALUES (120, '02', 'AL');
INSERT INTO `com_input` VALUES (121, '02', 'AL');
INSERT INTO `com_input` VALUES (122, '02', 'AL');
INSERT INTO `com_input` VALUES (123, '02', 'AL');
INSERT INTO `com_input` VALUES (124, '02', 'AL');
INSERT INTO `com_input` VALUES (125, '02', 'AL');
INSERT INTO `com_input` VALUES (126, '02', 'AL');
INSERT INTO `com_input` VALUES (127, '02', 'AL');
INSERT INTO `com_input` VALUES (128, '02', 'AL');
INSERT INTO `com_input` VALUES (129, '03', 'AL');
INSERT INTO `com_input` VALUES (130, '03', 'AL');
INSERT INTO `com_input` VALUES (131, '03', 'AL');
INSERT INTO `com_input` VALUES (132, '03', 'AL');
INSERT INTO `com_input` VALUES (133, '03', 'AL');
INSERT INTO `com_input` VALUES (134, '03', 'AL');
INSERT INTO `com_input` VALUES (135, '03', 'AL');
INSERT INTO `com_input` VALUES (136, '03', 'AL');
INSERT INTO `com_input` VALUES (137, '03', 'AL');
INSERT INTO `com_input` VALUES (138, '03', 'AL');
INSERT INTO `com_input` VALUES (139, '04', 'AL');
INSERT INTO `com_input` VALUES (140, '04', 'AL');
INSERT INTO `com_input` VALUES (141, '04', 'AL');
INSERT INTO `com_input` VALUES (142, '04', 'AL');
INSERT INTO `com_input` VALUES (143, '04', 'AL');
INSERT INTO `com_input` VALUES (144, '04', 'AL');
INSERT INTO `com_input` VALUES (145, '04', 'AL');
INSERT INTO `com_input` VALUES (146, '04', 'AL');
INSERT INTO `com_input` VALUES (147, '04', 'AL');
INSERT INTO `com_input` VALUES (148, '05', 'AL');
INSERT INTO `com_input` VALUES (149, '05', 'AL');
INSERT INTO `com_input` VALUES (150, '05', 'AL');
INSERT INTO `com_input` VALUES (151, '05', 'AL');
INSERT INTO `com_input` VALUES (152, '05', 'AL');
INSERT INTO `com_input` VALUES (153, '05', 'AL');
INSERT INTO `com_input` VALUES (154, '05', 'AL');
INSERT INTO `com_input` VALUES (155, '05', 'AL');
INSERT INTO `com_input` VALUES (156, '05', 'AL');
INSERT INTO `com_input` VALUES (157, '05', 'AL');
INSERT INTO `com_input` VALUES (158, '05', 'AL');
INSERT INTO `com_input` VALUES (159, '05', 'AL');
INSERT INTO `com_input` VALUES (160, '06', 'AL');
INSERT INTO `com_input` VALUES (161, '06', 'AL');
INSERT INTO `com_input` VALUES (162, '06', 'AL');
INSERT INTO `com_input` VALUES (163, '06', 'AL');
INSERT INTO `com_input` VALUES (164, '06', 'AL');
INSERT INTO `com_input` VALUES (165, '06', 'AL');
INSERT INTO `com_input` VALUES (166, '06', 'AL');
INSERT INTO `com_input` VALUES (167, '06', 'AL');
INSERT INTO `com_input` VALUES (168, '06', 'AL');
INSERT INTO `com_input` VALUES (169, '07', 'AL');
INSERT INTO `com_input` VALUES (170, '07', 'AL');
INSERT INTO `com_input` VALUES (171, '07', 'AL');
INSERT INTO `com_input` VALUES (172, '07', 'AL');
INSERT INTO `com_input` VALUES (173, '07', 'AL');
INSERT INTO `com_input` VALUES (174, '07', 'AL');
INSERT INTO `com_input` VALUES (175, '07', 'AL');
INSERT INTO `com_input` VALUES (176, '07', 'AL');
INSERT INTO `com_input` VALUES (177, '07', 'AL');
INSERT INTO `com_input` VALUES (178, '07', 'AL');
INSERT INTO `com_input` VALUES (179, '07', 'AL');
INSERT INTO `com_input` VALUES (180, '08', 'AL');
INSERT INTO `com_input` VALUES (181, '08', 'AL');
INSERT INTO `com_input` VALUES (182, '08', 'AL');
INSERT INTO `com_input` VALUES (183, '08', 'AL');
INSERT INTO `com_input` VALUES (184, '08', 'AL');
INSERT INTO `com_input` VALUES (185, '08', 'AL');
INSERT INTO `com_input` VALUES (186, '08', 'AL');
INSERT INTO `com_input` VALUES (187, '08', 'AL');
INSERT INTO `com_input` VALUES (188, '08', 'AL');
INSERT INTO `com_input` VALUES (189, '08', 'AL');
INSERT INTO `com_input` VALUES (190, '08', 'AL');
INSERT INTO `com_input` VALUES (191, '08', 'AL');
INSERT INTO `com_input` VALUES (192, '08', 'AL');
INSERT INTO `com_input` VALUES (193, '08', 'AL');
INSERT INTO `com_input` VALUES (194, '09', 'AL');
INSERT INTO `com_input` VALUES (195, '09', 'AL');
INSERT INTO `com_input` VALUES (196, '09', 'AL');
INSERT INTO `com_input` VALUES (197, '09', 'AL');
INSERT INTO `com_input` VALUES (198, '09', 'AL');
INSERT INTO `com_input` VALUES (199, '09', 'AL');
INSERT INTO `com_input` VALUES (200, '09', 'AL');
INSERT INTO `com_input` VALUES (201, '09', 'AL');
INSERT INTO `com_input` VALUES (202, '09', 'AL');
INSERT INTO `com_input` VALUES (203, '09', 'AL');
INSERT INTO `com_input` VALUES (204, '09', 'AL');
INSERT INTO `com_input` VALUES (205, '09', 'AL');
INSERT INTO `com_input` VALUES (206, '01', 'AL');
INSERT INTO `com_input` VALUES (207, '01', 'AL');
INSERT INTO `com_input` VALUES (208, '01', 'AL');
INSERT INTO `com_input` VALUES (209, '01', 'AL');
INSERT INTO `com_input` VALUES (210, '01', 'AL');
INSERT INTO `com_input` VALUES (211, '01', 'AL');
INSERT INTO `com_input` VALUES (212, '01', 'AL');
INSERT INTO `com_input` VALUES (213, '01', 'AL');
INSERT INTO `com_input` VALUES (214, '01', 'AL');
INSERT INTO `com_input` VALUES (215, '01', 'AL');
INSERT INTO `com_input` VALUES (216, '01', 'AL');
INSERT INTO `com_input` VALUES (217, '01', 'AL');
INSERT INTO `com_input` VALUES (218, '01', 'AL');
INSERT INTO `com_input` VALUES (219, '01', 'AL');
INSERT INTO `com_input` VALUES (220, '01', 'AL');
INSERT INTO `com_input` VALUES (221, '01', 'AL');
INSERT INTO `com_input` VALUES (222, '01', 'AL');
INSERT INTO `com_input` VALUES (223, '01', 'AL');
INSERT INTO `com_input` VALUES (224, '01', 'AL');
INSERT INTO `com_input` VALUES (225, '01', 'AL');
INSERT INTO `com_input` VALUES (226, '01', 'AL');
INSERT INTO `com_input` VALUES (227, '01', 'AL');
INSERT INTO `com_input` VALUES (228, '01', 'AL');
INSERT INTO `com_input` VALUES (229, '01', 'AL');
INSERT INTO `com_input` VALUES (230, '01', 'AL');
INSERT INTO `com_input` VALUES (231, '01', 'AL');
INSERT INTO `com_input` VALUES (232, '01', 'AL');
INSERT INTO `com_input` VALUES (233, '01', 'AL');
INSERT INTO `com_input` VALUES (234, '01', 'AL');
INSERT INTO `com_input` VALUES (235, '01', 'AL');
INSERT INTO `com_input` VALUES (236, '01', 'AL');
INSERT INTO `com_input` VALUES (237, '01', 'AL');
INSERT INTO `com_input` VALUES (238, '01', 'AL');
INSERT INTO `com_input` VALUES (239, '01', 'AL');
INSERT INTO `com_input` VALUES (240, '01', 'AL');
INSERT INTO `com_input` VALUES (241, '01', 'AL');
INSERT INTO `com_input` VALUES (242, '01', 'AL');
INSERT INTO `com_input` VALUES (243, '01', 'AL');
INSERT INTO `com_input` VALUES (244, '01', 'AL');
INSERT INTO `com_input` VALUES (245, '01', 'AL');
INSERT INTO `com_input` VALUES (246, '01', 'AL');
INSERT INTO `com_input` VALUES (247, '01', 'AL');
INSERT INTO `com_input` VALUES (248, '01', 'AL');
INSERT INTO `com_input` VALUES (249, '01', 'AL');
INSERT INTO `com_input` VALUES (250, '01', 'AL');
INSERT INTO `com_input` VALUES (251, '01', 'AL');
INSERT INTO `com_input` VALUES (252, '01', 'AL');
INSERT INTO `com_input` VALUES (253, '01', 'AL');
INSERT INTO `com_input` VALUES (254, '01', 'AL');
INSERT INTO `com_input` VALUES (255, '01', 'AL');
INSERT INTO `com_input` VALUES (256, '01', 'AL');
INSERT INTO `com_input` VALUES (257, '01', 'AL');
INSERT INTO `com_input` VALUES (258, '01', 'AL');
INSERT INTO `com_input` VALUES (259, '01', 'AL');
INSERT INTO `com_input` VALUES (260, '01', 'AL');
INSERT INTO `com_input` VALUES (261, '01', 'AL');
INSERT INTO `com_input` VALUES (262, '01', 'AL');
INSERT INTO `com_input` VALUES (263, '01', 'AL');
INSERT INTO `com_input` VALUES (264, '01', 'AL');
INSERT INTO `com_input` VALUES (265, '01', 'AL');
INSERT INTO `com_input` VALUES (266, '01', 'AL');
INSERT INTO `com_input` VALUES (267, '01', 'AL');
INSERT INTO `com_input` VALUES (268, '01', 'AL');
INSERT INTO `com_input` VALUES (269, '01', 'AL');
INSERT INTO `com_input` VALUES (270, '01', 'AL');
INSERT INTO `com_input` VALUES (271, '01', 'AL');
INSERT INTO `com_input` VALUES (272, '01', 'AL');
INSERT INTO `com_input` VALUES (273, '01', 'AL');
INSERT INTO `com_input` VALUES (274, '01', 'AL');
INSERT INTO `com_input` VALUES (275, '01', 'AL');
INSERT INTO `com_input` VALUES (276, '01', 'AL');
INSERT INTO `com_input` VALUES (277, '01', 'AL');
INSERT INTO `com_input` VALUES (278, '01', 'AL');
INSERT INTO `com_input` VALUES (279, '01', 'AL');
INSERT INTO `com_input` VALUES (280, '01', 'AL');
INSERT INTO `com_input` VALUES (281, '01', 'AL');
INSERT INTO `com_input` VALUES (282, '01', 'AL');
INSERT INTO `com_input` VALUES (283, '01', 'AL');
INSERT INTO `com_input` VALUES (284, '01', 'AL');
INSERT INTO `com_input` VALUES (285, '01', 'AL');
INSERT INTO `com_input` VALUES (286, '03', 'AL');
INSERT INTO `com_input` VALUES (287, '03', 'AL');
INSERT INTO `com_input` VALUES (288, '03', 'AL');
INSERT INTO `com_input` VALUES (289, '03', 'AL');
INSERT INTO `com_input` VALUES (290, '03', 'AL');
INSERT INTO `com_input` VALUES (291, '03', 'AL');
INSERT INTO `com_input` VALUES (292, '03', 'AL');
INSERT INTO `com_input` VALUES (293, '03', 'AL');
INSERT INTO `com_input` VALUES (294, '03', 'AL');
INSERT INTO `com_input` VALUES (295, '03', 'AL');
INSERT INTO `com_input` VALUES (296, '03', 'AL');
INSERT INTO `com_input` VALUES (297, '03', 'AL');
INSERT INTO `com_input` VALUES (298, '03', 'AL');
INSERT INTO `com_input` VALUES (299, '03', 'AL');
INSERT INTO `com_input` VALUES (300, '03', 'AL');
INSERT INTO `com_input` VALUES (301, '03', 'AL');
INSERT INTO `com_input` VALUES (302, '03', 'AL');
INSERT INTO `com_input` VALUES (303, '03', 'AL');
INSERT INTO `com_input` VALUES (304, '03', 'AL');
INSERT INTO `com_input` VALUES (305, '03', 'AL');
INSERT INTO `com_input` VALUES (306, '04', 'AL');
INSERT INTO `com_input` VALUES (307, '04', 'AL');
INSERT INTO `com_input` VALUES (308, '04', 'AL');
INSERT INTO `com_input` VALUES (309, '04', 'AL');
INSERT INTO `com_input` VALUES (310, '04', 'AL');
INSERT INTO `com_input` VALUES (311, '04', 'AL');
INSERT INTO `com_input` VALUES (312, '05', 'AL');
INSERT INTO `com_input` VALUES (313, '05', 'AL');
INSERT INTO `com_input` VALUES (314, '05', 'AL');
INSERT INTO `com_input` VALUES (315, '05', 'AL');

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
  `time` datetime(0) NULL DEFAULT NULL,
  `line` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `type` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `defType` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `qcPos` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '',
  `btn_pos` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `qty` int(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 59 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of history_input
-- ----------------------------
INSERT INTO `history_input` VALUES (33, '2020-03-09 15:06:18', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `history_input` VALUES (34, '2020-03-09 15:06:25', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `history_input` VALUES (35, '2020-03-09 15:06:30', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `history_input` VALUES (36, '2020-03-09 15:06:36', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `history_input` VALUES (37, '2020-03-09 15:06:41', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `history_input` VALUES (38, '2020-03-09 15:06:46', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `history_input` VALUES (39, '2020-03-09 15:47:54', 'AL', '针车不良', '5', '1', '07', 1);
INSERT INTO `history_input` VALUES (40, '2020-03-09 15:47:58', 'AL', '研磨线', '6', '1', '08', 1);
INSERT INTO `history_input` VALUES (41, '2020-03-09 15:48:03', 'Al', '投料', NULL, NULL, '01', 1);
INSERT INTO `history_input` VALUES (42, '2020-03-09 15:48:08', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `history_input` VALUES (43, '2020-03-09 15:48:13', 'AL', '投料', NULL, NULL, '01', 1);

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
  `time` datetime(0) NULL DEFAULT NULL,
  `line` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `type` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `defType` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `qcPos` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '',
  `btn_pos` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `qty` int(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 325 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of realtime_input
-- ----------------------------
INSERT INTO `realtime_input` VALUES (44, '2020-03-10 07:56:31', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (45, '2020-03-10 07:56:37', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (46, '2020-03-10 07:56:41', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (47, '2020-03-10 07:56:45', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (48, '2020-03-10 07:56:51', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (49, '2020-03-10 07:56:55', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (50, '2020-03-10 07:57:00', 'AL', '针车不良', '5', '1', '07', 1);
INSERT INTO `realtime_input` VALUES (51, '2020-03-10 07:57:05', 'AL', '研磨线', '6', '1', '08', 1);
INSERT INTO `realtime_input` VALUES (52, '2020-03-10 07:57:10', 'AL', '其他', '7', '1', '09', 1);
INSERT INTO `realtime_input` VALUES (53, '2020-03-10 08:09:12', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (54, '2020-03-10 08:09:31', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (55, '2020-03-10 08:09:35', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (56, '2020-03-10 08:09:38', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (57, '2020-03-10 08:09:42', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (58, '2020-03-10 08:09:46', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (59, '2020-03-11 08:30:19', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (60, '2020-03-11 08:30:20', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (61, '2020-03-11 09:30:20', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (62, '2020-03-11 19:30:20', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (63, '2020-03-11 10:30:20', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (64, '2020-03-11 10:30:21', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (65, '2020-03-11 10:30:21', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (66, '2020-03-11 11:05:21', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (67, '2020-03-11 11:06:21', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (68, '2020-03-11 19:30:21', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (69, '2020-03-11 19:30:21', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (70, '2020-03-11 19:30:22', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (71, '2020-03-11 19:30:22', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (72, '2020-03-11 19:30:22', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (73, '2020-03-11 19:30:22', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (74, '2020-03-11 19:30:22', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (75, '2020-03-11 19:30:23', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (76, '2020-03-11 19:30:23', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (77, '2020-03-11 19:30:23', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (78, '2020-03-11 19:30:23', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (79, '2020-03-11 19:30:23', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (80, '2020-03-11 19:30:23', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (81, '2020-03-11 19:30:23', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (82, '2020-03-11 19:30:24', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (83, '2020-03-11 19:30:24', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (84, '2020-03-11 19:30:24', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (85, '2020-03-11 19:30:24', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (86, '2020-03-11 19:30:24', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (87, '2020-03-11 19:30:24', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (88, '2020-03-11 19:30:25', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (89, '2020-03-11 19:30:25', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (90, '2020-03-11 19:30:25', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (91, '2020-03-11 19:30:25', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (92, '2020-03-11 19:30:25', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (93, '2020-03-11 19:30:26', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (94, '2020-03-11 19:30:26', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (95, '2020-03-11 19:30:26', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (96, '2020-03-11 19:30:26', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (97, '2020-03-11 19:30:26', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (98, '2020-03-11 19:30:26', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (99, '2020-03-11 19:30:27', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (100, '2020-03-11 19:30:27', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (101, '2020-03-11 19:30:27', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (102, '2020-03-11 19:30:27', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (103, '2020-03-11 19:30:27', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (104, '2020-03-11 19:30:27', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (105, '2020-03-11 19:30:28', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (106, '2020-03-11 19:30:28', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (107, '2020-03-11 19:30:28', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (108, '2020-03-11 19:30:31', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (109, '2020-03-11 19:30:31', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (110, '2020-03-11 19:30:31', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (111, '2020-03-11 19:30:31', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (112, '2020-03-11 19:30:32', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (113, '2020-03-11 19:30:32', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (114, '2020-03-11 19:30:32', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (115, '2020-03-11 19:30:32', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (116, '2020-03-11 19:30:32', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (117, '2020-03-11 19:30:32', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (118, '2020-03-11 19:30:33', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (119, '2020-03-11 19:30:33', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (120, '2020-03-11 19:30:33', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (121, '2020-03-11 19:30:33', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (122, '2020-03-11 19:30:33', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (123, '2020-03-11 19:30:33', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (124, '2020-03-11 19:30:34', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (125, '2020-03-11 19:30:34', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (126, '2020-03-11 19:30:34', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (127, '2020-03-11 19:30:34', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (128, '2020-03-11 19:30:34', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (129, '2020-03-11 19:30:34', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (130, '2020-03-11 19:30:35', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (131, '2020-03-11 19:30:35', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (132, '2020-03-11 19:30:35', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (133, '2020-03-11 19:30:35', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (134, '2020-03-11 19:30:35', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (135, '2020-03-11 19:30:35', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (136, '2020-03-11 19:30:36', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (137, '2020-03-11 19:30:36', 'AL', '包装', NULL, NULL, '02', 1);
INSERT INTO `realtime_input` VALUES (138, '2020-03-11 19:30:42', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (139, '2020-03-11 19:30:42', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (140, '2020-03-11 19:30:42', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (141, '2020-03-11 08:30:42', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (142, '2020-03-11 08:30:42', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (143, '2020-03-11 09:30:43', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (144, '2020-03-11 19:30:43', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (145, '2020-03-11 19:30:43', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (146, '2020-03-11 10:30:43', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (147, '2020-03-11 11:30:43', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (148, '2020-03-11 13:30:46', 'AL', '脱胶', '2', '1', '04', 1);
INSERT INTO `realtime_input` VALUES (149, '2020-03-11 08:30:46', 'AL', '脱胶', '2', '1', '04', 1);
INSERT INTO `realtime_input` VALUES (150, '2020-03-11 09:30:47', 'AL', '脱胶', '2', '1', '04', 1);
INSERT INTO `realtime_input` VALUES (151, '2020-03-11 09:30:47', 'AL', '脱胶', '2', '1', '04', 1);
INSERT INTO `realtime_input` VALUES (152, '2020-03-11 19:30:47', 'AL', '脱胶', '2', '1', '04', 1);
INSERT INTO `realtime_input` VALUES (153, '2020-03-11 19:30:47', 'AL', '脱胶', '2', '1', '04', 1);
INSERT INTO `realtime_input` VALUES (154, '2020-03-11 19:30:47', 'AL', '脱胶', '2', '1', '04', 1);
INSERT INTO `realtime_input` VALUES (155, '2020-03-11 19:30:47', 'AL', '脱胶', '2', '1', '04', 1);
INSERT INTO `realtime_input` VALUES (156, '2020-03-11 19:30:48', 'AL', '脱胶', '2', '1', '04', 1);
INSERT INTO `realtime_input` VALUES (157, '2020-03-11 19:30:51', 'AL', '不对称', '3', '1', '05', 1);
INSERT INTO `realtime_input` VALUES (158, '2020-03-11 19:30:52', 'AL', '不对称', '3', '1', '05', 1);
INSERT INTO `realtime_input` VALUES (159, '2020-03-11 19:30:52', 'AL', '不对称', '3', '1', '05', 1);
INSERT INTO `realtime_input` VALUES (160, '2020-03-11 19:30:52', 'AL', '不对称', '3', '1', '05', 1);
INSERT INTO `realtime_input` VALUES (161, '2020-03-11 19:30:52', 'AL', '不对称', '3', '1', '05', 1);
INSERT INTO `realtime_input` VALUES (162, '2020-03-11 19:30:52', 'AL', '不对称', '3', '1', '05', 1);
INSERT INTO `realtime_input` VALUES (163, '2020-03-11 19:30:52', 'AL', '不对称', '3', '1', '05', 1);
INSERT INTO `realtime_input` VALUES (164, '2020-03-11 19:30:53', 'AL', '不对称', '3', '1', '05', 1);
INSERT INTO `realtime_input` VALUES (165, '2020-03-11 19:30:53', 'AL', '不对称', '3', '1', '05', 1);
INSERT INTO `realtime_input` VALUES (166, '2020-03-11 19:30:53', 'AL', '不对称', '3', '1', '05', 1);
INSERT INTO `realtime_input` VALUES (167, '2020-03-11 19:30:53', 'AL', '不对称', '3', '1', '05', 1);
INSERT INTO `realtime_input` VALUES (168, '2020-03-11 19:30:53', 'AL', '不对称', '3', '1', '05', 1);
INSERT INTO `realtime_input` VALUES (169, '2020-03-11 19:30:56', 'AL', '清洁度', '4', '1', '06', 1);
INSERT INTO `realtime_input` VALUES (170, '2020-03-11 19:30:56', 'AL', '清洁度', '4', '1', '06', 1);
INSERT INTO `realtime_input` VALUES (171, '2020-03-11 19:30:56', 'AL', '清洁度', '4', '1', '06', 1);
INSERT INTO `realtime_input` VALUES (172, '2020-03-11 19:30:56', 'AL', '清洁度', '4', '1', '06', 1);
INSERT INTO `realtime_input` VALUES (173, '2020-03-11 19:30:57', 'AL', '清洁度', '4', '1', '06', 1);
INSERT INTO `realtime_input` VALUES (174, '2020-03-11 19:30:57', 'AL', '清洁度', '4', '1', '06', 1);
INSERT INTO `realtime_input` VALUES (175, '2020-03-11 19:30:57', 'AL', '清洁度', '4', '1', '06', 1);
INSERT INTO `realtime_input` VALUES (176, '2020-03-11 19:30:57', 'AL', '清洁度', '4', '1', '06', 1);
INSERT INTO `realtime_input` VALUES (177, '2020-03-11 19:30:57', 'AL', '清洁度', '4', '1', '06', 1);
INSERT INTO `realtime_input` VALUES (178, '2020-03-11 19:30:59', 'AL', '针车不良', '5', '1', '07', 1);
INSERT INTO `realtime_input` VALUES (179, '2020-03-11 19:31:00', 'AL', '针车不良', '5', '1', '07', 1);
INSERT INTO `realtime_input` VALUES (180, '2020-03-11 19:31:00', 'AL', '针车不良', '5', '1', '07', 1);
INSERT INTO `realtime_input` VALUES (181, '2020-03-11 19:31:00', 'AL', '针车不良', '5', '1', '07', 1);
INSERT INTO `realtime_input` VALUES (182, '2020-03-11 19:31:00', 'AL', '针车不良', '5', '1', '07', 1);
INSERT INTO `realtime_input` VALUES (183, '2020-03-11 19:31:00', 'AL', '针车不良', '5', '1', '07', 1);
INSERT INTO `realtime_input` VALUES (184, '2020-03-11 19:31:00', 'AL', '针车不良', '5', '1', '07', 1);
INSERT INTO `realtime_input` VALUES (185, '2020-03-11 19:31:01', 'AL', '针车不良', '5', '1', '07', 1);
INSERT INTO `realtime_input` VALUES (186, '2020-03-11 19:31:01', 'AL', '针车不良', '5', '1', '07', 1);
INSERT INTO `realtime_input` VALUES (187, '2020-03-11 19:31:01', 'AL', '针车不良', '5', '1', '07', 1);
INSERT INTO `realtime_input` VALUES (188, '2020-03-11 19:31:01', 'AL', '针车不良', '5', '1', '07', 1);
INSERT INTO `realtime_input` VALUES (189, '2020-03-11 19:31:03', 'AL', '研磨线', '6', '1', '08', 1);
INSERT INTO `realtime_input` VALUES (190, '2020-03-11 19:31:03', 'AL', '研磨线', '6', '1', '08', 1);
INSERT INTO `realtime_input` VALUES (191, '2020-03-11 19:31:03', 'AL', '研磨线', '6', '1', '08', 1);
INSERT INTO `realtime_input` VALUES (192, '2020-03-11 19:31:03', 'AL', '研磨线', '6', '1', '08', 1);
INSERT INTO `realtime_input` VALUES (193, '2020-03-11 19:31:03', 'AL', '研磨线', '6', '1', '08', 1);
INSERT INTO `realtime_input` VALUES (194, '2020-03-11 19:31:03', 'AL', '研磨线', '6', '1', '08', 1);
INSERT INTO `realtime_input` VALUES (195, '2020-03-11 19:31:03', 'AL', '研磨线', '6', '1', '08', 1);
INSERT INTO `realtime_input` VALUES (196, '2020-03-11 19:31:04', 'AL', '研磨线', '6', '1', '08', 1);
INSERT INTO `realtime_input` VALUES (197, '2020-03-11 19:31:04', 'AL', '研磨线', '6', '1', '08', 1);
INSERT INTO `realtime_input` VALUES (198, '2020-03-11 19:31:04', 'AL', '研磨线', '6', '1', '08', 1);
INSERT INTO `realtime_input` VALUES (199, '2020-03-11 19:31:04', 'AL', '研磨线', '6', '1', '08', 1);
INSERT INTO `realtime_input` VALUES (200, '2020-03-11 19:31:04', 'AL', '研磨线', '6', '1', '08', 1);
INSERT INTO `realtime_input` VALUES (201, '2020-03-11 19:31:04', 'AL', '研磨线', '6', '1', '08', 1);
INSERT INTO `realtime_input` VALUES (202, '2020-03-11 19:31:05', 'AL', '研磨线', '6', '1', '08', 1);
INSERT INTO `realtime_input` VALUES (203, '2020-03-11 19:31:07', 'AL', '其他', '7', '1', '09', 1);
INSERT INTO `realtime_input` VALUES (204, '2020-03-11 19:31:08', 'AL', '其他', '7', '1', '09', 1);
INSERT INTO `realtime_input` VALUES (205, '2020-03-11 19:31:08', 'AL', '其他', '7', '1', '09', 1);
INSERT INTO `realtime_input` VALUES (206, '2020-03-11 19:31:08', 'AL', '其他', '7', '1', '09', 1);
INSERT INTO `realtime_input` VALUES (207, '2020-03-11 19:31:08', 'AL', '其他', '7', '1', '09', 1);
INSERT INTO `realtime_input` VALUES (208, '2020-03-11 19:31:08', 'AL', '其他', '7', '1', '09', 1);
INSERT INTO `realtime_input` VALUES (209, '2020-03-11 19:31:08', 'AL', '其他', '7', '1', '09', 1);
INSERT INTO `realtime_input` VALUES (210, '2020-03-11 19:31:08', 'AL', '其他', '7', '1', '09', 1);
INSERT INTO `realtime_input` VALUES (211, '2020-03-11 19:31:09', 'AL', '其他', '7', '1', '09', 1);
INSERT INTO `realtime_input` VALUES (212, '2020-03-11 19:31:09', 'AL', '其他', '7', '1', '09', 1);
INSERT INTO `realtime_input` VALUES (213, '2020-03-11 19:31:09', 'AL', '其他', '7', '1', '09', 1);
INSERT INTO `realtime_input` VALUES (214, '2020-03-11 19:31:09', 'AL', '其他', '7', '1', '09', 1);
INSERT INTO `realtime_input` VALUES (215, '2020-03-11 19:31:49', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (216, '2020-03-11 19:31:49', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (217, '2020-03-11 19:31:49', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (218, '2020-03-11 19:31:49', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (219, '2020-03-11 19:31:49', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (220, '2020-03-11 19:31:49', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (221, '2020-03-11 19:31:50', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (222, '2020-03-11 19:31:50', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (223, '2020-03-11 19:31:50', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (224, '2020-03-11 19:31:50', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (225, '2020-03-11 19:31:50', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (226, '2020-03-11 19:31:50', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (227, '2020-03-11 19:31:51', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (228, '2020-03-11 19:31:51', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (229, '2020-03-11 19:31:51', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (230, '2020-03-11 19:31:51', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (231, '2020-03-11 19:31:51', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (232, '2020-03-11 19:31:51', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (233, '2020-03-11 19:31:52', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (234, '2020-03-11 19:31:52', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (235, '2020-03-11 19:31:52', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (236, '2020-03-11 19:31:52', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (237, '2020-03-11 19:31:52', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (238, '2020-03-11 19:31:52', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (239, '2020-03-11 19:31:53', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (240, '2020-03-11 19:31:53', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (241, '2020-03-11 19:31:53', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (242, '2020-03-11 19:31:53', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (243, '2020-03-11 19:31:53', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (244, '2020-03-11 19:31:53', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (245, '2020-03-11 19:31:54', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (246, '2020-03-11 19:31:54', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (247, '2020-03-11 19:31:54', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (248, '2020-03-11 19:31:54', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (249, '2020-03-11 19:31:54', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (250, '2020-03-11 19:31:54', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (251, '2020-03-11 19:31:55', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (252, '2020-03-11 19:31:55', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (253, '2020-03-11 19:31:55', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (254, '2020-03-11 19:31:55', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (255, '2020-03-11 19:31:56', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (256, '2020-03-11 19:31:56', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (257, '2020-03-11 19:31:56', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (258, '2020-03-11 19:31:56', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (259, '2020-03-11 19:31:56', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (260, '2020-03-11 19:31:56', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (261, '2020-03-11 19:31:57', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (262, '2020-03-11 19:31:57', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (263, '2020-03-11 19:31:57', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (264, '2020-03-11 19:31:57', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (265, '2020-03-11 19:31:57', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (266, '2020-03-11 19:31:58', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (267, '2020-03-11 19:31:58', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (268, '2020-03-11 19:31:58', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (269, '2020-03-11 19:31:58', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (270, '2020-03-11 19:31:58', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (271, '2020-03-11 19:31:58', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (272, '2020-03-11 19:31:59', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (273, '2020-03-11 19:31:59', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (274, '2020-03-11 19:31:59', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (275, '2020-03-11 19:31:59', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (276, '2020-03-11 19:31:59', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (277, '2020-03-11 19:31:59', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (278, '2020-03-11 19:32:00', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (279, '2020-03-11 19:32:00', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (280, '2020-03-11 19:32:00', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (281, '2020-03-11 19:32:00', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (282, '2020-03-11 19:32:00', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (283, '2020-03-11 19:32:01', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (284, '2020-03-11 19:32:01', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (285, '2020-03-11 19:32:01', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (286, '2020-03-11 19:32:01', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (287, '2020-03-11 19:32:01', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (288, '2020-03-11 19:32:01', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (289, '2020-03-11 19:32:02', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (290, '2020-03-11 19:32:02', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (291, '2020-03-11 19:32:02', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (292, '2020-03-11 19:32:02', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (293, '2020-03-11 19:32:02', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (294, '2020-03-11 19:32:02', 'AL', '投料', NULL, NULL, '01', 1);
INSERT INTO `realtime_input` VALUES (295, '2020-03-11 20:39:24', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (296, '2020-03-11 20:39:24', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (297, '2020-03-11 20:39:24', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (298, '2020-03-11 20:39:24', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (299, '2020-03-11 20:39:24', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (300, '2020-03-11 20:39:25', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (301, '2020-03-11 20:39:25', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (302, '2020-03-11 20:39:25', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (303, '2020-03-11 20:39:25', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (304, '2020-03-11 20:39:25', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (305, '2020-03-11 20:39:25', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (306, '2020-03-11 20:39:26', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (307, '2020-03-11 20:39:26', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (308, '2020-03-11 20:39:26', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (309, '2020-03-11 20:39:26', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (310, '2020-03-11 20:39:26', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (311, '2020-03-11 20:39:26', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (312, '2020-03-11 20:39:27', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (313, '2020-03-11 20:39:27', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (314, '2020-03-11 20:39:39', 'AL', '高胶', '1', '1', '03', 1);
INSERT INTO `realtime_input` VALUES (315, '2020-03-11 20:39:51', 'AL', '脱胶', '2', '1', '04', 1);
INSERT INTO `realtime_input` VALUES (316, '2020-03-11 20:39:51', 'AL', '脱胶', '2', '1', '04', 1);
INSERT INTO `realtime_input` VALUES (317, '2020-03-11 20:39:52', 'AL', '脱胶', '2', '1', '04', 1);
INSERT INTO `realtime_input` VALUES (318, '2020-03-11 20:39:52', 'AL', '脱胶', '2', '1', '04', 1);
INSERT INTO `realtime_input` VALUES (319, '2020-03-11 20:39:52', 'AL', '脱胶', '2', '1', '04', 1);
INSERT INTO `realtime_input` VALUES (320, '2020-03-11 20:39:52', 'AL', '脱胶', '2', '1', '04', 1);
INSERT INTO `realtime_input` VALUES (321, '2020-03-11 20:40:02', 'AL', '不对称', '3', '1', '05', 1);
INSERT INTO `realtime_input` VALUES (322, '2020-03-11 20:40:02', 'AL', '不对称', '3', '1', '05', 1);
INSERT INTO `realtime_input` VALUES (323, '2020-03-11 20:40:03', 'AL', '不对称', '3', '1', '05', 1);
INSERT INTO `realtime_input` VALUES (324, '2020-03-11 20:40:03', 'AL', '不对称', '3', '1', '05', 1);

-- ----------------------------
-- Triggers structure for table com_input
-- ----------------------------
DROP TRIGGER IF EXISTS `insert_to_realtime`;
delimiter ;;
CREATE TRIGGER `insert_to_realtime` AFTER INSERT ON `com_input` FOR EACH ROW insert into realtime_input(time, type, defType, qcPos, line, btn_pos, qty)
select now(), s.type, s.def_type_no, s.qcPos,c.line, NEW.btn_pos, 1
from config s, com_input c
where s.btn_pos = NEW.btn_pos and c.id = NEW.id
;
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
