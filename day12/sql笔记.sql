create database jing_dong charset = utf8;
use jing_dong;

create table goods (
    id         int unsigned primary key auto_increment not null,
    name       varchar(150)                            not null,
    cate_name  varchar(40)                             not null,
    brand_name varchar(40)                             not null,
    price      decimal(10, 3)                          not null default 0,
    is_show    bit                                     not null default 1,
    is_saleoff bit                                     not null default 0
);

insert into goods values (0, 'r510vc 15.6英⼨笔记本', '笔记本', '华硕', '3399', default, default);
insert into goods values (0, 'y400n 14.0英⼨笔记本电脑', '笔记本', '联想', '4999', default, default);
insert into goods values (0, 'g150th 15.6英⼨游戏本', '游戏本', '雷神', '8499', default, default);
insert into goods values (0, 'x550cc 15.6英⼨笔记本', '笔记本', '华硕', '2799', default, default);
insert into goods values (0, 'x240 超极本', '超级本', '联想', '4880', default, default);
insert into goods values (0, 'u330p 13.3英⼨超极本', '超级本', '联想', '4299', default, default);
insert into goods values (0, 'svp13226scb 触控超极本', '超级本', '索尼', '7999', default, default);
insert into goods values (0, 'ipad mini 7.9英⼨平板电脑', '平板电脑', '苹果', '1998', default, default);
insert into goods values (0, 'ipad air 9.7英⼨平板电脑', '平板电脑', '苹果', '3388', default, default);
insert into goods values (0, 'ipad mini 配备 retina 显示屏', '平板电脑', '苹果', '2788', default, default);
insert into goods values (0, 'ideacentre c340 20英⼨⼀体电脑 ', '台式机', '联想', '3499', default, default);
insert into goods values (0, 'vostro 3800-r1206 台式电脑', '台式机', '戴尔', '2899', default, default);
insert into goods values (0, 'imac me086ch/a 21.5英⼨⼀体电脑', '台式机', '苹果', '9188', default, default);
insert into goods values (0, 'at7-7414lp 台式电脑 linux ）', '台式机', '宏碁', '3699', default, default);
insert into goods values (0, 'z220sff f4f06pa⼯作站', '服务器/⼯作站', '惠普', '4288', default, default);
insert into goods values (0, 'poweredge ii服务器', '服务器/⼯作站', '戴尔', '5388', default, default);
insert into goods values (0, 'mac pro专业级台式电脑', '服务器/⼯作站', '苹果', '28888', default, default);
insert into goods values (0, 'hmz-t3w 头戴显示设备', '笔记本配件', '索尼', '6999', default, default);
insert into goods values (0, '商务双肩背包', '笔记本配件', '索尼', '99', default, default);
insert into goods values (0, 'x3250 m4机架式服务器', '服务器/⼯作站', 'ibm', '6888', default, default);
insert into goods values (0, '商务双肩背包', '笔记本配件', '索尼', '99', default, default);



-- sql强化演练( goods 表练习)

	-- 查询类型 cate_name 为 '超级本' 的商品名称 name 、价格 price ( where )
	select name, price from goods where cate_name = '超级本';


	-- 显示商品的种类
	-- 1）分组的方式( group by )
	select cate_name from goods group by cate_name;

	-- 2）去重的方法( distinct )
	select distinct cate_name from goods;


	-- 求所有电脑产品的平均价格 avg ,并且保留两位小数( round )
	select round(avg(price), 2) from goods;


	-- 显示 每种类型 cate_name (由此可知需要分组)的 平均价格
	select cate_name, avg(price) from goods group by cate_name;


	-- 查询 每种类型 的商品中 最贵 max 、最便宜 min 、平均价 avg 、数量 count
	select cate_name, max(price), min(price), avg(price), count(*) from goods group by cate_name;


	-- 查询所有价格大于 平均价格 的商品，并且按 价格降序 排序 order desc
	-- 1）查询平均价格 avg(price)
	select avg(price) from goods;
	-- 2）使用子查询
	select * from goods where price > (select avg(price) from goods) order by price desc;


	-- 查询每种类型中最贵的电脑的所有信息(难)
	select * from goods where price in (select max(price) from goods group by cate_name);

	-- 1 查找 每种类型 中 最贵的 max_price 价格
	select cate_name, max(price), group_concat(name) from goods group by cate_name;
	-- 2 关联查询 inner join 每种类型 中最贵的物品信息
	select * from goods
	inner join
	(select cate_name, max(price) as max_price from goods group by cate_name) as max_price_goods
	on goods.cate_name = max_price_goods.cate_name and goods.price = max_price_goods.max_price;



