# 通过数据库的表去创建Model
pip install flask-sqlacodegen
用法
flask-sqlacodegen "mysql://root:python123456@127.0.0.1/movie_cat" --tables user --outfile "common/models/user.py" --flask


创建数据库
CREATE DATABASE `movie_cat`CHARACTER SET utf8mb4 COLLATE utf8mb4_bin; 

创建表
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `nickname` varchar(30) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '昵称',
  `login_name` varchar(20) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '登录用户名',
  `login_pwd` varchar(32) COLLATE utf8mb4_bin NOT NULL COMMENT '登录密码',
  `login_salt` varchar(32) COLLATE utf8mb4_bin NOT NULL COMMENT '登录密码加密随机数',
  `status` tinyint(3) DEFAULT '0' COMMENT '状态 0：无效 1：有效',
  `update_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_login_name` (`login_name`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin

ALTER TABLE `movie_cat`.`user` ADD INDEX `uk_login_name` (`login_name`);

