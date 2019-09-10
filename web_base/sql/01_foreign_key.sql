-- 创建外键
/**/

-- 创建course表:id,cname,cduration
/*
create table course(
    id int primary key auto_increment,
    cname varchar(30) not null,
    cduration int not null
);

-- 向course表中插入测试数据
insert into course (cname,cduration)
values
("Python基础",20),("Python高级",15),("WEB基础",9),
("Python Web",15),("爬虫",10),("数据分析&人工智能",20);

*/
-- 创建teacher表:id,name,age,gender,hobby,course_id
-- course_id是外键，引用子course表的主键id.
/*
create table teacher(
    id int primary key auto_increment,
    name varchar(30) not null,
    age int not null,
    gender varchar(2) not null,
    hobby varchar(50) not null,
    course_id int ,
    -- 创建外键约束
    constraint fk_course_teacher foreign key(course_id)
    references course(id)
);
*/

-- 向teacher表中插入数据
/*
insert into teacher values
(null,'齐天大圣',28,'M','大保健',1),
(null,'吕泽Maria',30,'M','拍片',2),
(null,'赵萌萌',18,'F','看帅哥',3),
(null,'赵铭',35,'M','大保健',4);
*/

-- 创建major表:id,m_name
/*
create table major(
    id int primary key auto_increment,
    m_name varchar(30) not null
);
insert into major values
(null,"AID"),
(null,"UID"),
(null,"JSD"),
(null,"WEB");
*/

-- 创建student表:id,name,age,gender,school,class_id,major_id
/*
create table student(
    id int primary key auto_increment,
    name varchar(30) not null,
    age int not null,
    gender char(2) not null,
    school varchar(100) not null,
    class_id int not null,
    major_id int not null
    -- constraint fk_student_major
    -- foreign key(major_id) references major(id),
);
*/

-- 更新student表，增加外键关系在major_id上，引用major表的主键id
/*
alter table student add
constraint fk_major_student foreign key(major_id)
references major(id);
*/

/*
create table Classinfo(
    id int primary key auto_increment,
    classname varchar(10) not null,
    status tinyint
);
*/

/*
create table Score(
    id int primary key auto_increment,
    stu_id int not null,
    course_id int not null,
    score float not null
);
*/

/*
alter table student add
constraint fk_Classinfo_student foreign key(class_id)
references Classinfo(id);

alter table Score add
constraint fk_student_Score foreign key(stu_id)
references student(id);

alter table Score add
constraint fk_course_Score foreign key(course_id)
references course(id);
*/

/*
insert into Classinfo (classname,status) values
(1901,0),
(1902,1),
(1903,1),
(1904,1),
(1905,1);
*/

/*
insert into student (name,age,gender,school,class_id,major_id)
values
('张三',18,'M','哈佛大学',5,1),
('李四',19,'M','麻省理工',3,2),
('王二麻子',26,'F','蓝翔技校',4,3),
('猪刚鬣',23,'F','许职技校',2,1);
*/

/*
insert into Score (stu_id,course_id,score) values
(1,1,98),(1,2,85),(1,3,96),
(2,1,69),(2,2,89),(2,4,65),
(3,2,76),(3,3,88),(3,4,75);
*/

-- 删除score表中的fk_student_score外键
-- alter table Score drop foreign key fk_student_Score;

-- 为score表中的stu_id增加外键，引用自student主键id设置级联操作

/*
alter table Score
add constraint fk_student_score
foreign key(stu_id)
references student(id)
on delete cascade
on update cascade;
*/

-- 使用内连接查询teacher和course表中的数据（姓名，年龄，课程名称，课时）
/*
select name,age,cname,cduration from teacher as t
inner join course as c
on t.course_id=c.id;
*/

select s.name,s.age,c.classname,m.m_name from
student as s
inner join Classinfo as c
on s.class_id=c.id
inner join major as m
on s.major_id=m.id;


select s.name,s.school,c.classname,co.cname,S.score
from student as s
inner join Classinfo as c
on s.class_id=c.id
inner join Score as S
on s.id=S.stu_id
inner join course as co
on S.course_id=co.id;