-- 创建"商品分类"表
	-- 第一步	创建表 (商品种类表 goods_cates )
	create table if not exists goods_cates(
	    id int unsigned primary key auto_increment,
	    name varchar(40) not null
	);
    +-------+------------------+------+-----+---------+----------------+
    | Field | Type             | Null | Key | Default | Extra          |
    +-------+------------------+------+-----+---------+----------------+
    | id    | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
    | name  | varchar(40)      | NO   |     | NULL    |                |
    +-------+------------------+------+-----+---------+----------------+


	-- 第二步	同步 商品分类表 数据 将商品的所有 (种类信息) 写入到 (商品种类表) 中
	-- 按照 分组 的方式查询 goods 表中的所有 种类(cate_name)
	select cate_name from goods group by cate_name;
	-- 通过子查询插入数据到新的分类表中
	insert into goods_cates(name) select cate_name from goods group by cate_name;


	-- 第三步 同步 商品表 数据 通过 goods_cates 数据表来更新 goods 表
	-- 因为要通过 goods_cates表 更新 goods 表 所以要把两个表连接起来(goods.cate_name = goods_cates.name)
	select * from goods inner join goods_cates on goods.cate_name = goods_cates.name;
	-- 把商品表 goods 中的 cate_name 全部替换成 商品分类表中的 商品id ( update (...)... set )
	update goods inner join goods_cates on goods.cate_name = goods_cates.name set goods.cate_name = goods_cates.id;


	-- 第四步 修改表结构
	-- 查看表结构(注意 两个表中的 外键类型需要一致)
	desc goods;
	+------------+------------------+------+-----+---------+----------------+
	| Field      | Type             | Null | Key | Default | Extra          |
	+------------+------------------+------+-----+---------+----------------+
	| id         | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
	| name       | varchar(150)     | NO   |     | NULL    |                |
	| cate_name  | varchar(40)      | NO   |     | NULL    |                |
	| brand_name | varchar(40)      | NO   |     | NULL    |                |
	| price      | decimal(10,3)    | NO   |     | 0.000   |                |
	| is_show    | bit(1)           | NO   |     | b'1'    |                |
	| is_saleoff | bit(1)           | NO   |     | b'0'    |                |
	+------------+------------------+------+-----+---------+----------------+

	-- 修改表结构 (alter table) 字段名字不同 change,把 cate_name 改成 cate_id    int unsigned not null
	alter table goods change cate_name cate_id int unsigned not null;



-- 创建商品品牌表 goods_brands
	-- #第一步 创建 "商品品牌表" 表
	-- 第一种方式 先创建表
	create table goods_brands (
	    id int unsigned primary key auto_increment,
	    name varchar(40) not null
	);

	-- 插入数据 brand_name(分组)
	-- 按照 分组 的方式查询 goods 表中的所有 种类(brand_name)
	-- (注意) 把查询出来的 结果 写入 goods_brands 表里去 ( insert into ) 只插入 name
	insert into goods_brands(name) select brand_name from goods group by brand_name;
	-- 第二种方式 创建表的同时插入数据(了解,不建议使用)


	-- # 第二步 同步数据
	-- 通过goods_brands数据表来更新goods数据表 g.brand_name=b.id
	update goods inner join goods_brands on goods.brand_name = goods_brands.name
	set goods.brand_name = goods_brands.id;


	-- # 第三步 修改表结构
	-- 通过alter table语句修改表结构 brand_id int unsigned not null
	alter table goods change brand_name brand_id int unsigned not null;



