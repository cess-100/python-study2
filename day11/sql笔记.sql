create database python_test_1 charset = utf8;
use python_test_1;

-- students表
drop table  students;
create table students (
    id        int unsigned primary key auto_increment not null,
    name      varchar(20)              default '',
    age       tinyint unsigned         default 0,
    height    decimal(5, 2),
    gender    enum ('男','女','中性','保密') default '保密',
    cls_id    int unsigned             default 0,
    is_delete bit                      default 0
);
-- classes表
create table classes (
    id   int unsigned auto_increment primary key not null,
    name varchar(30)                             not null
);

-- 向students表中插⼊数据
insert into students
values (0, '小明', 18, 180.00, 2, 1, 0),
       (0, '小月月', 18, 180.00, 2, 2, 1),
       (0, '彭于晏', 29, 185.00, 1, 1, 0),
       (0, '刘德华', 59, 175.00, 1, 2, 1),
       (0, '黄蓉', 38, 160.00, 2, 1, 0),
       (0, '凤姐', 28, 150.00, 4, 2, 1),
       (0, '王祖贤', 18, 172.00, 2, 1, 1),
       (0, '周杰伦', 36, NULL, 1, 1, 0),
       (0, '程坤', 27, 181.00, 1, 2, 0),
       (0, '刘亦菲', 25, 166.00, 2, 2, 0),
       (0, '金星', 33, 162.00, 3, 3, 1),
       (0, '静⾹', 12, 180.00, 2, 4, 0),
       (0, '郭靖', 12, 170.00, 1, 4, 0),
       (0, '周杰', 34, 176.00, 2, 5, 0);

insert into classes values (0, 'python_01期'), (0, 'python_02期');


-- 查询练习
	-- 查询所有字段
	-- select * from 表名;
	select * from students;


	-- 查询指定字段
	-- select 列1,列2,... from 表名;
	select id,name,age from students;


	-- 使用 as 给字段起别名
	-- select 字段 as 名字.... from 表名;
	select id as '编号', name as '姓名' from students;
	select id '编号', name '姓名' from students;


	-- select 表名.字段 .... from 表名;
	select students.id ,students.name from students;


	-- 可以通过 as 给表起别名
	-- select 别名.字段 .... from 表名 as 别名;
	select s.id ,s.name from students as s;
	select s.id ,s.gender from students as s;

	-- 失败的
	-- select students.name, students.age from students as s;


	-- 消除重复行(查性别)
	-- distinct 字段
	select distinct gender from students;



-- 条件查询
	-- 比较运算符
		-- select .... from 表名 where .....

		-- >
		-- 查询大于18岁的信息
		select * from students where age > 18;


		-- <
		-- 查询小于18岁的信息
		select * from students where age < 18;


		-- >=
		-- <=
		-- 查询大于或者等于18岁的信息
        -- 查询小于或者等于18岁的信息
		select * from students where age >= 18;
		select * from students where age <= 18;


		-- =
		-- 查询年龄为18岁的所有学生的名字
		select name from students where age = 18;


		-- != 或者 <>
		select * from students where age != 18;
		select * from students where age <> 18;



	-- 逻辑运算符
		-- and
		-- 18和28之间的所有学生信息
		select * from students where age > 18 and age <=28;

		-- 失败
		-- select * from students where age>18 and <28;

		-- 18岁以上的女性
		select * from students where age > 18 and gender='女';


		-- or
		-- 18岁以上或者身高高过180(包含)以上
		select * from students where age > 18 or height >= 180;


		-- not
		-- 不在 18岁以上的女性 这个范围内的信息
		select * from students where not age > 18 and gender='女';


	-- 模糊查询(where name like 要查询的数据)
		-- like
		    -- % 替换任意个
		    -- _ 替换1个

		-- 查询姓名中 以 "小" 开始的名字
		select * from students where name like '小%';


		-- 查询姓名中 有 "小" 所有的名字
		select * from students where name like '%小%';


		-- 查询有2个字的名字
		select * from students where name like '__';


		-- 查询有3个字的名字
		select * from students where name like '___';


		-- 查询至少有2个字的名字
		select * from students where name like '__%';



	-- 范围查询
		-- in (1, 3, 8) 表示在一个非连续的范围内

		-- 查询 年龄为18、34的姓名
		select name from students where age = 18 or age = 34;
		select name from students where age in (18,34);

		-- not in 不非连续的范围之内
		-- 年龄不是 18、34岁的信息
		select name from students where age not in (18,34);

		-- (注意)
        select name from students where not age in (18,34);


		-- between ... and ...表示在一个连续的范围内 两端都包含

		-- 查询 年龄在18到34之间的的信息
		select * from students where age >=18 and age <=34;
		select * from students where age between 18 and 34;

		-- not between ... and ...表示不在一个连续的范围内
		-- 查询 年龄不在在18到34之间的的信息
		select * from students where age not between 18 and 34;

		-- 失败的
		-- select * from students where age not (between 18 and 34);


	-- 空判断
		-- 判空is null

		-- 查询身高为空的信息
		select * from students where height is null;


		-- 判非空is not null
		select * from students where height is not null;

		-- 失败
		-- select * from students where height not is null;



