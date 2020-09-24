-- 索引
	-- 注意
	-- 要注意的是，建立太多的索引将会影响更新和插入的速度，因为它需要同样更新每个索引文件。
	-- 对于一个经常需要更新和插入的表格，就没有必要为一个很少使用的where字句单独建立索引了，
	-- 对于比较小的表，排序的开销不会很大，也没有必要建立另外的索引。

	-- 建立索引会占用磁盘空间

    -- 索引最主要解决的问题
	    -- 当数据非常庞大时,并且这些数据不需要经常修改,为了加快查询速度,我们会使用索引

    create database python_index_db charset = 'utf8';
    use python_index_db;

    create table test_index (
        title varchar(10)
    );

    -- 插入100000条数据

    set profiling = 1;

    select * from test_index where title = "ha-99999";
    show profiles;

    create index idx_1 on test_index(title(10));
    select * from test_index where title = "ha-99999";
    show profiles;

-- 权限管理(了解) 对用户的管理

	-- 查看有哪些账户
    # 1 使用root账户登录
    # 2 使用mysql数据库
    # 3 用户的信息存放在 user 表中
    use mysql;
    show tables;
    desc user;
    select Host, User, authentication_string from User;


    -- 创建用户
    -- 使用root账户登录
    -- create user '用户名'@'主机' identified by '密码';
    create user 'cess'@'localhost' identified by '123';
    # 使得用户可以远程登录用 %
    create user 'cess'@'%' identified by '123';
    # 此时再登录 mysql -hIP地址 -ucess -p


    -- 授予权限
    -- grant 权限列表 on 数据库.表名 to '⽤户名'@'主机名';
    grant select on jing_dong.* to 'cess'@'localhost';
    flush privileges;



    -- 查看用户权限
    show grants for 'cess'@'localhost';


    -- 修改权限
    -- grant 权限名称 on 数据库 to 账户@主机 with grant option;
    grant select, update on jing_dong.* to 'cess'@'localhost' with grant option;


    -- 修改密码
    -- alter user '⽤户名'@'主机名' identified by '密码';
    alter user 'cess'@'localhost' identified by '123';


    -- 删除用户
    -- drop user '⽤户名'@'主机';
    -- delete from user where user='⽤户名';
    drop user 'cess'@'localhost';



-- 电影爬虫

    show databases;

    create database movie_db charset = utf8;
    use movie_db;

    create table if not exists movie_link (
        id        int(11) primary key auto_increment,
        movie_name varchar(255) not null,
        movie_link varchar(255) not null
    ) charset = utf8;

    -- 删除表所有数据,并将自增重新变为1
    truncate table movie_link;