-- 外键的使用(了解)

    +------------+------------------+------+-----+---------+----------------+
    | Field      | Type             | Null | Key | Default | Extra          |
    +------------+------------------+------+-----+---------+----------------+
    | id         | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
    | name       | varchar(150)     | NO   |     | NULL    |                |
    | cate_id    | int(10) unsigned | NO   |     | NULL    |                |
    | brand_id   | int(10) unsigned | NO   |     | NULL    |                |
    | price      | decimal(10,3)    | NO   |     | 0.000   |                |
    | is_show    | bit(1)           | NO   |     | b'1'    |                |
    | is_saleoff | bit(1)           | NO   |     | b'0'    |                |
    +------------+------------------+------+-----+---------+----------------+

    insert into goods_cates(name) values ('路由器'),('交换机'),('⽹卡');
    insert into goods_brands(name) values ('海尔'),('清华同⽅'),('神⾈');


	-- 向goods表里插入任意一条数据 (name,cate_id,brand_id,price),cate_id的值为12
	insert into goods (name, cate_id, brand_id, price) values('LaserJet Pro P1606dn 黑白激光打印机', 12, 4, '1849');


	-- 查询所有商品的详细信息 (通过左连接 将左表未显示数据添加到最终结果)
	select * from goods left join goods_cates on goods.cate_id = goods_cates.id;


	-- 约束 数据的插入 使用 外键 foreign key
	-- 添加外键: alter table 表名 add foreign key (外键字段) references 表名(主键id)
	alter table goods add foreign key (cate_id) references goods_cates(id);



	-- ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails
	-- (`jing_dong`.`#sql-372_26`, CONSTRAINT `goods_ibfk_1` FOREIGN KEY (`cate_id`) REFERENCES `goods_cates` (`id`))
	-- 错误的原因是：数据库已经存在一条 不符合规则的数据了，需要先删除数据再重新添加外键
	-- 删除数据 cate_id = 12
	delete from goods where cate_id = 12;


	-- 给 goods 表的brands_id 添加和 goods_brands 的id做外键关联
	alter table goods add constraint fk_id foreign key (cate_id) references goods_cates(id);



	-- 创建表的同时设置外键 (注意 goods_cates 和 goods_brands 两个表必须事先存在)
	-- 创建goods_test表,字段为(id, name, cate_id,brand_id )
	-- 其中 cate_id 外键关联 goods_cates的id字段
	-- 其中 brand_id 外键关联 goods_brands的id字段
	create table goods_test(
        id       int primary key auto_increment,
        name     varchar(150) not null,
        cate_id  int unsigned not null,
        brand_id int unsigned not null,
        foreign key (cate_id) references goods_cates (id),
        foreign key (brand_id) references goods_brands (id)
    );


	-- 如何取消外键约束
	-- 需要先获取外键约束名称(常见格式为：表名_ibfk_数字, 'goods_test_ibfk_1'),
	-- 该名称系统会自动生成,可以通过查看表创建语句来获取名称
	-- 查看外键名
	show create table goods_test;

	-- 获取名称之后就可以根据名称来删除外键约束
	alter table goods_test drop foreign key goods_test_ibfk_1;



-- 什么是视图?
	-- 通俗的讲，视图就是一条SELECT语句执行后返回的结果集。
	-- 所以我们在创建视图的时候，主要的工作就落在创建这条SQL查询语句上。

-- 视图的特点
	-- 视图是对若干张基本表的引用，一张虚表，查询语句执行的结果，
	-- 不存储具体的数据（基本表数据发生了改变，视图也会跟着改变）；

-- 视图的最主要的作用
	-- 如果数据库因为需求等原因发生了改变，为了保证查询出来的数据与之前相同，
	-- 则需要在多个地方进行修改，维护起来非常麻烦,这个时候使用视图就可解决这个问题
