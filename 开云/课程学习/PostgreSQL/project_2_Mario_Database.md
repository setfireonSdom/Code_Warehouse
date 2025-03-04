在写 SQL 时，是否使用大写完全取决于个人习惯和团队规范，并不是所有人都必须写大写。SQL 本身对大小写并不敏感，也就是说，SELECT 和 select 在执行时效果是一样的（不过，数据库中表名、列名等的大小写敏感性可能因数据库系统不同而有所差异，比如 MySQL 在某些配置下可能是大小写敏感的）。  

如果是个人项目，随你喜欢，写着舒服最重要。  
如果是团队开发，跟着团队的规范走，或者问问同事的习惯。
```bash
// 连接 PostgreSQL 数据库，指定要使用的数据库用户 (freecodecamp)，指定要连接的数据库 (postgres)
psql --username=freecodecamp --dbname=postgres
psql --username=<用户名> --dbname=<数据库名>

// see what databases are here
\l

// Create a new database
CREATE DATABASE database_name;

// connect to a database
\c database_name

// display the tables
\d
// more details about tables
\d table_name

// create a table
CREATE TABLE table_name();
// create table with columns
CREATE TABLE table_name(column_name DATATYPE CONSTRAINTS);
create table sounds(sound_id serial primary key);

// add columns
ALTER TABLE table_name ADD COLUMN column_name DATATYPE;
alter table sounds add column filename varchar(40) not null unique;

// remove columns
ALTER TABLE table_name DROP COLUMN column_name;

// VARCHAR datatype
ALTER TABLE second_table ADD COLUMN name VARCHAR(30);

// rename a column
ALTER TABLE table_name RENAME COLUMN column_name TO new_name;

// add rows
INSERT INTO table_name(column_1, column_2) VALUES(value1, value2);
insert into more_info(character_id,birthday ,height,weight) values(7,'1990-04-13',162,59.1);

// querying data to view it
SELECT columns FROM table_name;
// select in order
SELECT columns FROM table_name ORDER BY column_name;

// delete a row:
DELETE FROM table_name WHERE condition;

// drop table
DROP TABLE table_name;

// rename a database
ALTER DATABASE database_name RENAME TO new_database_name;

// drop database 
DROP DATABASE database_name

// SERIAL type,make your column an INT with a NOT NULL constraint,
// automatically increment the integer when a new row is added.
alter table characters add column character_id serial;

// Add a constraint by putting it right after the data type.
alter table characters add  column name varchar(30) not null;

// add more rows
insert into characters(name,homeland,favorite_color) values('Daisy','Sarasaland','Yellow'),('Yoshi','Dinosaur Land','Green');

// change a value
UPDATE table_name SET column_name=new_value WHERE condition;

// add a primary key
ALTER TABLE table_name ADD PRIMARY KEY(column_name);

// drop a constraint
ALTER TABLE table_name DROP CONSTRAINT constraint_name;

// decimals data type
alter table more_info add column weight numeric(4,1);

// set a foreign key
ALTER TABLE table_name ADD COLUMN column_name DATATYPE REFERENCES referenced_table_name(referenced_column_name);

// UNIQUE、NOT NULL constraint 
ALTER TABLE table_name ADD UNIQUE(column_name);
ALTER TABLE table_name ALTER COLUMN column_name SET NOT NULL;

// WHERE condition
SELECT columns FROM table_name WHERE condition;

// add "one-to-many" relationship 
ALTER TABLE table_name ADD COLUMN column_name DATATYPE CONSTRAINT REFERENCES referenced_table_name(referenced_column_name);

// "many-to-many" relationship, junction table（连接表）
// set an existing column as a foreign key 
ALTER TABLE table_name ADD FOREIGN KEY(column_name) REFERENCES referenced_table(referenced_column);

//  composite primary key
ALTER TABLE table_name ADD PRIMARY KEY(column1, column2);

// JOIN command
SELECT columns FROM table_1 FULL JOIN table_2 ON table_1.primary_key_column = table_2.foreign_key_column;
select * from characters a full join more_info m on a.character_id = m.character_id;


// some code 
SELECT columns FROM junction_table
FULL JOIN table_1 ON junction_table.foreign_key_column = table_1.primary_key_column
FULL JOIN table_2 ON junction_table.foreign_key_column = table_2.primary_key_column;

select * from character_actions full join characters on character_actions.character_id = characters.character_id full join actions on character_actions.action_id = actions.action_id;
```