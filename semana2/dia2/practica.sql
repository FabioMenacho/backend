create table if not exists rol(
    id int not null auto_increment,
    nombre varchar(50) not null,
    primary key (id)
)engine=innodb;


create table if not exists usuario(
    id int not null auto_increment,
    nombre varchar(50) not null,
    clave varchar(100) not null,
    rol_id int,
    primary key (id),
    foreign key (rol_id) references rol(id) on delete restrict on update restrict
)engine=innodb;