-- 排序
	-- order by 字段
	-- asc从小到大排列，即升序
	-- desc从大到小排序，即降序

	-- 查询年龄在18到34岁之间的男性，按照年龄从小到大到排序(默认是asc升序)
	select * from students where age between 18 and 34  and gender='男'
	order by age;

	-- 查询年龄在18到34岁之间的女性，身高从高到矮排序
	select * from students where age between 18 and 34 and gender='女'
	order by height desc;


	-- order by 多个字段
	-- 查询年龄在18到34岁之间的女性，身高从高到矮排序, 如果身高相同的情况下按照年龄从大到小排序
	select * from students where age between 18 and 34 and gender='女'
	order by height desc, age desc;

	-- 查询年龄在18到34岁之间的女性，身高从高到矮排序, 如果身高相同的情况下按照年龄从大到小排序,
	-- 如果年龄也相同那么按照id从大到小排序
	select * from students where age between 18 and 34 and gender='女'
	order by height desc, age desc, id desc;



-- 聚合函数
	-- count 总数
	-- 计算班级学生的总数
	select count(*) from students;
	select count(*) '总人数' from students;

	-- 查询男性有多少人，女性有多少人
	select count(*) from students where gender = '男';
	select count(*) from students where gender = '女';


	-- max 最大值
	-- 查询最大的年龄
	select max(age) from students;

    -- 查询女性最大的年龄
	select max(age) from students where gender='女';

	-- 查询女性的最高身高
	select max(height) from students where gender='女';


	-- min 最小值
	-- 查询女性的最小身高
	select min(height) from students where gender='女';


	-- sum 求和
	-- 计算所有人的年龄总和
	select sum(age) from students;


	-- avg 平均值
	-- 计算平均年龄
	select avg(age) from students;

    -- sum(age)/count(*)
	select sum(age)/count(*) from students;


	-- round() 四舍五入 round(123.23 , 1) 保留1位小数
	-- 计算所有人的平均年龄，保留2位小数
	select round(avg(age),2) from students;

	-- 计算男性的平均身高 保留2位小数
	select round(avg(height),2)  from students where gender = '男';



-- 分组(重点)

	-- group by

	-- 按照性别分组,查询所有的性别
	select gender from students group by gender;

	-- 失败
	-- select name,gender from students group by gender;
    -- select * from students group by gender;

	-- 计算每种性别中的人数
	select gender, count(*) from students group by gender;

	-- 计算每个年龄中的人数
	select age, count(*)  from students group by age;

	-- 查询 男、女性别中年龄的最大值
	select gender, max(age) from students where gender in ('男', '女') group by gender;

	-- 查询每组性别的平均年龄
	select gender, avg(age) from students group by gender;


	-- group_concat(...)

	-- 查询同种性别中的姓名
	select gender, group_concat(name) from students group by gender;


	-- 查询平均年龄超过30岁的性别，以及姓名 having avg(age) > 30(重点)
	select gender, avg(age) from students group by gender having avg(age) > 30;
	select gender, avg(age) av from students group by gender having av > 30; # 聚合函数在having前执行

	-- 查询每种性别的平均年龄和名字
	select gender, avg(age), group_concat(name) from students group by gender;

	-- 查询每种性别中的人数多于2个的性别和姓名（重点）
	select gender, count(*) c, group_concat(name)  from students group by gender having c > 2;


	-- with rollup 汇总的作用(了解)

	select gender, count(*) from students group by gender with rollup;



