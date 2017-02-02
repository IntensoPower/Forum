create table subjects (
    id smallint unsigned not null auto_increment,
    title varchar(40) not null,
    author varchar(20) not null default 'Invité',
    writeDate date not null,
    content text not null,
    primary key (id)
);
show tables;
describe subjects;
insert into subjects
    values (null,'salut', 'mathis', '2017/02/01', 'salut je suis nouveau faites moi un bon accueil');
insert into subjects
    values (null,'question', 'florian', '2017/02/01', 'bonjour y aurait il quelqu\'un qui sait comment on utilise SQL?');
insert into subjects
    values (null, 'reponse', 'gregory', '2017/02/01', 'salut florian demande a google :)');
select * from subjects;
insert into subjects (title, author, content, writeDate)
    values ('sûr?', 'florian', 'sudo dis moi comment utiliser SQL', '2017/02/02');
insert into subjects (title, content, writeDate)
    values ('login', 'bonjour comment on se fait un compte?', '2017/02/02');
insert into subjects (title, author, content, writeDate)
    values ('creer un compte', 'mathis', 'clique sur "creer un compte" en haut a droite', '2017/02/02');
insert into subjects (title, author, content, writeDate)
    values ('ok', 'gregory', 'viens dans mon bureau je vais te montrer', '2017/02/02');
insert into subjects (title, author, content, writeDate)
    values ('merci', 'sam', 'merci mathis de m\'avoir dit comment on se fait un compte ^^', '2017/02/02');
select * from subjects where author='mathis';
select distinct author from subjects;
select * from subjects where writeDate = 2017/01/31 || writeDate = 2017/02/01;
select * from subjects where content like '%salut%';