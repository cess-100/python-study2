-- 01 mysql 数据库的操作
    ctrl + a 回到开头
    ctrl + e 回到结尾
    ctrl + l 清屏


    -- 链接数据库
    mysql -uroot -p123123


	-- 不显示密码
    mysql -uroot -p
    123123


    -- 退出数据库
    exit
    quit
    ctrl + d


    -- sql语句最后需要有分号;结尾
    -- 显示数据库版本 version
    select version();


    -- 显示时间
    select now();


	-- 查看当前使用的数据库
    select database();


    -- 查看所有数据库
    show databases;


    -- 创建数据库(python_db)
    -- create database 数据库名 charset=utf8;
    create database python_db;

    -- 指定编码的数据库创建
    create database python_db character set utf8 collate utf8_general_ci;
    create database python_db character set utf8;


    -- 查看创建数据库的语句
    -- show create database ....
    show create database python_db;


    -- 使用数据库
    -- use 数据库的名字
    use python_db;


    -- 删除数据库
    -- drop database 数据库名;
    drop database python_db;



-- 02 数据表的操作

    -- 查看当前数据库中所有表
    show tables;


    -- 创建表
	-- int unsigned 无符号整形
    -- auto_increment 表示自动增长
    -- not null 表示不能为空
    -- primary key 表示主键
    -- default 默认值
    -- create table 数据表名字 (字段 类型 约束[, 字段 类型 约束]);


    -- 创建 classes 表(id、name)
    create table classes(
        id int unsigned primary key auto_increment,
        name varchar(10) not null,
        num tinyint
    );


    -- 查看表结构
    -- desc 数据表的名字;
    desc classes;


    -- 创建 students 表(id、name、age、high (decimal)、gender (enum)、cls_id)
    create table students(
        id int unsigned primary key auto_increment,
        name varchar(20) not null,
        age tinyint(1) ,
        high decimal(3,2),
        gender enum('男','女','妖'),
        cls_id int unsigned
    );


    -- 查看表的创建语句
    -- show create table 表名字;
    show create table students;


    -- 修改表-添加字段 生日 datatime
    -- alter table 表名 add 列名 类型;
    alter table students add birthday datetime;



    -- 修改表-修改字段：不重命名版
    -- alter table 表名 modify 列名 类型及约束;
    alter table students modify birth date not null;


    -- 修改表-修改字段：重命名版
    -- alter table 表名 change 原名 新名 类型及约束;
    alter table students change birthday birth datetime;


    -- 修改表-删除字段
    -- alter table 表名 drop 列名;
    alter table students drop birth;


    -- 删除表
    -- drop table 表名;
    -- drop database 数据库;
    drop table students;



-- 03 增删改查(curd)(重点--记忆)


    -- 增加
+-------+------------------+------+-----+---------+----------------+
| Field | Type             | Null | Key | Default | Extra          |
+-------+------------------+------+-----+---------+----------------+
| id    | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name  | varchar(10)      | NO   |     | NULL    |                |
| num   | tinyint(4)       | YES  |     | NULL    |                |
+-------+------------------+------+-----+---------+----------------+


        -- 全列插入
        -- insert [into] 表名 values(...)
        -- 主键字段 可以用 0  null   default 来占位
        -- 向classes表中插入 一个班级
        insert into classes values(1, 'python20', 70);
        insert into classes values(null, 'python19', 68);


        -- 向students表插入 一个学生信息
+--------+-------------------------+------+-----+---------+----------------+
| Field  | Type                    | Null | Key | Default | Extra          |
+--------+-------------------------+------+-----+---------+----------------+
| id     | int(10) unsigned        | NO   | PRI | NULL    | auto_increment |
| name   | varchar(20)             | NO   |     | NULL    |                |
| age    | tinyint(1)              | YES  |     | NULL    |                |
| high   | decimal(3,2)            | YES  |     | NULL    |                |
| gender | enum('男','女','妖')     | YES  |     | NULL    |                |
| cls_id | int(10) unsigned        | YES  |     | NULL    |                |
+--------+-------------------------+------+-----+---------+----------------+


        -- 部分插入
        -- insert into 表名(列1,...) values(值1,...)
        insert into students values(null, '司马二狗', 18, 1.78, '妖', 1);
        insert into students(id, name) values(null, '司马狗剩');


        -- 多行插入
        insert into students
        values(null, '欧阳铁娃', 18, 1.78, '妖', 1),
               (null, '诸葛铁锤', 18, 1.78, '妖', 1);


    -- 修改
    -- update 表名 set 列1=值1, 列2=值2, ... where 条件;

        -- 全部修改
        update students set age = 38;


		-- 按条件修改
        update students set age = 88 where name = '司马狗剩';
        update students set high = 1.2, gender='男' where name='司马狗剩';


    -- 查询基本使用
        -- 查询所有列
        -- select * from 表名;
        select * from students;


        -- 定条件查询
        select * from students where name='司马狗剩';
        select * from students where id = 2;


        -- 查询指定列
        -- select 列1,列2,... from 表名;
        select id,name from students;
        select id,age from students;


        -- 可以使用as为列或表指定别名
        -- select 字段[as 别名] , 字段[as 别名] from 数据表;
        select id as '编号', name as '姓名' from students;

        -- 字段的顺序
        select age,name from students;


    -- 删除
        -- 物理删除
        -- delete from 表名 where 条件
        delete from students where id = 2;


        -- 逻辑删除
        -- 用一个字段来表示 这条信息是否已经不能再使用了
        -- 给students表添加一个 is_delete 字段 bit 类型  默认为0
        alter table students add is_delete bit default 0;

        -- bit 类型，只能保存 0 或者 1
        -- is_delete = 1  逻辑删除
        update students set is_delete = 1 where id = 3;


	-- 数据库备份与恢复(了解)
		-- mysqldump –uroot –p 数据库名 > python.sql;
		-- mysql -uroot –p 新数据库名 < python.sql;

