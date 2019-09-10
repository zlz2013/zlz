-- 1.左外连接：左表:teacher，右表:course,
-- 关联条件:teacher.course_id=course.id
/*
select * from teacher left outer
join course on teacher.course_id=course.id;

select cname from course left
join teacher on course.id=teacher.course_id
where teacher.id is null;


-- 2.右外连接，左表:teacher,右表:course，
-- 关联条件:teacher.course_id=course.id
select * from teacher right
join course on teacher.course_id=course.id;
*/

/*
-- 3.完整外连接
select * from teacher full join
 course on course_id=course.id;
*/

/*
-- 4.查看没有参加过考试的同学的信息
select * from student left join
Score on student.id=Score.stu_id
where score is null
*/

/*
-- 5.子查询,查询student表中比李四年龄大的学生信息
select * from student where age>(
select age from student where name='李四'
);
*/

/*
-- 1.查询考过‘齐天大圣’老师所教课程的学员信息
select * from student where id in(
select stu_id from Score where course_id= (
select course_id from teacher where name='齐天大圣'
));
-- 2.查询在score表中有成绩的学员的信息
select * from student where id in(
select stu_id from Score where score is not null);
-- 3.查询‘Python基础’课程并且分数在80分以上的学员的姓名和毕业院校
select name,school from student where id in (
select stu_id from Score where course_id=(
select id from course where cname='Python基础') and score>80
);
-- 4.查询和‘张三’相同班级以及相同专业的同学的信息
select * from student where class_id=(select class_id from student where name='张三')
 and major_id=(select major_id from student where name='张三') and name!='张三';
*/

