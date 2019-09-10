-- 1.创建wife表，目的是实现与teacher表之间的一对一关系
/*
create table wife (
    id int primary key auto_increment,
    name varchar(20) not null,
    age tinyint not null,
    teacher_id int,
    constraint fk_teacher_wife foreign key(teacher_id)
    references teacher(id),
    unique(teacher_id)
)
*/

/*
insert into wife(name,age,teacher_id) values
('祁夫人',23,2),
('吕夫人',76,1),
('王夫人',18,3);
*/

/*
create table goods(
    id int primary key auto_increment,
    gname varchar(32) not null,
    gprice int not null
);
*/

/*
create table shoppingcart(
    id int primary key auto_increment,
    t_id int,
    g_id int,
    count int,
    constraint fk_teacher_shoppingcart
    foreign key(t_id) references teacher(id),
    constraint fk_goods_shoppingcart
    foreign key(g_id) references goods(id)
);
*/

/*
insert into goods(gname,gprice) values
('iphone56',18888),
('ipad43mini',8888),
('华为Mate3000',1888);

insert into shoppingcart(t_id,g_id,count) values
(1,1,1),(1,2,1),(1,3,15),(2,2,8),(2,3,1);
*/

select t.name,g.gname,g.gprice,sh.count from shoppingcart as sh
inner join teacher as t on t.id=sh.t_id
inner join goods as g on g.id=sh.g_id;