-- 视图是存储在数据库中的查询的SQL语句，它主要出于两种原因：
    -- 安全原因， 视图可以隐藏一些数据，如：社会保险基金表，可以用视图只显示姓名，地址，而不显示社会保险号和工资数等，
    -- 另一原因是可使复杂的查询易于理解和使用。

	select goods.name gname, goods_cates.name gcname, goods_brands.name gbname
	from goods
	    join goods_cates on goods.cate_id = goods_cates.id
	    join goods_brands on goods.brand_id = goods_brands.id;


-- 视图的定义方式
	-- crete view 视图名 as select ....

	-- 查出产品表中产品名称、分类名称以及对应品牌
	-- 创建上述结果的视图( v_goods_info)
	create view v_goods_info as
	    select goods.name gname,goods_cates.name gcname,goods_brands.name gbname
	    from goods
	        inner join goods_cates on goods.cate_id = goods_cates.id
	        inner join goods_brands on goods.brand_id = goods_brands.id;


	-- 查看所有表和视图
	show tables; # v_goods_info;

	-- 当原表产品名称改变后，会影响视图（视图是虚拟表）
	update goods set name = 'xxx' where id = 24;


	-- 删除视图
		-- drop view 视图名;
	drop view v_goods_info;


	-- 注意
		-- 视图只能进行搜索

-- 视图作用总结

	-- 1 提高了重用性，就像一个函数
	-- 2 对数据库重构，却不影响已经编写好的程序运行
	-- 3 提高了安全性能，可以对不同的用户
	-- 4 让数据更加清

-- 视图最主要解决的问题
	-- 程序对数据库操作,一旦数据库发生变化,程序需要修改,这时如果使用视图就可以解决这个问题



-- 事物(ACID)

    -- 基本使用：
    # 	1. begin 或 start transaction
    # 	2. 操作 insert update delete
    # 	3. 确认修改 commit
    # 	3. 反悔  rollback;


    -- 回滚(rollback)
    # 第一步 打开 终端1 begin
    # 第二步 终端1 update 表名 set 字段="xxx" where ...;
    # 第三步 rollback 数据返回最开始的原始值

    show engines;


	-- 原子性 一致性
    # 第一步 打开 终端1 终端2
    # 第二步 终端1 打开事物 begin
    #        终端1 update 表名 set 字段="xxx" where ...;
    #        终端1 select * from 表名;  发现数据改变
    # 第三步 终端2 select * from 表名;
    #        发现数据其实并没有改变 其实这个时候对数据的相关操作信息存在缓存中,
    #        当commit之后,这些操作才会一次性的完成
    # 第四步 终端1 commit 数据数数据真的改变
    #        终端2 select * from 表名,数据改变了


	-- 隔离性
    # 第一步 打开 终端1 终端2
    # 第二步 终端1 打开事物 begin
    #        终端1 update 表名 set 字段="xxx" where ...;
    # 第三步 终端2 update 表名 set 字段="yyy" where ...;
    #        发现 处于阻塞状态
    # 第四步 终端1 commit
    #        终端2 阻塞状态解除 数据修改成 yyy


	-- 持久性
		-- 一旦事务提交，则其所做的修改会永久保存到数据库

	-- 注意
		-- innodb能使用事物
		-- 使用python操作数据库的时候 默认开启事物的
		-- 但是python对数据库进行增删改的时候 需要手动commit

		-- 使用终端操作数据库(也就是mysql的客户端)的时候 也是默认开始事物的
		-- 只是在回车确认操作的时候 终端会默认的commit 所以我们不需要commit


-- 事物最主要解决的问题
	-- 某些事情需要一次性完成 中途不允许出现中断 例如银行取钱 事物可以解决这种问题



-- sql注入  ' or 1=1 or '1
select * from goods where name = '' % name
select * from goods where name = '' or 1 or '';