-- limit 查询
	-- limit start, count

	-- 限制查询出来的数据个数
	-- 查询前5个数据
	select * from students limit 0,5;
	select * from students limit 5;
	select * from students limit 4,2;


    -- 分页查询:

	-- 每页显示2个，第1个页面
	select * from students limit 0, 2;

	-- 每页显示2个，第2个页面
	select * from students limit 2, 2;

	-- 每页显示2个，第3个页面
	select * from students limit 4, 2;

	-- 每页显示2个，显示第6页的信息
	select * from students limit 10, 2;


	-- 展示第一页，最新数据，每页显示2条
	select * from students order by id desc limit 0,2;


	-- limit 放在最后面(注意)
	-- 错误
    -- select * from students limit 10,2 order by age asc;
    -- select * from students limit 2*(6-1),2;



-- 连接查询(重点)
	-- inner join ... on
	-- select ... from 表A inner join 表B;

	select * from students inner join classes;

	-- 查询 有能够对应班级的学生以及班级信息
	select * from students inner join classes on students.cls_id = classes.id;


	-- 按照要求显示姓名、班级
	select students.name, classes.name from students inner join classes on students.cls_id = classes.id;

	-- 给数据表起名字
	select s.name, c.name from students s inner join classes c on s.cls_id = c.id;
	-- 92写法
	select s.name, c.name from students s, classes c where s.cls_id = c.id;


	-- 查询 有能够对应班级的学生以及班级信息，显示学生的所有信息 students.*，只显示班级名称 classes.name.
	select students.*, classes.name from students inner join classes on students.cls_id = classes.id;

	-- 在以上的查询中，将班级名称显示在第1列
	select classes.name,students.* from students inner join classes on students.cls_id = classes.id;


	-- 查询 有能够对应班级的学生以及班级信息, 按照班级编号进行排序
	-- select c.xxx s.xxx from students as s inner join clssses as c on .... order by ....;
	select * from students s inner join classes c on s.cls_id = c.id order by c.id;


	-- 当时同一个班级的时候，按照学生的id进行从小到大排序
	select * from students s inner join classes c on s.cls_id = c.id order by c.id, s.id;



	-- left/right join ....on

	-- 查询每位学生对应的班级信息
	select * from students left join classes on students.cls_id = classes.id;


	-- 查询每班级对应的学生信息
	select * from students right join classes on students.cls_id = classes.id;


	-- 查询没有对应班级信息的学生
	-- select ... from xxx as s left join xxx as c on..... where .....
	-- select ... from xxx as s left join xxx as c on..... having ..... 不要使用
	select students.*  from students left join classes on students.cls_id = classes.id where classes.id is null;



-- 自连接查询
	-- 表和自己建立连接

	-- 1、查询一共有多少个省
	select count(*) from areas where pid is null;


	-- 2、查询省的名称为“山西省”的所有城市
	select * from areas city inner join areas province on city.pid = province.aid where province.atitle='山西省';


	-- 3、查询省的名称为“广州市”的所有县
	select * from areas city inner join areas province on city.pid = province.aid where province.atitle='广州市';



-- 子查询
	-- 标量子查询: 子查询返回的结果是一个数据(一行一列)
	-- 列子查询: 返回的结果是一列(一列多行)
	-- 行子查询: 返回的结果是一行(一行多列)

	-- 查询出高于平均身高的信息(height)
	-- 1 查出平均身高
	select avg(height) from students;
	-- 2 查出高于平均身高的信息
	select * from students where height > (select avg(height) from students);


	-- 查询学生的学号和班级编号对应的学生信息
	-- select name from students where cls_id in (select id from classes);
	-- 1 查出所有的班级id
	select id from classes;
	-- 2 查出能够对应上班级号的学生信息
	select * from students where id in (select id from classes);

show variables like '%auto_increment%';
